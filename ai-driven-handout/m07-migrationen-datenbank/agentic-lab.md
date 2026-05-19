# m07 — Agentic Lab: Migrationen mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/migrations.instructions.md`

```markdown
---
applyTo: "Infrastructure/Migrations/**/*.cs"
---

## EF Core Migrations-Konventionen

- Eine Migration = eine logische Änderung (niemals mehrere Features in einer Migration)
- Migrationsnamen sind sprechend: `AddBookingCancellationFee`, `CreateRoomIndex` — nicht `Update1`
- Niemals eine bereits angewendete Migration bearbeiten
- Jede neue Spalte an existierender Tabelle braucht einen Default-Wert
- Fremdschlüssel-Spalten immer mit Index versehen
- Enum-Spalten werden als `string` gespeichert (HasConversion<string>), nicht als `int`
- `decimal`-Properties brauchen immer `.HasPrecision(18, 2)`
- `DateTime`-Spalten brauchen `HasDefaultValueSql("GETUTCDATE()")`
- Produktions-Skripte immer mit `--idempotent` generieren
```

---

## 2. `.github/prompts/review-migration.prompt.md`

Aufruf: `/review-migration`

```markdown
---
name: review-migration
description: Analysiert eine EF Core Migration und findet Qualitätsprobleme
---

Du bist erfahrener Datenbankentwickler und EF Core Experte.

Analysiere diese EF Core Migration auf folgende Probleme.
Gib für jeden Fund den konkreten Fix als C# FluentAPI-Code an:

**Prüfliste:**

1. Fehlende Indizes auf FK-Spalten (`HasIndex`)
2. Fehlende UNIQUE Constraints (`IsUnique()`)
3. `decimal` ohne Precision → `.HasPrecision(18, 2)`
4. Enum-Spalten als `int` statt `string` → `.HasConversion<string>()`
5. `DateTime`-Spalten ohne Default → `.HasDefaultValueSql("GETUTCDATE()")`
6. Neue NOT NULL Spalten ohne Default-Wert (Data Loss Risiko)
7. Fehlende `nvarchar`-Längenbegrenzungen auf string-Spalten

Migration:
{{selection}}
```

**Verwendung:**

1. Inhalt der `Up()`-Methode im Editor markieren
2. `/review-migration` in Copilot Chat

---

## 3. `.github/agents/migration-reviewer.agent.md`

```markdown
---
name: migration-reviewer
description: >
  Liest alle Migrations-Dateien im Projekt, prüft sie auf Qualitätsprobleme
  und erstellt einen Bericht mit konkreten Fixes
tools:
  - codebase
---

Du bist EF Core Experte und Senior Datenbankentwickler.

Aufgabe:

1. Lese alle `.cs`-Dateien unter `Infrastructure/Migrations/`
2. Prüfe jede Migration auf:
   - Fehlende Indizes auf FK-Spalten
   - Fehlende UNIQUE Constraints
   - decimal ohne HasPrecision(18,2)
   - Enums als int (sollten string sein)
   - DateTime ohne HasDefaultValueSql
   - Data-Loss-Operationen (DROP COLUMN, ALTER NOT NULL auf befüllte Spalten)
3. Erstelle einen Bericht `migration-review.md` mit:
   - Problem pro Migration
   - Konkrete FluentAPI-Fix als C#-Code
   - Priorität: KRITISCH / WARNUNG / HINWEIS
```

**Workflow:**

```
Infrastructure/Migrations/*.cs  →  [migration-reviewer]  →  migration-review.md
```

---

## Befehle — direkt kopieren

```powershell
# Migration erstellen
dotnet ef migrations add InitialCreate --project Infrastructure --startup-project Api

# Datenbank aktualisieren
dotnet ef database update --project Infrastructure --startup-project Api

# Idempotentes SQL-Skript für Produktion
dotnet ef migrations script --idempotent --output migrations.sql --project Infrastructure --startup-project Api

# Letzte Migration rückgängig machen
dotnet ef migrations remove --project Infrastructure --startup-project Api
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese alle Migrationsdateien unter Infrastructure/Migrations/ und erstelle
einen vollständigen Review-Bericht als migration-review.md mit konkreten
FluentAPI-Fixes für jedes gefundene Problem.
```
