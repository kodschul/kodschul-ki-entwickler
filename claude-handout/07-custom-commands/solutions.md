# Lösungen: Custom Commands

## Aufgabe 1 – `.claude/commands/todo-review.md`

```markdown
# Todo-App Code Review

Führe einen vollständigen Code-Review der Todo-App durch.

## Prüfpunkte

1. Lies app.py komplett
2. Prüfe alle Flask-Routen auf:
   - Fehlende Input-Validierung
   - Fehlende Fehlerbehandlung
   - Sicherheitsprobleme (z. B. keine Auth)
3. Prüfe todos.json-Handling auf Race-Conditions
4. Erstelle eine Checkliste mit Problemen (kritisch / mittel / niedrig)

## Ausgabe

Gib die Ergebnisse als Markdown-Tabelle aus:
| Problem | Datei | Schwere | Empfehlung |
```

## Aufgabe 2 – `.claude/commands/add-feature.md`

```markdown
# Neues Feature zur Todo-App hinzufügen

Feature-Anfrage: $ARGUMENTS

## Schritte

1. Erstelle eine Spec-Datei unter specs/$ARGUMENTS.md mit:
   - User Story (Als Nutzer möchte ich...)
   - Datenmodell-Änderungen (falls nötig)
   - UI-Anforderungen
   - Akzeptanzkriterien (mindestens 3)
2. Zeige die Spec und warte auf Bestätigung
3. Implementiere das Feature erst nach Bestätigung

## Regeln

- Schreibe IMMER zuerst die Spec, nie direkt Code
- Halte die Implementierung minimal und fokussiert
- Erstelle nach der Implementierung Tests in test_app.py
```
