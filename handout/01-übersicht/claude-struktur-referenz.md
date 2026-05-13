# .claude – Vollständige Struktur & Referenz

---

## Verzeichnisstruktur

```
mein-projekt/
└── .claude/
    ├── settings.local.json       ← Projektspezifische Konfiguration
    ├── commands/
    │   ├── todo-review.md        ← /todo-review
    │   ├── add-feature.md        ← /add-feature
    │   └── run-tests.md          ← /run-tests
    ├── agents/
    │   ├── security-reviewer.md  ← Sicherheits-Audit Agent
    │   └── test-writer.md        ← Test-Generierungs Agent
    └── skills/
        ├── feature-builder/
        │   └── SKILL.md
        ├── api-designer/
        │   └── SKILL.md
        └── bug-finder/
            └── SKILL.md

~/.claude/
├── settings.json                 ← Globale Konfiguration (alle Projekte)
└── commands/
    └── daily-review.md           ← Globaler Command
```

---

## settings.json – Alle Optionen

```jsonc
{
  // ─── Modell ───────────────────────────────────────────────
  "model": "claude-sonnet-4-5",
  // Verfügbare Modelle: claude-opus-4-5, claude-sonnet-4-5, claude-haiku-4-5

  // ─── API-Key (für Nicht-Anthropic-Provider) ───────────────
  "apiKeyHelper": "cat ~/.secrets/anthropic-key",
  // Shell-Befehl dessen Ausgabe als API-Key verwendet wird
  // Niemals den Key direkt hier eintragen

  // ─── Darstellung ──────────────────────────────────────────
  "theme": "dark",
  // Werte: "dark" | "light" | "auto"

  "outputStyle": "default",
  // Werte: "default" | "compact" | "verbose"

  "statusLine": true,
  // Zeigt Token-Zähler und Modell-Info in der Statuszeile

  // ─── Verhalten ────────────────────────────────────────────
  "autoApprove": false,
  // true = Claude fragt nicht nach Bestätigung (gefährlich!)

  "verbose": false,
  // true = mehr interne Ausgaben sichtbar

  "maxTurns": 10,
  // Maximale Anzahl an Schritten pro Aufgabe

  // ─── Berechtigungen ───────────────────────────────────────
  "permissions": {
    "allow": [
      // Bash-Befehle die ohne Rückfrage ausgeführt werden dürfen
      "Bash(python -m pytest *)",
      "Bash(pip install *)",
      "Bash(cat *)",
      "Bash(ls *)",
      "Bash(FLASK_DEBUG=1 python app.py)",

      // MCP-Tool-Erlaubnisse
      "mcp__playwright__browser_navigate",
      "mcp__playwright__browser_take_screenshot",
      "mcp__playwright__browser_fill_form",
      "mcp__playwright__browser_click",

      // Datei-Operationen
      "Read",
      "Write"
    ],
    "deny": [
      // Komplett gesperrte Befehle
      "Bash(rm -rf *)",
      "Bash(git push *)",
      "Bash(git reset --hard *)",
      "Bash(DROP TABLE *)",
      "Write(/etc/*)",
      "Write(~/.ssh/*)"
    ]
  },

  // ─── MCP-Server ───────────────────────────────────────────
  // Jeder Eintrag startet beim Claude-Start einen eigenen Prozess.
  // Claude verbindet sich per stdio und erhält die Tools des Servers.
  // Die Tools erscheinen für Claude wie eingebaute Tools (Read, Write, Bash).
  "mcpServers": {
    // ── Playwright (Browser-Automation) ──────────────────────
    "playwright": {
      // "command": Das Programm das den MCP-Server startet
      "command": "npx",
      // "args": Argumente an das Programm
      "args": ["@playwright/mcp@latest"],
      // "env": Zusätzliche Umgebungsvariablen für den Server-Prozess
      "env": {}
      // Verfügbare Tools danach: mcp__playwright__browser_navigate,
      //   browser_click, browser_fill_form, browser_take_screenshot, ...
    },

    // ── Filesystem-Server ────────────────────────────────────
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/pfad/zum/projekt" // ← Nur dieses Verzeichnis ist zugänglich
        // Claude kann außerhalb dieses Pfads NICHTS lesen oder schreiben
        // → gezielt statt ganzes Dateisystem freigeben
      ]
      // Verfügbare Tools: read_file, write_file, list_directory, search_files
    },

    // ── Eigener Python-Server ────────────────────────────────
    "custom-server": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {
        // Shell-Variablen referenzieren: ${VAR} wird zur Laufzeit aufgelöst
        // Der echte Wert steht NICHT in dieser Datei → sicher versionierbar
        "DATABASE_URL": "${DATABASE_URL}",
        "API_KEY": "${MY_API_KEY}"
        // ⚠ Nie echte Werte hier eintragen – immer ${VAR} Referenz
      }
    }
  },

  // ─── Hooks ────────────────────────────────────────────────
  "hooks": {
    // Vor einem Tool-Aufruf
    "PreToolUse": [
      {
        "matcher": "Write(todos.json)",
        "hooks": [
          {
            "type": "command",
            "command": "cp todos.json todos.backup.json 2>/dev/null || true"
          }
        ]
      }
    ],

    // Nach einem Tool-Aufruf
    "PostToolUse": [
      {
        "matcher": "Write(app.py)",
        "hooks": [
          {
            "type": "command",
            "command": "python -m pytest test_app.py -q --tb=line"
          }
        ]
      },
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {
            "type": "command",
            "command": "python -m flake8 --max-line-length=120 $TOOL_INPUT_PATH 2>/dev/null || true"
          }
        ]
      }
    ],

    // Wenn Claude die Session beendet
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo \"Session beendet: $(date '+%d.%m.%Y %H:%M')\""
          }
        ]
      }
    ],

    // Wenn Claude eine Benachrichtigung schickt
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude ist fertig\" with title \"Claude Code\"'"
            // macOS-Benachrichtigung
          }
        ]
      }
    ]
  }
}
```

---

## CLAUDE.md – Aufbau

```markdown
# CLAUDE.md

## Project Goal

[Ein Satz was die App tut]

## Commands

FLASK_DEBUG=1 python app.py # Dev-Server
python -m pytest test_app.py -v # Tests

## Architecture

Request → app.py (Flask) → todos.json → Jinja2-Template → Browser

## Do

- Post/Redirect/Get Pattern verwenden
- Daten in todos.json speichern
- Tailwind CDN für Styling

## Don't

- Kein eval() oder exec()
- Keine Passwörter im Code
- Keine zusätzlichen Python-Dateien
```

---

## SKILL.md – Aufbau

```markdown
---
name: skill-name
description: Wann wird dieser Skill automatisch aktiviert?
model: sonnet # optional
---

# Titel

- Regel / Schritt 1
- Regel / Schritt 2
- Regel / Schritt 3
```

---

## commands/<name>.md – Aufbau

```markdown
# Command-Titel

[Was dieser Command tut]

## Schritte

1. Schritt 1
2. Schritt 2
3. Ausgabe / Ergebnis

## Regeln

- Regel A
- Regel B
```

**Platzhalter:**

| Variable        | Wert                          |
| --------------- | ----------------------------- |
| `$ARGUMENTS`    | Text nach `/command-name ...` |
| `$CURRENT_FILE` | Aktuell geöffnete Datei       |
| `$CURRENT_DIR`  | Aktuelles Verzeichnis         |

---

## agents/<name>.md – Aufbau

```markdown
---
name: agent-name
description: Wann wird dieser Agent aufgerufen?
model: sonnet # optional
tools: # optional – Tool-Whitelist
  - Read
  - Write(test_app.py)
---

# Agent-Titel

[Aufgabe des Agents]

## Schritte

1. ...
2. ...

## Regeln

- ...
```

---

## Output-Formate (CLI)

```bash
# Interaktiv (Standard)
claude

# Nur Antwort, kein UI – für Skripte
claude --print "Was macht app.py?"

# Markdown-Ausgabe
claude --print "Review app.py" > review.md

# JSON-Ausgabe
claude --output-format json --print "Review app.py"

# Streaming JSON (für Echtzeit-Verarbeitung)
claude --output-format stream-json --print "Review app.py"

# Kompakter Modus (weniger UI-Rauschen)
claude --output-format compact

# Kein Bestätigungsdialog
claude --dangerously-skip-permissions --print "..."
# ⚠ Nur in kontrollierten CI-Umgebungen
```

---

## Hooks – Matcher-Referenz

| Matcher          | Auslöser                            |
| ---------------- | ----------------------------------- |
| `Write`          | Jede Datei schreiben                |
| `Write(app.py)`  | Nur `app.py` schreiben              |
| `Write(*.py)`    | Alle Python-Dateien                 |
| `Bash`           | Jeder Bash-Aufruf                   |
| `Bash(pytest *)` | Bash-Befehle die mit pytest starten |
| `Read`           | Jede Datei lesen                    |
| `*`              | Alle Tools                          |

---

## .env & Secrets – Was Claude lesen darf und was nicht

### Das Problem

Claude hat standardmäßig Lesezugriff auf **alle Dateien im Projekt**.  
Das bedeutet: Claude kann `.env`, `secrets.json`, SSH-Keys lesen – wenn niemand es verhindert.

### Schutzmechanismen

**1. `deny` in permissions – Lesen bestimmter Dateien sperren**

```json
"permissions": {
  "deny": [
    "Read(.env)",
    "Read(.env.*)",
    "Read(*.pem)",
    "Read(*.key)",
    "Write(.env)"
  ]
}
```

**2. `.claudeignore` – Dateien komplett ausblenden**

Datei `.claudeignore` im Projektroot:

```
.env
.env.local
.env.production
secrets/
*.pem
*.key
~/.ssh/
```

> Funktioniert wie `.gitignore` – Claude sieht diese Dateien nicht, auch wenn es danach sucht.

**3. Env-Variablen statt Dateien**

Sensible Werte als Shell-Variablen setzen, nicht in Dateien:

```bash
export API_KEY="mein-geheimer-key"
claude
```

In `settings.json` dann per `${API_KEY}` referenzieren – kein echter Wert in der Config-Datei.

**4. `apiKeyHelper` statt direktem Key**

```json
"apiKeyHelper": "cat ~/.secrets/anthropic-key"
```

→ Key liegt außerhalb des Projekts, wird nur zur Laufzeit gelesen.

### Zusammenfassung: Was wohin gehört

| Wo                                      | Was speichern                          | Was nicht                |
| --------------------------------------- | -------------------------------------- | ------------------------ |
| `settings.json` / `settings.local.json` | Permissions, Hooks, MCP-Config         | API-Keys, Passwörter     |
| `.env`                                  | Lokale Umgebungsvariablen              | Niemals in Git committen |
| `.claudeignore`                         | Dateipfade die Claude nicht sehen soll | –                        |
| `~/.secrets/`                           | Sensitive Keys außerhalb des Repos     | –                        |
| Shell-Umgebung (`export`)               | Temporäre Werte für aktuelle Session   | –                        |
