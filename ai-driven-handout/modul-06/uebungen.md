# Modul 6 — Übungen

---

## Übung 6.1-A — Klassen aus Anforderungen ableiten

**Anforderung:**
```
Ein Hotelreservierungssystem verwaltet Zimmer, Gäste und Buchungen.
Gäste buchen Zimmer für Zeiträume. Zimmer haben Kategorien (Einzel, Doppel, Suite)
und einen Preis pro Nacht. Buchungen durchlaufen: Anfrage → Bestätigt → Eingecheckt
→ Ausgecheckt → Storniert. Bei Stornierung nach Bestätigung fällt eine Gebühr an.
```

**Aufgaben:**
1. Identifizieren Sie alle benötigten Klassen
2. Formulieren Sie einen vollständigen KI-Prompt für die `Booking`-Klasse (Aggregate Root)
3. Führen Sie den Prompt aus und wenden Sie die Checkliste an:
   - [ ] `private set` überall?
   - [ ] Check-in < Check-out Validierung?
   - [ ] Status-Guards bei allen Übergängen?
   - [ ] Domain Events: `BookingConfirmed`, `BookingCancelled`?
   - [ ] `protected` EF Core Ctor?
   - [ ] `DateTime.UtcNow`?
4. Korrigieren Sie alle Mängel

---

## Übung 6.1-B — Code-Review mit KI

**Aufgabe:** Erstellen Sie einen Review-Prompt für folgende problematische Klasse und führen Sie ihn aus. Dokumentieren Sie alle gefundenen Probleme.

```csharp
public class Room
{
    public int Id { get; set; }
    public string Type { get; set; }
    public double PricePerNight { get; set; }
    public bool IsAvailable { get; set; } = true;
    public List<Booking> Bookings { get; set; } = new();

    public void Book(DateTime from, DateTime to, string guestName)
    {
        if (!IsAvailable) throw new Exception("Not available");
        Bookings.Add(new Booking { From = from, To = to, GuestName = guestName });
        IsAvailable = false;
    }

    public void Release() => IsAvailable = true;
}
```

Ihr Review-Prompt soll die Klasse auf prüfen auf: DDD-Verletzungen · EF Core Anti-Patterns · .NET 9 Verbesserungen · Sicherheitsprobleme

---

## Übung 6.2-A — DbContext und Konfigurationen

**Aufgabe:** Erstellen Sie mit KI-Unterstützung:

1. `HotelDbContext` mit korrekter Registrierung
2. `RoomConfiguration : IEntityTypeConfiguration<Room>`:
   - RoomCategory als String gespeichert
   - PricePerNight mit Precision(10,2)
   - Unique Index auf Zimmernummer
3. `BookingConfiguration : IEntityTypeConfiguration<Booking>`:
   - Status als String
   - GuestId als FK mit Index
   - CancellationFee mit Precision(10,2), nullable

**Prüfen Sie:**
- `ApplyConfigurationsFromAssembly` genutzt?
- `ValueGeneratedNever()` für Guids?
- Enum-Konvertierung korrekt?

---

## Übung 6.2-B — Beziehungen modellieren

**Beziehungen im Hotelreservierungssystem:**
- Ein Gast kann mehrere Buchungen haben (1:n)
- Eine Buchung gehört zu genau einem Zimmer (n:1)
- Eine Buchung hat eine Rechnungsadresse (1:1, Value Object / Owned Type)
- Beim Löschen eines Gastes: Buchungen auf Storniert setzen, nicht löschen

Erstellen Sie die EF Core Fluent API Konfiguration für alle Beziehungen.

---

## Übung 6.3-A — Projektstruktur aufsetzen

**Aufgabe:** Richten Sie die Clean Architecture Projektstruktur für das Hotelreservierungssystem ein.

```powershell
dotnet new sln -n HotelReservation
dotnet new classlib -n HotelReservation.Domain --framework net9.0
dotnet new classlib -n HotelReservation.Application --framework net9.0
dotnet new classlib -n HotelReservation.Infrastructure --framework net9.0
dotnet new webapi -n HotelReservation.Api --framework net9.0

# Referenzen setzen
dotnet add HotelReservation.Application reference HotelReservation.Domain
dotnet add HotelReservation.Infrastructure reference HotelReservation.Application
dotnet add HotelReservation.Api reference HotelReservation.Infrastructure

# EF Core Pakete
dotnet add HotelReservation.Infrastructure package Microsoft.EntityFrameworkCore.SqlServer --version 9.*
dotnet add HotelReservation.Infrastructure package Microsoft.EntityFrameworkCore.Design --version 9.*
```

Nutzen Sie KI wenn Fehler auftreten: Zeigen Sie der KI die vollständige Fehlermeldung.

---

## Übung 6.3-B — User Secrets konfigurieren

**Aufgabe:** Konfigurieren Sie User Secrets so, dass kein echter Connection String im Repository landet.

1. User Secrets initialisieren: `dotnet user-secrets init --project HotelReservation.Api`
2. Connection String setzen: `dotnet user-secrets set "ConnectionStrings:Default" "..."`
3. `Program.cs` liest den Connection String aus
4. `appsettings.json` enthält nur einen Platzhalter
5. `.gitignore` ist korrekt konfiguriert

Erstellen Sie einen KI-Prompt der Ihnen den vollständigen `Program.cs`-Abschnitt für DbContext-Registration mit Retry-Logik (`.EnableRetryOnFailure()`) generiert.

---

## Übung 6.4-A — Basisklassen und automatische Felder

**Aufgabe:**
1. Implementieren Sie `Entity`, `AuditableEntity` (mit CreatedAt, UpdatedAt, CreatedBy) und `SoftDeletableEntity` (mit IsDeleted, DeletedAt)
2. Überschreiben Sie `SaveChangesAsync` im DbContext um `UpdatedAt` automatisch zu setzen
3. Fügen Sie einen Global Query Filter hinzu der `IsDeleted = false` automatisch anwendet
4. Schreiben Sie xUnit-Tests die beweisen, dass `UpdatedAt` beim Speichern korrekt gesetzt wird

---

## Übung 6.4-B — Typische EF Core Konfigurationsfehler

Finden Sie in jeder Konfiguration den kritischen Fehler und schreiben Sie die Korrektur:

**Konfiguration 1:**
```csharp
builder.Property(r => r.PricePerNight).HasColumnType("float").IsRequired();
```

**Konfiguration 2:**
```csharp
builder.Property(b => b.Status).HasConversion<int>().IsRequired();
```

**Konfiguration 3:**
```csharp
builder.HasOne(b => b.Guest).WithMany(g => g.Bookings).OnDelete(DeleteBehavior.Cascade);
```

**Konfiguration 4:**
```csharp
builder.Property(b => b.Id).ValueGeneratedOnAdd();
```

**Konfiguration 5:**
```csharp
services.AddSingleton<HotelDbContext>(provider => new HotelDbContext(options));
```
