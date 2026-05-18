# Übung: Custom Agents

**Zeit:** 10:45 – 12:15 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – `security-reviewer` Agent erstellen (20 min)

**Ziel:** Agent, der nur liest und einen Sicherheitsbericht erstellt.

**Verzeichnis anlegen:**

```bash
mkdir -p .github/agents
```

Erstelle `.github/agents/security-reviewer.agent.md`:

```markdown
---
name: security-reviewer
description: "Führt einen Sicherheits-Audit der App durch. Nur lesen, kein Code ändern."
tools:
  - codebase
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

**Testen (in Copilot Agent-Modus):**

```
Mach einen Sicherheits-Audit der Todo-App.
```

**Beobachten:**

- Welche Probleme findet der Agent?
- Versucht er, Code zu ändern? (Sollte er nicht – `terminal` nicht in tools)
- Wie unterscheidet sich das Ergebnis vom `/todo-review` Prompt?

---

## Aufgabe 2 – `test-writer` Agent erstellen (25 min)

**Ziel:** Agent, der fehlende Tests schreibt – nur in `test_app.py`.

Erstelle `.github/agents/test-writer.agent.md`:

```markdown
---
name: test-writer
description: "Generiert pytest-Tests für neue oder ungetestete Routen in app.py"
tools:
  - codebase
  - terminal
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

**Testen (in Copilot Agent-Modus):**

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

| Idee                  | Agent-Datei                         | Beschreibung                                                |
| --------------------- | ----------------------------------- | ----------------------------------------------------------- |
| **Dokumentations-Bot** | `doc-writer.agent.md`              | Schreibt Docstrings für undokumentierte Funktionen          |
| **Dependency-Checker** | `dependency-checker.agent.md`      | Prüft requirements.txt auf veraltete/unsichere Pakete       |
| **Refactoring-Agent** | `refactor-advisor.agent.md`         | Identifiziert Refactoring-Möglichkeiten ohne Code zu ändern |
| **i18n-Agent**        | `translation-agent.agent.md`        | Erstellt Übersetzungsdateien für App-Texte                  |

**Vorlage:**

```markdown
---
name: [name]
description: "[Wann wird dieser Agent aktiviert?]"
tools:
  - codebase
---

# [Agent-Titel]

[Was soll der Agent tun?]

## Schritte

1. [Schritt 1]
2. [Schritt 2]

## Regeln

- [Regel 1]
- [Regel 2]
```

**Reflektieren:**

- Was ist der Unterschied zwischen diesem Agent und einem Prompt?
- Wann würdest du einen Agent statt einem Prompt nehmen?
- Welche Tools braucht dein Agent wirklich?

---

## Aufgabe 4 – gh copilot CLI als "Agent" (10 min)

```bash
# Security-Audit über CLI
gh copilot suggest "Alle Python-Dateien auf Sicherheitsprobleme analysieren" -t shell

# Test-Lücken finden
gh copilot suggest "Routen in app.py finden die noch keine Tests haben" -t shell

# Befehl direkt ausführen
gh copilot suggest "pytest mit Coverage-Report ausführen" --execute
```

**Vergleich:** CLI vs. Agent-Modus im Editor – was sind die Stärken und Schwächen?
