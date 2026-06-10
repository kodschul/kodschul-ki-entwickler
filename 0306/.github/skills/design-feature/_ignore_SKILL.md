---
name: design-feature
description: Use this when adding, creating, designing, thinking, building or editing any feature or main changes  of any kind
disable-model-invocation: true
---

Always before building any Feature, make sure to add a spec and get user EXPLICIT approval before running or writing any CODE!

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
