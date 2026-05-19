# m06 — Lab: Datenklassen & Datenmodell

---

## Demo

**Szenario:** Aus dem DDD-Modell eine vollständige C# Entitätsklasse generieren.

**Prompt:**

```
Du bist Senior C#-Entwickler. .NET 9, C# 13, DDD.
Erstelle die Klasse `Room` als Entity:

Properties:
- Id: Guid
- RoomNumber: string (nicht leer, max. 10 Zeichen)
- Category: RoomCategory (Enum: Single, Double, Suite)
- PricePerNight: decimal (größer 0)
- IsAvailable: bool

Methoden:
- UpdatePrice(decimal newPrice) — Preis darf nicht negativ sein
- SetAvailability(bool available)

Anforderungen:
- private setter überall
- protected parameterloser Konstruktor für EF Core
- Validierung im Konstruktor mit ArgumentException
- XML-Dokumentation
- Nur Code, keine Erklärungen
```

Copilot generiert die Klasse → gemeinsam Checkliste durchgehen:

- [ ] `private set` überall?
- [ ] `protected` EF-Konstruktor vorhanden?
- [ ] Validierung im Konstruktor?
- [ ] `decimal` für Geld?

---

## Deine Aufgabe

Generiere die Klasse `Booking` als Aggregate Root mit diesem Prompt (anpassen erlaubt):

```
Du bist Senior C#-Entwickler. .NET 9, C# 13, DDD.
Erstelle die Klasse `Booking` als AggregateRoot:

Properties:
- Id: Guid
- RoomId: Guid
- GuestId: Guid
- CheckInDate: DateOnly
- CheckOutDate: DateOnly
- Status: BookingStatus (Enum: Requested, Confirmed, CheckedIn, CheckedOut, Cancelled)
- TotalPrice: decimal
- CancellationFee: decimal?

Methoden:
- Confirm() — nur wenn Status = Requested
- Cancel(DateTimeOffset cancellationTime) — berechnet Stornierungsgebühr
- CheckIn() — nur wenn Status = Confirmed und heute = CheckInDate

Anforderungen:
- private setter überall
- protected EF-Konstruktor
- Check-out muss nach Check-in liegen (Validierung im Konstruktor)
- Nur Code, keine Erklärungen
```

Wende danach die Checkliste an und notiere was Copilot richtig/falsch gemacht hat.

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

```csharp
/// <summary>Represents a hotel room booking (Aggregate Root).</summary>
public sealed class Booking
{
    /// <summary>Unique identifier.</summary>
    public Guid Id { get; private set; }

    /// <summary>Associated room.</summary>
    public Guid RoomId { get; private set; }

    /// <summary>Associated guest.</summary>
    public Guid GuestId { get; private set; }

    /// <summary>Check-in date.</summary>
    public DateOnly CheckInDate { get; private set; }

    /// <summary>Check-out date. Must be after check-in.</summary>
    public DateOnly CheckOutDate { get; private set; }

    /// <summary>Current booking status.</summary>
    public BookingStatus Status { get; private set; }

    /// <summary>Total price for the stay.</summary>
    public decimal TotalPrice { get; private set; }

    /// <summary>Cancellation fee if applicable.</summary>
    public decimal? CancellationFee { get; private set; }

    /// <summary>Required by EF Core.</summary>
    protected Booking() { }

    /// <summary>Creates a new booking request.</summary>
    public Booking(Guid roomId, Guid guestId, DateOnly checkIn, DateOnly checkOut, decimal totalPrice)
    {
        if (checkOut <= checkIn)
            throw new ArgumentException("Check-out must be after check-in.");
        if (totalPrice <= 0)
            throw new ArgumentException("Total price must be positive.");

        Id = Guid.NewGuid();
        RoomId = roomId;
        GuestId = guestId;
        CheckInDate = checkIn;
        CheckOutDate = checkOut;
        TotalPrice = totalPrice;
        Status = BookingStatus.Requested;
    }

    /// <summary>Confirms the booking. Only valid from Requested status.</summary>
    public void Confirm()
    {
        if (Status != BookingStatus.Requested)
            throw new InvalidOperationException("Only requested bookings can be confirmed.");
        Status = BookingStatus.Confirmed;
    }

    /// <summary>Cancels the booking and calculates the cancellation fee.</summary>
    public void Cancel(DateTimeOffset cancellationTime)
    {
        if (Status is BookingStatus.CheckedIn or BookingStatus.CheckedOut or BookingStatus.Cancelled)
            throw new InvalidOperationException("Cannot cancel a booking in current status.");

        var checkInDateTime = new DateTimeOffset(CheckInDate.ToDateTime(TimeOnly.MinValue));
        var hoursUntilCheckIn = (checkInDateTime - cancellationTime).TotalHours;

        CancellationFee = hoursUntilCheckIn switch
        {
            > 48 => 0m,
            > 24 => TotalPrice * 0.5m,
            _ => TotalPrice
        };

        Status = BookingStatus.Cancelled;
    }

    /// <summary>Marks the guest as checked in.</summary>
    public void CheckIn()
    {
        if (Status != BookingStatus.Confirmed)
            throw new InvalidOperationException("Only confirmed bookings can be checked in.");
        Status = BookingStatus.CheckedIn;
    }
}

public enum BookingStatus
{
    Requested,
    Confirmed,
    CheckedIn,
    CheckedOut,
    Cancelled
}
```

### Checkliste ✅

- `private set` überall ✅
- `protected` EF-Konstruktor vorhanden ✅
- Check-out > Check-in Validierung ✅
- `decimal` für Geld ✅
- Status-Guards in allen Methoden ✅

</details>
