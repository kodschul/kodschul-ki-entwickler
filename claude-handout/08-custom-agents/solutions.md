# Lösungen: Custom Agents

## `.claude/agents/security-reviewer.md`

```markdown
---
name: security-reviewer
description: Führt einen Sicherheits-Audit der App durch. Nur lesen, kein Code ändern.
tools:
  - Read
---

# Security Reviewer

Analysiere alle Python-Dateien auf Sicherheitsprobleme.

## Prüfpunkte

- Hardcodierte Tokens oder Passwörter
- Fehlende Input-Validierung in Flask-Routen
- `eval()` oder `exec()` Aufrufe
- Fehlende Authentifizierung an sensiblen Routen
- Unsichere Dateioperationen

## Ausgabe

Markdown-Tabelle:
| Problem | Datei | Zeile | Schwere | Empfehlung |
```

## `.claude/agents/test-writer.md`

```markdown
---
name: test-writer
description: Generiert pytest-Tests für neue oder ungetestete Routen in app.py
tools:
  - Read
  - Write(test_app.py)
---

# Test Writer

1. Lies app.py und test_app.py komplett
2. Finde alle Routen in app.py, die noch keinen Test haben
3. Schreibe für jede fehlende Route mindestens 2 Tests:
   - Happy path (normaler Aufruf)
   - Edge case (leere Eingabe, ungültiger Wert)
4. Nutze das bestehende `client`-Fixture aus test_app.py

## Regeln

- Keine neuen Fixtures einführen
- Bestehende Tests nicht verändern
```
