# m09 — Lab: Softwaretests mit KI

---

## Demo

**Szenario:** Aus einer fertigen Methode vollständige xUnit Tests generieren lassen.

**Prompt:**

```
Du bist Senior C#-Entwickler mit TDD-Erfahrung. Schreibe xUnit Unit-Tests
für diese Methode. Verwende FluentAssertions.

Testanforderungen:
- Happy Path: normale Stornierung > 48h vor Check-in → keine Gebühr
- Grenzfall: genau 48h → keine Gebühr
- Grenzfall: 47h → 50% Gebühr
- Grenzfall: genau 24h → 50% Gebühr
- Grenzfall: 23h → 100% Gebühr
- Fehlerfall: Stornierung eines bereits stornierten Booking → Exception

Methode:
[Cancel()-Methode aus Booking-Klasse hier einfügen]

Namenskonvention: MethodName_Scenario_ExpectedResult
Nur Code, keine Erklärungen.
```

Copilot schreibt 6 Tests mit korrekten Grenzwerten — Testdaten komplett KI-generiert.

---

## Deine Aufgabe

Generiere Tests für die `Confirm()`-Methode und die Validierung im Konstruktor:

```
Du bist Senior C#-Entwickler. Schreibe xUnit Unit-Tests mit FluentAssertions
für die Booking-Klasse.

Teste folgende Szenarien:

Für Confirm():
- Happy Path: Status = Requested → nach Confirm() ist Status = Confirmed
- Fehlerfall: Status = Confirmed → zweites Confirm() wirft Exception
- Fehlerfall: Status = Cancelled → Confirm() wirft Exception

Für den Konstruktor:
- Fehlerfall: CheckOutDate = CheckInDate → ArgumentException
- Fehlerfall: CheckOutDate vor CheckInDate → ArgumentException
- Fehlerfall: TotalPrice = 0 → ArgumentException
- Happy Path: gültige Daten → Booking erstellt, Status = Requested

Namenskonvention: MethodName_Scenario_ExpectedResult
Nur Code, keine Erklärungen.
```

Prüfe danach: Haben die Tests aussagekräftige Namen? Sind alle Grenzfälle abgedeckt?

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

```csharp
public class BookingTests
{
    private static Booking CreateValidBooking(decimal price = 200m) =>
        new(
            roomId: Guid.NewGuid(),
            guestId: Guid.NewGuid(),
            checkIn: DateOnly.FromDateTime(DateTime.UtcNow.AddDays(5)),
            checkOut: DateOnly.FromDateTime(DateTime.UtcNow.AddDays(7)),
            totalPrice: price
        );

    // --- Konstruktor ---

    [Fact]
    public void Constructor_ValidData_CreatesBookingWithRequestedStatus()
    {
        var booking = CreateValidBooking();
        booking.Status.Should().Be(BookingStatus.Requested);
        booking.Id.Should().NotBeEmpty();
    }

    [Fact]
    public void Constructor_CheckOutEqualsCheckIn_ThrowsArgumentException()
    {
        var date = DateOnly.FromDateTime(DateTime.UtcNow.AddDays(5));
        var act = () => new Booking(Guid.NewGuid(), Guid.NewGuid(), date, date, 100m);
        act.Should().Throw<ArgumentException>();
    }

    [Fact]
    public void Constructor_CheckOutBeforeCheckIn_ThrowsArgumentException()
    {
        var checkIn = DateOnly.FromDateTime(DateTime.UtcNow.AddDays(5));
        var checkOut = checkIn.AddDays(-1);
        var act = () => new Booking(Guid.NewGuid(), Guid.NewGuid(), checkIn, checkOut, 100m);
        act.Should().Throw<ArgumentException>();
    }

    [Fact]
    public void Constructor_ZeroPrice_ThrowsArgumentException()
    {
        var act = () => CreateValidBooking(price: 0m);
        act.Should().Throw<ArgumentException>();
    }

    // --- Confirm() ---

    [Fact]
    public void Confirm_StatusIsRequested_ChangesStatusToConfirmed()
    {
        var booking = CreateValidBooking();
        booking.Confirm();
        booking.Status.Should().Be(BookingStatus.Confirmed);
    }

    [Fact]
    public void Confirm_StatusIsAlreadyConfirmed_ThrowsInvalidOperationException()
    {
        var booking = CreateValidBooking();
        booking.Confirm();
        var act = () => booking.Confirm();
        act.Should().Throw<InvalidOperationException>();
    }

    [Fact]
    public void Confirm_StatusIsCancelled_ThrowsInvalidOperationException()
    {
        var booking = CreateValidBooking();
        booking.Cancel(DateTimeOffset.UtcNow);
        var act = () => booking.Confirm();
        act.Should().Throw<InvalidOperationException>();
    }

    // --- Cancel() ---

    [Fact]
    public void Cancel_MoreThan48HoursBeforeCheckIn_NoCancellationFee()
    {
        var booking = CreateValidBooking();
        var checkInMinus49H = DateTimeOffset.UtcNow; // CheckIn is 5 days away
        booking.Cancel(checkInMinus49H);
        booking.CancellationFee.Should().Be(0m);
        booking.Status.Should().Be(BookingStatus.Cancelled);
    }

    [Fact]
    public void Cancel_Between24And48HoursBeforeCheckIn_HalfCancellationFee()
    {
        var booking = CreateValidBooking(price: 200m);
        var checkInDatetime = new DateTimeOffset(
            booking.CheckInDate.ToDateTime(TimeOnly.MinValue), TimeSpan.Zero);
        var cancellationTime = checkInDatetime.AddHours(-36);
        booking.Cancel(cancellationTime);
        booking.CancellationFee.Should().Be(100m);
    }

    [Fact]
    public void Cancel_LessThan24HoursBeforeCheckIn_FullCancellationFee()
    {
        var booking = CreateValidBooking(price: 200m);
        var checkInDatetime = new DateTimeOffset(
            booking.CheckInDate.ToDateTime(TimeOnly.MinValue), TimeSpan.Zero);
        var cancellationTime = checkInDatetime.AddHours(-12);
        booking.Cancel(cancellationTime);
        booking.CancellationFee.Should().Be(200m);
    }

    [Fact]
    public void Cancel_AlreadyCancelled_ThrowsInvalidOperationException()
    {
        var booking = CreateValidBooking();
        booking.Cancel(DateTimeOffset.UtcNow);
        var act = () => booking.Cancel(DateTimeOffset.UtcNow);
        act.Should().Throw<InvalidOperationException>();
    }
}
```

</details>
