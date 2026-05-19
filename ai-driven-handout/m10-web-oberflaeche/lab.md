# m10 — Lab: Web-Oberfläche & Schnittstellen

---

## Demo

**Szenario:** Aus fertigen Application Services einen vollständigen ASP.NET MVC Controller + REST API generieren.

**Prompt:**

```
Du bist Senior ASP.NET Core Entwickler. Erstelle einen vollständigen
`BookingsController` für folgende Anforderungen:

Vorhandene Services (bereits implementiert):
- BookingApplicationService.CreateBookingAsync(roomId, guestId, checkIn, checkOut)
- BookingApplicationService.CancelBookingAsync(bookingId, guestId)
- BookingQueryService.GetBookingDetailsAsync(bookingId)
- BookingQueryService.GetGuestBookingsAsync(guestId)

Endpunkte:
- GET    /api/bookings/{id}            → Buchungsdetails
- GET    /api/bookings?guestId={id}    → Alle Buchungen eines Gastes
- POST   /api/bookings                 → Neue Buchung erstellen
- DELETE /api/bookings/{id}            → Buchung stornieren

Anforderungen:
- Minimal API ODER Controller (beides zeigen)
- Request/Response DTOs (keine Entitäten direkt zurückgeben)
- CORS für http://localhost:4200 erlauben
- Fehlerbehandlung: 404, 400, 401 mit sinnvollen Meldungen
- Nur Code, keine Erklärungen
```

CORS konfigurieren in `Program.cs` → API ist von außen erreichbar.

---

## Deine Aufgabe

Füge einen `RoomsController` für die Zimmerverwaltung hinzu:

```
Du bist Senior ASP.NET Core Entwickler. Erstelle einen `RoomsController`:

Endpunkte:
- GET  /api/rooms                  → Alle verfügbaren Zimmer
- GET  /api/rooms/{id}             → Zimmerdetails
- GET  /api/rooms/available?checkIn=DATUM&checkOut=DATUM → Freie Zimmer für Zeitraum
- POST /api/rooms                  → Neues Zimmer anlegen (Admin only)

Request DTO für POST:
- RoomNumber: string
- Category: string ("Single", "Double", "Suite")
- PricePerNight: decimal

Response DTO:
- Id, RoomNumber, Category, PricePerNight, IsAvailable

Fehlerbehandlung:
- 400 wenn RoomNumber leer oder PricePerNight <= 0
- 409 wenn RoomNumber bereits existiert
- Nur Code, keine Erklärungen
```

Danach: Teste alle Endpunkte in Swagger UI (`/swagger`).

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

### Program.cs — CORS + Swagger Setup

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod());
});

builder.Services.AddDbContext<AppDbContext>(opt =>
    opt.UseSqlite(builder.Configuration.GetConnectionString("Default")));

builder.Services.AddScoped<BookingApplicationService>();
builder.Services.AddScoped<RoomApplicationService>();

var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();
app.UseCors("AllowAll");
app.MapControllers();
app.Run();
```

### RoomsController

```csharp
[ApiController]
[Route("api/[controller]")]
public sealed class RoomsController(AppDbContext db) : ControllerBase
{
    [HttpGet]
    public async Task<IActionResult> GetAll()
    {
        var rooms = await db.Rooms
            .Select(r => new RoomResponse(r.Id, r.RoomNumber, r.Category.ToString(), r.PricePerNight, r.IsAvailable))
            .ToListAsync();
        return Ok(rooms);
    }

    [HttpGet("{id:guid}")]
    public async Task<IActionResult> GetById(Guid id)
    {
        var room = await db.Rooms.FindAsync(id);
        if (room is null) return NotFound();
        return Ok(new RoomResponse(room.Id, room.RoomNumber, room.Category.ToString(), room.PricePerNight, room.IsAvailable));
    }

    [HttpGet("available")]
    public async Task<IActionResult> GetAvailable([FromQuery] DateOnly checkIn, [FromQuery] DateOnly checkOut)
    {
        var bookedRoomIds = await db.Bookings
            .Where(b => b.Status != BookingStatus.Cancelled
                && b.CheckInDate < checkOut
                && b.CheckOutDate > checkIn)
            .Select(b => b.RoomId)
            .ToListAsync();

        var available = await db.Rooms
            .Where(r => r.IsAvailable && !bookedRoomIds.Contains(r.Id))
            .Select(r => new RoomResponse(r.Id, r.RoomNumber, r.Category.ToString(), r.PricePerNight, r.IsAvailable))
            .ToListAsync();

        return Ok(available);
    }

    [HttpPost]
    public async Task<IActionResult> Create([FromBody] CreateRoomRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.RoomNumber))
            return BadRequest("RoomNumber darf nicht leer sein.");
        if (request.PricePerNight <= 0)
            return BadRequest("PricePerNight muss größer als 0 sein.");

        var exists = await db.Rooms.AnyAsync(r => r.RoomNumber == request.RoomNumber);
        if (exists) return Conflict($"Zimmer '{request.RoomNumber}' existiert bereits.");

        if (!Enum.TryParse<RoomCategory>(request.Category, ignoreCase: true, out var category))
            return BadRequest($"Ungültige Kategorie: {request.Category}");

        var room = new Room(request.RoomNumber, category, request.PricePerNight);
        db.Rooms.Add(room);
        await db.SaveChangesAsync();

        return CreatedAtAction(nameof(GetById), new { id = room.Id },
            new RoomResponse(room.Id, room.RoomNumber, room.Category.ToString(), room.PricePerNight, room.IsAvailable));
    }
}

public record CreateRoomRequest(string RoomNumber, string Category, decimal PricePerNight);
public record RoomResponse(Guid Id, string RoomNumber, string Category, decimal PricePerNight, bool IsAvailable);
```

### Razor View — Zimmerliste anzeigen

```csharp
// Controllers/RoomsController.cs (MVC)
public sealed class RoomsController(RoomApplicationService service) : Controller
{
    [HttpGet]
    public async Task<IActionResult> Index()
    {
        var rooms = await service.GetAllAsync();
        return View(rooms.Select(r => new RoomViewModel
        {
            Id = r.Id,
            RoomNumber = r.RoomNumber,
            Category = r.Category.ToString(),
            PricePerNight = r.PricePerNight,
            IsAvailable = r.IsAvailable
        }));
    }
}
```

```html
<!-- Views/Rooms/Index.cshtml -->
@model IEnumerable<RoomViewModel>
  <h1>Zimmer</h1>
  <table class="table">
    <thead>
      <tr>
        <th>Nummer</th>
        <th>Kategorie</th>
        <th>Preis/Nacht</th>
        <th>Verfügbar</th>
      </tr>
    </thead>
    <tbody>
      @foreach (var room in Model) {
      <tr>
        <td>@room.RoomNumber</td>
        <td>@room.Category</td>
        <td>@room.PricePerNight.ToString("C")</td>
        <td>@(room.IsAvailable ? "✅" : "❌")</td>
      </tr>
      }
    </tbody>
  </table></RoomViewModel
>
```

</details>
