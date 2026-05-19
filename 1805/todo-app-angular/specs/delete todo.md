# Feature-Spec: delete todo

## User Story

Als Nutzer möchte ich bestehende Todos löschen können, damit ich erledigte oder nicht mehr relevante Aufgaben aus meiner Liste entfernen und die Übersicht behalten kann.

## Datenmodell-Änderungen

Für dieses Feature sind keine strukturellen Änderungen am bestehenden Todo-Datenmodell erforderlich.

Optional (empfohlen bei Persistenz):

- deletedAt (Zeitpunkt der Löschung), falls ein Soft-Delete-Konzept oder Audit-Logging genutzt werden soll.

## UI-Anforderungen

- Jedes Todo besitzt eine klar erkennbare Löschaktion (z. B. Papierkorb-Button).
- Vor dem endgültigen Löschen wird eine Bestätigung abgefragt, um versehentliche Löschungen zu vermeiden.
- Nach erfolgreichem Löschen wird das Todo sofort aus der Liste entfernt.
- Die UI bleibt nach dem Löschen konsistent (z. B. korrekte Anzahl verbleibender Todos, kein fehlerhafter Fokuszustand).
- Falls das Löschen fehlschlägt (z. B. Backend-Fehler), wird eine verständliche Fehlermeldung angezeigt und das Todo bleibt sichtbar.

## Akzeptanzkriterien

1. Klickt ein Nutzer auf die Löschaktion eines Todos und bestätigt den Dialog, wird genau dieses Todo gelöscht und aus der Liste entfernt.
2. Bricht der Nutzer die Bestätigung ab, wird kein Todo gelöscht und die Liste bleibt unverändert.
3. Nach erfolgreichem Löschen wird die sichtbare Todo-Anzahl korrekt aktualisiert.
4. Schlägt das Löschen fehl, wird eine Fehlermeldung angezeigt und das Todo bleibt in der Liste erhalten.
5. Das Löschen eines Todos beeinflusst keine anderen Todos oder deren Zustände (z. B. completed-Status).
