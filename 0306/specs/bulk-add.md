# Feature Spec: Mehrere Todos auf einmal hinzufügen

## User Story

Als Nutzer möchte ich mehrere Todos gleichzeitig eingeben können, damit ich meine Aufgabenliste schnell befüllen kann, ohne jedes Todo einzeln abzusenden.

## Datenmodell-Änderungen

Keine. Todos bleiben unverändert in `todos.json`. Der neue Endpunkt erstellt mehrere Einträge mit denselben Feldern wie der bestehende `/add`-Endpunkt.

## UI-Anforderungen

- Unterhalb des bestehenden Einzeleingabe-Formulars erscheint ein **aufklappbarer Bereich** (z. B. `<details>`/`<summary>`) mit dem Titel „Mehrere Todos hinzufügen".
- Im aufgeklappten Bereich befindet sich ein `<textarea>` mit Placeholder `"Ein Todo pro Zeile…"`.
- Daneben ein **Priority-Select** (high / medium / low), das für alle Einträge der Batch-Eingabe gilt.
- Ein **„Alle hinzufügen"-Button** in der Primärfarbe sendet das Formular ab.
- Das Formular hat `action="/add-many"` und `method="post"`.
- Leere Zeilen werden ignoriert; maximal 50 Todos pro Anfrage.
- Nach dem Hinzufügen erfolgt ein **Redirect** zur Startseite (Post/Redirect/Get).

## Backend-Änderungen

- Neue Route: `POST /add-many`
- Liest Formularfeld `titles` (Textarea-Inhalt) und `priority`.
- Splittet den Text zeilenweise, bereinigt Whitespace, ignoriert Leerzeilen.
- Kürzt jeden Titel auf max. 200 Zeichen (wie `/add`).
- Fügt alle validen Einträge in einem einzigen `mutate_todos_list`-Aufruf ein (thread-safe).
- Wenn keine validen Titles vorhanden sind, wird ohne Änderung weitergeleitet.
- Maximal 50 Todos pro Anfrage; darüber hinausgehende Einträge werden still ignoriert.

## Akzeptanzkriterien

1. Nutzer kann mehrere Zeilen in die Textarea eingeben und alle auf einmal anlegen.
2. Leere Zeilen werden ignoriert – kein leerer Todo-Eintrag entsteht.
3. Werden mehr als 50 Zeilen eingegeben, werden nur die ersten 50 gespeichert.
4. Einzelne Todos der Batch-Eingabe erhalten dieselbe Priority wie im Select gewählt.
5. Nach dem Absenden landet der Nutzer wieder auf der Hauptseite (kein Doppel-Submit beim Reload).
6. Das bestehende Einzeleingabe-Formular funktioniert weiterhin unverändert.
