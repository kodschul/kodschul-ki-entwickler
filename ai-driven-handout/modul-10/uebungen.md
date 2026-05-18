# Modul 10 — Übungen

---

## Übung 10.1-A — Frontend einordnen und planen

**Aufgabe:** Planen Sie die Web-Oberfläche für das Hotelreservierungssystem.

Gegeben: Alle Application Services sind implementiert:
- `BookingApplicationService`: CreateBooking, ConfirmBooking, CancelBooking, GetBookingDetails
- `RoomQueryService`: GetAvailableRooms, GetRoomDetails
- `GuestApplicationService`: RegisterGuest, GetGuestProfile

**Erstellen Sie einen KI-Prompt der folgendes plant:**
1. Controller und deren Actions
2. Zugehörige Views und ViewModels
3. URL-Routing-Struktur
4. Welche Actions POST vs. GET sind

**User Stories:**
- Als Gast möchte ich verfügbare Zimmer für mein Reisedatum suchen
- Als Gast möchte ich ein Zimmer buchen
- Als Gast möchte ich meine Buchungsübersicht sehen
- Als Gast möchte ich eine Buchung stornieren
- Als Gast möchte ich die Details einer Buchung sehen

**Füllen Sie folgende Tabelle aus:**

| Controller | Action | HTTP | URL | View | ViewModel |
|---|---|---|---|---|---|
| RoomsController | Search | GET | /rooms/search | Search.cshtml | RoomSearchViewModel |
| ... | | | | | |

---

## Übung 10.1-B — Übergang planen: Backend → Frontend

**Aufgabe:** Skizzieren Sie den Datenfluss für den Use Case „Zimmer buchen":

```
[Nutzer füllt Buchungsformular aus]
         ↓
[POST /bookings/create]
         ↓
[?? Controller ??]
         ↓
[?? Application Service ??]
         ↓
[?? Domain ??]
         ↓
[?? Datenbank ??]
         ↓
[?? Response ??]
         ↓
[Redirect auf Buchungsbestätigung]
```

Ergänzen Sie jeden Pfeil mit:
- Welche Klasse / Methode ist verantwortlich?
- Welches Datenformat wird übergeben (ViewModel, Command, Entity, DTO)?
- Was passiert bei einem Fehler in dieser Schicht?

---

## Übung 10.2-A — MVC Controller und Views implementieren

**Aufgabe:** Implementieren Sie den `BookingsController` mit KI-Unterstützung.

**Benötigte Actions:**

| Action | HTTP | Beschreibung |
|---|---|---|
| `Index` | GET | Liste aller Buchungen des eingeloggten Gastes |
| `Details(Guid id)` | GET | Detailansicht einer Buchung |
| `Create` | GET | Buchungsformular anzeigen |
| `Create(CreateBookingViewModel)` | POST | Buchung erstellen |
| `Cancel(Guid id)` | POST | Buchung stornieren (mit Bestätigung) |

**Erstellen Sie zuerst den Prompt, dann den Code. Prüfen Sie:**
- [ ] Slim Controller (keine Businesslogik im Controller)?
- [ ] ViewModels statt Entities?
- [ ] ModelState-Validierung bei POST?
- [ ] TempData für Erfolgsmeldungen?
- [ ] Korrekte Redirects nach POST?
- [ ] 404-Handling für nicht gefundene Buchungen?

---

## Übung 10.2-B — ViewModels mit Mapping

**Aufgabe:** Implementieren Sie folgende ViewModels:

1. **`BookingListViewModel`** (für die Index-Seite):
   - Id, RoomName, CategoryName
   - CheckInDate und CheckOutDate formatiert (dd.MM.yyyy)
   - TotalPrice formatiert (€ mit deutschem Format)
   - Status als lesbarer Text (z. B. „Bestätigt" statt „Confirmed")
   - CanCancel: bool (nur wenn Status Pending oder Confirmed)
   - Static Factory-Methode `FromDto(BookingDto dto)`

2. **`CreateBookingViewModel`** (für das Formular):
   - RoomId: Guid (als Hidden Field)
   - CheckInDate: DateTime (Required, muss in Zukunft liegen)
   - CheckOutDate: DateTime (Required, muss nach CheckIn liegen)
   - SelectList für Zimmerkategorien
   - DataAnnotations oder eigene Validierung

Nutzen Sie KI für die Generierung. Prüfen Sie: Sind alle Properties die die View braucht vorhanden?

---

## Übung 10.2-C — Razor View mit Tag Helpers

**Aufgabe:** Erstellen Sie die `Index.cshtml`-View für die Buchungsübersicht.

Anforderungen:
- Bootstrap 5 Tabelle mit allen Buchungen
- Spalten: Zimmer, Kategorie, Check-in, Check-out, Preis, Status, Aktionen
- Aktionsbuttons: „Details" (Link) und „Stornieren" (nur wenn `CanCancel = true`)
- Leerzustand wenn keine Buchungen: „Noch keine Buchungen. Jetzt buchen!"
- TempData-Alert für Erfolgsmeldungen oben
- Paginierung wenn mehr als 10 Buchungen

Nutzen Sie KI für die Generierung. Prüfen Sie: `asp-action`, `asp-route-id`, `asp-for` korrekt?

---

## Übung 10.3-A — Scaffolding einsetzen und anpassen

**Aufgabe:** Nutzen Sie Scaffolding als Ausgangspunkt und passen Sie den Output an.

1. Generieren Sie mit `dotnet aspnet-codegenerator` einen `RoomsController` für die Room-Entität
2. Analysieren Sie den generierten Code: Was funktioniert? Was muss ersetzt werden?
3. Erstellen Sie einen KI-Prompt der den Scaffolding-Output anpasst auf:
   - IRoomQueryService statt direktem DbContext
   - RoomListViewModel statt Room-Entität
   - Korrekte Fehlerbehandlung

**Dokumentieren Sie:** Wie viel Zeit haben Sie beim Scaffolding + KI-Anpassung gespart gegenüber manuell schreiben?

---

## Übung 10.3-B — Scaffolding-Output kritisch bewerten

**Gegeben ist dieser Scaffolding-Output:**
```csharp
// Scaffolded RoomsController.cs (Auszug)
public class RoomsController : Controller
{
    private readonly HotelDbContext _context;

    public RoomsController(HotelDbContext context)
    {
        _context = context;
    }

    public async Task<IActionResult> Index()
    {
        return View(await _context.Rooms.ToListAsync());
    }

    public async Task<IActionResult> Details(int? id)
    {
        if (id == null) return NotFound();
        var room = await _context.Rooms
            .FirstOrDefaultAsync(m => m.Id == id);
        if (room == null) return NotFound();
        return View(room);
    }
}
```

**Aufgabe:** Identifizieren Sie alle Probleme und erstellen Sie einen vollständig überarbeiteten Controller.

---

## Übung 10.4-A — Minimal API Endpunkte implementieren

**Aufgabe:** Implementieren Sie vollständige Minimal API Endpunkte für das Buchungssystem.

Erstellen Sie die Endpunkte in einer separaten `BookingEndpoints.cs`-Klasse mit Extension Method:

```csharp
public static class BookingEndpoints
{
    public static IEndpointRouteBuilder MapBookingEndpoints(this IEndpointRouteBuilder app)
    {
        // Hier alle Endpunkte definieren
        return app;
    }
}
```

**Benötigte Endpunkte:**

| Methode | Route | Beschreibung | Response |
|---|---|---|---|
| GET | /api/bookings/{id} | Details laden | 200 / 404 |
| POST | /api/bookings | Neue Buchung | 201 / 400 |
| POST | /api/bookings/{id}/confirm | Bestätigen | 204 / 400 / 404 |
| DELETE | /api/bookings/{id} | Stornieren | 204 / 400 / 404 |
| GET | /api/bookings | Liste paginiert | 200 |

**Anforderungen:** Problem Details bei Fehlern, CancellationToken, OpenAPI-Dokumentation

---

## Übung 10.4-B — OpenAPI und Scalar konfigurieren

**Aufgabe:** Konfigurieren Sie die vollständige OpenAPI-Dokumentation.

1. Fügen Sie `AddOpenApi()` und `MapScalarApiReference()` zu `Program.cs` hinzu
2. Ergänzen Sie alle API-Endpunkte mit:
   - `WithSummary("...")` – kurze Beschreibung
   - `WithDescription("...")` – ausführliche Beschreibung
   - `Produces<T>(statusCode)` – Erfolgsantwort
   - `ProducesProblem(statusCode)` – Fehlerantworten
   - `WithTags("Bookings")` – Gruppierung
3. Implementieren Sie einen globalen Exception Handler der `KeyNotFoundException` → 404 und `InvalidOperationException` → 400 mappt
4. Testen Sie die Dokumentation unter `/scalar/v1`

Nutzen Sie KI für die Implementierung. Prüfen Sie: Ist die Scalar-Oberfläche vollständig und korrekt?

---

## Übung 10.4-C — API-Tests mit HttpClient

**Aufgabe:** Schreiben Sie API-Tests mit `WebApplicationFactory<Program>`.

```csharp
public sealed class BookingApiTests(WebApplicationFactory<Program> factory)
    : IClassFixture<WebApplicationFactory<Program>>
{
    [Fact]
    public async Task CreateBooking_ValidRequest_Returns201WithLocationHeader() { ... }

    [Fact]
    public async Task CreateBooking_InvalidDates_Returns400WithProblemDetails() { ... }

    [Fact]
    public async Task GetById_ExistingBooking_Returns200WithDetails() { ... }

    [Fact]
    public async Task GetById_NotFound_Returns404() { ... }

    [Fact]
    public async Task ConfirmBooking_AlreadyConfirmed_Returns400() { ... }
}
```

Erstellen Sie den KI-Prompt und implementieren Sie alle fünf Tests. Stellen Sie sicher, dass:
- Eine Testdatenbank (SQLite in-memory) verwendet wird
- Der `Location`-Header bei 201-Antworten geprüft wird
- Problem Details bei Fehlerantworten deserialisiert und geprüft werden
