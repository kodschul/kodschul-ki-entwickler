# Feature-Spec: create-todo

## User Story

Als Nutzer möchte ich neue Todos erstellen können, damit ich meine Aufgaben schnell erfassen und später verwalten kann.

## Datenmodell-Änderungen

Für dieses Feature sind keine zwingenden strukturellen Änderungen am bestehenden Todo-Datenmodell erforderlich, sofern bereits mindestens folgende Felder vorhanden sind:

- id
- title
- completed

Optional (empfohlen für bessere Nachvollziehbarkeit):

- createdAt (Zeitpunkt der Erstellung)

## UI-Anforderungen

- Es gibt ein Eingabefeld für den Titel eines neuen Todos.
- Es gibt eine gut sichtbare Aktion zum Erstellen (Button oder Enter-Taste).
- Nach erfolgreichem Erstellen wird das neue Todo in der Liste angezeigt.
- Das Eingabefeld wird nach erfolgreicher Erstellung geleert.
- Leere oder nur aus Leerzeichen bestehende Eingaben dürfen nicht gespeichert werden.
- Bei ungültiger Eingabe wird eine verständliche Rückmeldung angezeigt.

## Akzeptanzkriterien

1. Wenn ein Nutzer einen gültigen Titel eingibt und die Erstellen-Aktion ausführt, wird ein neues Todo erzeugt und in der Todo-Liste angezeigt.
2. Wenn der Nutzer eine leere Eingabe (oder nur Leerzeichen) absendet, wird kein Todo erstellt und eine Validierungsrückmeldung angezeigt.
3. Nach erfolgreicher Erstellung wird das Eingabefeld zurückgesetzt, sodass direkt ein weiteres Todo erfasst werden kann.
4. Das neu erstellte Todo ist standardmäßig als nicht erledigt markiert.
5. Die Erstellung funktioniert sowohl per Klick auf den Erstellen-Button als auch per Enter-Taste im Eingabefeld.
