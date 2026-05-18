# Spec-Driven Development

**Block:** 13:15 – 15:00 Uhr

---

## Wie funktioniert das unter der Haube?

```
Spec schreiben (SPEC.md)
  → Copilot liest Spec als Aufgabenbeschreibung (via #-Referenz)
  → Implementiert nur was in der Spec steht
  → Tests werden gegen Akzeptanzkriterien geschrieben
  → Review: Weicht Implementierung von Spec ab?
```

> Spec-Driven heißt: **zuerst beschreiben, dann umsetzen**.  
> Die Spec ist das einzige, was zählt – nicht was Copilot denkt, was gemeint war.

**Warum das funktioniert:**  
Copilot hat keine Meinung über dein Feature. Eine gute Spec = gutes Ergebnis. Schlechte Spec = Copilot rät.

---

## Warum / Wann nicht?

| Warum nutzen                      | Wann nicht                                |
| --------------------------------- | ----------------------------------------- |
| Klare Erwartungen vor dem Code    | Kleines 2-Zeilen-Fix → direkt umsetzen    |
| Reproduzierbar im Team            | Explorativer Prototyp → Spec käme zu früh |
| Testkriterien bereits in der Spec | Wegwerfcode / Experiment                  |
| Nachvollziehbar: Spec im Repo     | Feature ändert sich noch stark            |

---

## Spec-Vorlage

```markdown
# Feature: [Name]

## User Story

Als [Nutzertyp] möchte ich [Funktion], damit [Nutzen].

## Datenmodell

Änderungen in todos.json:

- Neues Feld: `due_date` (string, ISO-Format YYYY-MM-DD, optional)

## UI-Anforderungen

- Eingabefeld im Formular (type="date")
- Datum wird in der Todo-Liste angezeigt
- Überfällige Todos werden rot markiert

## API / Routen

| Route  | Methode | Änderung                             |
| ------ | ------- | ------------------------------------ |
| `/add` | POST    | Neues Feld `due_date` entgegennehmen |
| `/`    | GET     | `due_date` im Template rendern       |

## Akzeptanzkriterien

- [ ] Todo kann mit Datum angelegt werden
- [ ] Todo ohne Datum funktioniert weiterhin
- [ ] Abgelaufene Todos werden visuell hervorgehoben
- [ ] Datum wird korrekt in todos.json gespeichert
```

---

## Workflow: Plan → Implement → Test

**Schritt 1 – Spec schreiben (Copilot Chat):**

```
Schreibe eine Spec unter specs/due-dates.md für das Feature
"Fälligkeitsdatum für Todos". Nutze die Vorlage aus dem Handout.
Warte auf meine Bestätigung bevor du Code schreibst.
```

**Schritt 2 – Spec an Copilot übergeben:**

In Copilot Chat die Spec-Datei mit `#` referenzieren:

```
Implementiere das Feature aus #specs/due-dates.md.
Halte dich genau an die Spec. Informiere mich, wenn etwas unklar ist.
```

**Schritt 3 – Tests schreiben:**

```
Schreibe Tests für das Due-Dates-Feature basierend auf den
Akzeptanzkriterien in #specs/due-dates.md.
```

**Schritt 4 – Review:**

```
Vergleiche die Implementierung in #app.py mit der Spec in
#specs/due-dates.md. Gibt es Abweichungen?
```

---

## Spec mit Custom Prompt automatisieren

Erstelle `.github/prompts/spec-feature.prompt.md` für ein vollständiges Spec-Kit:

```markdown
---
mode: agent
description: "Feature-Spec erstellen und dann implementieren"
tools:
  - codebase
  - terminal
---

# Feature Spec Workflow

Feature: ${input:featureName}

## Phase 1 – Spec schreiben

Erstelle specs/${input:featureName}.md mit:
- User Story
- Datenmodell-Änderungen
- UI-Anforderungen
- Betroffene Routen
- Mindestens 4 Akzeptanzkriterien als Checkboxen

Zeige die Spec. Schreibe NOCH KEINEN Code. Warte auf meine Freigabe.

## Phase 2 – Implementieren (nur nach Bestätigung)

Implementiere das Feature genau nach der Spec.
Hake jeden Schritt in der Spec ab wenn erledigt.

## Phase 3 – Tests generieren

Schreibe Tests basierend auf den Akzeptanzkriterien in der Spec.
```

---

## Ordnerstruktur

```
1205/todo-app/
└── specs/
    ├── due-dates.md        ← heute erstellt
    └── priorities.md       ← (Referenz-Beispiel)
```

---

## # Referenz-Syntax in Copilot Chat

| Syntax            | Beschreibung                                      |
| ----------------- | ------------------------------------------------- |
| `#dateiname.md`   | Einzelne Datei an Copilot übergeben               |
| `#codebase`       | Gesamte Codebase als Kontext                      |
| `#selection`      | Aktuell markierter Code                           |
| `@workspace`      | Workspace-weite Suche aktivieren                  |
