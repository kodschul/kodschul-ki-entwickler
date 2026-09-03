# Übung: VS Code Tasks (Hook-Äquivalent)

**Zeit:** 10:45 – 12:15 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Auto-Test Task einrichten (15 min)

**Ziel:** Tests können per Task schnell ausgeführt werden, wenn Copilot `app.py` ändert.

Erstelle `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Tests: Schnell",
      "type": "shell",
      "command": "python -m pytest test_app.py -q --tb=line",
      "group": {
        "kind": "test",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "shared",
        "clear": true
      }
    }
  ]
}
```

**Testen:**

1. `Strg+Shift+P` → `Tasks: Run Test Task`
2. Oder: `Strg+Shift+P` → `Tasks: Run Task` → `Tests: Schnell`

Beobachte: Laufen die Tests im integrierten Terminal?

**Mit gh copilot CLI denselben Befehl finden:**

```bash
gh copilot suggest "pytest mit quicken output ausführen" -t shell
```

---

## Aufgabe 2 – Backup Task für todos.json (15 min)

**Ziel:** Bevor `todos.json` verändert wird, entsteht ein Backup.

Da VS Code keine Pre-Save-Hooks hat, nutzen wir einen Git Pre-Commit Hook:

```bash
# Datei erstellen
mkdir -p .git/hooks
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
if [ -f "todos.json" ]; then
  cp todos.json todos.backup.json
  echo "Backup erstellt: todos.backup.json"
fi
EOF
chmod +x .git/hooks/pre-commit
```

**Oder per gh copilot CLI:**

```bash
gh copilot suggest "pre-commit git hook erstellen der todos.json sichert" -t shell
```

**Testen:**

```bash
git add . && git commit -m "test backup hook"
ls -la todos*.json
```

Prüfe: Existiert danach `todos.backup.json`?

---

## Aufgabe 3 – Vollständige tasks.json (10 min)

**Ziel:** Mehrere häufig genutzte Befehle als Tasks hinterlegen.

Erweitere `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Tests: Schnell",
      "type": "shell",
      "command": "python -m pytest test_app.py -q --tb=line",
      "group": { "kind": "test", "isDefault": true }
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
      "command": "python -m flake8 app.py --max-line-length=100",
      "group": "build"
    },
    {
      "label": "App starten",
      "type": "shell",
      "command": "FLASK_DEBUG=1 python app.py",
      "group": "build",
      "isBackground": true,
      "problemMatcher": []
    }
  ]
}
```

**Testen:** Alle Tasks nacheinander ausführen.

---

## Aufgabe 4 – GitHub Actions Workflow erstellen (15 min)

**Ziel:** Tests laufen automatisch bei jedem Push – echtes CI/CD.

```
Erstelle eine GitHub Actions Workflow-Datei unter .github/workflows/test.yml,
die bei jedem Push zu Python-Dateien automatisch pytest ausführt.
Nutze Python 3.12 und installiere requirements.txt.
```

**Oder manuell erstellen** `.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    paths:
      - "**.py"
      - "requirements.txt"
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Abhängigkeiten installieren
        run: pip install -r requirements.txt
      - name: Tests ausführen
        run: python -m pytest test_app.py -v --tb=short
```

**Mit gh copilot CLI validieren:**

```bash
gh copilot explain "actions/checkout@v4"
gh copilot suggest "GitHub Actions Workflow syntax prüfen"
```

**Diskussion:**

- Was ist der Unterschied zwischen einem VS Code Task und einem GitHub Actions Workflow?
- Wann nutzt du welchen Ansatz?
