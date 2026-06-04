---
agent: agent
name: add-feature
description: add new feature to the todo app
model: Claude Sonnet 4.6 (copilot)
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
- Spec-Datei im Ordner specs/ anlegen
- app.py erst nach Bestätigung ändern
