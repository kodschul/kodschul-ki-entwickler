# Modul 10 — Lösungen

---

## Lösung 10.1-A — Frontend-Planung

| Controller | Action | HTTP | URL | View | ViewModel |
|---|---|---|---|---|---|
| RoomsController | Search | GET | /rooms/search | Search.cshtml | RoomSearchViewModel |
| RoomsController | SearchResults | GET | /rooms/search?checkIn=&checkOut= | SearchResults.cshtml | RoomSearchResultsViewModel |
| RoomsController | Details | GET | /rooms/{id} | Details.cshtml | RoomDetailsViewModel |
| BookingsController | Index | GET | /bookings | Index.cshtml | List\<BookingListViewModel\> |
| BookingsController | Details | GET | /bookings/{id} | Details.cshtml | BookingDetailsViewModel |
| BookingsController | Create | GET | /bookings/create?roomId= | Create.cshtml | CreateBookingViewModel |
| BookingsController | Create | POST | /bookings/create | — | CreateBookingViewModel |
| BookingsController | Cancel | POST | /bookings/{id}/cancel | — | — |

---

## Lösung 10.2-A — BookingsController (Musterlösung)

```csharp
[Route("bookings")]
[Authorize]
public sealed class BookingsController(
    IBookingApplicationService bookingService,
    ILogger<BookingsController> logger) : Controller
{
    [HttpGet]
    public async Task<IActionResult> Index(CancellationToken ct)
    {
        var guestId = User.GetGuestId();
        var bookings = await bookingService.GetGuestBookingsAsync(guestId, page: 1, pageSize: 20, ct);
        return View(bookings.Select(BookingListViewModel.FromDto).ToList());
    }

    [HttpGet("{id:guid}")]
    public async Task<IActionResult> Details(Guid id, CancellationToken ct)
    {
        var booking = await bookingService.GetBookingDetailsAsync(id, ct);
        if (booking is null) return NotFound();
        return View(BookingDetailsViewModel.FromDto(booking));
    }

    [HttpGet("create")]
    public async Task<IActionResult> Create([FromQuery] Guid? roomId, CancellationToken ct)
    {
        var model = new CreateBookingViewModel { RoomId = roomId ?? Guid.Empty };
        return View(model);
    }

    [HttpPost("create")]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create(CreateBookingViewModel model, CancellationToken ct)
    {
        if (!ModelState.IsValid) return View(model);

        try
        {
            var id = await bookingService.CreateBookingAsync(model.ToCommand(User.GetGuestId()), ct);
            TempData["Success"] = "Buchung erfolgreich erstellt!";
            return RedirectToAction(nameof(Details), new { id });
        }
        catch (InvalidOperationException ex)
        {
            ModelState.AddModelError(string.Empty, ex.Message);
            return View(model);
        }
    }

    [HttpPost("{id:guid}/cancel")]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Cancel(Guid id, CancellationToken ct)
    {
        try
        {
            await bookingService.CancelBookingAsync(id, User.GetGuestId(), ct);
            TempData["Success"] = "Buchung erfolgreich storniert.";
        }
        catch (InvalidOperationException ex)
        {
            TempData["Error"] = ex.Message;
        }
        catch (UnauthorizedAccessException)
        {
            return Forbid();
        }
        return RedirectToAction(nameof(Index));
    }
}
```

---

## Lösung 10.2-B — ViewModels

```csharp
public sealed class BookingListViewModel
{
    public Guid Id { get; init; }
    public string RoomName { get; init; } = string.Empty;
    public string CategoryName { get; init; } = string.Empty;
    public string CheckInFormatted { get; init; } = string.Empty;
    public string CheckOutFormatted { get; init; } = string.Empty;
    public string TotalPriceFormatted { get; init; } = string.Empty;
    public string StatusDisplay { get; init; } = string.Empty;
    public bool CanCancel { get; init; }

    private static readonly CultureInfo German = CultureInfo.GetCultureInfo("de-DE");

    public static BookingListViewModel FromDto(BookingDto dto) => new()
    {
        Id = dto.Id,
        RoomName = dto.RoomName,
        CategoryName = dto.CategoryName,
        CheckInFormatted = dto.CheckInDate.ToString("dd.MM.yyyy"),
        CheckOutFormatted = dto.CheckOutDate.ToString("dd.MM.yyyy"),
        TotalPriceFormatted = dto.TotalPrice.ToString("C", German),
        StatusDisplay = dto.Status switch
        {
            "Pending"   => "Anfrage",
            "Confirmed" => "Bestätigt",
            "CheckedIn" => "Eingecheckt",
            "CheckedOut"=> "Ausgecheckt",
            "Cancelled" => "Storniert",
            _           => dto.Status
        },
        CanCancel = dto.Status is "Pending" or "Confirmed"
    };
}

public sealed class CreateBookingViewModel
{
    [Required(ErrorMessage = "Bitte wählen Sie ein Zimmer.")]
    public Guid RoomId { get; set; }

    public string RoomName { get; set; } = string.Empty;

    [Required(ErrorMessage = "Anreisedatum ist erforderlich.")]
    [DataType(DataType.Date)]
    [Display(Name = "Anreisedatum")]
    public DateTime CheckInDate { get; set; } = DateTime.Today.AddDays(1);

    [Required(ErrorMessage = "Abreisedatum ist erforderlich.")]
    [DataType(DataType.Date)]
    [Display(Name = "Abreisedatum")]
    public DateTime CheckOutDate { get; set; } = DateTime.Today.AddDays(2);

    public CreateBookingCommand ToCommand(Guid guestId) => new(
        RoomId,
        guestId,
        CheckInDate,
        CheckOutDate
    );
}
```

---

## Lösung 10.3-B — Scaffolding-Probleme und Korrektur

**Gefundene Probleme:**

| Problem | Stelle | Erklärung |
|---|---|---|
| Direkter DbContext | `HotelDbContext _context` | Verletzt Schichttrennung; Application Service verwenden |
| Entity in View | `_context.Rooms.ToListAsync()` | Domain-Entity direkt in View → ViewModel verwenden |
| `int? id` | `Details(int? id)` | Guid verwenden, nicht int |
| Keine CancellationToken | beide Actions | Async-Best-Practice verletzt |
| Kein Logging | gesamter Controller | Kritische Operationen sollen geloggt werden |

**Korrigierter Controller:**
```csharp
[Route("rooms")]
public sealed class RoomsController(
    IRoomQueryService roomService,
    ILogger<RoomsController> logger) : Controller
{
    [HttpGet]
    public async Task<IActionResult> Index(CancellationToken ct)
    {
        var rooms = await roomService.GetAllRoomsAsync(ct);
        return View(rooms.Select(RoomListViewModel.FromDto).ToList());
    }

    [HttpGet("{id:guid}")]
    public async Task<IActionResult> Details(Guid id, CancellationToken ct)
    {
        var room = await roomService.GetRoomDetailsAsync(id, ct);
        if (room is null)
        {
            logger.LogWarning("Zimmer {RoomId} nicht gefunden.", id);
            return NotFound();
        }
        return View(RoomDetailsViewModel.FromDto(room));
    }
}
```

---

## Lösung 10.4-A — Minimal API Endpunkte

```csharp
public static class BookingEndpoints
{
    public static IEndpointRouteBuilder MapBookingEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/bookings")
            .WithTags("Bookings")
            .RequireAuthorization();

        group.MapGet("/{id:guid}", async (
            Guid id,
            IBookingApplicationService service,
            CancellationToken ct) =>
        {
            var booking = await service.GetBookingDetailsAsync(id, ct);
            return booking is null
                ? Results.NotFound(new ProblemDetails { Title = "Buchung nicht gefunden", Status = 404 })
                : Results.Ok(BookingDetailsResponse.FromDto(booking));
        })
        .WithName("GetBooking")
        .WithSummary("Lädt die Details einer Buchung.")
        .Produces<BookingDetailsResponse>()
        .ProducesProblem(404);

        group.MapPost("/", async (
            CreateBookingRequest request,
            ClaimsPrincipal user,
            IBookingApplicationService service,
            CancellationToken ct) =>
        {
            var id = await service.CreateBookingAsync(request.ToCommand(user.GetGuestId()), ct);
            return Results.CreatedAtRoute("GetBooking", new { id }, new { id });
        })
        .WithName("CreateBooking")
        .WithSummary("Erstellt eine neue Buchung.")
        .Produces<object>(201)
        .ProducesProblem(400);

        group.MapPost("/{id:guid}/confirm", async (
            Guid id,
            IBookingApplicationService service,
            CancellationToken ct) =>
        {
            await service.ConfirmBookingAsync(id, ct);
            return Results.NoContent();
        })
        .WithName("ConfirmBooking")
        .WithSummary("Bestätigt eine Buchung.")
        .Produces(204)
        .ProducesProblem(400)
        .ProducesProblem(404);

        group.MapDelete("/{id:guid}", async (
            Guid id,
            ClaimsPrincipal user,
            IBookingApplicationService service,
            CancellationToken ct) =>
        {
            await service.CancelBookingAsync(id, user.GetGuestId(), ct);
            return Results.NoContent();
        })
        .WithName("CancelBooking")
        .WithSummary("Storniert eine Buchung.")
        .Produces(204)
        .ProducesProblem(400)
        .ProducesProblem(404);

        group.MapGet("/", async (
            [FromQuery] Guid? guestId,
            [FromQuery] int page,
            [FromQuery] int pageSize,
            IBookingApplicationService service,
            CancellationToken ct) =>
        {
            var bookings = await service.GetGuestBookingsAsync(
                guestId ?? Guid.Empty, page, pageSize, ct);
            return Results.Ok(bookings);
        })
        .WithName("ListBookings")
        .WithSummary("Listet Buchungen paginiert.")
        .Produces<PagedResult<BookingDto>>();

        return app;
    }
}
```

---

## Lösung 10.4-C — API-Tests

```csharp
public sealed class BookingApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;
    private readonly JsonSerializerOptions _jsonOptions = new(JsonSerializerDefaults.Web);

    public BookingApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.WithWebHostBuilder(builder =>
        {
            builder.ConfigureServices(services =>
            {
                // Produktions-DbContext durch SQLite In-Memory ersetzen
                var descriptor = services.Single(d => d.ServiceType == typeof(DbContextOptions<HotelDbContext>));
                services.Remove(descriptor);
                services.AddDbContext<HotelDbContext>(opts =>
                    opts.UseSqlite("Data Source=:memory:"));
            });
        }).CreateClient();
    }

    [Fact]
    public async Task CreateBooking_ValidRequest_Returns201WithLocationHeader()
    {
        // Arrange
        var request = new CreateBookingRequest(
            RoomId: TestGuids.Room1,
            CheckInDate: DateTime.Today.AddDays(10),
            CheckOutDate: DateTime.Today.AddDays(13));

        // Act
        var response = await _client.PostAsJsonAsync("/api/bookings", request);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.Created);
        response.Headers.Location.Should().NotBeNull();
        response.Headers.Location!.ToString().Should().Contain("/api/bookings/");
    }

    [Fact]
    public async Task CreateBooking_CheckOutBeforeCheckIn_Returns400WithProblemDetails()
    {
        // Arrange
        var request = new CreateBookingRequest(
            RoomId: TestGuids.Room1,
            CheckInDate: DateTime.Today.AddDays(5),
            CheckOutDate: DateTime.Today.AddDays(3));  // CheckOut vor CheckIn!

        // Act
        var response = await _client.PostAsJsonAsync("/api/bookings", request);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
        var problem = await response.Content.ReadFromJsonAsync<ProblemDetails>(_jsonOptions);
        problem.Should().NotBeNull();
        problem!.Status.Should().Be(400);
    }

    [Fact]
    public async Task GetById_ExistingBooking_Returns200WithDetails()
    {
        // Arrange: erst Buchung erstellen
        var createRequest = new CreateBookingRequest(TestGuids.Room1, DateTime.Today.AddDays(5), DateTime.Today.AddDays(8));
        var createResponse = await _client.PostAsJsonAsync("/api/bookings", createRequest);
        var created = await createResponse.Content.ReadFromJsonAsync<BookingCreatedResponse>(_jsonOptions);

        // Act
        var response = await _client.GetAsync($"/api/bookings/{created!.Id}");

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var booking = await response.Content.ReadFromJsonAsync<BookingDetailsResponse>(_jsonOptions);
        booking.Should().NotBeNull();
        booking!.Id.Should().Be(created.Id);
    }

    [Fact]
    public async Task GetById_NotFound_Returns404()
    {
        var response = await _client.GetAsync($"/api/bookings/{Guid.NewGuid()}");
        response.StatusCode.Should().Be(HttpStatusCode.NotFound);
    }

    [Fact]
    public async Task ConfirmBooking_AlreadyConfirmed_Returns400()
    {
        // Arrange: Buchung erstellen und bestätigen
        var createRequest = new CreateBookingRequest(TestGuids.Room1, DateTime.Today.AddDays(5), DateTime.Today.AddDays(8));
        var createResponse = await _client.PostAsJsonAsync("/api/bookings", createRequest);
        var created = await createResponse.Content.ReadFromJsonAsync<BookingCreatedResponse>(_jsonOptions);

        await _client.PostAsync($"/api/bookings/{created!.Id}/confirm", null);  // erste Bestätigung

        // Act: zweite Bestätigung
        var response = await _client.PostAsync($"/api/bookings/{created.Id}/confirm", null);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
        var problem = await response.Content.ReadFromJsonAsync<ProblemDetails>(_jsonOptions);
        problem!.Status.Should().Be(400);
    }
}
```
