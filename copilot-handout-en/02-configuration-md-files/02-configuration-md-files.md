# Configuration & .md Files

**Block:** 09:15 – 10:30

---

## How does it work under the hood?

At startup, GitHub Copilot automatically reads defined files and builds the **system prompt** from them – invisible, before every response.

```
Chat opened
  → copilot-instructions.md     → project context
  → .github/instructions/       → file-specific rules
  → .vscode/settings.json       → which instructions are loaded
  → First response is already contextually correct
```

> These files are not code – they are **context**. Copilot reads them like a briefing.

---

## Why / When not?

| Why use it                     | When not to                                              |
| ------------------------------ | -------------------------------------------------------- |
| Same context at every start    | One-time prompt → type it directly                       |
| Team context shareable via Git | Sensitive data → never in `.md`, always `.env`           |
| Control behavior deliberately  | Too many instructions (>10) → Copilot gets less accurate |
| Save long prompts as files     | Very specific exception → comment in code                |

---

## Overview: Which file does what?

| File                      | Location                | Purpose                                            |
| ------------------------- | ----------------------- | -------------------------------------------------- |
| `copilot-instructions.md` | `.github/`              | Global context & rules for Copilot in this project |
| `*.instructions.md`       | `.github/instructions/` | Reusable instruction for specific file types       |
| `*.prompt.md`             | `.github/prompts/`      | Slash command (`/name`) with its own workflow      |
| `*.agent.md`              | `.github/agents/`       | Specialized agent with its own tools/rules         |
| `settings.json`           | `.vscode/`              | Project-specific Copilot settings & hooks          |
| `tasks.json`              | `.vscode/`              | Automation tasks (hook equivalent)                 |

---

## copilot-instructions.md – Project Context

Copilot reads `.github/copilot-instructions.md` **automatically** in every chat session.  
This is where everything Copilot needs to know about the project lives.

**Structure:**

```markdown
# GitHub Copilot Instructions

## Project Goal

[One sentence – what does this app do?]

## Commands

[How do I start/test the app?]

## Do

[What should Copilot do?]

## Don't

[What should Copilot NOT do?]
```

**Example – our Todo App:**

```markdown
# GitHub Copilot Instructions

## Project Goal

Minimal Todo web app for learning – Flask + HTML forms.
Users can create, edit, check off, and delete todos.

## Commands

FLASK_DEBUG=1 python app.py # Start dev server
python -m pytest test_app.py # Run tests

## Do

- Use HTML form POSTs with redirect (Post/Redirect/Get)
- Store all data in todos.json
- Use Tailwind CDN for styling

## Don't

- No REST API or JavaScript fetch
- No database or ORM
- No additional Python files
```

**Tip:** The more precise the `copilot-instructions.md`, the less you have to explain to Copilot.

---

## .instructions.md – Reusable Instructions

An instruction file is an **instruction for a specific task or file group** that Copilot should always follow the same way.

**Structure:**

```markdown
---
applyTo: "**/*.py"
description: "When is this instruction used?"
---

# Title

- Rule 1
- Rule 2
- Step A
- Step B
```

**Example – Python rules:**

```markdown
---
applyTo: "**/*.py"
description: "Python code generation rules"
---

# Python Guidelines

- Use Python 3.12+ syntax
- Always write type annotations
- Use pytest for tests
- Handle all exceptions explicitly
```

**Example – Flask-specific:**

```markdown
---
applyTo: "**/app.py"
description: "Flask application guidelines"
---

# Flask Guidelines

- Use Post/Redirect/Get pattern
- Validate all form inputs
- Use flash() for user messages
```

---

## .vscode/settings.json – Configuring Copilot

Control which instructions apply to which context:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/instructions/python.instructions.md"
    }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Use pytest. Create happy path and edge case tests."
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

## gh copilot CLI – Quick Reference

```bash
# Install Copilot CLI (once)
gh extension install github/gh-copilot

# Suggest a command
gh copilot suggest "Run tests for Python app"

# Explain a command
gh copilot explain "python -m pytest -v --tb=short"

# Interactive mode
gh copilot suggest -t shell "Show all Python files in the project"
```
