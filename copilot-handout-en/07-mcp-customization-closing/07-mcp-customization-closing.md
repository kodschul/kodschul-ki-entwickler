# 07 – MCP, Customization & Closing

**Block:** 60 min | **Day 3**

---

## Part 1 – MCP: Model Context Protocol

### What is MCP?

MCP (Model Context Protocol) is an open standard that allows Copilot to connect to external tools and services via a unified interface.

```
Copilot Chat
  → .vscode/mcp.json (Server configuration)
  → MCP Server (e.g. Playwright, Filesystem, GitHub)
  → External tool (Browser, Database, API)
  → Returns result to Copilot
```

### Why / When not?

| Why MCP                                  | When not to                              |
| ---------------------------------------- | ---------------------------------------- |
| Copilot should control a browser         | Simple file operations (use #file)       |
| Access to external APIs without coding   | Quick questions (use @workspace)         |
| Integration with existing tools          | API unavailable or no server             |
| End-to-end testing via Copilot           | Security-critical data (careful!)        |

### .vscode/mcp.json

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
        "/path/to/allowed/folder"
      ]
    }
  }
}
```

### Playwright MCP – Example

After setup in mcp.json:

```
Open http://localhost:5000 in the browser.
Add a todo "Test MCP" and confirm it appears in the list.
Take a screenshot.
```

Copilot controls the browser automatically, clicks, fills in forms, takes screenshots.

---

## Part 2 – gh copilot CLI

### Installation & Setup

```bash
# Requires GitHub CLI (gh)
brew install gh              # macOS
gh auth login                # Authenticate
gh extension install github/gh-copilot
```

### Two Main Commands

```bash
gh copilot suggest "..."     # Suggest a shell command
gh copilot explain "..."     # Explain a command
```

### suggest – All Options

```bash
# Basic
gh copilot suggest "Run Flask tests"

# Target type (shell / git / github-actions)
gh copilot suggest -t git "Stage and commit all changes"
gh copilot suggest -t github-actions "Run tests on push to main"

# Non-interactive (for scripts)
gh copilot suggest --no-interaction "List all Python files"
```

### explain – Examples

```bash
gh copilot explain "python -m pytest -v --tb=short"
gh copilot explain "git rebase -i HEAD~3"
gh copilot explain "docker-compose up -d --build"
```

### Setting Up Aliases

```bash
# gh aliases
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Shell aliases (in ~/.zshrc)
alias ghcs='gh copilot suggest'
alias ghce='gh copilot explain'
```

---

## Part 3 – Customization & Output Control

### Structured Output via Instructions

```markdown
# .github/instructions/output.instructions.md
---
applyTo: "**"
---

# Output Rules

- Always output code changes as full functions, not snippets
- Always create a summary table at the end
- Use German error messages in the UI, English in the code
- All code examples with syntax highlighting
```

### Permissions via Instructions

```markdown
# .github/instructions/permissions.instructions.md
---
applyTo: "**"
---

# Restrictions

- NEVER change files in the /config folder
- NEVER change requirements.txt without asking
- NEVER use external APIs (no requests.get to external URLs)
- NEVER store passwords in code
```

---

## Part 4 – Closing: What Our Todo App Now Has

```
1205/todo-app/
├── app.py                           ← Flask app with all features
├── test_app.py                      ← Comprehensive tests
├── SPEC.md                          ← Feature spec (due dates)
├── todos.json                       ← Data storage
│
├── .github/
│   ├── copilot-instructions.md      ← Project context
│   ├── instructions/
│   │   ├── python.instructions.md   ← Python rules
│   │   ├── security.instructions.md ← Security rules
│   │   └── testing.instructions.md  ← Test rules
│   ├── prompts/
│   │   ├── todo-review.prompt.md    ← /todo-review
│   │   ├── add-feature.prompt.md    ← /add-feature
│   │   ├── spec-plan.prompt.md      ← /spec-plan
│   │   ├── spec-build.prompt.md     ← /spec-build
│   │   └── spec-test.prompt.md      ← /spec-test
│   ├── agents/
│   │   ├── security-reviewer.agent.md
│   │   └── test-writer.agent.md
│   └── workflows/
│       └── test.yml                 ← GitHub Actions CI
│
└── .vscode/
    ├── settings.json                ← Copilot config
    ├── tasks.json                   ← Automation tasks
    └── mcp.json                     ← MCP servers
```
