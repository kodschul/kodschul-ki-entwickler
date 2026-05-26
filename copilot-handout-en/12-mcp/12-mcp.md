# 12 – MCP & Customization – Closing

**Block:** Day 3 | **Topic:** MCP, gh CLI, Permissions, Wrap-Up

---

## What is MCP?

**Model Context Protocol (MCP)** – A standard for connecting external tools to AI models.

```
VS Code / Agent Mode
       ↓
   MCP Client
       ↓
  MCP Server (local or remote)
       ↓
  Tool (Browser, DB, GitHub, ...)
```

MCP allows Copilot to access real tools – not just static context.

---

## mcp.json – Configuration

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "type": "stdio"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "type": "stdio",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

**Location options:**

- `.vscode/mcp.json` – project-specific
- VS Code Settings → MCP – user-wide

---

## gh CLI – Installation & Setup

```bash
# Install GitHub CLI
brew install gh           # macOS
# winget install GitHub.cli  # Windows

# Authenticate
gh auth login

# Install Copilot extension
gh extension install github/gh-copilot

# Verify
gh copilot --version
```

---

## gh CLI – Overview of Most Important Commands

### gh copilot

```bash
# Suggest shell commands
gh copilot suggest "Run Flask tests"

# Suggest git commands
gh copilot suggest -t git "Stage only Python files"

# Suggest GitHub Actions
gh copilot suggest -t github-actions "Run tests on pull request"

# Explain a command
gh copilot explain "git rebase -i HEAD~3"

# Without interaction (for scripts)
gh copilot suggest --no-interaction "Run tests"
```

### gh alias (Shortcuts)

```bash
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Use:
gh cs "Show all open ports"
gh ce "lsof -i -P -n | grep LISTEN"
```

### gh api (Direct API access)

```bash
# Create issue
gh api repos/:owner/:repo/issues \
  -f title="Bug: Login fails" \
  -f body="Steps to reproduce..."

# List open PRs
gh api repos/:owner/:repo/pulls \
  -q '.[].title'
```

---

## Controlling Copilot Permissions via Instructions

**`.github/copilot-instructions.md`:**

```markdown
# Security Constraints

## Allowed Tools

The agent may use:

- read_file, write_file, list_dir
- run_in_terminal: only for test and lint commands
- Playwright MCP: only for localhost URLs

## Prohibited Actions

The agent must NOT:

- Execute git push without explicit user approval
- Install new packages (pip, npm) without approval
- Make HTTP calls to external APIs
- Access files outside the project directory

## Required Approval

Always ask before:

- Deleting files
- Changing configuration files (pyproject.toml, package.json)
- Modifying GitHub Actions workflows
```

---

## Final File Structure Overview

```
.github/
├── copilot-instructions.md      ← Global instructions
├── prompts/
│   ├── spec-plan.prompt.md      ← /spec-plan
│   ├── spec-build.prompt.md     ← /spec-build
│   ├── spec-test.prompt.md      ← /spec-test
│   ├── todo-review.prompt.md    ← /todo-review
│   └── add-feature.prompt.md    ← /add-feature
└── instructions/
    ├── python.instructions.md   ← Python conventions
    ├── security.instructions.md ← Security rules
    └── testing.instructions.md  ← Test standards

.vscode/
├── mcp.json                     ← MCP server configuration
├── settings.json                ← Copilot settings
└── tasks.json                   ← Automation tasks
```

---

## 3-Day Course Wrap-Up

### Day 1 – Foundations

| Topic               | Key Takeaway                                |
| ------------------- | ------------------------------------------- |
| Inline Completions  | Ghost Text, NES, keyboard shortcuts         |
| Chat & Context      | Context variables, modes, agents            |
| Built-in Commands   | /explain, /fix, /tests, /doc                |
| Configuration (.md) | copilot-instructions.md = permanent context |

### Day 2 – Automation

| Topic                 | Key Takeaway                                  |
| --------------------- | --------------------------------------------- |
| Custom Commands       | .prompt.md – repeatable workflows             |
| Custom Agents         | .agent.md – specialized assistants with tools |
| Skills & Instructions | .instructions.md – automatic context per file |
| VS Code Tasks & Hooks | tasks.json – automation without AI tokens     |

### Day 3 – Scale

| Topic                   | Key Takeaway                                      |
| ----------------------- | ------------------------------------------------- |
| Token Management        | Slim context, short instructions, CLI             |
| Copilot CLI             | gh copilot suggest/explain – 0 Copilot tokens     |
| Spec-Driven Development | SPEC.md → consistent, reproducible implementation |
| MCP                     | External tools in Agent Mode                      |
