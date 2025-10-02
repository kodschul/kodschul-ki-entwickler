# Lösungen – Lab 5.1 Copilot erweitern & anpassen

1. **Eigener Copilot‑Endpoint (C#):**

```csharp
using Microsoft.AspNetCore.Builder;
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/info", () => new { name = "MeinAgent", description = "Beantwortet Fragen" });
app.MapPost("/", async (HttpContext ctx) => {
    using var reader = new StreamReader(ctx.Request.Body);
    var body = await reader.ReadToEndAsync();
    // JSON parsen
    var obj = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string,string>>(body);
    var question = obj?["question"] ?? "";
    return Results.Json(new { answer = $"Du hast gefragt: {question}" });
});
app.Run();
```

Starte mit `dotnet run` und teste:

```
curl http://localhost:5000/info
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"question":"Was ist KI?"}'
```

2. **Express‑Agent (TypeScript):**

```ts
import express, { Request, Response } from 'express';
const app = express();
app.use(express.json());
app.get('/info', (_req: Request, res: Response) => {
  res.json({ name: 'MeinAgent', description: 'Beantwortet Fragen' });
});
app.post('/', (req: Request, res: Response) => {
  const question = req.body.question ?? '';
  res.json({ answer: `Du hast gefragt: ${question}` });
});
const port = 3000;
app.listen(port, () => console.log(`Agent läuft auf Port ${port}`));
```

Führe `npm install express` aus und starte den Server mit `node index.ts`.  Teste mit `curl` analog zur C#‑Version.

3. **GitHub‑Info abrufen (C#):**

```csharp
using Microsoft.AspNetCore.Builder;
using Octokit;
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapPost("/", async (HttpContext ctx) => {
    using var reader = new StreamReader(ctx.Request.Body);
    var body = await reader.ReadToEndAsync();
    var obj = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string,string>>(body);
    string owner = obj?["owner"] ?? "dotnet";
    string name  = obj?["repo"]  ?? "runtime";
    var client = new GitHubClient(new ProductHeaderValue("MyAgent"));
    // Optional: GitHub‑Token setzen mit client.Credentials = new Credentials("TOKEN");
    var repo = await client.Repository.Get(owner, name);
    var issues = await client.Issue.GetAllForRepository(repo.Id);
    return Results.Json(new { answer = $"{repo.FullName} hat {issues.Count} offene Issues" });
});
app.Run();
```

Dieses Beispiel liest `owner` und `repo` aus der Anfrage, holt Repository‑Informationen über Octokit und gibt die Anzahl offener Issues aus.  Ohne Token sind nur öffentliche Repositories verfügbar.
