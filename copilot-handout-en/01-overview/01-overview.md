# Daily Overview – GitHub Copilot

**Training hours:** 09:00 – 17:00

---

## What have we done so far?

| Topic                     | Content                                                                |
| ------------------------- | ---------------------------------------------------------------------- |
| GitHub Copilot Basics     | Installation, first prompts, copilot-instructions.md introduced        |
| Built the Todo App        | Flask app with CRUD, JSON storage, Tailwind UI                         |
| Instructions introduced   | Understanding `.instructions.md` and writing first instructions        |

**Our App:** `1205/todo-app/` – this is the app we continue building today.

---

## Red Thread for Today

We simulate a real developer day:

```
Morning standup
 → Set up configuration professionally
 → Write prompt files (custom slash commands)
 → Build custom agents (specialized AI helpers)
 → Connect VS Code Tasks (automation)
 → Develop a feature spec-driven
 → Connect MCP
 → CLI & CI mode with gh copilot
```

Each block = **one real problem** solved on the Todo App.  
Each exercise = **one artifact** that stays in the app.

---

## Day Plan

| Time              | Block                                  | Format         |
| ----------------- | -------------------------------------- | -------------- |
| 09:00 – 09:15     | Overview (this block)                  | Lecture        |
| 09:15 – 10:30     | Configuration & .md files              | Theory + Demo  |
| **10:30 – 10:45** | **Break**                              |                |
| 10:45 – 12:15     | Custom Prompts + Custom Agents + Tasks | Demo + Exercise|
| **12:15 – 13:15** | **Lunch Break**                        |                |
| 13:15 – 15:00     | Spec-Driven Development                | Demo + Exercise|
| **15:00 – 15:15** | **Break**                              |                |
| 15:15 – 17:00     | MCP + gh copilot CLI + Wrap-up         | Demo + Retro   |

---

## Goal by End of Day

The Todo App will have:

- Professional `.github/copilot-instructions.md` + `.github/instructions/*.instructions.md`
- Custom slash commands (`.github/prompts/todo-review.prompt.md`, `/add-feature`)
- Specialized agents (`.github/agents/security-reviewer.agent.md`)
- Automated tasks (tests run via `.vscode/tasks.json`)
- A new feature implemented and tested via a spec
- `gh copilot suggest` used for CLI automation

---

## GitHub Copilot vs. Claude Code – Quick Comparison

| Claude Code                   | GitHub Copilot Equivalent                |
| ----------------------------- | ---------------------------------------- |
| `CLAUDE.md`                   | `.github/copilot-instructions.md`        |
| `~/.claude/settings.json`     | VS Code User Settings (`settings.json`)  |
| `.claude/settings.local.json` | `.vscode/settings.json`                  |
| `.claude/commands/*.md`       | `.github/prompts/*.prompt.md`            |
| `.claude/agents/*.md`         | `.github/agents/*.agent.md`              |
| `.claude/skills/*/SKILL.md`   | `.github/instructions/*.instructions.md` |
| `hooks` in settings.json      | `.vscode/tasks.json` + GitHub Actions    |
| `mcpServers` in settings.json | `.vscode/mcp.json`                       |
| `claude --print "..."`        | `gh copilot suggest "..."`               |
