# m08 — Lab: Geschäftslogik implementieren

---

## Demo

**Szenario:** Geschäftsregeln aus Anforderungstext extrahieren und direkt als C# implementieren lassen.

**Schritt 1 — Regeln kategorisieren:**

```
Analysiere diese Anforderung. Kategorisiere alle Geschäftsregeln:
- Muss-Regeln (immer gültig, wirft Exception)
- Kann-Regeln (konfigurierbar, Default-Verhalten)
- Verbots-Regeln (Pre-Conditions, verhindert Aktion)

Anforderung:
"Buchungen können frühestens heute und höchstens 2 Jahre im Voraus gemacht werden.
Check-out muss mindestens einen Tag nach Check-in liegen.
Maximal 3 aktive Buchungen pro Gast gleichzeitig.
Stammkunden (> 5 abgeschlossene Buchungen) erhalten 10% Rabatt."
```

**Schritt 2 — Direkt implementieren lassen:**

```
Implementiere diese Geschäftsregeln als Methode `ValidateNewBooking`
in einem C# Application Service `BookingApplicationService`.

Regeln:
- CheckInDate >= heute
- CheckInDate <= heute + 2 Jahre
- CheckOutDate > CheckInDate
- Gast hat max. 3 aktive Buchungen (Status = Requested oder Confirmed)
- Stammkunde (> 5 CheckedOut-Buchungen) → 10% Rabatt auf TotalPrice

Vohandene Typen: Booking, BookingStatus, AppDbContext
Wirft: BookingValidationException mit sprechender Fehlermeldung
Nur Code, keine Erklärungen.
```

Copilot schreibt den ganzen Service — kein einziges Zeichen tippen.

---

## Deine Aufgabe

Erweitere den `BookingApplicationService` um die Stornierungslogik:

```
Implementiere die Methode `CancelBookingAsync(Guid bookingId, Guid guestId)`
im BookingApplicationService.

Regeln:
- Nur der Gast der gebucht hat darf stornieren (guestId muss übereinstimmen)
- Buchungen mit Status CheckedIn oder CheckedOut können nicht storniert werden
- Stornierungsgebühr berechnen: booking.Cancel(DateTimeOffset.UtcNow) aufrufen
- Änderung in DB speichern

Vohandene Typen: Booking, AppDbContext, BookingStatus
Wirft: UnauthorizedAccessException wenn falsche GuestId
Wirft: InvalidOperationException wenn Status nicht stornierbar
Nur Code, keine Erklärungen.
```

Vergleiche danach mit der Musterlösung.

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

```csharp
public sealed class BookingApplicationService(AppDbContext db)
{
    public async Task<Booking> CreateBookingAsync(
        Guid roomId, Guid guestId, DateOnly checkIn, DateOnly checkOut)
    {
        ValidateNewBooking(checkIn, checkOut);

        var activeBookings = await db.Bookings
            .CountAsync(b => b.GuestId == guestId
                && (b.Status == BookingStatus.Requested
                    || b.Status == BookingStatus.Confirmed));

        if (activeBookings >= 3)
            throw new BookingValidationException("Maximal 3 aktive Buchungen pro Gast.");

        var completedBookings = await db.Bookings
            .CountAsync(b => b.GuestId == guestId && b.Status == BookingStatus.CheckedOut);

        var room = await db.Rooms.FindAsync(roomId)
            ?? throw new NotFoundException($"Room {roomId} not found.");

        var nights = checkOut.DayNumber - checkIn.DayNumber;
        var totalPrice = room.PricePerNight * nights;

        if (completedBookings > 5)
            totalPrice *= 0.9m; // 10% Stammkundenrabatt

        var booking = new Booking(roomId, guestId, checkIn, checkOut, totalPrice);
        db.Bookings.Add(booking);
        await db.SaveChangesAsync();
        return booking;
    }

    public async Task CancelBookingAsync(Guid bookingId, Guid guestId)
    {
        var booking = await db.Bookings.FindAsync(bookingId)
            ?? throw new NotFoundException($"Booking {bookingId} not found.");

        if (booking.GuestId != guestId)
            throw new UnauthorizedAccessException("Nur der buchende Gast darf stornieren.");

        booking.Cancel(DateTimeOffset.UtcNow);
        await db.SaveChangesAsync();
    }

    private static void ValidateNewBooking(DateOnly checkIn, DateOnly checkOut)
    {
        var today = DateOnly.FromDateTime(DateTime.UtcNow);
        if (checkIn < today)
            throw new BookingValidationException("Check-in darf nicht in der Vergangenheit liegen.");
        if (checkIn > today.AddYears(2))
            throw new BookingValidationException("Buchung höchstens 2 Jahre im Voraus möglich.");
        if (checkOut <= checkIn)
            throw new BookingValidationException("Check-out muss nach Check-in liegen.");
    }
}
```

</details>
