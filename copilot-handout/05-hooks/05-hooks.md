# VS Code Tasks (Hook-Äquivalent)

**Block:** 10:45 – 12:15 Uhr (zusammen mit Prompts & Agents)

---

## Wie funktioniert das unter der Haube?

```
Datei wird gespeichert (oder Build-Trigger)
  → VS Code Task-Event wird ausgelöst (z.B. onSave)
  → tasks.json führt den konfigurierten Befehl aus
  → Ausgabe erscheint im Terminal-Panel
```

> Tasks sind **Shell-Befehle**, die automatisch vor oder nach bestimmten Aktionen laufen.  
> Konfiguriert in `.vscode/tasks.json`.

> **Hinweis:** GitHub Copilot hat keine direkten „Hooks" wie Claude Code (`PostToolUse`, `PreToolUse`).  
> Das nächstgelegene Äquivalent in VS Code sind **Tasks** + **GitHub Actions** für CI-Pipelines.

---

## Warum / Wann nicht?

| Warum nutzen                        | Wann nicht                                                |
| ----------------------------------- | --------------------------------------------------------- |
| Tests automatisch nach Codeänderung | Task-Befehl dauert sehr lang → blockiert Editor           |
| Linting erzwingen                   | Zu komplexe Logik → lieber separates Skript               |
| Build-Automatisierung               | Vertrauliche Daten in Task-Output → sichtbar im Terminal  |
| Benachrichtigung bei Fertigstellung | Zu viele Tasks → Übersicht verloren                       |

---

## Aufbau in `.vscode/tasks.json`

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "python -m pytest test_app.py -q --tb=line",
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      },
      "runOptions": {
        "runOn": "folderOpen"
      }
    }
  ]
}
```

**Task-Typen:**

| Typ       | Beschreibung                              |
| --------- | ----------------------------------------- |
| `shell`   | Shell-Befehl ausführen                    |
| `process` | Prozess direkt starten (ohne Shell)       |
| `npm`     | npm-Skript ausführen                      |

**`group`-Werte:**

| Gruppe    | Bedeutung                                           |
| --------- | --------------------------------------------------- |
| `build`   | Wird mit `Strg+Shift+B` gestartet                   |
| `test`    | Wird mit Test-Runner ausgeführt                     |
| `none`    | Nur manuell über Command Palette                    |

---

## Vergleich: Claude Hooks vs. VS Code Tasks

| Claude Code Hook             | VS Code Äquivalent                                     |
| ---------------------------- | ------------------------------------------------------ |
| `PostToolUse` bei `Write`    | Task mit `onSave`-Trigger (via Extension)              |
| `PreToolUse` bei `Write`     | Pre-Build Task / Git Hook (`.git/hooks/pre-commit`)    |
| `Stop` (Session-Ende)        | `runOptions: { runOn: "default" }` + Terminal          |
| `Bash(pytest *)` erlauben    | Task direkt definieren + starten                       |

---

## Beispiel 1 – Tests nach Codeänderung

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Auto: Tests ausführen",
      "type": "shell",
      "command": "python -m pytest test_app.py -q --tb=line",
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "shared",
        "clear": true
      }
    }
  ]
}
```

→ Mit `Strg+Shift+P` → `Tasks: Run Task` → `Auto: Tests ausführen` starten.  
→ Oder: Tastenkombination in `keybindings.json` hinterlegen.

---

## Beispiel 2 – Backup vor Überschreiben (Git Hook)

Da VS Code Tasks keine „Before-Save"-Hooks bieten, nutzen wir einen Git Pre-Commit Hook:

```bash
# .git/hooks/pre-commit
#!/bin/bash
cp todos.json todos.backup.json 2>/dev/null || true
echo "Backup erstellt: todos.backup.json"
```

```bash
chmod +x .git/hooks/pre-commit
```

---

## Beispiel 3 – Mehrere Tasks

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Tests: Schnell",
      "type": "shell",
      "command": "python -m pytest test_app.py -q",
      "group": "test"
    },
    {
      "label": "Tests: Verbose",
      "type": "shell",
      "command": "python -m pytest test_app.py -v --tb=short",
      "group": "test"
    },
    {
      "label": "Lint: flake8",
      "type": "shell",
      "command": "python -m flake8 app.py",
      "group": "build"
    },
    {
      "label": "App starten",
      "type": "shell",
      "command": "FLASK_DEBUG=1 python app.py",
      "group": "build",
      "isBackground": true
    }
  ]
}
```

---

## GitHub Actions – CI-Äquivalent zu Hooks

Für echte Automation im Team (analog zu Claude Headless-Mode):

```yaml
# .github/workflows/test.yml
name: Tests

on:
  push:
    paths:
      - "**.py"
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest test_app.py -v --tb=short
```

→ Jedes Mal wenn eine Python-Datei gepusht wird, laufen Tests automatisch.

---

## gh copilot CLI – Befehle für Automation

```bash
# Passenden Befehl für Auto-Test vorschlagen lassen
gh copilot suggest "Tests nach jeder Python-Dateiänderung automatisch ausführen"

# Git-Hook-Skript generieren lassen
gh copilot suggest -t shell "pre-commit Hook erstellen der pytest ausführt"
```
