# Lab 5.1 – Copilot erweitern & anpassen

In diesem Lab erfährst du, wie sich Entwickler‑Assistenten wie GitHub Copilot erweitern lassen.  Copilot kann nicht nur Prompts interpretieren, sondern über sogenannte **Custom Commands** oder **Plugins** auch Informationen aus eigenen Diensten einbinden.  Die Slides zeigen Beispiele in C# und Node/TypeScript.

## Minimal‑API in .NET

```csharp
// Program.cs – Copilot‑Extension
using Microsoft.AspNetCore.Builder;
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/info", () => new { name = "Inventar‑Agent", description = "Erzeugt Use‑Cases." });
app.MapPost("/", (HttpContext ctx) => {
    // Header und Body lesen
    var prompt = new StreamReader(ctx.Request.Body).ReadToEndAsync().Result;
    return Results.Json(new { answer = $"Du hast gefragt: {prompt}" });
});
app.Run();
```

Diese Minimal‑API stellt einen `/info`‑Endpunkt bereit, der Metadaten liefert, und einen Root‑Endpunkt `/`, der Benutzereingaben entgegennimmt und beantwortet.

## Node/TypeScript‑Agent

```ts
import express from 'express';
const app = express();
app.use(express.json());
app.get('/info', (req, res) => {
  res.json({ name: 'Inventar‑Agent', description: 'Erzeugt Use‑Cases' });
});
app.post('/', (req, res) => {
  const { prompt } = req.body;
  res.json({ answer: `Du hast gefragt: ${prompt}` });
});
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Agent listening on ${port}`));
```

Dieses Express‑Backend erfüllt dieselben Aufgaben wie die .NET‑Version, ist aber in TypeScript umgesetzt.

## GitHub‑API mit Octokit

Die Slides zeigen außerdem einen C#‑Agenten, der mithilfe der GitHub‑Bibliothek `Octokit` Repository‑Informationen abruft:

```csharp
using Octokit;
app.MapGet("/info", async () => new { name = "GitHub‑Agent", description = "Gibt Repo‑Info aus" });
app.MapPost("/", async (HttpContext ctx) => {
    var gh = new GitHubClient(new ProductHeaderValue("Agent"));
    var repo = await gh.Repository.Get("dotnet", "runtime");
    var issues = await gh.Issue.GetAllForRepository(repo.Id);
    var message = $"{repo.FullName} hat {issues.Count} offene Issues";
    return Results.Json(new { answer = message });
});
```

Dieses Beispiel liest einen Repository‑Namen aus dem Body, ruft Details via GitHub API ab und liefert eine Antwort.  Für die Nutzung ist ein Personal‑Access‑Token erforderlich.
