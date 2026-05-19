# m06 — Agentic Lab: Datenklassen mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/csharp-entities.instructions.md`

```markdown
---
applyTo: "HotelApp.Domain/**/*.cs"
---

## C# Entitäts-Konventionen (.NET 9, DDD)

- Alle Properties haben `private set` — niemals `public set`
- Immer ein `protected` parameterloser Konstruktor für EF Core Materialisation
- Validierung ausschließlich im öffentlichen Konstruktor mit `ArgumentException`
- `decimal` für alle Geldbeträge — niemals `float` oder `double`
- `Guid` für alle IDs — niemals `int`
- `DateTime.UtcNow` — niemals `DateTime.Now`
- `DateOnly` für Datumsfelder ohne Uhrzeit (Check-in, Check-out)
- Nullable Reference Types sind aktiviert — alle nicht-nullbaren Properties müssen initialisiert sein
- Methoden prüfen den Status vor Ausführung und werfen `InvalidOperationException`
- Domain Events als `sealed record` am Ende der Datei definieren
- XML-Dokumentation für alle public Members
- Enums als eigene Datei im selben Namespace
```

---

## 2. `.github/prompts/generate-entity.prompt.md`

Aufruf: `/generate-entity`

```markdown
---
name: generate-entity
description: Generiert eine vollständige C# Entitätsklasse nach DDD-Konventionen
---

Du bist Senior C#-Entwickler (.NET 9, C# 13, DDD).

Erstelle eine C# Klasse nach diesen fixen Regeln:

- `private set` für alle Properties
- `protected` parameterloser EF-Core-Konstruktor
- Validierung im Konstruktor (ArgumentException bei Verletzung)
- `decimal` für Geld, `Guid` für IDs, `DateOnly` für Datumsfelder
- Statusprüfung in jeder Zustandsmethode (InvalidOperationException)
- Domain Events als `sealed record` am Ende
- XML-Dokumentation
- Nur Code, keine Erklärungen

Klasse: {{input:Klassenname (z.B. Booking, Room, Guest)}}
Properties: {{input:Properties mit Typen}}
Methoden: {{input:Methoden mit Domänenregeln}}
```

---

## 3. `.github/agents/entity-generator.agent.md`

```markdown
---
name: entity-generator
description: >
  Liest das Domänenmodell aus Domain/Glossar.md und generiert alle fehlenden
  C#-Entitätsklassen vollständig nach Projektkonventionen
tools:
  - codebase
  - new_file
---

Du bist Senior C#-Entwickler (.NET 9, DDD).

Aufgabe:

1. Lese `HotelApp.Domain/Glossar.md` und alle vorhandenen `.cs`-Dateien unter `HotelApp.Domain/`
2. Identifiziere welche Entitäten noch nicht als `.cs`-Datei existieren
3. Generiere für jede fehlende Entität eine vollständige `.cs`-Datei unter `HotelApp.Domain/`
4. Generiere den passenden `IEntityTypeConfiguration<T>` unter `HotelApp.Infrastructure/Configurations/`

Klassenregeln (immer einhalten):

- `private set` überall
- `protected` EF-Konstruktor
- Validierung im Konstruktor
- Domain Events als `sealed record` am Ende der Datei
- Namespace: `HotelApp.Domain`
- Configuration-Namespace: `HotelApp.Infrastructure.Configurations`
```

**Workflow:**

```
Domain/Glossar.md  →  [entity-generator]  →  Domain/*.cs
                                          →  Infrastructure/Configurations/*Configuration.cs
```

---

## Checkliste — nach jeder generierten Klasse abhaken

```
[ ] private set überall?
[ ] protected EF-Konstruktor vorhanden?
[ ] Validierung im Konstruktor (nicht in Properties)?
[ ] decimal für Geldbeträge?
[ ] Guid für IDs?
[ ] Statusprüfung in Methoden (InvalidOperationException)?
[ ] Domain Events definiert?
[ ] XML-Dokumentation vorhanden?
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese HotelApp.Domain/Glossar.md und generiere alle fehlenden Entitätsklassen.
Folge den Konventionen aus csharp-entities.instructions.md.
Erstelle zusätzlich die EF Core Konfigurationsklassen unter HotelApp.Infrastructure/Configurations/.
```

---

## 4. `.github/skills/entity-scaffolder/SKILL.md`

Per `/entity-scaffolder` abrufbar — generiert Entitäten + EF Core Konfigurationen in einem Schritt.

```markdown
---
name: entity-scaffolder
description: >
  Generates complete C# entity classes and EF Core configurations for a .NET
  DDD project. Use when creating new domain entities, adding EF Core
  IEntityTypeConfiguration, or scaffolding missing classes from a domain
  glossary. Trigger words: entity, C# class, EF Core, configuration,
  domain model, private set, Guid Id, sealed record, value object scaffold.
---

# Entity Scaffolder

Generiert vollständige C#-Entitäten und EF Core Konfigurationen aus dem Domänenmodell.

## Wann verwenden

- Neue Entitätsklassen nach DDD-Konventionen anlegen
- EF Core `IEntityTypeConfiguration<T>` für vorhandene Klassen generieren
- Domänenglossar in Code übersetzen
- Klassen-Gerüste reviewen und vervollständigen

## Voraussetzungen

- `HotelApp.Domain/Glossar.md` mit Ubiquitous Language vorhanden
- Konventionen aus [`references/entity-conventions.md`](./references/entity-conventions.md)

## Vorgehen

1. Lese `HotelApp.Domain/Glossar.md`
2. Prüfe vorhandene `.cs`-Dateien unter `HotelApp.Domain/` — keine Duplikate
3. Generiere fehlende Entitätsklassen unter `HotelApp.Domain/`
4. Generiere passende `IEntityTypeConfiguration<T>` unter `HotelApp.Infrastructure/Configurations/`
5. Validiere: private set, Guid Id, protected EF-Konstruktor, decimal-Precision

## Ausgabe

| Datei                                                           | Inhalt                               |
| --------------------------------------------------------------- | ------------------------------------ |
| `HotelApp.Domain/<Name>.cs`                                     | Vollständige Entität nach DDD-Regeln |
| `HotelApp.Infrastructure/Configurations/<Name>Configuration.cs` | EF Core Fluent-Konfiguration         |

## Beispiel-Aufruf
```

/entity-scaffolder
Generiere alle fehlenden Entitäten aus HotelApp.Domain/Glossar.md

```

```

**Skill-Struktur anlegen:**

```
.github/skills/entity-scaffolder/
├── SKILL.md
└── references/
    └── entity-conventions.md    ← Regeln aus csharp-entities.instructions.md
```
