# Konfiguration & .md-Dateien

**Block:** 09:15 – 10:30 Uhr

---

## Wie funktioniert das unter der Haube?

Beim Start liest GitHub Copilot automatisch definierte Dateien und baut daraus den **System-Prompt** – unsichtbar, vor jeder Antwort.

```
Chat geöffnet
  → copilot-instructions.md     → Projektkontext
  → .github/instructions/       → dateispezifische Regeln
  → .vscode/settings.json       → welche Instructions geladen werden
  → Erste Antwort ist bereits kontextuell korrekt
```

> Diese Dateien sind kein Code – sie sind **Kontext**. Copilot liest sie wie ein Briefing.

---

## Warum / Wann nicht?

| Warum nutzen                      | Wann nicht                                         |
| --------------------------------- | -------------------------------------------------- |
| Gleicher Kontext bei jedem Start  | Einmaliger Prompt → direkt tippen                  |
| Teamkontext via Git teilbar       | Sensible Daten → niemals in `.md`, immer `.env`    |
| Verhalten gezielt steuern         | Zu viele Instructions (>10) → Copilot wird ungenau |
| Lange Prompts als Datei speichern | Sehr spezifische Ausnahme → Kommentar im Code      |

---

## Überblick: Welche Datei macht was?

| Datei                     | Wo                      | Zweck                                                   |
| ------------------------- | ----------------------- | ------------------------------------------------------- |
| `copilot-instructions.md` | `.github/`              | Globaler Kontext & Regeln für Copilot in diesem Projekt |
| `*.instructions.md`       | `.github/instructions/` | Wiederverwendbare Anweisung für bestimmte Dateitypen    |
| `*.prompt.md`             | `.github/prompts/`      | Slash-Command (`/name`) mit eigenem Workflow            |
| `*.agent.md`              | `.github/agents/`       | Spezialisierter Agent mit eigenen Tools/Regeln          |
| `settings.json`           | `.vscode/`              | Projektspezifische Copilot-Einstellungen & Hooks        |
| `tasks.json`              | `.vscode/`              | Automatisierungsaufgaben (Hook-Äquivalent)              |

---

## copilot-instructions.md – Projektkontext

Copilot liest `.github/copilot-instructions.md` **automatisch** in jeder Chat-Session.  
Hier steht alles, was Copilot über das Projekt wissen muss.

**Aufbau:**

```markdown
# GitHub Copilot Instructions

## Project Goal

[Ein Satz – was macht diese App?]

## Commands

[Wie starte/teste ich die App?]

## Do

[Was soll Copilot tun?]

## Don't

[Was soll Copilot NICHT tun?]
```

**Beispiel – unsere Todo-App:**

```markdown
# GitHub Copilot Instructions

## Project Goal

Minimale Todo-Web-App zum Lernen – Flask + HTML-Forms.
Nutzer können Todos anlegen, bearbeiten, abhaken, löschen.

## Commands

FLASK_DEBUG=1 python app.py # Dev-Server starten
python -m pytest test_app.py # Tests ausführen

## Do

- HTML-Form-POSTs mit Redirect verwenden (Post/Redirect/Get)
- Alle Daten in todos.json speichern
- Tailwind CDN für Styling nutzen

## Don't

- Keine REST-API oder JavaScript fetch
- Keine Datenbank oder ORM
- Keine zusätzlichen Python-Dateien
```

**Tipp:** Je präziser die `copilot-instructions.md`, desto weniger muss man Copilot erklären.

---

## .instructions.md – Wiederverwendbare Anweisungen

Eine Instruction-Datei ist eine **Anleitung für eine bestimmte Aufgabe oder Dateigruppe**, die Copilot immer gleich ausführen soll.

**Aufbau:**

```markdown
---
applyTo: "**/*.py"
description: "Wann wird diese Instruction verwendet?"
---

# Titel

- Regel 1
- Regel 2
- Schritt A
- Schritt B
```

**Beispiel – Python-Regeln:**

```markdown
---
applyTo: "**/*.py"
description: "Python code generation rules"
---

# Python Guidelines

- Verwende Python 3.12+ Syntax
- Schreibe immer Typ-Annotationen
- Nutze pytest für Tests
- Behandle alle Exceptions explizit
```

**Beispiel – Flask-spezifisch:**

```markdown
---
applyTo: "**/app.py"
description: "Flask application guidelines"
---

# Flask Guidelines

- Nutze Post/Redirect/Get Pattern
- Validiere alle Formular-Eingaben
- Verwende flash() für Nutzermeldungen
```

---

## .vscode/settings.json – Copilot konfigurieren

Steuere, welche Instructions für welchen Kontext gelten:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/instructions/python.instructions.md"
    }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze pytest. Erstelle happy path und edge case Tests."
    }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    {
      "file": ".github/instructions/security.instructions.md"
    }
  ]
}
```

---

## gh copilot CLI – Kurzreferenz

```bash
# Copilot CLI installieren (einmalig)
gh extension install github/gh-copilot

# Befehl vorschlagen lassen
gh copilot suggest "Tests für Python-App ausführen"

# Befehl erklären lassen
gh copilot explain "python -m pytest -v --tb=short"

# Interaktiver Modus
gh copilot suggest -t shell "Zeige alle Python-Dateien im Projekt"
```
