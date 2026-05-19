# Modul 10 — Web-Oberfläche und Schnittstellen

---

## Lab 10.1 — Frontend als nächster Entwicklungsschritt einordnen

### Rolle der Benutzeroberfläche

Die Präsentationsschicht ist der letzte Baustein einer vollständigen Anwendung. Sie greift auf die bereits vorhandene Geschäftslogik und Datenschicht zurück und macht die Funktionalität für Benutzer nutzbar.

```
Browser / Client
       │
       ▼
Controller / Razor Pages    ← Präsentationsschicht (Modul 10)
       │
       ▼
Application Services        ← bereits implementiert (Modul 8)
       │
       ▼
Domain Layer               ← bereits implementiert (Modul 5)
       │
       ▼
EF Core / Datenbank        ← bereits implementiert (Modul 6–7)
```

### Entscheidung: MVC, Razor Pages oder API + SPA?

| Ansatz | Wann geeignet? | Vorteil |
|---|---|---|
| **ASP.NET MVC** | Klassische Web-App, serverseitiges Rendering | Einfach, gut strukturiert, KI-Unterstützung sehr gut |
| **Razor Pages** | Einfachere Szenarien, eine Page = ein Feature | Weniger Boilerplate als MVC |
| **Minimal API + SPA** | React/Angular/Vue Frontend, Mobile App | Klare Trennung, moderne UX |
| **Blazor Server/WASM** | .NET durch und durch, kein JS | Vollständig in C# |

### KI für Frontend-Planung

```
Du bist Senior ASP.NET Core Entwickler.

Ich habe folgende Application Services fertig implementiert:
- BookingApplicationService: CreateBookingAsync, ConfirmBookingAsync, CancelBookingAsync
- RoomQueryService: GetAvailableRoomsAsync, GetRoomDetailsAsync

Plane die MVC-Struktur für diese User Stories:
- [US 1]: Als Gast möchte ich verfügbare Zimmer suchen und buchen
- [US 2]: Als Gast möchte ich meine Buchungen sehen und stornieren

Erstelle:
1. Controller-Namen und zugehörige Actions
2. View-Namen und benötigte ViewModels
3. URL-Struktur (Routing)
```

---

## Lab 10.2 — Web UI mit ASP.NET MVC aufbauen

### MVC-Strukturprinzip

```
Request → Controller → (Application Service aufrufen) → ViewModel erstellen → View rendern → Response
```

**Controller – Slim Controller Pattern:**
```csharp
[Route("bookings")]
public sealed class BookingsController(IBookingApplicationService bookingService) : Controller
{
    [HttpGet]
    public async Task<IActionResult> Index(CancellationToken ct)
    {
        var bookings = await bookingService.GetMyBookingsAsync(User.GetGuestId(), ct);
        var model = bookings.Select(BookingListViewModel.FromDto).ToList();
        return View(model);
    }

    [HttpGet("{id:guid}")]
    public async Task<IActionResult> Details(Guid id, CancellationToken ct)
    {
        var booking = await bookingService.GetDetailsAsync(id, ct);
        if (booking is null) return NotFound();
        return View(BookingDetailsViewModel.FromDto(booking));
    }

    [HttpGet("create")]
    public IActionResult Create() => View(new CreateBookingViewModel());

    [HttpPost("create")]
    public async Task<IActionResult> Create(CreateBookingViewModel model, CancellationToken ct)
    {
        if (!ModelState.IsValid) return View(model);
        var id = await bookingService.CreateBookingAsync(model.ToCommand(), ct);
        return RedirectToAction(nameof(Details), new { id });
    }
}
```

### ViewModels – niemals Domain-Entities direkt verwenden

```csharp
// ❌ Falsch: Domain-Entity direkt in View
return View(booking);

// ✅ Korrekt: ViewModel als Zwischenschicht
public sealed class BookingListViewModel
{
    public Guid Id { get; init; }
    public string RoomName { get; init; } = string.Empty;
    public string CheckInFormatted { get; init; } = string.Empty;
    public string Status { get; init; } = string.Empty;
    public string TotalPriceFormatted { get; init; } = string.Empty;

    public static BookingListViewModel FromDto(BookingDto dto) => new()
    {
        Id = dto.Id,
        RoomName = dto.RoomName,
        CheckInFormatted = dto.CheckInDate.ToString("dd.MM.yyyy"),
        Status = dto.Status,
        TotalPriceFormatted = dto.TotalPrice.ToString("C", CultureInfo.GetCultureInfo("de-DE"))
    };
}
```

### Tag Helpers in Razor Views

```html
<!-- Formular mit Tag Helpers -->
<form asp-action="Create" method="post">
    <div class="mb-3">
        <label asp-for="CheckInDate" class="form-label">Anreisedatum</label>
        <input asp-for="CheckInDate" type="date" class="form-control" />
        <span asp-validation-for="CheckInDate" class="text-danger"></span>
    </div>
    <button type="submit" class="btn btn-primary">Buchung erstellen</button>
</form>

<!-- Navigation und Links -->
<a asp-action="Details" asp-route-id="@booking.Id" class="btn btn-outline-primary">Details</a>
```

### TempData für Erfolgs-/Fehlermeldungen

```csharp
// Im Controller
TempData["Success"] = "Buchung erfolgreich erstellt!";
return RedirectToAction(nameof(Index));

// Im Layout oder View
@if (TempData["Success"] is string msg)
{
    <div class="alert alert-success alert-dismissible">@msg</div>
}
```

---

## Lab 10.3 — Scaffolding als Beschleuniger

### Was ist Scaffolding?

Scaffolding generiert automatisch vollständigen CRUD-Code (Controller + Views) aus einer Entitätsklasse und einem DbContext. Es ist ein Ausgangspunkt, nicht ein Endpunkt.

```bash
# Scaffolding-Tool installieren
dotnet tool install --global dotnet-aspnet-codegenerator

# Controller + Views generieren
dotnet aspnet-codegenerator controller \
  -name BookingsController \
  -m Booking \
  -dc HotelDbContext \
  --relativeFolderPath Controllers \
  --useDefaultLayout \
  --referenceScriptLibraries \
  -p HotelReservation.Api
```

### Scaffolding + KI kombinieren

```
Ich habe folgenden Scaffolding-Output für den BookingsController:
[generierten Code einfügen]

Passe den Code an:
1. Entferne direkte DbContext-Nutzung, nutze stattdessen IBookingApplicationService
2. Füge korrekte Fehlerbehandlung hinzu (KeyNotFoundException → 404, InvalidOperationException → BadRequest)
3. Ersetze Entity-Typen durch ViewModels (BookingListViewModel, BookingDetailsViewModel)
4. Füge TempData-Erfolgsmeldungen nach Create/Edit/Delete hinzu
5. Ergänze [Authorize]-Attribute wo nötig
```

### Was Scaffolding immer braucht

Nach dem Scaffolding **muss** manuell angepasst werden:
- Direct-DbContext-Calls → Application Service
- Entity-Typen in Views → ViewModels
- Validierungslogik → FluentValidation / DataAnnotations
- Authentifizierung / Autorisierung
- UI-Design und Benutzerfreundlichkeit

---

## Lab 10.4 — API-Endpunkte bereitstellen

### Controller-based API vs. Minimal API

**Controller-based API** (klassisch, mehr Struktur):
```csharp
[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
public sealed class BookingsController(IBookingApplicationService bookingService) : ControllerBase
{
    /// <summary>Erstellt eine neue Buchung.</summary>
    [HttpPost]
    [ProducesResponseType<BookingCreatedResponse>(StatusCodes.Status201Created)]
    [ProducesResponseType<ValidationProblemDetails>(StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> Create(
        [FromBody] CreateBookingRequest request, CancellationToken ct)
    {
        var id = await bookingService.CreateBookingAsync(request.ToCommand(), ct);
        return CreatedAtAction(nameof(GetById), new { id }, new BookingCreatedResponse(id));
    }

    /// <summary>Lädt Buchungsdetails.</summary>
    [HttpGet("{id:guid}")]
    [ProducesResponseType<BookingDetailsResponse>(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> GetById(Guid id, CancellationToken ct)
    {
        var booking = await bookingService.GetDetailsAsync(id, ct);
        return booking is null ? NotFound() : Ok(BookingDetailsResponse.FromDto(booking));
    }
}
```

**Minimal API** (.NET 9, kompakt):
```csharp
var bookings = app.MapGroup("/api/bookings")
    .WithTags("Bookings")
    .RequireAuthorization();

bookings.MapPost("/", async (
    CreateBookingRequest request,
    IBookingApplicationService service,
    CancellationToken ct) =>
{
    var id = await service.CreateBookingAsync(request.ToCommand(), ct);
    return Results.CreatedAtRoute("GetBooking", new { id }, new { id });
})
.WithName("CreateBooking")
.Produces<BookingCreatedResponse>(201)
.ProducesProblem(400);

bookings.MapGet("/{id:guid}", async (Guid id, IBookingApplicationService service, CancellationToken ct) =>
{
    var booking = await service.GetDetailsAsync(id, ct);
    return booking is null ? Results.NotFound() : Results.Ok(BookingDetailsResponse.FromDto(booking));
})
.WithName("GetBooking")
.Produces<BookingDetailsResponse>()
.ProducesProblem(404);
```

### OpenAPI / Scalar

```csharp
// Program.cs
builder.Services.AddOpenApi();

app.MapOpenApi();        // generiert /openapi/v1.json
app.MapScalarApiReference();  // Scalar UI unter /scalar/v1
```

### Fehlerbehandlung mit Problem Details

```csharp
// Globale Fehlerbehandlung (Global Exception Handler)
app.UseExceptionHandler(errorApp =>
{
    errorApp.Run(async context =>
    {
        var exception = context.Features.Get<IExceptionHandlerFeature>()?.Error;
        var (statusCode, title) = exception switch
        {
            KeyNotFoundException   => (404, "Ressource nicht gefunden"),
            InvalidOperationException => (400, "Ungültige Operation"),
            UnauthorizedAccessException => (403, "Zugriff verweigert"),
            _ => (500, "Interner Serverfehler")
        };

        context.Response.StatusCode = statusCode;
        await context.Response.WriteAsJsonAsync(new ProblemDetails
        {
            Status = statusCode,
            Title = title,
            Detail = exception?.Message
        });
    });
});
```

### KI-Prompt für API-Endpunkte

```
Du bist Senior ASP.NET Core 9 Entwickler.

Erstelle Minimal API Endpunkte für IBookingApplicationService:
- POST /api/bookings → Buchung erstellen → 201 Created
- GET /api/bookings/{id} → Details laden → 200 OK / 404
- PUT /api/bookings/{id}/confirm → Bestätigen → 204 / 400 / 404
- DELETE /api/bookings/{id} → Stornieren → 204 / 400 / 404
- GET /api/bookings?guestId=...&page=1&pageSize=20 → Liste paginiert → 200

Anforderungen:
- .NET 9 Minimal API
- Problem Details für Fehler (RFC 7807)
- CancellationToken
- OpenAPI-Dokumentation (WithName, WithSummary, Produces<T>)
- [Authorize] für alle Endpunkte
- Globaler Exception Handler für KeyNotFoundException → 404, InvalidOperationException → 400

Nur Code. Kein Fließtext.
```
