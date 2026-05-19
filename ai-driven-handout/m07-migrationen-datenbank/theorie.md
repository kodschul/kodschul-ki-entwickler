# Modul 7 — Migrationen, Datenbank und technische Basis

---

## Lab 7.1 — Migrationen mit KI-Unterstützung erzeugen

### Migration-Workflow

```powershell
# Migration erstellen
dotnet ef migrations add InitialCreate --project Infrastructure --startup-project Api

# Datenbank aktualisieren
dotnet ef database update --project Infrastructure --startup-project Api

# Auf vorherige Migration zurück
dotnet ef database update PreviousMigrationName --project Infrastructure --startup-project Api

# Produktions-SQL-Skript (idempotent)
dotnet ef migrations script --idempotent --output migrations.sql --project Infrastructure --startup-project Api
```

### Migrations-Qualität mit KI prüfen

```
Prüfe diese EF Core Migration auf:
1. Fehlende Indizes auf FK-Spalten
2. Potenzielle Data-Loss-Operationen (DROP COLUMN, ALTER NOT NULL)
3. Falsche Datentypen (float statt decimal, int statt nvarchar für Enums)
4. Fehlende Constraints (NOT NULL, UNIQUE, CHECK)
5. Fehlende Standardwerte bei neuen required Spalten

[Migration-Code einfügen]
```

### Migrations-Konventionen

- **Kleine Migrationen:** Eine logische Änderung = eine Migration
- **Sprechende Namen:** `AddProductDescriptionColumn`, `CreateOrderStatusIndex`
- **Niemals bearbeiten** wenn bereits in Produktion angewendet
- **SQL immer prüfen** bevor auf Produktionsdatenbank angewendet

---

## Lab 7.2 — Datenbank erstellen und initialisieren

### Seed-Daten mit fixen GUIDs

```csharp
protected override void OnModelCreating(ModelBuilder builder)
{
    base.OnModelCreating(builder);

    // Feste GUIDs für Idempotenz (seed läuft mehrfach = gleiche Daten)
    builder.Entity<Booking>().HasData(
        new
        {
            Id             = Guid.Parse("aaaaaaaa-0000-0000-0000-000000000001"),
            RoomId         = Guid.Parse("bbbbbbbb-0000-0000-0000-000000000001"),
            GuestId        = Guid.Parse("cccccccc-0000-0000-0000-000000000001"),
            CheckInDate    = new DateOnly(2026, 6, 1),
            CheckOutDate   = new DateOnly(2026, 6, 5),
            Status         = "Confirmed",
            TotalPrice     = 516.00m,
            CancellationFee = (decimal?)null
        },
        new
        {
            Id             = Guid.Parse("aaaaaaaa-0000-0000-0000-000000000002"),
            RoomId         = Guid.Parse("bbbbbbbb-0000-0000-0000-000000000002"),
            GuestId        = Guid.Parse("cccccccc-0000-0000-0000-000000000002"),
            CheckInDate    = new DateOnly(2026, 7, 10),
            CheckOutDate   = new DateOnly(2026, 7, 14),
            Status         = "Requested",
            TotalPrice     = 356.00m,
            CancellationFee = (decimal?)null
        },
        new
        {
            Id             = Guid.Parse("aaaaaaaa-0000-0000-0000-000000000003"),
            RoomId         = Guid.Parse("bbbbbbbb-0000-0000-0000-000000000001"),
            GuestId        = Guid.Parse("cccccccc-0000-0000-0000-000000000003"),
            CheckInDate    = new DateOnly(2026, 5, 1),
            CheckOutDate   = new DateOnly(2026, 5, 3),
            Status         = "Cancelled",
            TotalPrice     = 258.00m,
            CancellationFee = 50.00m
        }
    );
}
```

> **Hinweis:** Bei `HasData` muss ein anonymes Objekt verwendet werden, da der `Booking`-Konstruktor Validierungslogik enthält. EF Core befüllt Seed-Daten direkt ohne den Konstruktor aufzurufen.

### Auto-Migration beim Start (nur Development)

```csharp
if (app.Environment.IsDevelopment())
{
    using var scope = app.Services.CreateScope();
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    await db.Database.MigrateAsync();
}
```

---

## Lab 7.3 — CLI zur Einrichtung vorbereiten

### Setup-Skript (PowerShell)

```powershell
# setup.ps1
param([string]$Environment = "Development")

Write-Host "🚀 Setup wird gestartet..." -ForegroundColor Cyan

# sqllocaldb starten
sqllocaldb start MSSQLLocalDB
if ($LASTEXITCODE -ne 0) { Write-Error "sqllocaldb konnte nicht gestartet werden"; exit 1 }

# Migrationen anwenden
dotnet ef database update --project src/Infrastructure --startup-project src/Api
if ($LASTEXITCODE -ne 0) { Write-Error "Migrationen fehlgeschlagen"; exit 1 }

Write-Host "✅ Setup abgeschlossen!" -ForegroundColor Green
```

---

## Lab 7.4 — Wartung und Weiterentwicklung

### Modell ändern ohne Datenverlust

Sicheres Vorgehen für Breaking Changes (z. B. Spalte required machen):

```
Migration 1: Neue Spalte nullable hinzufügen
Migration 2: Data Migration (SQL UPDATE) – Daten befüllen
Migration 3: Spalte auf NOT NULL setzen
```

**KI-Prompt für Breaking Changes:**

```
Ich möchte folgende Modellände ohne Datenverlust durchführen:
Aktuell: [Modell-Code]
Neu:     [Gewünschter Modell-Code]

Welche Migration-Schritte sind nötig?
Gibt es Data-Loss-Risiken?
Erstelle die EF Core 9 Migration-Klassen.
```
