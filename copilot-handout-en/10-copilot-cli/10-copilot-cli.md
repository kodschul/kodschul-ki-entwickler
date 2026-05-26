# 10 – Copilot CLI – Complete Reference

**Block:** 90 min | **Day 3**

---

## Installation & Setup

```bash
# Prerequisites: GitHub CLI must be installed
brew install gh            # macOS
# winget install GitHub.cli  # Windows

# Authenticate
gh auth login

# Install Copilot extension
gh extension install github/gh-copilot

# Verify installation
gh copilot --version
```

---

## Two Main Commands

| Command                    | Purpose                                  |
| -------------------------- | ---------------------------------------- |
| `gh copilot suggest "..."` | Suggest a shell command for a task       |
| `gh copilot explain "..."` | Explain what a command does              |

---

## gh copilot suggest – All Options

### Basic

```bash
gh copilot suggest "Run Flask tests and show only failures"
```

### `-t` / `--target` – Command Type

```bash
gh copilot suggest -t shell "Show all Python files modified today"
gh copilot suggest -t git "Undo last commit without losing changes"
gh copilot suggest -t github-actions "Run tests only on Python file changes"
```

| Target           | Generates                         |
| ---------------- | --------------------------------- |
| `shell`          | bash/zsh commands                 |
| `git`            | git commands                      |
| `github-actions` | GitHub Actions workflow YAML      |

### `--no-interaction` – For Scripts

```bash
gh copilot suggest --no-interaction "List all .py files"
```

### Interactive Menu Options

After `gh copilot suggest` runs interactively, you get options:
- `Copy command to clipboard` – copies to clipboard
- `Explain command` – explains the suggestion
- `Execute command` – runs it directly
- `Revise query` – refine your question
- `Exit` – cancel

---

## gh copilot explain – Examples

```bash
# Explain a command
gh copilot explain "python -m pytest -v --tb=short"

# Explain a complex pipeline
gh copilot explain "find . -name '*.py' | xargs grep -l 'import flask'"

# Explain a git command
gh copilot explain "git log --oneline --graph --decorate --all"

# Explain a Docker command
gh copilot explain "docker-compose up -d --build --remove-orphans"
```

---

## Setting Up Aliases

### gh aliases (permanent)

```bash
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Use:
gh cs "Run Flask in debug mode"
gh ce "FLASK_DEBUG=1 python app.py"
```

### Shell aliases (in ~/.zshrc or ~/.bashrc)

```bash
alias ghcs='gh copilot suggest'
alias ghce='gh copilot explain'
alias ghcss='gh copilot suggest -t shell'
alias ghcsg='gh copilot suggest -t git'

# Reload:
source ~/.zshrc
```

---

## Workflow Examples

### Code Review in the Terminal

```bash
# Review a file
cat app.py | gh copilot explain "Are there security issues in this code?"

# Review only specific functions
sed -n '/def func_add_todo/,/^def /p' app.py | \
  gh copilot explain "Is this function correct?"
```

### Git Workflow Automation

```bash
# Suggest git commands
gh copilot suggest -t git "Stage only Python files and create a commit"

gh copilot suggest -t git "Merge feature branch and squash commits"

gh copilot suggest -t git "Create hotfix branch from main"
```

### CI/CD Debugging

```bash
# Analyze GitHub Actions error
gh copilot explain "Error: Process completed with exit code 1"

# Suggest fix for failing workflow
gh copilot suggest -t github-actions \
  "Cache Python dependencies in GitHub Actions"
```

---

## Headless Review Script

```bash
#!/bin/bash
# review.sh – Automated code review via CLI

echo "=== Test Run ==="
python -m pytest test_app.py -v 2>&1 | tail -20

echo ""
echo "=== Code Review ==="
gh copilot suggest --no-interaction \
  "Review this Flask app for security issues and code quality" \
  < app.py

echo ""
echo "=== Git Status ==="
gh copilot suggest -t git --no-interaction \
  "Create a commit for my current changes with a Conventional Commit message"
```

---

## Token Saving with CLI

| Task                                | VS Code Chat    | CLI                    |
| ----------------------------------- | --------------- | ---------------------- |
| "How do I run pytest?"              | ~500 tokens     | 0 Copilot tokens       |
| "Explain git rebase"                | ~300 tokens     | 0 Copilot tokens       |
| "Generate GitHub Actions workflow"  | ~800 tokens     | 0 Copilot tokens       |
| Analyze code in file                | ~2,000 tokens   | 0 Copilot tokens       |

---

## Complete Flag Overview

### suggest

| Flag              | Short | Description                        |
| ----------------- | ----- | ---------------------------------- |
| `--target`        | `-t`  | Command type (shell/git/github-actions) |
| `--no-interaction`|       | Headless mode (no interactive menu)|
| `--help`          | `-h`  | Help                               |

### explain

| Flag    | Short | Description  |
| ------- | ----- | ------------ |
| `--help`| `-h`  | Help         |

---

## CLI vs. Editor Chat Comparison

| Aspect              | CLI (`gh copilot`)       | VS Code Chat               |
| ------------------- | ------------------------ | -------------------------- |
| Token consumption   | Separate quota           | Copilot Chat tokens        |
| Context             | Piped input only         | Files, workspace, symbols  |
| Interaction         | Terminal                 | Chat UI                    |
| Scriptable          | ✅ (--no-interaction)    | ❌                         |
| Code editing        | ❌                       | ✅ (Edit/Agent mode)       |
| Best for            | Terminal commands, git   | Code writing, debugging    |
