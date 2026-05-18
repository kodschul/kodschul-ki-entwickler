# 04 – Konfiguration

**Block:** 60 min | **Tag 1**

---

## Die drei Konfigurationsebenen

```
Ebene 1 – Projekt (Team teilt via Git):
  .github/copilot-instructions.md     ← Projektkontext (immer geladen)
  .github/instructions/*.md           ← Skills / dateispezifische Regeln
  .github/prompts/*.prompt.md         ← Custom Slash-Commands
  .github/agents/*.agent.md           ← Custom Agents

Ebene 2 – Projekt-IDE (lokal, nicht committen):
  .vscode/settings.json               ← Copilot-Einstellungen
  .vscode/tasks.json                  ← Automatisierung
  .vscode/mcp.json                    ← MCP-Server

Ebene 3 – Global (alle Projekte):
  VS Code User settings.json          ← Globale Copilot-Defaults
```

---

## copilot-instructions.md – Aufbau

```markdown
# GitHub Copilot Instructions

## Project Goal

[Ein Satz – was macht diese App?]

## Stack

[Sprachen, Frameworks, wichtige Bibliotheken]

## Commands

[Start, Test, Build]

## Architecture

[Dateistruktur, Datenfluss in 3–5 Zeilen]

## Do

- [Regel 1]
- [Regel 2]

## Don't

- [Regel 1]
- [Regel 2]
```

**Goldene Regel:** Maximal 100 Zeilen. Details → `.instructions.md`

---

## .vscode/settings.json – alle Copilot-Optionen

```json
{
  // ─── Instructions für verschiedene Aktionen ───────────────
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/instructions/python.instructions.md" },
    { "text": "Schreibe immer Typ-Annotationen." }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": ".github/instructions/security.instructions.md" }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Format: type(scope): kurze Beschreibung. Englisch." }
  ],

  // ─── Inline Completions ────────────────────────────────────
  "github.copilot.enable": {
    "*": true,
    "markdown": false,
    "plaintext": false,
    "yaml": true
  },

  // ─── Editor Verhalten ─────────────────────────────────────
  "editor.inlineSuggest.enabled": true,
  "editor.inlineSuggest.suppressSuggestions": false,

  // ─── Chat ──────────────────────────────────────────────────
  "github.copilot.chat.localeOverride": "de"
}
```

---

## Commit-Message-Generierung konfigurieren

```json
{
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "text": "Commit-Messages auf Englisch. Format: type(scope): Beschreibung. Typen: feat, fix, docs, refactor, test, chore."
    }
  ]
}
```

Nutzen: Source Control Panel → Zauberstab-Icon neben dem Commit-Eingabefeld.

---

## Sprache der Antworten einstellen

```json
{
  "github.copilot.chat.localeOverride": "de"
}
```

| Wert   | Sprache        |
| ------ | -------------- |
| `de`   | Deutsch        |
| `en`   | Englisch       |
| `auto` | Browser/System |

---

## Globale vs. Projekt-Einstellungen

| Einstellung                   | Global (User) | Projekt (.vscode) |
| ----------------------------- | ------------- | ----------------- |
| `copilot.enable`              | ✅            | ✅                |
| `codeGeneration.instructions` | ✅            | ✅ (überschreibt) |
| `localeOverride`              | ✅            | ✅                |
| `tasks.json`                  | ❌            | ✅                |
| `mcp.json`                    | ❌            | ✅                |

---

## Checkliste: Neues Projekt aufsetzen

```bash
mkdir -p .github/instructions .github/prompts .github/agents .vscode

# Pflicht:
touch .github/copilot-instructions.md

# Empfohlen:
touch .github/instructions/python.instructions.md
touch .github/instructions/security.instructions.md
touch .vscode/settings.json
```

**Minimale `copilot-instructions.md`:**

```markdown
# GitHub Copilot Instructions

## Project

Flask Todo-App. Speicherung in todos.json. Kein ORM, kein JavaScript.

## Commands

FLASK_DEBUG=1 python app.py
python -m pytest test_app.py

## Rules

- Post/Redirect/Get für alle Forms
- Tailwind CDN für Styling
- Keine zusätzlichen Python-Pakete ohne Rückfrage
```
