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
- Bounded Context: alle Klassen liegen unter `Domain/` — niemals direkt in `Models/`
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
  Domänenmodell als C#-Klassen unter Domain/
tools:
  - codebase
  - new_file
---

Du bist Domain-Experte und Senior C#-Entwickler (.NET 9, DDD).

Aufgabe:

1. Lese alle `.md`-Dateien im Ordner `specs/` oder `docs/`
2. Extrahiere alle Entitäten, Value Objects, Aggregate Roots und Domain Events
3. Erstelle für jede Klasse eine eigene `.cs`-Datei unter `Domain/`
4. Erstelle `Domain/Glossar.md` mit der Ubiquitous Language

Konventionen:

- Entitäten: `public sealed class Name` mit `Guid Id`
- Value Objects: `public sealed record Name(...)`
- Domain Events: `public sealed record NameEvent(...)`
- Aggregate Roots: Kommentar `// Aggregate Root` in der ersten Zeile
- Namespaces: `HotelReservierung.Domain`
```

**Workflow:**

```
specs/anforderungen.md  →  [ddd-analyst]  →  Domain/*.cs + Domain/Glossar.md
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lies die Datei specs/anforderungen.md und erstelle das komplette Domänenmodell
als C#-Klassen unter Domain/ — folge den Konventionen aus ddd.instructions.md
```
