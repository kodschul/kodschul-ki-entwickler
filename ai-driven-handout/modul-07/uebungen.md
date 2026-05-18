# Modul 7 — Übungen

---

## Übung 7.1-A — Erste Migration erstellen und analysieren

**Aufgabe:** Erstellen Sie die `InitialCreate`-Migration für das Hotelreservierungssystem.

1. Führen Sie `dotnet ef migrations add InitialCreate` aus
2. Analysieren Sie die generierte Migration mit KI:
```
Prüfe diese EF Core Migration auf:
- Fehlende Indizes auf FK-Spalten
- Potenzielle Data-Loss-Risiken
- Falsche Datentypen
- Fehlende Constraints
[Migration-Code einfügen]
```
3. Wenden Sie die Migration an: `dotnet ef database update`
4. Vergleichen Sie die erstellten Tabellen mit dem erwarteten Schema (via SQL Server Management Studio oder `dotnet ef dbcontext info`)

---

## Übung 7.1-B — Migration für eine Modelländerung

**Szenario:** Das `Room`-Modell soll eine `Description`-Eigenschaft bekommen (nullable, max. 500 Zeichen).

**Aufgabe:**
1. Ergänzen Sie die Entität und die Konfiguration
2. Erstellen Sie die Migration: `AddRoomDescription`
3. Lassen Sie KI erklären was die Migration macht und ob Data-Loss-Risiko besteht
4. Wenden Sie die Migration an

**Bonus:** Machen Sie `Description` in einer zweiten Migration zu einem Pflichtfeld – ohne Datenverlust. Wie viele Migrations-Schritte sind nötig?

---

## Übung 7.2-A — Seed-Daten mit Migration

**Aufgabe:** Erstellen Sie Seed-Daten für:
- 3 Zimmerkategorien (Einzel €89, Doppel €129, Suite €249)
- 5 Zimmer verteilt auf die Kategorien

Nutzen Sie KI um:
1. Die `HasData()`-Konfiguration mit fixen GUIDs zu generieren
2. Eine Migration `SeedRoomCategories` zu erstellen
3. Einen xUnit-Test zu schreiben der nach der Migration prüft ob alle Seed-Daten vorhanden sind

**Wichtig:** Die GUIDs müssen fest kodiert sein (kein `Guid.NewGuid()`), damit der Seed idempotent ist.

---

## Übung 7.2-B — Datenbank-Initialisierer implementieren

**Aufgabe:** Implementieren Sie einen `DatabaseInitializer`-Service der beim Start:
1. Prüft ob Datenbankverbindung funktioniert
2. Ausstehende Migrationen anwendet
3. Meldet wie viele Migrationen angewendet wurden
4. Einen Health-Check-Endpoint bereitstellt: `GET /health/database`

```csharp
public interface IDatabaseInitializer
{
    Task InitializeAsync(CancellationToken ct = default);
    Task<bool> IsHealthyAsync(CancellationToken ct = default);
}
```

Nutzen Sie KI für die Implementierung. Schreiben Sie dann Integrationstests.

---

## Übung 7.3-A — Vollständiges Setup-Skript

**Aufgabe:** Erstellen Sie `setup.ps1` mit:
1. Prüfung ob .NET 9 SDK installiert (Fehlermeldung wenn nicht)
2. Prüfung ob sqllocaldb verfügbar
3. Starten von sqllocaldb MSSQLLocalDB
4. NuGet-Pakete wiederherstellen
5. Migrationen anwenden
6. Erfolg/Fehler-Ausgabe mit Farben

Nutzen Sie KI für die Erstellung. Prüfen Sie: Werden alle Fehler abgefangen? Gibt es sinnvolle Fehlermeldungen?

---

## Übung 7.4-A — Breaking Change sicher migrieren

**Szenario:** Die Spalte `GuestName` (string, nullable) soll ersetzt werden durch `CustomerId` (Guid, required FK auf Customers-Tabelle). Es gibt bereits Produktionsdaten.

**Aufgabe:**
1. Formulieren Sie den KI-Prompt der den sicheren Migrationspfad erklärt
2. Identifizieren Sie welches Data-Loss-Risiko bei einem naiven Rename besteht
3. Entwickeln Sie den 3-stufigen sicheren Migrationspfad
4. Schreiben Sie die EF Core Migrations-Klassen für alle drei Stufen

---

## Übung 7.4-B — Migrations-Analyse und Verbesserung

**Aufgabe:** Analysieren Sie folgende generierte Migration. Finden Sie mindestens 6 Probleme.

```csharp
public partial class AddBookingTable : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.CreateTable(
            name: "Bookings",
            columns: table => new
            {
                Id = table.Column<int>(nullable: false)
                    .Annotation("SqlServer:Identity", "1, 1"),
                GuestName = table.Column<string>(nullable: true),
                CheckIn = table.Column<DateTime>(nullable: false),
                CheckOut = table.Column<DateTime>(nullable: false),
                Price = table.Column<double>(nullable: false),
                Status = table.Column<int>(nullable: false),
                RoomId = table.Column<int>(nullable: false)
            });
        // keine weiteren Befehle
    }
}
```

Für jedes Problem: Stelle benennen → Problem erklären → Korrektur zeigen.
