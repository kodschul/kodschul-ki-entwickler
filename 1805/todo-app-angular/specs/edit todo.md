# Feature-Spec: edit todo

## User Story

Als Nutzer möchte ich ein bestehendes Todo per Doppelklick bearbeiten können, damit ich Inhalte schnell korrigieren und aktualisieren kann, ohne das Todo neu anzulegen.

## Datenmodell-Änderungen

Für dieses Feature sind keine zwingenden strukturellen Änderungen notwendig, sofern das Todo bereits folgende Felder enthält:

- title
- description
- dueDate

Optional (empfohlen):

- updatedAt (Zeitpunkt der letzten Änderung), um Änderungen nachvollziehbar zu machen.

## UI-Anforderungen

- Ein Todo kann per Doppelklick in den Bearbeitungsmodus versetzt werden.
- Im Bearbeitungsmodus sind die Felder Titel, Beschreibung und Fälligkeitsdatum editierbar.
- Änderungen werden automatisch gespeichert, sobald ein Feld den Fokus verliert.
- Wenn der Bearbeitungsmodus abgebrochen wird, werden alle noch nicht gespeicherten Änderungen vollständig verworfen.
- Bei ungültigen Eingaben (mindestens: leerer Titel) wird eine verständliche Validierungsrückmeldung angezeigt.

## Akzeptanzkriterien

1. Ein Doppelklick auf ein Todo öffnet den Bearbeitungsmodus für genau dieses Todo.
2. Titel, Beschreibung und Fälligkeitsdatum sind im Bearbeitungsmodus änderbar.
3. Beim Verlassen eines Eingabefeldes (Blur) werden gültige Änderungen automatisch gespeichert.
4. Ist der Titel leer, wird nicht gespeichert und eine Validierungsrückmeldung angezeigt.
5. Beim Abbrechen des Bearbeitungsmodus werden nicht gespeicherte Änderungen verworfen und der zuletzt gespeicherte Zustand wiederhergestellt.
6. Nach erfolgreichem Speichern sind die aktualisierten Werte direkt in der Todo-Liste sichtbar.
