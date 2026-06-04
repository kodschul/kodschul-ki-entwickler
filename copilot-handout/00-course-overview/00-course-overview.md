# GitHub Copilot – 3-Tages-Schulung

**Ziel:** GitHub Copilot professionell einsetzen – vom ersten Ghost-Text bis zu eigenen Agents, CI-Pipelines und CLI-Automation.

---

## Themenübersicht (alle 3 Tage)

| #   | Thema                           | Tag   | Dauer  |
| --- | ------------------------------- | ----- | ------ |
| 01  | Inline Completions              | Tag 1 | 90 min |
| 02  | Chat & Kontext-Variablen        | Tag 1 | 90 min |
| 03  | Integrierte Commands            | Tag 1 | 90 min |
| 04  | Konfiguration & Instructions    | Tag 1 | 60 min |
| 05  | Skills & .instructions.md       | Tag 2 | 90 min |
| 06  | Custom Prompts (Slash Commands) | Tag 2 | 90 min |
| 07  | Custom Agents                   | Tag 2 | 90 min |
| 08  | Automation & Tasks              | Tag 2 | 60 min |
| 09  | Token-Management                | Tag 3 | 60 min |
| 10  | Copilot CLI – vollständig       | Tag 3 | 90 min |
| 11  | Spec-Driven Development         | Tag 3 | 90 min |
| 12  | MCP – Model Context Protocol    | Tag 3 | 60 min |

---

## Tag 1 – Fundamentals

```
09:00  01 Inline Completions        Ghost Text, Shortcuts, Multi-Suggestion
10:45  02 Chat & Kontext            #file #codebase @workspace @github @vscode
13:15  03 Integrierte Commands      /fix /explain /tests /doc /new /terminal
15:15  04 Konfiguration             copilot-instructions.md, settings.json
```

**App:** `1205/todo-app/` – Flask, pytest, Tailwind

---

## Tag 2 – Customization

```
09:00  05 Skills & Instructions     .instructions.md, applyTo, stacking
10:45  06 Custom Prompts            .prompt.md, mode, ${input:}, /slash
13:15  07 Custom Agents             .agent.md, tools, Scope
15:15  08 Automation & Tasks        tasks.json, Git Hooks, GitHub Actions
```

---

## Tag 3 – Advanced & Produktion

```
09:00  09 Token-Management          Kontext sparen, effizient prompten
10:00  10 Copilot CLI               gh copilot suggest/explain, alle Flags
13:15  11 Spec-Driven Development   Plan → Build → Test Workflow
15:15  12 MCP                       .vscode/mcp.json, Playwright, eigene Server
```

---

## Vollständige Dateistruktur am Ende

```
.github/
├── copilot-instructions.md          ← Projektkontext (Thema 04)
├── instructions/
│   ├── python.instructions.md       ← applyTo: **/*.py (Thema 05)
│   ├── flask.instructions.md        ← applyTo: **/app.py
│   └── security.instructions.md    ← applyTo: **
├── prompts/
│   ├── todo-review.prompt.md        ← /todo-review (Thema 06)
│   ├── add-feature.prompt.md        ← /add-feature
│   ├── spec-plan.prompt.md          ← /spec-plan (Thema 11)
│   ├── spec-build.prompt.md         ← /spec-build
│   └── spec-test.prompt.md          ← /spec-test
└── agents/
    ├── security-reviewer.agent.md   ← Sicherheits-Audit (Thema 07)
    └── test-writer.agent.md         ← Test-Generierung

.vscode/
├── settings.json                    ← Copilot-Einstellungen (Thema 04)
├── tasks.json                       ← Automatisierung (Thema 08)
└── mcp.json                         ← MCP-Server (Thema 12)

.github/workflows/
└── test.yml                         ← CI/CD (Thema 08)
```

---

## Copilot vs. Claude Code – Mapping-Referenz

| Claude Code                   | GitHub Copilot                           |
| ----------------------------- | ---------------------------------------- |
| `CLAUDE.md`                   | `.github/copilot-instructions.md`        |
| `~/.claude/settings.json`     | VS Code User `settings.json`             |
| `.claude/settings.local.json` | `.vscode/settings.json`                  |
| `.claude/skills/*/SKILL.md`   | `.github/instructions/*.instructions.md` |
| `.claude/commands/*.md`       | `.github/prompts/*.prompt.md`            |
| `.claude/agents/*.md`         | `.github/agents/*.agent.md`              |
| `hooks` in settings.json      | `.vscode/tasks.json` + GitHub Actions    |
| `mcpServers` in settings.json | `.vscode/mcp.json`                       |
| `claude --print "..."`        | `gh copilot suggest "..."`               |
