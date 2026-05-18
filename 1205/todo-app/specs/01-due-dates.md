# Feature: due-dates

## User Story

Als Nutzer möchte ich ein Fälligkeitsdatum für meine Todos festlegen können, damit ich meine Aufgaben besser organisieren kann.

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
