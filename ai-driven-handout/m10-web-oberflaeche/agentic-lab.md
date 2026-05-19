# m10 — Agentic Lab: Web-Oberfläche mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/api-mvc.instructions.md`

```markdown
---
applyTo: "HotelApp.Web/**/*.cs"
---

## ASP.NET Core Controller & API Konventionen

- Controller-Klassen sind `sealed` und erben von `ControllerBase` (API)
- Dependency Injection über primären Konstruktor — niemals `[Inject]` oder Service Locator
- Niemals Entitätsklassen direkt als Request/Response zurückgeben — immer DTOs/Records
- Request-DTOs als `record` mit Validierung via `[Required]`, `[MaxLength]`, `[Range]`
- Response-DTOs als `record` — unveränderlich
- HTTP-Statuscodes: 200 OK, 201 Created, 204 NoContent, 400 BadRequest, 404 NotFound, 409 Conflict
- `CreatedAtAction` für POST-Endpunkte — gibt Location-Header zurück
- CORS ist global in `Program.cs` konfiguriert — niemals per Controller
- Swagger/OpenAPI ist immer aktiviert in Development
- Fehlerbehandlung über globalen Exception-Handler — kein try/catch in Controllern

## Blazor-spezifisch

- Razor Components liegen unter `HotelApp.Web/Components/Pages/`
- `@inject` für Dependency Injection in Components
- `@rendermode InteractiveServer` für interaktive Komponenten
- API Controllers liegen unter `HotelApp.Web/Controllers/`
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

1. Lese alle `*ApplicationService.cs` und `*QueryService.cs` unter `HotelApp.Application/`
2. Prüfe welche Services noch keinen Controller unter `HotelApp.Web/Controllers/` haben
3. Generiere für jeden fehlenden Service:
   - `HotelApp.Web/Controllers/[Name]Controller.cs` — vollständiger Controller
   - `HotelApp.Web/DTOs/[Name]Requests.cs` — alle Request-Records
   - `HotelApp.Web/DTOs/[Name]Responses.cs` — alle Response-Records
4. Aktualisiere `HotelApp.Web/Program.cs` falls neue Services registriert werden müssen
4b. Generiere für jeden Service eine Blazor-Komponente unter `HotelApp.Web/Components/Pages/`
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
HotelApp.Application/*Service.cs  →  [api-scaffolder]  →  HotelApp.Web/Controllers/*.cs
                                              →  HotelApp.Web/DTOs/*.cs
                                              →  api-endpoints.md
```

---

## Program.cs Vorlage — direkt kopieren

```csharp
// HotelApp.Web/Program.cs
using HotelApp.Application;
using HotelApp.Infrastructure;
using HotelApp.Web.Components;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new() { Title = "HotelApp API", Version = "v1" });
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

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseAntiforgery();
app.UseCors("AllowAll");

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapControllers();
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();
app.Run();
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese alle Application Services unter HotelApp.Application/.
Generiere vollständige Controller unter HotelApp.Web/Controllers/ mit DTOs für alle Services die noch keinen
Controller haben. Erstelle danach api-endpoints.md mit der vollständigen
Endpunkt-Übersicht.
```

---

## 4. `.github/skills/api-scaffolder/SKILL.md`

Per `/api-scaffolder` abrufbar — generiert Controller, DTOs und Swagger-Dokumentation.

```markdown
---
name: api-scaffolder
description: >
  Scaffolds complete ASP.NET Core Web API controllers, DTOs, and Swagger
  documentation from application services in .NET projects. Use when
  creating new API endpoints, generating request/response records,
  adding OpenAPI documentation, or auditing missing controllers.
  Trigger words: ASP.NET Core, controller, API endpoint, DTO, scaffold,
  REST, Swagger, OpenAPI, CreatedAtAction, HTTP status codes, minimal API,
  web API, MVC controller, route, api scaffold.
---

# API Scaffolder

Generiert vollständige ASP.NET Core Controller mit DTOs und Swagger-Doku.

## Wann verwenden

- Neue Endpunkte aus Application Services ableiten
- Request- und Response-Records (DTOs) anlegen
- Swagger/OpenAPI-Dokumentation (XML-Kommentare) hinzufügen
- Übersicht aller Endpunkte als `api-endpoints.md` erstellen

## Voraussetzungen

- Application Services unter `HotelApp.Application/` vorhanden
- `HotelApp.Web/Controllers/` Ordner existiert
- Konventionen aus [`references/api-conventions.md`](./references/api-conventions.md)

## HTTP-Statuscodes Checkliste

| Situation                             | Statuscode                                        |
| ------------------------------------- | ------------------------------------------------- |
| Lesen                                 | 200 OK                                            |
| Anlegen                               | 201 Created + Location-Header (`CreatedAtAction`) |
| Löschen / kein Inhalt                 | 204 NoContent                                     |
| Validierungsfehler                    | 400 BadRequest                                    |
| Nicht gefunden                        | 404 NotFound                                      |
| Konflikt (z.B. doppelte Zimmernummer) | 409 Conflict                                      |

## Vorgehen

1. Lese alle `*ApplicationService.cs` unter `HotelApp.Application/`
2. Prüfe welche Services noch keinen Controller haben
3. Generiere `HotelApp.Web/Controllers/[Name]Controller.cs`
4. Generiere `HotelApp.Web/DTOs/[Name]Requests.cs` und `[Name]Responses.cs`
5. Aktualisiere `api-endpoints.md`

## Ausgabe

| Datei                                              | Inhalt                                       |
| -------------------------------------------------- | -------------------------------------------- |
| `HotelApp.Web/Controllers/<Name>Controller.cs`     | sealed Controller, Primärkonstruktor         |
| `HotelApp.Web/DTOs/<Name>Requests.cs`              | Request-Records mit Validierung              |
| `HotelApp.Web/DTOs/<Name>Responses.cs`             | Response-Records (unveränderlich)            |
| `HotelApp.Web/Components/Pages/<Name>.razor`       | Blazor Component für den Service             |
| `api-endpoints.md`                                 | Methode + URL + Beschreibung aller Endpunkte |

## Beispiel-Aufruf
```

/api-scaffolder
Generiere alle fehlenden Controller für Application Services in HotelApp.Application/

```

```

**Skill-Struktur anlegen:**

```
.github/skills/api-scaffolder/
├── SKILL.md
└── references/
    └── api-conventions.md    ← Regeln aus api-mvc.instructions.md
```
