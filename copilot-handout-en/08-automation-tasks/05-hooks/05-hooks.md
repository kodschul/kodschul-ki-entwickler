# 05 – Automation & Tasks (VS Code Tasks)

**Block:** 60 min | **Day 2**

---

## How do VS Code Tasks work?

Tasks are defined in `.vscode/tasks.json` and triggered by:

- Keyboard shortcut (`⌘ Shift B` for default build task)
- `Terminal → Run Task`
- Saved file (via `runOn: "folderOpen"` or file watcher)
- Other tasks (as `dependsOn`)

```
.vscode/tasks.json
  → VS Code reads the file on startup
  → "Run Task" command shows all defined tasks
  → Tasks run in the integrated terminal
  → Dependencies (dependsOn) are resolved automatically
```

---

## Why / When not?

| Why use Tasks                   | When not to                                |
| ------------------------------- | ------------------------------------------ |
| Runs same command repeatedly    | One-time script → run in terminal directly |
| Run tests automatically on save | Complex CI/CD → use GitHub Actions         |
| Chain multiple commands         | Team-wide automation → GitHub Actions      |
| Local development automation    | Doesn't need VS Code → Makefile or script  |

---

## tasks.json Structure

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests", // Name shown in "Run Task"
      "type": "shell", // shell | process | npm
      "command": "python", // Command to execute
      "args": ["-m", "pytest", "-v"], // Arguments
      "group": {
        "kind": "test", // build | test | none
        "isDefault": true // Default task for the group
      },
      "presentation": {
        "reveal": "always", // always | never | silent
        "panel": "shared" // shared | dedicated | new
      },
      "problemMatcher": "$pytest" // Error pattern for Problems pane
    }
  ]
}
```

---

## Task Types and Groups

| `type`    | Used for                        |
| --------- | ------------------------------- |
| `shell`   | Shell commands (bash, zsh, cmd) |
| `process` | Direct program execution        |
| `npm`     | npm scripts from package.json   |

| `group.kind` | Keyboard shortcut           |
| ------------ | --------------------------- |
| `build`      | `⌘ Shift B`                 |
| `test`       | `⌘ Shift P` → Run Test Task |

---

## Claude Hooks vs. VS Code Tasks

| Claude Hooks                      | VS Code Tasks                   |
| --------------------------------- | ------------------------------- |
| Runs before/after agent action    | Runs on demand or on file save  |
| Configured in settings.json       | Configured in tasks.json        |
| Automatic (no user action)        | Manually triggered              |
| AI-driven                         | Deterministic                   |
| E.g.: Validate before every write | E.g.: Run tests at start of dev |

---

## Example 1 – Auto-Test Task

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests (pytest)",
      "type": "shell",
      "command": "python",
      "args": ["-m", "pytest", "test_app.py", "-v"],
      "group": {
        "kind": "test",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    }
  ]
}
```

→ `⌘ Shift P` → **Run Test Task** → tests run immediately.

---

## Example 2 – Backup via Git Hook

```json
{
  "label": "Git: Stage and Commit",
  "type": "shell",
  "command": "git",
  "args": [
    "add",
    "-A",
    "&&",
    "git",
    "commit",
    "-m",
    "Auto-backup: ${env:USER} $(date)"
  ],
  "group": "none",
  "presentation": {
    "reveal": "silent"
  }
}
```

**Git Hook equivalent (`.git/hooks/pre-commit`):**

```bash
#!/bin/bash
python -m pytest test_app.py -q
if [ $? -ne 0 ]; then
  echo "Tests failed – commit aborted!"
  exit 1
fi
```

---

## Example 3 – Multiple Tasks

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start Flask",
      "type": "shell",
      "command": "FLASK_DEBUG=1 python app.py",
      "group": "build",
      "isBackground": true
    },
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "python -m pytest -v",
      "group": { "kind": "test", "isDefault": true }
    },
    {
      "label": "Start + Test",
      "dependsOn": ["Start Flask", "Run Tests"],
      "group": "build"
    }
  ]
}
```

---

## GitHub Actions – CI/CD Equivalent

````yaml
# .github/workflows/test.yml
name: Run Tests

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest test_app.py -v

---

## gh copilot CLI – Automation

```bash
# Automate common tasks in the terminal
gh copilot suggest "Run Flask tests and show me which ones fail"

gh copilot suggest "Stage all Python files and commit with Conventional Commits"

gh copilot suggest "Show me the last 5 git commits as a summary"
````
