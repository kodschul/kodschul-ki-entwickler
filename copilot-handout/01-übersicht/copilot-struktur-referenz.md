# .github – Vollständige Struktur & Referenz

---

## Verzeichnisstruktur

```
mein-projekt/
├── .github/
│   ├── copilot-instructions.md          ← Projektweite Anweisungen für Copilot
│   ├── instructions/
│   │   ├── python.instructions.md       ← Gilt für alle *.py Dateien
│   │   ├── flask.instructions.md        ← Flask-spezifische Regeln
│   │   └── security.instructions.md    ← Sicherheitsregeln
│   ├── prompts/
│   │   ├── todo-review.prompt.md        ← /todo-review
│   │   ├── add-feature.prompt.md        ← /add-feature
│   │   └── run-tests.prompt.md          ← /run-tests
│   └── agents/
│       ├── security-reviewer.agent.md   ← Sicherheits-Audit Agent
│       └── test-writer.agent.md         ← Test-Generierungs Agent
└── .vscode/
    ├── settings.json                    ← Projektspezifische VS Code Einstellungen
    ├── tasks.json                       ← Automatisierungsaufgaben (Hook-Äquivalent)
    └── mcp.json                         ← MCP-Server Konfiguration

~/.config/github-copilot/               ← Globale Konfiguration (alle Projekte)
```

---

## copilot-instructions.md – Alle Optionen

```markdown
# GitHub Copilot Instructions

## Projekt

[Projektbeschreibung]

## Sprache & Stil

- Antworte auf Deutsch
- Verwende Python 3.12+
- Nutze Flask für alle Web-Endpunkte

## Regeln

- Schreibe immer Tests für neuen Code
- Nutze keine eval() oder exec()
- Kein Hardcoding von Passwörtern

## Architektur

[Beschreibe Datenfluss, Ordnerstruktur etc.]
```

---

## .instructions.md – Datei-spezifische Anweisungen

**Frontmatter-Felder:**

```yaml
---
applyTo: "**/*.py"        # Glob-Pattern: welche Dateien betroffen sind
description: "..."        # Optionale Beschreibung
---
```

**Verfügbare `applyTo`-Muster:**

| Muster             | Bedeutung                            |
| ------------------ | ------------------------------------ |
| `**`               | Alle Dateien (global)                |
| `**/*.py`          | Alle Python-Dateien                  |
| `src/**`           | Alles im src-Ordner                  |
| `**/test_*.py`     | Alle Test-Dateien                    |
| `templates/**`     | Alle Templates                       |

---

## .prompt.md – Custom Slash Commands

**Frontmatter-Felder:**

```yaml
---
mode: ask           # "ask" | "edit" | "agent"
description: "..."  # Beschreibung des Commands
tools:              # Optional: erlaubte Tools
  - codebase
  - terminal
---
```

**Modi:**

| Modus    | Bedeutung                                           |
| -------- | --------------------------------------------------- |
| `ask`    | Stellt Fragen / analysiert Code (kein Schreiben)    |
| `edit`   | Bearbeitet aktuelle Datei direkt                    |
| `agent`  | Voller Agentenmodus mit Tool-Zugriff                |

---

## .agent.md – Custom Agents

**Frontmatter-Felder:**

```yaml
---
name: agent-name
description: "Wann wird dieser Agent verwendet?"
tools:
  - codebase
  - terminal
  - githubRepo
---
```

---

## .vscode/settings.json – Projektspezifische Einstellungen

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/instructions/python.instructions.md"
    }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze pytest. Erstelle immer happy path und edge case Tests."
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

## .vscode/mcp.json – MCP-Server Konfiguration

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
