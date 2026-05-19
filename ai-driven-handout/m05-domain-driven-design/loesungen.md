# Modul 5 — Lösungen

---

## Lösung 5.1-A — Ubiquitous Language Bibliothek

| Umgangssprache | Fachbegriff (DE) | Code-Name | Definition | Abgrenzung |
|---|---|---|---|---|
| „Buch" | Exemplar | `BookCopy` | Ein physisches Exemplar mit Inventarnummer | Nicht der Titel (Werk), sondern die physische Kopie |
| „Leute" | Mitglied | `Member` | Registrierte Person mit Ausleihberechtigung | Nicht „Benutzer" – es gibt keine anonyme Nutzung |
| „angemeldet sein" | Mitgliedschaft | `Membership` | Aktive Berechtigung zur Ausleihe mit Ablaufdatum | Nicht gleichzusetzen mit der Person |
| „nehmen" | Ausleihen | `Borrow` / `CreateLoan` | Formaler Leihvorgang mit Rückgabedatum | Nicht „mieten" – keine Kosten bei pünktlicher Rückgabe |
| „zu spät zurückbringen" | Überfälligkeit | `Overdue` | Status wenn `DueDate` überschritten | Nicht „Verlust" – Exemplar ist noch beim Mitglied |
| „zahlen" | Mahngebühr | `Fine` | Betrag bei überfälliger Rückgabe | Nicht „Strafe" – es ist eine Gebühr |
| „schon weg" | Nicht verfügbar | `Unavailable` | Alle Exemplare eines Titels ausgeliehen | Nicht „nicht vorhanden" – Exemplare existieren |
| „Warteliste" | Vormerkung | `Reservation` | Reservierung für ein Exemplar wenn verfügbar | Nicht „Buchung" – noch keine feste Zusage |
| „kaputt sein" | Beschädigung | `DamageReport` | Dokumentierter Schaden der Verfügbarkeit einschränkt | Abgrenzung zu „verloren" – noch physisch vorhanden |
| „verfügbar" | Ausleihbar | `IsAvailable` | Berechneter Zustand: nicht ausgeliehen, nicht beschädigt | Abgeleiteter Zustand, kein eigenes Feld |

---

## Lösung 5.2-A — Entity vs. Value Object

| Konzept | Entscheidung | Begründung |
|---|---|---|
| Lieferadresse | **Value Object** | Keine Identität; zwei gleiche Adressen sind austauschbar; unveränderlich |
| Fahrer | **Entity** | Hat eindeutige Identität (Führerscheinnummer), Lebenszyklus (Einstellung/Kündigung) |
| Preis (Betrag, Währung) | **Value Object** | Unveränderlich; 10 EUR == 10 EUR egal woher |
| Paket | **Entity** | Hat Tracking-Nummer, Lebenszyklus (aufgegeben → zugestellt) |
| GPS-Koordinate | **Value Object** | Reine Daten, keine Identität; unveränderlich |
| Zustellversuch | **Entity** | Hat Zeitstempel und Ergebnis; bildet Geschichte ab |
| E-Mail-Adresse | **Value Object** | Unveränderlich, Gleichheit über Inhalt |
| Benutzer-Session | **Entity** | Hat Session-ID, Lebenszyklus (Start → Ablauf) |
| Währungsbetrag | **Value Object** | Unveränderlich; Operationen erzeugen neue Instanz |
| Lieferzeitraum | **Value Object** | Unveränderlich; nur zwei Daten ohne eigene Identität |

---

## Lösung 5.2-B — Kurierdienst Domänenmodell (Auszug)

```csharp
public interface IDomainEvent { DateTime OccurredAt { get; } }

// Domain Events
public record ShipmentPickedUp(Guid ShipmentId, Guid DriverId, DateTime OccurredAt) : IDomainEvent;
public record ShipmentDelivered(Guid ShipmentId, DateTime OccurredAt) : IDomainEvent;
public record DeliveryFailed(Guid ShipmentId, string Reason, DateTime OccurredAt) : IDomainEvent;

// Value Object
public sealed record Address(string Street, string HouseNumber, string PostalCode, string City, string Country = "DE")
{
    public Address(string street, string houseNumber, string postalCode, string city, string country = "DE")
        : this(street, houseNumber, postalCode, city, country)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(street);
        ArgumentException.ThrowIfNullOrWhiteSpace(houseNumber);
        if (country == "DE" && !System.Text.RegularExpressions.Regex.IsMatch(postalCode, @"^\d{5}$"))
            throw new ArgumentException("Deutsche PLZ muss genau 5 Ziffern haben.");
    }

    public string Format() => $"{Street} {HouseNumber}, {PostalCode} {City}, {Country}";
}

// Enum
public enum DeliverySpeed { Standard, Express, SameDay }

public static class DeliverySpeedExtensions
{
    public static int GetMaxDeliveryDays(this DeliverySpeed speed) => speed switch
    {
        DeliverySpeed.Standard => 5,
        DeliverySpeed.Express  => 2,
        DeliverySpeed.SameDay  => 1,
        _ => throw new ArgumentOutOfRangeException(nameof(speed))
    };
}

// Aggregate Root
public class Shipment : Entity
{
    public Guid SenderId { get; private set; }
    public Address PickupAddress { get; private set; } = null!;
    public Address DeliveryAddress { get; private set; } = null!;
    public ShipmentStatus Status { get; private set; }
    public DeliverySpeed Speed { get; private set; }
    public decimal Weight { get; private set; }
    public Guid? DriverId { get; private set; }
    public DateTime CreatedAt { get; private set; }

    private readonly List<DeliveryAttempt> _attempts = [];
    public IReadOnlyCollection<DeliveryAttempt> Attempts => _attempts.AsReadOnly();

    private readonly List<IDomainEvent> _events = [];
    public IReadOnlyCollection<IDomainEvent> DomainEvents => _events.AsReadOnly();

    protected Shipment() { }

    public Shipment(Guid senderId, Address pickup, Address delivery, decimal weight, DeliverySpeed speed)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(weight);
        Id = Guid.NewGuid();
        SenderId = senderId;
        PickupAddress = pickup;
        DeliveryAddress = delivery;
        Weight = weight;
        Speed = speed;
        Status = ShipmentStatus.Created;
        CreatedAt = DateTime.UtcNow;
    }

    public void AssignDriver(Guid driverId)
    {
        if (Status != ShipmentStatus.Created)
            throw new InvalidOperationException("Fahrer kann nur neuen Paketen zugewiesen werden.");
        DriverId = driverId;
        Status = ShipmentStatus.PickedUp;
        _events.Add(new ShipmentPickedUp(Id, driverId, DateTime.UtcNow));
    }

    public void MarkDelivered()
    {
        if (Status != ShipmentStatus.InDelivery)
            throw new InvalidOperationException("Nur Pakete in Zustellung können zugestellt werden.");
        Status = ShipmentStatus.Delivered;
        _events.Add(new ShipmentDelivered(Id, DateTime.UtcNow));
    }

    public void RecordFailedDelivery(string reason)
    {
        if (Status != ShipmentStatus.InDelivery)
            throw new InvalidOperationException("Zustellversuch nur bei Paketen in Zustellung.");
        _attempts.Add(new DeliveryAttempt(Id, reason, DateTime.UtcNow));
        Status = ShipmentStatus.DeliveryFailed;
        _events.Add(new DeliveryFailed(Id, reason, DateTime.UtcNow));
    }
}
```

---

## Lösung 5.4-A — Modellierungsfehler

| Stelle | Problem | Typ | Korrektur |
|---|---|---|---|
| A: `int Id` | int statt Guid → kein globales Unique | Technisch | `Guid Id { get; private set; }` |
| B: `string Status` | String statt Enum → keine Typsicherheit | DDD | `ShipmentStatus Status { get; private set; }` |
| C: `double Weight` | Rundungsfehler bei double | Technisch | `decimal Weight { get; private set; }` |
| D: `CreatedAt { get; set; }` | Öffentlicher Setter → von außen manipulierbar | DDD | `{ get; private set; }` |
| E: `List<> { get; set; }` | Öffentliche Liste + Setter → Kapselung verletzt | DDD | `private readonly List<> _attempts = []; IReadOnlyCollection<> Attempts => ...` |
| F: `int DriverId` | int statt Guid → Typ-Inkonsistenz | Technisch | `Guid? DriverId { get; private set; }` |
| G: `Driver { get; set; }` | Navigation mit public setter | DDD/EF | `Driver? Driver { get; private set; }` |
| H: `public Shipment() { }` | Public Default-Ctor → ungültige Objekte erzeugbar | DDD | `protected Shipment() { }` |
| I: `SetStatus(string)` | Beliebiger Status setzbar, keine Domänenregeln | DDD | Explizite Methoden: `AssignDriver()`, `MarkDelivered()`, etc. |

---

## Lösung 5.4-B — EF Core Konfiguration (Musterlösung)

```csharp
public sealed class ShipmentConfiguration : IEntityTypeConfiguration<Shipment>
{
    public void Configure(EntityTypeBuilder<Shipment> builder)
    {
        builder.HasKey(s => s.Id);
        builder.Property(s => s.Id).ValueGeneratedNever();

        builder.Property(s => s.Status)
               .HasConversion<string>().HasMaxLength(30).IsRequired();

        builder.Property(s => s.Speed)
               .HasConversion<string>().HasMaxLength(20).IsRequired();

        builder.Property(s => s.Weight)
               .HasPrecision(10, 3).IsRequired();

        builder.OwnsOne(s => s.PickupAddress, a =>
        {
            a.Property(x => x.Street).HasColumnName("Pickup_Street").HasMaxLength(200).IsRequired();
            a.Property(x => x.HouseNumber).HasColumnName("Pickup_HouseNumber").HasMaxLength(20).IsRequired();
            a.Property(x => x.PostalCode).HasColumnName("Pickup_PostalCode").HasMaxLength(10).IsRequired();
            a.Property(x => x.City).HasColumnName("Pickup_City").HasMaxLength(100).IsRequired();
            a.Property(x => x.Country).HasColumnName("Pickup_Country").HasMaxLength(3).IsRequired();
        });

        builder.OwnsOne(s => s.DeliveryAddress, a =>
        {
            a.Property(x => x.Street).HasColumnName("Delivery_Street").HasMaxLength(200).IsRequired();
            a.Property(x => x.HouseNumber).HasColumnName("Delivery_HouseNumber").HasMaxLength(20).IsRequired();
            a.Property(x => x.PostalCode).HasColumnName("Delivery_PostalCode").HasMaxLength(10).IsRequired();
            a.Property(x => x.City).HasColumnName("Delivery_City").HasMaxLength(100).IsRequired();
            a.Property(x => x.Country).HasColumnName("Delivery_Country").HasMaxLength(3).IsRequired();
        });

        builder.OwnsMany(s => s.Attempts, a =>
        {
            a.WithOwner().HasForeignKey("ShipmentId");
            a.HasKey("Id");
            a.Property(x => x.Reason).HasMaxLength(500);
            a.Property(x => x.OccurredAt).IsRequired();
            a.ToTable("DeliveryAttempts");
        });

        builder.Ignore(s => s.DomainEvents);

        builder.HasIndex("SenderId");
        builder.HasIndex("DriverId");
        builder.ToTable("Shipments");
    }
}
```
