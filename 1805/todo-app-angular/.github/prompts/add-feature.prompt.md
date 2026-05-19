---
name: add-feature
description: 'Neues Feature planen und implementieren'
---

# Neues Feature zur Todo-App hinzufügen

Feature-Anfrage: ${input:featureName}

## Schritte

1. Erstelle eine Spec-Datei unter specs/${input:featureName}.md mit:
   - User Story (Als Nutzer möchte ich...)
   - Datenmodell-Änderungen (falls nötig)
   - UI-Anforderungen
   - Akzeptanzkriterien (mindestens 3)
2. Zeige die Spec und warte auf Bestätigung
3. Implementiere das Feature erst nach Bestätigung

## Regeln

- IMMER zuerst die Spec, nie direkt Code
- IMMER Spec-Datei im Ordner specs/ anlegen
