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
    builder.Entity<RoomCategory>().HasData(
        new RoomCategory { Id = Guid.Parse("11111111-0000-0000-0000-000000000001"), Name = "Einzelzimmer", BasePrice = 89.00m },
        new RoomCategory { Id = Guid.Parse("11111111-0000-0000-0000-000000000002"), Name = "Doppelzimmer", BasePrice = 129.00m },
        new RoomCategory { Id = Guid.Parse("11111111-0000-0000-0000-000000000003"), Name = "Suite", BasePrice = 249.00m }
    );
}
```

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
