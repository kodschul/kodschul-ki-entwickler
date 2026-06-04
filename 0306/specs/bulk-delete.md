# Feature Spec: Bulk Delete Todos

## User Story

Als Nutzer möchte ich mehrere Todos gleichzeitig auswählen und auf einmal löschen können, damit ich meine Liste schnell aufräumen kann, ohne jeden Eintrag einzeln zu entfernen.

## Datenmodell-Änderungen

Keine. Todos bleiben unverändert in `todos.json`. Der neue Endpunkt arbeitet nur mit bestehenden IDs.

## UI-Anforderungen

- Jedes Todo-Item erhält eine **Checkbox** am linken Rand.
- Unterhalb der Todo-Liste erscheint ein **"Delete Selected"-Button**, der nur aktiv/sichtbar ist, wenn mindestens eine Checkbox angehakt ist.
- Die Checkboxen und der Button befinden sich in einem gemeinsamen `<form>` mit `action="/delete-many"` und `method="post"`.
- Der Button ist rot (konsistent mit dem bestehenden einzelnen Delete-Button).
- Nach dem Löschen erfolgt ein **Redirect** zurück zur Startseite (Post/Redirect/Get).

## Backend-Änderungen

- Neuer Route: `POST /delete-many`
- Liest mehrere `ids`-Formularwerte (Checkboxen mit `name="ids"` und `value="{{ todo.id }}"`)
- Entfernt alle Todos, deren ID in der übermittelten Liste enthalten ist.
- Ignoriert ungültige/unbekannte IDs stillschweigend.

## Akzeptanzkriterien

1. Nutzer kann eine oder mehrere Checkboxen ankreuzen und alle markierten Todos mit einem Klick löschen.
2. Todos ohne Checkbox-Auswahl bleiben nach dem Löschen unverändert in der Liste.
3. Wird kein Todo ausgewählt und das Formular abgeschickt (z. B. direkter POST), passiert nichts — alle Todos bleiben erhalten.
4. Nach dem Löschen landet der Nutzer wieder auf der Hauptseite (kein doppeltes Absenden beim Reload).
5. Der "Delete Selected"-Button ist visuell konsistent mit den bestehenden Delete-Buttons (rot).
