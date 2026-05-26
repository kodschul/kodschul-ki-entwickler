# GitHub Copilot – 3-Day Training

**Goal:** Use GitHub Copilot professionally – from your first Ghost Text to custom Agents, CI pipelines, and CLI automation.

---

## Topic Overview (all 3 days)

| #   | Topic                            | Day   | Duration |
| --- | -------------------------------- | ----- | -------- |
| 01  | Prompt Engineering               | Day 1 | 90 min   |
| 02  | AI Agents & Multi-Step Prompting | Day 1 | 90 min   |
| 03  | Inline Completions               | Day 1 | 90 min   |
| 04  | Chat & Context Variables         | Day 1 | 90 min   |
| 05  | Built-in Commands                | Day 1 | 90 min   |
| 06  | Configuration & Instructions     | Day 1 | 60 min   |
| 07  | Skills & .instructions.md        | Day 2 | 90 min   |
| 08  | Custom Prompts (Slash Commands)  | Day 2 | 90 min   |
| 09  | Custom Agents                    | Day 2 | 90 min   |
| 10  | Automation & Tasks               | Day 2 | 60 min   |
| 11  | Token Management                 | Day 3 | 60 min   |
| 12  | Copilot CLI – complete           | Day 3 | 90 min   |
| 13  | Spec-Driven Development          | Day 3 | 90 min   |
| 14  | MCP – Model Context Protocol     | Day 3 | 60 min   |

---

## Day 1 – Fundamentals

```
09:00  01 Inline Completions        Ghost Text, Shortcuts, Multi-Suggestion
10:45  02 Chat & Context            #file #codebase @workspace @github @vscode
13:15  03 Built-in Commands         /fix /explain /tests /doc /new /terminal
15:15  04 Configuration             copilot-instructions.md, settings.json
```

**App:** `1205/todo-app/` – Flask, pytest, Tailwind

---

## Day 2 – Customization

```
09:00  05 Skills & Instructions     .instructions.md, applyTo, stacking
10:45  06 Custom Prompts            .prompt.md, mode, ${input:}, /slash
13:15  07 Custom Agents             .agent.md, tools, Scope
15:15  08 Automation & Tasks        tasks.json, Git Hooks, GitHub Actions
```

---

## Day 3 – Advanced & Production

```
09:00  09 Token Management          Save context, prompt efficiently
10:00  10 Copilot CLI               gh copilot suggest/explain, all flags
13:15  11 Spec-Driven Development   Plan → Build → Test Workflow
15:15  12 MCP                       .vscode/mcp.json, Playwright, custom servers
```

---

## Complete File Structure at the End

```
.github/
├── copilot-instructions.md          ← Project context (Topic 04)
├── instructions/
│   ├── python.instructions.md       ← applyTo: **/*.py (Topic 05)
│   ├── flask.instructions.md        ← Flask-specific rules
│   └── security.instructions.md    ← applyTo: **
├── prompts/
│   ├── todo-review.prompt.md        ← /todo-review (Topic 06)
│   ├── add-feature.prompt.md        ← /add-feature
│   ├── spec-plan.prompt.md          ← /spec-plan (Topic 11)
│   ├── spec-build.prompt.md         ← /spec-build
│   └── spec-test.prompt.md          ← /spec-test
└── agents/
    ├── security-reviewer.agent.md   ← Security Audit (Topic 07)
    └── test-writer.agent.md         ← Test Generation

.vscode/
├── settings.json                    ← Copilot settings (Topic 04)
├── tasks.json                       ← Automation (Topic 08)
└── mcp.json                         ← MCP Server (Topic 12)

.github/workflows/
└── test.yml                         ← CI/CD (Topic 08)
```

---

## Copilot vs. Claude Code – Mapping Reference

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
