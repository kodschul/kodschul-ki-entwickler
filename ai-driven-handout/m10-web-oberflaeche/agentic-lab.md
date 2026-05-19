# m10 — Agentic Lab: Web-Oberfläche mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/api-mvc.instructions.md`

```markdown
---
applyTo: "Api/**/*.cs,Web/**/*.cs"
---

## ASP.NET Core Controller & API Konventionen

- Controller-Klassen sind `sealed` und erben von `ControllerBase` (API) oder `Controller` (MVC)
- Dependency Injection über primären Konstruktor — niemals `[Inject]` oder Service Locator
- Niemals Entitätsklassen direkt als Request/Response zurückgeben — immer DTOs/Records
- Request-DTOs als `record` mit Validierung via `[Required]`, `[MaxLength]`, `[Range]`
- Response-DTOs als `record` — unveränderlich
- HTTP-Statuscodes: 200 OK, 201 Created, 204 NoContent, 400 BadRequest, 404 NotFound, 409 Conflict
- `CreatedAtAction` für POST-Endpunkte — gibt Location-Header zurück
- CORS ist global in `Program.cs` konfiguriert — niemals per Controller
- Swagger/OpenAPI ist immer aktiviert in Development
- Fehlerbehandlung über globalen Exception-Handler — kein try/catch in Controllern

## MVC-spezifisch

- ViewModels als eigene Klassen unter `Web/ViewModels/`
- Razor Views nutzen stark typisierte `@model`-Direktive
- Kein Business-Logik-Code in Views oder Controllern
```

---

## 2. `.github/prompts/scaffold-controller.prompt.md`

Aufruf: `/scaffold-controller`

```markdown
---
name: scaffold-controller
description: Generiert einen vollständigen ASP.NET Core Controller mit DTOs aus einem Application Service
---

Du bist Senior ASP.NET Core Entwickler (.NET 9).

Generiere einen vollständigen Controller für den folgenden Application Service.

Pflichtbestandteile:

- `[ApiController]` + `[Route("api/[controller]")]`
- Primärer Konstruktor für Dependency Injection
- Ein Endpunkt pro Service-Methode (GET/POST/PUT/DELETE sinnvoll vergeben)
- Request-Record und Response-Record als DTOs
- Statuscodes: 200, 201 (mit CreatedAtAction), 400, 404, 409
- Keine Business-Logik im Controller — nur delegieren
- XML-Dokumentation für Swagger
- Nur Code, keine Erklärungen

Application Service:
{{selection}}
```

**Verwendung:**

1. Application Service Klasse im Editor markieren
2. `/scaffold-controller` in Copilot Chat

---

## 3. `.github/agents/api-scaffolder.agent.md`

```markdown
---
name: api-scaffolder
description: >
  Liest alle Application Services und generiert vollständige Controller,
  DTOs und Swagger-Dokumentation für noch nicht implementierte Endpunkte
tools:
  - codebase
  - new_file
---

Du bist Senior ASP.NET Core Entwickler (.NET 9).

Aufgabe:

1. Lese alle `*ApplicationService.cs` und `*QueryService.cs` unter `Application/`
2. Prüfe welche Services noch keinen Controller unter `Api/Controllers/` haben
3. Generiere für jeden fehlenden Service:
   - `Api/Controllers/[Name]Controller.cs` — vollständiger Controller
   - `Api/DTOs/[Name]Requests.cs` — alle Request-Records
   - `Api/DTOs/[Name]Responses.cs` — alle Response-Records
4. Aktualisiere `Program.cs` falls neue Services registriert werden müssen
5. Erstelle `api-endpoints.md` mit Übersicht aller Endpunkte (Methode + URL + Beschreibung)

Konventionen:

- sealed Controller-Klassen
- Primärer Konstruktor
- Keine Entitäten direkt zurückgeben
- CreatedAtAction für alle POST-Endpunkte
- HTTP 409 bei Konflikten (z.B. doppelte RoomNumber)
```

**Workflow:**

```
Application/*Service.cs  →  [api-scaffolder]  →  Api/Controllers/*.cs
                                              →  Api/DTOs/*.cs
                                              →  api-endpoints.md
```

---

## Program.cs Vorlage — direkt kopieren

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new() { Title = "Hotel Reservierung API", Version = "v1" });
});

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
        policy.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod());
});

builder.Services.AddDbContext<AppDbContext>(opt =>
    opt.UseSqlite(builder.Configuration.GetConnectionString("Default")
        ?? "Data Source=hotel.db"));

builder.Services.AddScoped<BookingApplicationService>();
builder.Services.AddScoped<RoomApplicationService>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseCors("AllowAll");
app.MapControllers();
app.Run();
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese alle Application Services unter Application/.
Generiere vollständige Controller mit DTOs für alle Services die noch keinen
Controller haben. Erstelle danach api-endpoints.md mit der vollständigen
Endpunkt-Übersicht.
```
