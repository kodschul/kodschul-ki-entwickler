# m05 — Agentic Lab: DDD mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/ddd.instructions.md`

Legt fest wie Copilot Domänenmodelle in diesem Projekt benennt und strukturiert.

```markdown
---
applyTo: "**"
---

## Domänenmodell-Konventionen

- Ubiquitous Language: Verwende immer die deutschen Fachbegriffe aus dem Glossar
  als englische Code-Begriffe (Buchung → Booking, Gast → Guest, Zimmer → Room)
- Entitäten haben immer eine `Id`-Property vom Typ `Guid`
- Aggregate Roots sind mit dem Kommentar `// Aggregate Root` markiert
- Value Objects sind `sealed record` ohne eigene Id
- Domain Events sind `sealed record` mit Suffix `Event` (z.B. `BookingCancelledEvent`)
- Bounded Context: alle Klassen liegen unter `HotelApp.Domain/` — niemals direkt in `Models/`
- Niemals `null` zurückgeben — stattdessen `Option<T>` oder Exception werfen
```

---

## 2. `.github/prompts/domain-model.prompt.md`

Aufruf in Copilot Chat: `/domain-model`

```markdown
---
name: domain-model
description: Extrahiert ein vollständiges Domänenmodell aus einem Anforderungstext
---

Du bist Domain-Experte und Senior C#-Entwickler (.NET 9, DDD).

Analysiere den folgenden Anforderungstext und liefere:

1. **Entitäten** — mit Eigenschaften und Lebenszyklus
2. **Value Objects** — ohne eigene Identität, als `sealed record`
3. **Aggregate Roots** — welche Entität "besitzt" andere?
4. **Domain Events** — Was passiert fachlich? (Vergangenheitsform, `sealed record`)
5. **Ubiquitous Language Glossar** — Deutsch → C#-Begriff (min. 10 Einträge)

Ausgabeformat: Markdown mit C#-Codeblöcken für jede Klasse.
Nur Klassengerüste — keine Implementierungslogik.

Anforderungstext:
{{selection}}
```

**Verwendung:**

1. Anforderungstext im Editor markieren
2. Copilot Chat öffnen → `/domain-model` eingeben
3. Copilot analysiert den markierten Text

---

## 3. `.github/agents/ddd-analyst.agent.md`

```markdown
---
name: ddd-analyst
description: >
  Analysiert Anforderungsdokumente im Projekt und erstellt ein vollständiges
  Domänenmodell als C#-Klassen unter HotelApp.Domain/
tools:
  - codebase
  - new_file
---

Du bist Domain-Experte und Senior C#-Entwickler (.NET 9, DDD).

Aufgabe:

1. Lese alle `.md`-Dateien im Ordner `specs/` oder `docs/`
2. Extrahiere alle Entitäten, Value Objects, Aggregate Roots und Domain Events
3. Erstelle für jede Klasse eine eigene `.cs`-Datei unter `HotelApp.Domain/`
4. Erstelle `HotelApp.Domain/Glossar.md` mit der Ubiquitous Language

Konventionen:

- Entitäten: `public sealed class Name` mit `Guid Id`
- Value Objects: `public sealed record Name(...)`
- Domain Events: `public sealed record NameEvent(...)`
- Aggregate Roots: Kommentar `// Aggregate Root` in der ersten Zeile
- Namespaces: `HotelApp.Domain`
```

**Workflow:**

```
HotelApp.Domain/ (leer)  →  [ddd-analyst]  →  HotelApp.Domain/*.cs + HotelApp.Domain/Glossar.md
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Analysiere das Hotelreservierungs-Domänenmodell (Booking, Room, Guest, HousekeepingTask) und erstelle das komplette Domänenmodell
als C#-Klassen unter HotelApp.Domain/ — folge den Konventionen aus ddd.instructions.md
```

---

## 4. `.github/skills/ddd-scaffolder/SKILL.md`

Ein wiederverwendbarer Workflow — per `/ddd-scaffolder` in Copilot Chat aufrufbar.

```markdown
---
name: ddd-scaffolder
description: >
  Scaffolds a complete DDD domain model for a .NET project. Use when starting
  a new bounded context, modelling a domain from requirements, generating
  entities, value objects, aggregate roots, domain events, and a ubiquitous
  language glossary. Trigger words: DDD, domain model, bounded context,
  aggregate, value object, ubiquitous language, domain event, C# domain.
---

# DDD Scaffolder

Erstellt ein vollständiges Domänenmodell aus Anforderungstexten.

## Wann verwenden

- Neues Bounded Context anlegen
- Domänenmodell aus User Stories oder Spec-Dateien ableiten
- Entitäten, Value Objects und Domain Events generieren
- Ubiquitous Language Glossar erstellen oder erweitern

## Voraussetzungen

- Anforderungstext liegt unter `specs/` oder `docs/` (`.md`-Datei)
- HotelApp ist bereits angelegt — Klassen kommen nach `HotelApp.Domain/`

## Vorgehen

1. Analysiere das bestehende HotelApp-Domänenmodell (Booking, Room, Guest)
2. Extrahiere Entitäten, Value Objects, Aggregate Roots, Domain Events
3. Prüfe bestehende Dateien unter `HotelApp.Domain/` — keine Duplikate anlegen
4. Erstelle fehlende `.cs`-Gerüste unter `HotelApp.Domain/`
5. Erstelle oder aktualisiere `HotelApp.Domain/Glossar.md`

## Ausgabe

| Datei                        | Inhalt                                   |
| ---------------------------- | ---------------------------------------- |
| `HotelApp.Domain/<Name>.cs`  | Klassengerüst pro Entität / Value Object |
| `HotelApp.Domain/Glossar.md` | Deutsch → C#-Begriff (min. 10 Einträge)  |

## Beispiel-Aufruf
```

/ddd-scaffolder
Erstelle das HousekeepingTask-Domänenmodell für HotelApp.Domain/

```

```

**Skill-Struktur anlegen:**

```
.github/skills/ddd-scaffolder/
├── SKILL.md
└── references/
    └── ddd-conventions.md    ← Konventionen aus ddd.instructions.md hier zusammenfassen
```
