# MCP + gh copilot CLI + Abschluss

**Block:** 15:15 – 17:00 Uhr

---

## Teil 1: MCP – Model Context Protocol

### Wie funktioniert das unter der Haube?

```
VS Code startet
  → liest .vscode/mcp.json
  → verbindet sich zu jedem Server (stdio oder SSE)
  → Server registriert Tools (z.B. browser_navigate)
  → Copilot kann diese Tools wie eigene nutzen
```

> MCP ist ein offenes Protokoll. Jeder kann einen MCP-Server bauen.  
> Copilot sieht MCP-Tools genauso wie eingebaute Tools (codebase, terminal).

### Warum / Wann nicht?

| Warum nutzen                    | Wann nicht                                        |
| ------------------------------- | ------------------------------------------------- |
| Browser-Automation (Playwright) | Server nicht vertrauenswürdig → Sicherheitsrisiko |
| Externe Datenquellen anbinden   | Latenz kritisch → stdio-Server bevorzugen         |
| Eigene Firma-Tools in Copilot   | Nur ein Tool nötig → Terminal reicht oft          |
| Parallelisierte Sub-Aufgaben    | MCP-Server nicht stabil → bremst Copilot          |

### Konfiguration in `.vscode/mcp.json`

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {}
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/pfad/zum/projekt"
      ]
    }
  }
}
```

### Playwright MCP – Beispiel

```
Öffne die Todo-App unter http://localhost:5000,
füge ein Todo mit dem Titel "MCP Test" hinzu und
mach einen Screenshot.
```

Copilot nutzt dann automatisch:

- `playwright_navigate`
- `playwright_fill`
- `playwright_screenshot`

---

## Teil 2: gh copilot CLI – Vollständige Referenz

### Installation

```bash
# GitHub CLI installieren (falls nicht vorhanden)
brew install gh         # macOS
winget install GitHub.cli  # Windows

# Anmelden
gh auth login

# Copilot Extension installieren
gh extension install github/gh-copilot

# Verfügbare Befehle anzeigen
gh copilot --help
```

### Befehle im Überblick

```bash
# Shell-Befehl vorschlagen
gh copilot suggest "Tests für Python-App ausführen"

# Zieltyp angeben
gh copilot suggest -t shell  "..."   # Shell-Befehl
gh copilot suggest -t git   "..."   # Git-Befehl
gh copilot suggest -t gh    "..."   # GitHub CLI-Befehl

# Befehl erklären
gh copilot explain "python -m pytest -v --tb=short"
gh copilot explain "git rebase -i HEAD~3"

# Alias einrichten (Kurzform)
gh copilot alias set suggest "ghcs"
gh copilot alias set explain "ghce"
```

### Headless Mode – für CI/Automation

```bash
# Review als CI-Schritt
gh copilot suggest \
  "Code-Review von app.py durchführen und als Markdown ausgeben" \
  | tee review-output.md
```

```bash
# In einem Shell-Skript (review.sh)
#!/bin/bash
echo "Starte Code-Review..."

# Copilot CLI für Terminal-Befehl fragen
REVIEW_CMD=$(gh copilot suggest -t shell \
  "Python-Datei app.py auf Sicherheitsprobleme analysieren" \
  --no-interaction 2>/dev/null)

echo "Empfohlener Befehl: $REVIEW_CMD"
echo "Review gespeichert: review-output.md"
```

### Output-Formate

```bash
# Standard-Ausgabe
gh copilot suggest "pytest ausführen"

# Direkt ausführen (nach Bestätigung)
gh copilot suggest "pytest mit Coverage" --execute

# Ohne Interaktion (für Skripte)
gh copilot suggest "..." --no-interaction
```

---

## Teil 3: Customization & Output-Kontrolle

### Copilot Chat – Ausgabe steuern

```
# Structured Output anfordern
Analysiere app.py. Ausgabe NUR als JSON-Array:
[{"problem": "", "severity": "", "line": 0}]

# Markdown-Tabelle erzwingen
Erstelle einen Review als Markdown-Tabelle:
| Problem | Datei | Schwere | Empfehlung |

# Kompakte Ausgabe
Fasse die Probleme in 3 Bulletpoints zusammen.
```

### Permissions – via Instructions steuern

```markdown
<!-- .github/copilot-instructions.md -->

## Einschränkungen

- Führe keine destruktiven Operationen aus (rm -rf, DROP TABLE)
- Kein git push ohne explizite Anweisung
- Sensible Daten niemals im Code – immer Umgebungsvariablen nutzen
- Ändere requirements.txt nur wenn explizit angefragt
```

---

## Teil 4: Abschluss & Retrospektive

### Was hat die Todo-App heute bekommen?

```
1205/todo-app/
├── app.py                         + Due-Dates Feature
├── test_app.py                    + Tests für Due-Dates
├── specs/due-dates.md             Spec-Driven Workflow
└── .github/
    ├── copilot-instructions.md    Projektkontext
    ├── instructions/
    │   ├── python.instructions.md
    │   └── security.instructions.md
    ├── prompts/
    │   ├── todo-review.prompt.md
    │   ├── add-feature.prompt.md
    │   ├── spec-plan.prompt.md
    │   ├── spec-build.prompt.md
    │   └── spec-test.prompt.md
    ├── agents/
    │   ├── security-reviewer.agent.md
    │   └── test-writer.agent.md
    └── workflows/
        └── test.yml               CI/CD Automation
└── .vscode/
    ├── settings.json              Copilot-Einstellungen
    ├── tasks.json                 Test-Tasks
    └── mcp.json                   MCP-Server
```

### GitHub Copilot vs. Claude Code – Abschlussvergleich

| Feature                    | Claude Code                  | GitHub Copilot                          |
| -------------------------- | ---------------------------- | --------------------------------------- |
| Projektkontext             | `CLAUDE.md`                  | `.github/copilot-instructions.md`       |
| Globale Einstellungen      | `~/.claude/settings.json`    | VS Code User Settings                   |
| Custom Commands            | `.claude/commands/*.md`      | `.github/prompts/*.prompt.md`           |
| Custom Agents              | `.claude/agents/*.md`        | `.github/agents/*.agent.md`             |
| Skills / Instructions      | `.claude/skills/*/SKILL.md`  | `.github/instructions/*.instructions.md` |
| Hooks                      | `hooks` in settings.json     | `.vscode/tasks.json` + GitHub Actions   |
| MCP                        | `mcpServers` in settings.json | `.vscode/mcp.json`                     |
| CLI (Headless)             | `claude --print "..."`       | `gh copilot suggest "..."`              |
| Sandbox / Permissions      | `"deny": [...]`              | Instructions + keine `terminal`-Tools   |
