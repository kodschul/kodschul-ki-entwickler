# m07 — Agentic Lab: Migrationen mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/migrations.instructions.md`

```markdown
---
applyTo: "HotelApp.Infrastructure/Migrations/**/*.cs"
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
HotelApp.Infrastructure/Migrations/*.cs  →  [migration-reviewer]  →  migration-review.md
```

---

## Befehle — direkt kopieren

```powershell
# Migration erstellen
dotnet ef migrations add InitialCreate --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Datenbank aktualisieren
dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Idempotentes SQL-Skript für Produktion
dotnet ef migrations script --idempotent --output migrations.sql --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Letzte Migration rückgängig machen
dotnet ef migrations remove --project HotelApp.Infrastructure --startup-project HotelApp.Web
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese alle Migrationsdateien unter HotelApp.Infrastructure/Migrations/ und erstelle
einen vollständigen Review-Bericht als migration-review.md mit konkreten
FluentAPI-Fixes für jedes gefundene Problem.
```

---

## 4. `.github/skills/migration-helper/SKILL.md`

Per `/migration-helper` abrufbar — erstellt und reviewed EF Core Migrationen.

```markdown
---
name: migration-helper
description: >
  Assists with EF Core migrations in .NET projects: reviewing existing
  migrations for quality issues, generating migration scripts, and
  producing idempotent SQL for production. Use when creating a new
  migration, reviewing migration quality, checking for missing indexes
  or precision settings, or generating deployment scripts.
  Trigger words: migration, EF Core, database, schema, dotnet ef,
  idempotent, FluentAPI, HasPrecision, HasIndex, HasConversion.
---

# Migration Helper

Erstellt, reviewed und dokumentiert EF Core Migrationen.

## Wann verwenden

- Neue Migration nach einer Modelländerung anlegen
- Bestehende Migrationen auf Qualitätsprobleme prüfen
- Idempotentes SQL-Skript für Produktion generieren
- Fehlende Indizes oder Precision-Settings nachträglich ergänzen

## Voraussetzungen

- EF Core Projekt mit `HotelApp.Infrastructure/Migrations/`-Ordner
- Konventionen aus [`references/migration-conventions.md`](./references/migration-conventions.md)

## Vorgehen (Review-Modus)

1. Lese alle `.cs`-Dateien unter `HotelApp.Infrastructure/Migrations/`
2. Prüfe jede `Up()`-Methode auf Qualitätsprobleme (Checkliste)
3. Erstelle `migration-review.md` mit Befunden und FluentAPI-Fixes

## Vorgehen (Erstell-Modus)

1. Prüfe `HotelApp.Domain/` und `HotelApp.Infrastructure/Configurations/` auf Modelländerungen
2. Schlage einen sprechenden Migrationsnamen vor
3. Generiere die benötigten FluentAPI-Calls für `Up()` und `Down()`

## Prüfliste

- [ ] FK-Spalten haben `HasIndex`?
- [ ] `decimal` mit `.HasPrecision(18, 2)`?
- [ ] Enums als `string` (`HasConversion<string>()`)?
- [ ] `DateTime` mit `HasDefaultValueSql("GETUTCDATE()")`?
- [ ] Data-Loss-Operationen (DROP, ALTER NOT NULL) sicher?

## Beispiel-Aufruf
```

/migration-helper
Review alle Migrationen unter HotelApp.Infrastructure/Migrations/ und erstelle migration-review.md

```

```

**Skill-Struktur anlegen:**

```
.github/skills/migration-helper/
├── SKILL.md
└── references/
    └── migration-conventions.md    ← Regeln aus migrations.instructions.md
```
