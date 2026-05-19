# m07 — Lab: Migrationen & Datenbank

---

## Demo

**Szenario:** Migration erstellen und mit KI auf Qualität prüfen.

**Schritt 1 — Migration erstellen:**

```powershell
dotnet ef migrations add InitialCreate --project HotelApp.Infrastructure --startup-project HotelApp.Web
dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web
```

**Schritt 2 — Generierte Migration mit KI reviewen:**

```
Prüfe diese EF Core Migration auf folgende Probleme und gib für jeden Punkt
eine konkrete Verbesserung an:

1. Fehlende Indizes auf Fremdschlüssel-Spalten
2. Falsche Datentypen (z.B. float statt decimal für Geldbeträge)
3. Fehlende NOT NULL Constraints bei required Properties
4. Potenzielle Data-Loss-Operationen
5. Fehlende UNIQUE Constraints (z.B. RoomNumber)

[generierte Migration hier einfügen]
```

Copilot findet mindestens 2–3 echte Probleme in der generierten Migration → Fixes direkt übernehmen.

---

## Deine Aufgabe

Führe folgende Schritte aus:

1. Öffne die generierte Migration-Datei (`HotelApp.Infrastructure/Migrations/TIMESTAMP_InitialCreate.cs`)
2. Kopiere den `Up()`-Methodeninhalt
3. Füge ihn in diesen Prompt ein und führe ihn aus:

```
Du bist ein erfahrener Datenbankentwickler. Analysiere diese EF Core Migration:

Suche nach:
- Fehlenden Indizes auf FK-Spalten (RoomId, GuestId etc.)
- Fehlenden UNIQUE Constraints
- Enum-Spalten als int statt nvarchar (Lesbarkeit in DB)
- Fehlenden Default-Werten für CreatedAt / UpdatedAt Spalten

Gib für jeden Fund den korrekten EF Core FluentAPI-Code an.

[Deine Migration hier einfügen]
```

4. Vergleiche das Feedback mit der Musterlösung.

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

### Typische Probleme in einer generierten InitialCreate Migration

**Problem 1 — Fehlende Indizes auf FK-Spalten**

```csharp
// In ModelBuilder / IEntityTypeConfiguration<Booking>:
entity.HasIndex(b => b.RoomId);
entity.HasIndex(b => b.GuestId);
```

**Problem 2 — RoomNumber ohne UNIQUE Constraint**

```csharp
entity.HasIndex(r => r.RoomNumber).IsUnique();
```

**Problem 3 — Enum als int (unleserlich in DB)**

```csharp
// In DbContext.OnModelCreating:
entity.Property(b => b.Status)
    .HasConversion<string>()  // speichert "Confirmed" statt 1
    .HasMaxLength(20);
```

**Problem 4 — CreatedAt ohne Default-Wert**

```csharp
entity.Property(b => b.CreatedAt)
    .HasDefaultValueSql("GETUTCDATE()");
```

**Problem 5 — decimal ohne Precision**

```csharp
entity.Property(b => b.TotalPrice)
    .HasPrecision(18, 2);  // verhindert Rundungsfehler
```

### Migration erneut anwenden nach Fixes:

```powershell
dotnet ef migrations remove --project HotelApp.Infrastructure --startup-project HotelApp.Web
dotnet ef migrations add InitialCreate --project HotelApp.Infrastructure --startup-project HotelApp.Web
dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web
```

</details>
