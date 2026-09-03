# 12 – Spec-Driven Development

**Block:** 90 min | **Tag 4**

---

## Wie funktioniert das unter der Haube?

```
Spec schreiben (specs/feature.md)
  → Claude liest Spec als Aufgabenbeschreibung
  → Implementiert nur was in der Spec steht
  → Tests werden gegen Akzeptanzkriterien geschrieben
  → Review: Weicht Implementierung von Spec ab?
```

> Spec-Driven heißt: **zuerst beschreiben, dann umsetzen**. Die Spec ist das einzige, was zählt – nicht was Claude denkt, was gemeint war.

**Warum das funktioniert:** Claude hat keine Meinung über dein Feature. Eine gute Spec = gutes Ergebnis. Schlechte Spec = Claude rät.

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

```
Schritt 1 – Spec schreiben:
Schreibe eine Spec unter specs/due-dates.md für das Feature
"Fälligkeitsdatum für Todos". Nutze die Vorlage aus dem Handout.
Warte auf meine Bestätigung bevor du Code schreibst.

Schritt 2 – Implementieren:
Implementiere das Feature aus specs/due-dates.md.
Halte dich genau an die Spec.

Schritt 3 – Tests schreiben:
Schreibe Tests für das Due-Dates-Feature basierend auf den
Akzeptanzkriterien in specs/due-dates.md.

Schritt 4 – Review:
Vergleiche die Implementierung in app.py mit der Spec in
specs/due-dates.md. Gibt es Abweichungen?
```

---

## Spec-Kit – der eingebaute Claude-Code-Workflow

Für strukturiertes, dreistufiges Entwickeln bringt Claude Code einen eigenen Workflow mit:

```
/spec plan    → Claude erstellt einen Plan aus deiner Anforderung
/spec         → Claude implementiert nach dem Plan
/spec test    → Claude schreibt Tests gegen den Plan
```

Details, Aufbau der generierten `SPEC.md` und Schritt-für-Schritt-Anleitung: [12b-spec-kit.md](12b-spec-kit.md).

---

## Ordnerstruktur

```
1205/todo-app/
└── specs/
    ├── due-dates.md        ← heute erstellt (manuelle Spec)
    └── priorities.md       ← (bereits vorhanden als Referenz)
```
