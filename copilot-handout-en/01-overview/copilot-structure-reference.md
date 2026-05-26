# .github – Complete Structure & Reference

---

## Directory Structure

```
my-project/
├── .github/
│   ├── copilot-instructions.md          ← Project-wide instructions for Copilot
│   ├── instructions/
│   │   ├── python.instructions.md       ← Applies to all *.py files
│   │   ├── flask.instructions.md        ← Flask-specific rules
│   │   └── security.instructions.md    ← Security rules
│   ├── prompts/
│   │   ├── todo-review.prompt.md        ← /todo-review
│   │   ├── add-feature.prompt.md        ← /add-feature
│   │   └── run-tests.prompt.md          ← /run-tests
│   └── agents/
│       ├── security-reviewer.agent.md   ← Security audit agent
│       └── test-writer.agent.md         ← Test generation agent
└── .vscode/
    ├── settings.json                    ← Project-specific VS Code settings
    ├── tasks.json                       ← Automation tasks (hook equivalent)
    └── mcp.json                         ← MCP server configuration

~/.config/github-copilot/               ← Global configuration (all projects)
```

---

## copilot-instructions.md – All Options

```markdown
# GitHub Copilot Instructions

## Project

[Project description]

## Language & Style

- Respond in English
- Use Python 3.12+
- Use Flask for all web endpoints

## Rules

- Always write tests for new code
- Do not use eval() or exec()
- No hardcoded passwords

## Architecture

[Describe data flow, folder structure, etc.]
```

---

## .instructions.md – File-Specific Instructions

**Frontmatter fields:**

```yaml
---
applyTo: "**/*.py" # Glob pattern: which files are affected
description: "..." # Optional description
---
```

**Available `applyTo` patterns:**

| Pattern        | Meaning               |
| -------------- | --------------------- |
| `**`           | All files (global)    |
| `**/*.py`      | All Python files      |
| `src/**`       | Everything in src/    |
| `**/test_*.py` | All test files        |
| `templates/**` | All templates         |

---

## .prompt.md – Custom Slash Commands

**Frontmatter fields:**

```yaml
---
mode: ask # "ask" | "edit" | "agent"
description: "..." # Command description
tools: # Optional: allowed tools
  - codebase
  - terminal
---
```

**Modes:**

| Mode    | Meaning                                          |
| ------- | ------------------------------------------------ |
| `ask`   | Ask questions / analyze code (no writing)        |
| `edit`  | Edit current file directly                       |
| `agent` | Full agent mode with tool access                 |

---

## .agent.md – Custom Agents

**Frontmatter fields:**

```yaml
---
name: agent-name
description: "When is this agent used?"
tools:
  - codebase
  - terminal
  - githubRepo
---
```

---

## .vscode/settings.json – Project-Specific Settings

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/instructions/python.instructions.md"
    }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Use pytest. Always create happy path and edge case tests."
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

## .vscode/mcp.json – MCP Server Configuration

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
        "/path/to/project"
      ]
    }
  }
}
```
