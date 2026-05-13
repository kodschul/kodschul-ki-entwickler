# MCP + Customization + Abschluss

**Block:** 15:15 – 17:00 Uhr

---

## Teil 1: MCP – Model Context Protocol

### Wie funktioniert das unter der Haube?

```
Claude Code startet
  → liest mcpServers aus settings.json
  → verbindet sich zu jedem Server (stdio oder SSE)
  → Server registriert Tools (z.B. browser_navigate)
  → Claude kann diese Tools wie eigene nutzen
```

> MCP ist ein offenes Protokoll. Jeder kann einen MCP-Server bauen.  
> Claude sieht MCP-Tools genauso wie eingebaute Tools (Read, Write, Bash).

### Warum / Wann nicht?

| Warum nutzen                    | Wann nicht                                        |
| ------------------------------- | ------------------------------------------------- |
| Browser-Automation (Playwright) | Server nicht vertrauenswürdig → Sicherheitsrisiko |
| Externe Datenquellen anbinden   | Latenz kritisch → stdio-Server bevorzugen         |
| Eigene Firma-Tools in Claude    | Nur ein Tool nötig → Bash reicht oft              |
| Parallelisierte Sub-Aufgaben    | MCP-Server nicht stabil → bremst Claude           |

### Konfiguration in `settings.json`

```json
{
  "mcpServers": {
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

Bereits in der Todo-App vorhanden (`.playwright-mcp/`).

```
Öffne die Todo-App unter http://localhost:5000,
füge ein Todo mit dem Titel "MCP Test" hinzu und
mach einen Screenshot.
```

Claude nutzt dann automatisch:

- `mcp__playwright__browser_navigate`
- `mcp__playwright__browser_fill_form`
- `mcp__playwright__browser_take_screenshot`

---

## Teil 2: Customization & Output-Kontrolle

### Output-Formate

```bash
# Standard (interaktiv)
claude

# Nur Antwort ausgeben, kein UI
claude --print "Was macht app.py?"

# JSON-Ausgabe (für Skripte)
claude --output-format json --print "Review app.py"

# Streaming JSON
claude --output-format stream-json --print "Review app.py"
```

### Headless Mode – für Automation

```bash
# Review als CI-Schritt
claude --print "Führe einen Code-Review von app.py durch. Ausgabe als Markdown." \
  > review-output.md
```

```bash
# In einem Shell-Skript (review.sh)
#!/bin/bash
claude --print \
  "Analysiere app.py auf Sicherheitsprobleme. Ausgabe als JSON-Array mit Feldern: problem, severity, line." \
  --output-format json \
  > review-output.json

echo "Review gespeichert: review-output.json"
```

### Permissions – Least Privilege

```json
{
  "permissions": {
    "allow": ["Bash(python -m pytest *)", "Read"],
    "deny": ["Bash(rm *)", "Bash(git push *)", "Write(/etc/*)"]
  }
}
```

### Sandbox Mode

```bash
# Claude darf nichts ausführen außer was explizit erlaubt ist
claude --sandbox
```

Nützlich für: Code-Review-Pipelines, öffentliche Umgebungen, Demos.

---

## Teil 3: Abschluss & Retrospektive

### Was hat die Todo-App heute bekommen?

```
1205/todo-app/
├── app.py                    + Due-Dates Feature
├── test_app.py               + Tests für Due-Dates
├── specs/due-dates.md        Spec-Driven Workflow
├── review.sh                 Headless CI-Skript
└── .claude/
    ├── settings.local.json   + Hooks + MCP
    ├── commands/
    │   ├── todo-review.md
    │   └── add-feature.md
    ├── agents/
    │   ├── security-reviewer.md
    │   └── test-writer.md
    └── skills/
        ├── feature-builder/
        ├── api-designer/
        └── bug-finder/        (heute erstellt)
```

### Retrospektive

**3 Fragen – jeder beantwortet kurz:**

| Frage                     |                           |
| ------------------------- | ------------------------- |
| Was nehme ich mit?        | Konkretes Tool / Workflow |
| Was war zu komplex?       | Offen ansprechen          |
| Was setze ich morgen ein? | Realer Use Case           |
