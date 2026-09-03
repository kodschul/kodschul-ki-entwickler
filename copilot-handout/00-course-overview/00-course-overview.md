# GitHub Copilot – 4-Tages-Schulung

**Ziel:** GitHub Copilot professionell einsetzen – von den Grundlagen generativer KI über den ersten Ghost-Text bis zu eigenen Agents, CI-Pipelines und CLI-Automation.

> **Hinweis:** Der Kurs war ursprünglich auf 3 Tage ausgelegt. Durch die Ergänzung des Grundlagen-Moduls (01), des Neuerungen-Moduls (14) und des Best-Practices-Moduls (15) sind es jetzt 4 Tage. Zeiten sind Richtwerte.

---

## Inhalte

**Grundlagen (Modul 01 – 6 Unterthemen in einem Ordner)**

- Arten von KI-Integrationen (Autocomplete, Chat, Agent lokal/cloud)
- Generative KI und LLMs in a Nutshell
- Generative KI im Coding (planen, schreiben, analysieren, refactoren, testen)
- Generative KI in Softwareprojekten (Requirements, Konzeption, Styles)
- Generative KI kreativ eingesetzt (Skills, Modelle, Ausblick)
- Recht, Sicherheit & Datenschutz bei KI-generiertem Code

**Copilot-Praxis (Modul 02–13)**

- Inline Completions, Chat & Kontext, integrierte Commands, Konfiguration
- Skills & Instructions, Custom Prompts, Custom Agents, Automation
- Token-Management, Copilot CLI, Spec-Driven Development, MCP

**Abschluss (Modul 14–16)**

- Neuerungen: Custom Chat Modes, Subagents, Coding Agent, Copilot Code Review
- Best Practices (Modul 15 – 7 Unterthemen in einem Ordner): Multi-Agent-Orchestrierung, Kostenoptimierung, Team-Zusammenarbeit, parallele Sessions & Delegation, große Codebases, EU-KI-Verordnung, Wissen persistieren
- Outro: Zusammenfassung & nächste Schritte

---

## Themenübersicht (alle 4 Tage)

| #   | Thema                                   | Tag   | Dauer   |
| --- | --------------------------------------- | ----- | ------- |
| 01  | Grundlagen (6 Unterthemen, siehe unten) | Tag 1 | 255 min |
| 02  | Inline Completions                      | Tag 2 | 90 min  |
| 03  | Chat & Kontext-Variablen                | Tag 2 | 90 min  |
| 04  | Integrierte Commands                    | Tag 2 | 90 min  |
| 05  | Konfiguration & Instructions            | Tag 2 | 60 min  |
| 06  | Skills & .instructions.md               | Tag 3 | 90 min  |
| 07  | Custom Prompts (Slash Commands)         | Tag 3 | 90 min  |
| 08  | Custom Agents                           | Tag 3 | 90 min  |
| 09  | Automation & Tasks                      | Tag 3 | 60 min  |
| 10  | Token-Management                        | Tag 4 | 60 min  |
| 11  | Copilot CLI – vollständig               | Tag 4 | 90 min  |
| 12  | Spec-Driven Development                 | Tag 4 | 90 min  |
| 13  | MCP – Model Context Protocol            | Tag 4 | 60 min  |
| 14  | Neuerungen                              | Tag 4 | 60 min  |
| 15  | Outro                                   | Tag 4 | 30 min  |

---

## Tag 1 – Grundlagen (Modul 01)

```
09:00  01a Intro: Integrationsarten  Autocomplete vs. Chat vs. Agent (lokal/cloud)
09:30  01b LLMs in a Nutshell        Tokens, Context Window, RAG, Kontext einbringen
10:30  01c KI im Coding              Planen, Schreiben, Analyse, Refactoring, Testing
13:00  01d KI in Softwareprojekten   Requirements, Konzeption, Styles & Patterns
14:00  01e KI kreativ eingesetzt     Skills, Modelle, Ausblick
15:00  01f Recht & Security          Urheberrecht, Haftung, Privacy-by-design
```

**Dateien:** `01-grundlagen/01-intro-ki-integrationsarten.md` … `01-grundlagen/06-recht-sicherheit-privacy.md`

---

## Tag 2 – Fundamentals

```
09:00  02 Inline Completions        Ghost Text, Shortcuts, Multi-Suggestion
10:45  03 Chat & Kontext            #file #codebase @workspace @github @vscode
13:15  04 Integrierte Commands      /fix /explain /tests /doc /new /terminal
15:15  05 Konfiguration             copilot-instructions.md, settings.json
```

**App:** `1205/todo-app/` – Flask, pytest, Tailwind

---

## Tag 3 – Customization

```
09:00  06 Skills & Instructions     .instructions.md, SKILL.md, applyTo, stacking
10:45  07 Custom Prompts            .prompt.md, mode, ${input:}, /slash
13:15  08 Custom Agents             .agent.md, tools, Scope
15:15  09 Automation & Tasks        tasks.json, Git Hooks, GitHub Actions
```

---

## Tag 4 – Advanced, Produktion & Neuerungen

```
09:00  10 Token-Management          Kontext sparen, effizient prompten
10:00  11 Copilot CLI               gh copilot suggest/explain, alle Flags
13:15  12 Spec-Driven Development   Plan → Build → Test Workflow
15:15  13 MCP                       .vscode/mcp.json, Playwright, eigene Server
16:15  14 Neuerungen                14a Chat Modes, 14b Coding Agent, 14c Code Review, 14d Subagents
16:45  15 Best Practices           Multi-Agent, Kosten, Team, Delegation, große Codebases, EU-KI-Verordnung, Wissen persistieren
17:45  16 Outro                     Zusammenfassung, nächste Schritte
```

**Dateien Modul 14:** `14-neuerungen/01-custom-chat-modes.md` … `14-neuerungen/04-subagents.md` – je eine Datei pro Neuerung, inkl. "Seit wann"-Angabe zum Prüfen gegen den aktuellen Changelog.

**Dateien Modul 15:** `15-best-practices/01-multi-agent-orchestrierung.md` … `15-best-practices/07-wissen-persistieren.md`

---

## Vollständige Dateistruktur am Ende

```
.github/
├── copilot-instructions.md          ← Projektkontext (Thema 05)
├── instructions/
│   ├── python.instructions.md       ← applyTo: **/*.py (Thema 06)
│   ├── flask.instructions.md        ← applyTo: **/app.py
│   └── security.instructions.md    ← applyTo: **
├── skills/
│   └── pdf-report-generator/
│       └── SKILL.md                 ← Agent Skill (Thema 06)
├── chatmodes/
│   └── reviewer.chatmode.md         ← Custom Chat Mode (Thema 14)
├── prompts/
│   ├── todo-review.prompt.md        ← /todo-review (Thema 07)
│   ├── add-feature.prompt.md        ← /add-feature
│   ├── spec-plan.prompt.md          ← /spec-plan (Thema 12)
│   ├── spec-build.prompt.md         ← /spec-build
│   └── spec-test.prompt.md          ← /spec-test
└── agents/
    ├── security-reviewer.agent.md   ← Sicherheits-Audit (Thema 08)
    └── test-writer.agent.md         ← Test-Generierung

.vscode/
├── settings.json                    ← Copilot-Einstellungen (Thema 05)
├── tasks.json                       ← Automatisierung (Thema 09)
└── mcp.json                         ← MCP-Server (Thema 13)

.github/workflows/
└── test.yml                         ← CI/CD (Thema 09)
```

---

## Copilot vs. Claude Code – Mapping-Referenz

| Claude Code                   | GitHub Copilot                                                   |
| ----------------------------- | ---------------------------------------------------------------- |
| `CLAUDE.md`                   | `.github/copilot-instructions.md`                                |
| `~/.claude/settings.json`     | VS Code User `settings.json`                                     |
| `.claude/settings.local.json` | `.vscode/settings.json`                                          |
| `.claude/skills/*/SKILL.md`   | `.github/skills/*/SKILL.md` (eigenes Konzept, nicht nur Mapping) |
| `.claude/commands/*.md`       | `.github/prompts/*.prompt.md`                                    |
| `.claude/agents/*.md`         | `.github/agents/*.agent.md`                                      |
| (kein direktes Äquivalent)    | `.github/chatmodes/*.chatmode.md`                                |
| `hooks` in settings.json      | `.vscode/tasks.json` + GitHub Actions                            |
| `mcpServers` in settings.json | `.vscode/mcp.json`                                               |
| `claude --print "..."`        | `gh copilot suggest "..."`                                       |
