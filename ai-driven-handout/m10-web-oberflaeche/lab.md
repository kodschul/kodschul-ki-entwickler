# m10 — Lab: Web-Oberfläche & Schnittstellen

---

## Demo

**Szenario:** Blazor Server component + REST API endpoint in HotelApp.Web generieren.

**Prompt:**

```
Du bist Senior ASP.NET Core Entwickler. HotelApp.Web ist ein Blazor Server Projekt.

Aufgabe 1 — REST API Controller hinzufügen:
Erstelle einen `BookingsController` unter `HotelApp.Web/Controllers/`:

Vorhandene Services (bereits implementiert in HotelApp.Application):
- BookingApplicationService.CreateBookingAsync(roomId, guestId, checkIn, checkOut)
- BookingApplicationService.CancelBookingAsync(bookingId, guestId)

Endpunkte:
- GET    /api/bookings/{id}            → Buchungsdetails
- POST   /api/bookings                 → Neue Buchung erstellen
- DELETE /api/bookings/{id}            → Buchung stornieren

Anforderungen:
- [ApiController] + [Route("api/[controller]")]
- sealed class, Primärkonstruktor für DI
- Request/Response Records als DTOs (keine Entitäten direkt)
- HTTP 200, 201 (CreatedAtAction), 400, 404
- Nur Code, keine Erklärungen
```

Aufgabe 2 — Blazor Component:
Erstelle eine Blazor Komponente `HotelApp.Web/Components/Pages/Bookings.razor`
die alle Buchungen eines Gastes anzeigt (als Tabelle).

---

## Deine Aufgabe

Füge einen `RoomsController` für die Zimmerverwaltung hinzu unter `HotelApp.Web/Controllers/RoomsController.cs`:

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

### Program.cs — Blazor Server + API Setup

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
builder.Services.AddSwaggerGen();

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod());
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

### Blazor Component — Zimmerliste anzeigen

```razor
@* HotelApp.Web/Components/Pages/Rooms.razor *@
@page "/rooms"
@inject RoomApplicationService RoomService
@rendermode InteractiveServer

<h1>Zimmer</h1>

@if (rooms is null)
{
    <p>Wird geladen...</p>
}
else
{
    <table class="table">
        <thead>
            <tr>
                <th>Nummer</th><th>Kategorie</th><th>Preis/Nacht</th><th>Verfügbar</th>
            </tr>
        </thead>
        <tbody>
            @foreach (var room in rooms)
            {
                <tr>
                    <td>@room.RoomNumber</td>
                    <td>@room.Category</td>
                    <td>@room.PricePerNight.ToString("C")</td>
                    <td>@(room.IsAvailable ? "✅" : "❌")</td>
                </tr>
            }
        </tbody>
    </table>
}

@code {
    private IEnumerable<RoomDto>? rooms;

    protected override async Task OnInitializedAsync()
    {
        rooms = await RoomService.GetAllAsync();
    }
}
```

</details>
