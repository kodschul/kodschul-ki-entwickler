# m06 — Agentic Lab: Datenklassen mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/csharp-entities.instructions.md`

```markdown
---
applyTo: "Domain/**/*.cs"
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

1. Lese `Domain/Glossar.md` und alle vorhandenen `.cs`-Dateien unter `Domain/`
2. Identifiziere welche Entitäten noch nicht als `.cs`-Datei existieren
3. Generiere für jede fehlende Entität eine vollständige `.cs`-Datei unter `Domain/`
4. Generiere den passenden `IEntityTypeConfiguration<T>` unter `Infrastructure/Configurations/`

Klassenregeln (immer einhalten):

- `private set` überall
- `protected` EF-Konstruktor
- Validierung im Konstruktor
- Domain Events als `sealed record` am Ende der Datei
- Namespace: `HotelReservierung.Domain`
- Configuration-Namespace: `HotelReservierung.Infrastructure.Configurations`
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
Lese Domain/Glossar.md und generiere alle fehlenden Entitätsklassen.
Folge den Konventionen aus csharp-entities.instructions.md.
Erstelle zusätzlich die EF Core Konfigurationsklassen unter Infrastructure/Configurations/.
```
