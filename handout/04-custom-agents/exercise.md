# Übung: Custom Agents

**Zeit:** 10:45 – 12:15 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – `security-reviewer` Agent erstellen (20 min)

**Ziel:** Agent, der nur liest und einen Sicherheitsbericht erstellt.

Erstelle `.claude/agents/security-reviewer.md`:

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
- eval() oder exec() Aufrufe
- Fehlende Authentifizierung an sensiblen Routen
- Unsichere Dateioperationen

## Ausgabe

Markdown-Tabelle:
| Problem | Datei | Zeile | Schwere | Empfehlung |
```

**Testen:**

```
Mach einen Sicherheits-Audit der Todo-App.
```

**Beobachten:**

- Welche Probleme findet der Agent?
- Versucht er, Code zu ändern? (Sollte er nicht können)

---

## Aufgabe 2 – `test-writer` Agent erstellen (25 min)

**Ziel:** Agent, der fehlende Tests schreibt – nur in `test_app.py`.

Erstelle `.claude/agents/test-writer.md`:

```markdown
---
name: test-writer
description: Generiert pytest-Tests für neue oder ungetestete Routen in app.py
tools:
  - Read
  - Write(test_app.py)
---

# Test Writer

1. Lies app.py und test_app.py
2. Finde alle Routen ohne Test
3. Schreibe für jede fehlende Route mindestens 2 Tests:
   - Happy path
   - Edge case (leere Eingabe, ungültiger Wert)
4. Nutze das bestehende client-Fixture
5. Nur test_app.py ändern

## Regeln

- Keine neuen Fixtures
- Bestehende Tests nicht ändern
- Kommentare auf Deutsch
```

**Testen:**

```
Schreib Tests für alle Routen in app.py, die noch nicht in test_app.py getestet sind.
```

Danach ausführen:

```bash
python -m pytest test_app.py -v
```

---

## Aufgabe 3 – Eigenen Agent bauen (15 min)

Wähle eine der folgenden Ideen oder erfinde eine eigene:

| Agent              | Beschreibung                                                      |
| ------------------ | ----------------------------------------------------------------- |
| `doc-writer`       | Schreibt Docstrings für alle Funktionen ohne Dokumentation        |
| `refactor-advisor` | Analysiert Code und schlägt Refactorings vor (nur lesen)          |
| `todo-cleaner`     | Findet und löscht abgehakte Todos aus todos.json (nur JSON-Datei) |

**Prompt zum Starten:**

```
Erstelle einen neuen Agent unter .claude/agents/<name>.md.
Der Agent soll [AUFGABE].
Er darf nur folgende Tools nutzen: [TOOLS].
Ausgabe soll [FORMAT] sein.
```

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] `.claude/agents/security-reviewer.md` erstellt und getestet
- [ ] `.claude/agents/test-writer.md` erstellt, Tests generiert und ausgeführt
- [ ] Einen eigenen Agent nach Wahl erstellt
