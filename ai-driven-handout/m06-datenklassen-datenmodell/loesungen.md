# Modul 6 — Lösungen

---

## Lösung 6.1-A — Booking-Klasse (Musterlösung)

```csharp
public enum BookingStatus { Pending, Confirmed, CheckedIn, CheckedOut, Cancelled }

public record BookingConfirmed(Guid BookingId, DateTime OccurredAt) : IDomainEvent;
public record BookingCancelled(Guid BookingId, decimal CancellationFee, DateTime OccurredAt) : IDomainEvent;

public class Booking : AuditableEntity
{
    public Guid RoomId { get; private set; }
    public Guid GuestId { get; private set; }
    public DateTime CheckInDate { get; private set; }
    public DateTime CheckOutDate { get; private set; }
    public BookingStatus Status { get; private set; }
    public decimal TotalPrice { get; private set; }
    public decimal CancellationFee { get; private set; }
    public Address BillingAddress { get; private set; } = null!;

    public int NightCount => (CheckOutDate - CheckInDate).Days;

    private readonly List<IDomainEvent> _events = [];
    public IReadOnlyCollection<IDomainEvent> DomainEvents => _events.AsReadOnly();

    protected Booking() { }

    public Booking(Guid roomId, Guid guestId, DateTime checkIn, DateTime checkOut,
                   decimal pricePerNight, Address billingAddress)
    {
        if (checkIn.Date >= checkOut.Date)
            throw new ArgumentException("Check-out muss nach Check-in liegen.");
        if (checkIn.Date < DateTime.UtcNow.Date)
            throw new ArgumentException("Check-in kann nicht in der Vergangenheit liegen.");
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(pricePerNight);

        Id = Guid.NewGuid();
        RoomId = roomId;
        GuestId = guestId;
        CheckInDate = checkIn.Date;
        CheckOutDate = checkOut.Date;
        TotalPrice = pricePerNight * NightCount;
        BillingAddress = billingAddress;
        Status = BookingStatus.Pending;
    }

    public void Confirm()
    {
        if (Status != BookingStatus.Pending)
            throw new InvalidOperationException("Nur Anfragen können bestätigt werden.");
        Status = BookingStatus.Confirmed;
        _events.Add(new BookingConfirmed(Id, DateTime.UtcNow));
    }

    public void Cancel(decimal cancellationFeeAmount = 0)
    {
        if (Status is BookingStatus.CheckedIn or BookingStatus.CheckedOut or BookingStatus.Cancelled)
            throw new InvalidOperationException($"Buchung im Status {Status} kann nicht storniert werden.");
        CancellationFee = cancellationFeeAmount;
        Status = BookingStatus.Cancelled;
        _events.Add(new BookingCancelled(Id, CancellationFee, DateTime.UtcNow));
    }

    public void CheckIn()
    {
        if (Status != BookingStatus.Confirmed)
            throw new InvalidOperationException("Nur bestätigte Buchungen können eingecheckt werden.");
        Status = BookingStatus.CheckedIn;
    }

    public void CheckOut()
    {
        if (Status != BookingStatus.CheckedIn)
            throw new InvalidOperationException("Nur eingecheckte Gäste können ausgecheckt werden.");
        Status = BookingStatus.CheckedOut;
    }
}
```

---

## Lösung 6.1-B — Code-Review Ergebnisse

| Stelle | Problem | Typ | Korrektur |
|---|---|---|---|
| `int Id` | int statt Guid | Technisch | `Guid Id { get; private set; }` |
| `string Type` | String statt Enum | DDD | `RoomCategory Type { get; private set; }` |
| `double PricePerNight` | Rundungsfehler | Technisch | `decimal PricePerNight { get; private set; }` |
| `bool IsAvailable { get; set; }` | Abgeleiteter Zustand als speicherbares Feld | DDD | Berechnen aus aktiven Buchungen |
| `List<> { get; set; }` | Public Liste + Setter | DDD | `private readonly List<> _bookings = []; IReadOnlyCollection<> ...` |
| `new Exception(...)` | Zu generisch | .NET 9 | `new InvalidOperationException(...)` |
| `string guestName` | Name als primitiver String | DDD | `Guid guestId` – Gast ist eigene Entität |
| `public Room() { }` | Public Ctor | DDD/EF | `protected Room() { }` |

---

## Lösung 6.4-A — Basisklassen und automatische Felder

```csharp
public abstract class Entity
{
    public Guid Id { get; protected set; }
    public override bool Equals(object? obj) =>
        obj is Entity e && GetType() == e.GetType() && Id == e.Id;
    public override int GetHashCode() => Id.GetHashCode();
    public static bool operator ==(Entity? a, Entity? b) => a?.Equals(b) ?? b is null;
    public static bool operator !=(Entity? a, Entity? b) => !(a == b);
}

public abstract class AuditableEntity : Entity
{
    public DateTime CreatedAt { get; private set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; private set; } = DateTime.UtcNow;
    public string? CreatedBy { get; private set; }
    public string? UpdatedBy { get; private set; }

    internal void SetAudit(string? userId, bool isNew)
    {
        if (isNew) { CreatedAt = DateTime.UtcNow; CreatedBy = userId; }
        UpdatedAt = DateTime.UtcNow;
        UpdatedBy = userId;
    }
}

// Im DbContext:
public override async Task<int> SaveChangesAsync(CancellationToken ct = default)
{
    foreach (var entry in ChangeTracker.Entries<AuditableEntity>())
    {
        entry.Entity.SetAudit(
            _currentUser?.UserId,
            entry.State == EntityState.Added);
        if (entry.State == EntityState.Modified)
        {
            entry.Property(e => e.CreatedAt).IsModified = false;
            entry.Property(e => e.CreatedBy).IsModified = false;
        }
    }
    return await base.SaveChangesAsync(ct);
}
```

---

## Lösung 6.4-B — EF Core Konfigurationsfehler

| Konfiguration | Fehler | Korrektur |
|---|---|---|
| 1 | `float` verursacht Rundungsfehler bei Geldbeträgen | `HasPrecision(10, 2)` (ohne explizites `HasColumnType`) |
| 2 | Enum als `int` → Zahlenwerte in DB, unleserlich und brüchig | `HasConversion<string>().HasMaxLength(30)` |
| 3 | `Cascade Delete` löscht Buchungen wenn Gast gelöscht wird → Datenverlust | `OnDelete(DeleteBehavior.Restrict)` oder Soft Delete |
| 4 | `ValueGeneratedOnAdd()` für Guid → Datenbank generiert, nicht Anwendung → verliert DDD-Kontrolle | `ValueGeneratedNever()` (wir setzen Id im Ctor selbst) |
| 5 | `AddSingleton` für DbContext → nicht thread-safe, gleichzeitige Requests teilen einen Context | `AddDbContext<>()` → automatisch Scoped |
