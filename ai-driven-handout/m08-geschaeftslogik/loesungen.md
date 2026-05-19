# Modul 8 — Lösungen

---

## Lösung 8.1-A — Geschäftsregeln kategorisiert

| Regel | Kategorie | Implementierungsort | Begründung |
|---|---|---|---|
| Check-in heute oder später | Muss-Regel | `Booking` Ctor | Invariante des Buchungsobjekts |
| Check-out nach Check-in | Muss-Regel | `Booking` Ctor | Invariante, immer prüfbar |
| 48h/24h Stornierungsgebühr | Muss-Regel | `Booking.CalculateCancellationFee()` | Domänenregel, nur Buchungs-Daten nötig |
| Stammkunden-Rabatt | Kann-Regel | `BookingPricingService` | Braucht Guest-Daten + Booking |
| Suiten nicht online | Verbots-Regel | Application Layer | Kennt Buchungskanal (online vs. telefonisch) |
| Max. 3 aktive Buchungen | Invariante | Application Layer | Braucht Repository für Datenbankabfrage |
| Gesamtpreis berechnen | Muss-Regel | `BookingPricingService` | Braucht Room + Guest → Domain Service |

---

## Lösung 8.2-B — PricingService (Musterlösung)

```csharp
public sealed class BookingPricingService
{
    private const decimal WeekendSurcharge = 0.20m;
    private const decimal LoyaltyDiscount = 0.10m;
    private const decimal EarlyBirdDiscount = 0.15m;
    private const decimal MaxTotalDiscount = 0.25m;
    private const int LoyaltyThreshold = 5;
    private const int EarlyBirdDays = 60;

    public decimal Calculate(Room room, int guestCompletedBookings,
                              DateTime checkIn, DateTime checkOut, DateTime bookingDate)
    {
        ArgumentOutOfRangeException.ThrowIfGreaterThanOrEqual(checkIn.Date, checkOut.Date);

        var basePrice = CalculateBasePrice(room.PricePerNight, checkIn, checkOut);
        var discount = CalculateDiscount(guestCompletedBookings, bookingDate, checkIn);
        return Math.Round(basePrice * (1 - discount), 2, MidpointRounding.AwayFromZero);
    }

    private static decimal CalculateBasePrice(decimal pricePerNight, DateTime checkIn, DateTime checkOut)
    {
        decimal total = 0;
        for (var day = checkIn.Date; day < checkOut.Date; day = day.AddDays(1))
        {
            var isWeekend = day.DayOfWeek is DayOfWeek.Saturday or DayOfWeek.Sunday;
            total += pricePerNight * (isWeekend ? 1 + WeekendSurcharge : 1);
        }
        return total;
    }

    private static decimal CalculateDiscount(int completedBookings, DateTime bookingDate, DateTime checkIn)
    {
        decimal discount = 0;
        if (completedBookings > LoyaltyThreshold) discount += LoyaltyDiscount;
        if ((checkIn.Date - bookingDate.Date).TotalDays > EarlyBirdDays) discount += EarlyBirdDiscount;
        return Math.Min(discount, MaxTotalDiscount);
    }
}
```

**Tests:**
```csharp
[Theory]
[InlineData(6, 61, 0.25)]  // Beide Rabatte → Cap bei 25%
[InlineData(6, 59, 0.10)]  // Nur Loyalty
[InlineData(4, 61, 0.15)]  // Nur EarlyBird
[InlineData(4, 59, 0.00)]  // Kein Rabatt
[InlineData(5, 61, 0.15)]  // Grenzwert: genau 5 → kein Loyalty (braucht > 5)
[InlineData(6, 60, 0.10)]  // Grenzwert: genau 60 → kein EarlyBird (braucht > 60)
public void Calculate_AppliesDiscountsCorrectly(int completedBookings, int daysInAdvance, decimal expectedDiscount)
{
    var service = new BookingPricingService();
    // Montag, sodass kein Wochenendaufschlag
    var bookingDate = new DateTime(2025, 3, 3); // Montag
    var checkIn = bookingDate.AddDays(daysInAdvance);
    var checkOut = checkIn.AddDays(1);
    var room = new TestRoom(pricePerNight: 100m);

    var price = service.Calculate(room, completedBookings, checkIn, checkOut, bookingDate);

    price.Should().Be(100m * (1 - expectedDiscount));
}
```

---

## Lösung 8.3-B — Fehler in CalculateCancellationFee

**Gefundene Probleme:**

1. **DateTime statt DateTimeOffset:** Bei Zeitzonenwechsel (Sommerzeit) kann die 48h-Grenze falsch berechnet werden → `DateTimeOffset` verwenden
2. **Kein Guard gegen Post-Check-in:** Wenn `cancellationTime > CheckInDate`, ist `hoursUntilCheckIn` negativ → fällt in 100%-Zweig, was zufällig korrekt ist, aber undokumentiert und irreführend
3. **Kein expliziter Fehler bei Stornierung nach Check-out:** Sollte `InvalidOperationException` werfen

**Korrigierte Version:**
```csharp
public decimal CalculateCancellationFee(DateTimeOffset cancellationTime)
{
    var checkInUtc = new DateTimeOffset(CheckInDate.Date, TimeSpan.Zero);

    if (cancellationTime > new DateTimeOffset(CheckOutDate.Date, TimeSpan.Zero))
        throw new InvalidOperationException("Stornierung nach Check-out nicht möglich.");

    var hoursUntilCheckIn = (checkInUtc - cancellationTime).TotalHours;

    return hoursUntilCheckIn switch
    {
        >= 48 => 0m,
        >= 24 => TotalPrice * 0.5m,
        _     => TotalPrice   // Auch für Stornierung nach Check-in (No-Show)
    };
}
```

**5 Grenzwert-Tests:**
```csharp
[Fact] void Fee_MoreThan48h_Zero() { /* 72h vorher → 0 */ }
[Fact] void Fee_Exactly48h_Zero() { /* Genau 48h → 0 (≥ 48 ist kostenlos) */ }
[Fact] void Fee_47h_HalfPrice() { /* 47h → 50% */ }
[Fact] void Fee_Exactly24h_HalfPrice() { /* Genau 24h → 50% (≥ 24) */ }
[Fact] void Fee_Under24h_FullPrice() { /* 12h → 100% */ }
```
