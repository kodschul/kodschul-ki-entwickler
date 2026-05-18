# Modul 9 — Lösungen

---

## Lösung 9.1-A — Teststrategie

| Schicht | Testart | Framework | Abdeckungsziel | Beispiel |
|---|---|---|---|---|
| Domain | Unit-Test | xUnit + FluentAssertions | > 90% | `Booking.Cancel_After48h_ZeroFee` |
| Application | Unit-Test + Mock | xUnit + NSubstitute | > 80% | `BookingService.Create_SuiteOnline_ThrowsException` |
| Infrastructure | Integrationstest | xUnit + SQLite/Testcontainers | > 70% | `EfRepo.Save_NewBooking_CanBeRetrieved` |
| API | API-Test | WebApplicationFactory | > 60% | `POST /bookings → 201 Created` |
| E2E | E2E | Playwright | Hauptworkflows | Buchung erstellen → bestätigen → stornieren |

**Begründung:** E2E-Tests sind 10-100x langsamer als Unit-Tests und schwerer zu warten. Die meisten Fehler werden in Unit-Tests gefunden. Integration- und API-Tests sichern die Zusammenarbeit der Schichten ab.

---

## Lösung 9.2-A — Testdaten für CalculateCancellationFee

```csharp
public static IEnumerable<object[]> CancellationFeeTestData =>
[
    // Happy Path: kostenlose Stornierung (>= 48h vorher)
    [72.0, 100m, 0m,   "72h vorher → kostenlos"],
    [48.0, 100m, 0m,   "Genau 48h → kostenlos (Grenzwert)"],
    [168.0, 200m, 0m,  "1 Woche vorher → kostenlos"],

    // Boundary: 50% Zone (24-48h)
    [47.9, 100m, 50m,  "47,9h → 50% (knapp unter 48h-Grenze)"],
    [36.0, 100m, 50m,  "36h → 50%"],
    [24.0, 100m, 50m,  "Genau 24h → 50% (Grenzwert)"],

    // 100% Zone (< 24h)
    [23.9, 100m, 100m, "23,9h → 100% (knapp unter 24h-Grenze)"],
    [12.0, 100m, 100m, "12h → 100%"],
    [0.5,  100m, 100m, "30min → 100%"],

    // Edge Cases
    [0.0,  100m, 100m, "Genau Check-in-Zeitpunkt → 100%"],
    [-1.0, 100m, 100m, "Nach Check-in (No-Show) → 100%"],
];

[Theory, MemberData(nameof(CancellationFeeTestData))]
public void CalculateCancellationFee_ReturnsCorrectFee(
    double hoursBeforeCheckIn, decimal totalPrice, decimal expectedFee, string description)
{
    // Arrange
    var checkIn = DateTime.UtcNow.Date.AddDays(7);
    var booking = BookingTestDataBuilder.Create()
        .WithDates(checkIn, checkIn.AddDays(2))
        .WithTotalPrice(totalPrice)
        .AsConfirmed()
        .Build();
    var cancellationTime = new DateTimeOffset(checkIn, TimeSpan.Zero)
        .AddHours(-hoursBeforeCheckIn);

    // Act
    var fee = booking.CalculateCancellationFee(cancellationTime);

    // Assert
    fee.Should().Be(expectedFee, because: description);
}
```

---

## Lösung 9.3-A — Testdaten-Validierung

| Zeile | Sinnvoll? | Problem |
|---|---|---|
| A: checkOut vor checkIn | ❌ | Ungültige Kombination – sollte Exception testen, nicht Preis |
| B: checkIn == checkOut | ❌ | 0 Nächte – sollte Exception testen (gleiche Daten) |
| C: 1 Nacht, €100 | ✅ | Valider Happy Path |
| D: Preis 0.00 | ❌ | Preis 0 sollte Exception im Ctor werfen → kein gültiger Booking-Zustand |
| E: Negativer Preis | ❌ | Negativer Preis → Constructor-Exception → kein gültiges Objekt |
| F: 7 Nächte, €100 | ✅ | Valider Testfall (andere Dauer) |
| G: Identisch zu F | ❌ | Duplikat von Zeile F, bringt keinen Mehrwert |

**Fazit:** 4 von 7 Testdatensätzen sind problematisch. Die Fälle A, B testen eher den Konstruktor als die Preisberechnung. D und E erzeugen ungültige Objekte. G ist redundant.

---

## Lösung 9.3-B — Fehlende Tests für AddLine

**Nicht abgedeckte Zweige:**
1. `Status != OrderStatus.Open` → `InvalidOperationException`
2. `quantity <= 0` (negative Menge!) → `ArgumentOutOfRangeException`
3. `!product.HasSufficientStock(quantity)` → `InvalidOperationException`
4. Grenzwert: `quantity = 1` (genau erlaubt)

**Fehlende Tests:**
```csharp
[Fact]
public void AddLine_ConfirmedOrder_ThrowsInvalidOperationException()
{
    // Arrange
    var order = CreateConfirmedOrder();
    var product = CreateProductWithStock(10);

    // Act
    var act = () => order.AddLine(product, 1);

    // Assert
    act.Should().Throw<InvalidOperationException>()
       .WithMessage("*offene*");
}

[Fact]
public void AddLine_NegativeQuantity_ThrowsArgumentOutOfRange()
{
    // Arrange
    var order = CreateOpenOrder();
    var product = CreateProductWithStock(10);

    // Act
    var act = () => order.AddLine(product, -1);

    // Assert
    act.Should().Throw<ArgumentOutOfRangeException>()
       .WithParameterName("quantity");
}

[Fact]
public void AddLine_InsufficientStock_ThrowsInvalidOperationException()
{
    // Arrange
    var order = CreateOpenOrder();
    var product = CreateProductWithStock(2); // nur 2 auf Lager

    // Act
    var act = () => order.AddLine(product, 5); // 5 bestellt

    // Assert
    act.Should().Throw<InvalidOperationException>()
       .WithMessage("*Lagerbestand*");
}

[Fact]
public void AddLine_QuantityOfOne_AddsSuccessfully()
{
    // Arrange
    var order = CreateOpenOrder();
    var product = CreateProductWithStock(1);

    // Act
    order.AddLine(product, 1); // Grenzwert: minimum gültige Menge

    // Assert
    order.Lines.Should().HaveCount(1);
}
```

---

## Lösung 9.4-A — CRUD-Tests für Repository (Muster)

```csharp
public sealed class EfBookingRepositoryTests : IAsyncLifetime
{
    private HotelDbContext _context = null!;
    private EfBookingRepository _sut = null!;

    public async Task InitializeAsync()
    {
        var options = new DbContextOptionsBuilder<HotelDbContext>()
            .UseSqlite("Data Source=:memory:")
            .Options;
        _context = new HotelDbContext(options);
        await _context.Database.EnsureCreatedAsync();
        _sut = new EfBookingRepository(_context);
    }

    public async Task DisposeAsync() => await _context.DisposeAsync();

    [Fact]
    public async Task SaveAsync_NewBooking_CanBeRetrievedById()
    {
        // Arrange
        var booking = BookingTestDataBuilder.Create().Build();

        // Act
        await _sut.SaveAsync(booking);
        var retrieved = await _sut.GetByIdAsync(booking.Id);

        // Assert
        retrieved.Should().NotBeNull();
        retrieved!.Id.Should().Be(booking.Id);
        retrieved.Status.Should().Be(BookingStatus.Pending);
    }

    [Fact]
    public async Task GetByIdAsync_NonExistingId_ReturnsNull()
    {
        var result = await _sut.GetByIdAsync(Guid.NewGuid());
        result.Should().BeNull();
    }

    [Fact]
    public async Task SoftDeleteAsync_ExistingBooking_IsNotFoundAfterwards()
    {
        // Arrange
        var booking = BookingTestDataBuilder.Create().Build();
        await _sut.SaveAsync(booking);

        // Act
        await _sut.SoftDeleteAsync(booking.Id);
        var result = await _sut.GetByIdAsync(booking.Id);

        // Assert
        result.Should().BeNull();
    }

    [Fact]
    public async Task SaveAsync_UpdatedBooking_PersistsChanges()
    {
        // Arrange
        var booking = BookingTestDataBuilder.Create().Build();
        await _sut.SaveAsync(booking);
        booking.Confirm();

        // Act
        await _sut.SaveAsync(booking);
        var retrieved = await _sut.GetByIdAsync(booking.Id);

        // Assert
        retrieved!.Status.Should().Be(BookingStatus.Confirmed);
    }
}
```
