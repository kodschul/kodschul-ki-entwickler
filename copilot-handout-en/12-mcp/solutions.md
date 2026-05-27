# Module 12 — Solutions

---

## Solution 12.1 – mcp.json (Playwright + GitHub)

`.vscode/mcp.json`:

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
      "args": ["@modelcontextprotocol/server-github@latest"],
      "type": "stdio",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

**Verification prompt:**

```
Open http://localhost:5000, add a todo called "MCP Test", and confirm it appears in the list.
```

---

## Solution 12.2 – gh CLI Setup + Aliases

```bash
# Install (macOS / Linux)
brew install gh
gh auth login
gh extension install github/gh-copilot

# Windows
winget install GitHub.cli
gh auth login
gh extension install github/gh-copilot

# Register aliases
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Verify
gh copilot suggest "Run Flask tests only for /add route"
# → python -m pytest test_app.py -v -k "add"

gh copilot explain "python -m pytest -v -k 'add'"
# → natural-language explanation
```

---

## Solution 12.3 – review.sh

```bash
#!/bin/bash
echo "=== Running Tests ==="
python -m pytest test_app.py -v 2>&1 | tail -20

echo ""
echo "=== Security Check ==="
gh copilot suggest --no-interaction \
  "What security issues do Flask apps with file-based JSON storage typically have?"

echo ""
echo "=== Commit Suggestion ==="
gh copilot suggest -t git --no-interaction \
  "Create a Conventional Commit message for my staged changes"
```

```bash
chmod +x review.sh
./review.sh
```

---

## Solution 12.4 – Permissions in copilot-instructions.md

```markdown
# Project: Flask Todo App

## Permissions

Copilot MAY:

- Read and modify all `.py`, `.html`, `.json`, `.md`, `.sh` files in this project
- Run `python -m pytest test_app.py` to verify changes
- Run `python app.py` to start the development server
- Use the gh CLI to suggest commit messages and explain commands
- Control the browser via Playwright MCP to test http://localhost:5000

Copilot MUST NOT:

- Push to any Git remote without explicit user approval
- Modify `.git/` contents other than hooks
- Access files outside this project directory
- Install packages not in `requirements.txt` without asking first
- Make GitHub API calls that write (create issues, open PRs) without explicit approval
```

---

## Solution 12.5 – Free Experimentation Options

### Option A – MCP Extension

Install the VS Code MCP marketplace extension and explore additional servers (e.g., filesystem, sqlite). Add a second server entry to `mcp.json` and test it in Agent Mode.

### Option B – Custom Spec-Kit

Create a mini Spec-Kit specific to this project:

`.github/prompts/spec-due-date.prompt.md`:

```markdown
---
mode: agent
description: "Plan, build, and test a new feature for the Flask Todo App using Spec-Driven Development"
tools:
  - codebase
  - terminal
---

# Feature Spec Kit

1. Write a SPEC.md for "${input:feature_name}" following the project template.
2. Run /spec-plan on the spec: identify all files to change and the implementation order.
3. Implement step by step, running `python -m pytest test_app.py -v` after each step.
4. Generate tests for every acceptance criterion.
5. Produce a comparison table: Criterion | Implemented? | Notes.
```

### Option C – CLI Scripting

```bash
# Automate a full review cycle
echo "=== Lint ===" && python -m flake8 app.py
echo "=== Tests ===" && python -m pytest test_app.py -q
echo "=== Security ===" && gh cs --no-interaction "Security issues in a Flask JSON file app?"
echo "=== Commit ===" && gh cs -t git --no-interaction "Conventional Commit for current changes"
```

---

## 3-Day Course Summary

| Day | Key Topics                                                           | Output                          |
| --- | -------------------------------------------------------------------- | ------------------------------- |
| 1   | Inline completions, Chat context, Built-in commands, Custom commands | Prompt library, slash commands  |
| 2   | Instructions, Skills, Custom prompts, Custom agents, Automation      | `.github/` config, tasks, hooks |
| 3   | Spec-Driven Development, MCP, gh CLI, Permissions                    | SPEC.md workflow, `review.sh`   |
