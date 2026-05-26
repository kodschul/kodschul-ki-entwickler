# Day 1 – Overview

**Goal of the Day:** Get productive with GitHub Copilot – inline completions, chat, built-in commands, and configuration.

---

## Day Schedule

| Time        | Topic                         | Duration  |
| ----------- | ----------------------------- | --------- |
| 09:00–09:30 | Setup Check & Course Overview | 30 min    |
| 09:30–10:30 | Inline Completions            | 60 min    |
| 10:30–10:45 | Break                         | 15 min    |
| 10:45–12:00 | Chat & Context                | 75 min    |
| 12:00–13:00 | Lunch Break                   | 60 min    |
| 13:00–14:15 | Built-in Commands             | 75 min    |
| 14:15–14:30 | Break                         | 15 min    |
| 14:30–16:00 | Configuration (md files)      | 90 min    |
| 16:00–16:30 | Day 1 Recap & Questions       | 30 min    |

---

## 3-Day Overview

| Day   | Focus             | Topics                                                        |
| ----- | ----------------- | ------------------------------------------------------------- |
| Day 1 | Foundations       | Inline Completions, Chat, Built-in Commands, Configuration    |
| Day 2 | Automation        | Custom Commands, Agents, Instructions, Tasks & Hooks          |
| Day 3 | Scale & Workflow  | Token Management, CLI, Spec-Driven Development, MCP           |

---

## Setup Check

Run these commands before the course starts:

```bash
# Check GitHub CLI
gh --version
# Expected: gh version 2.x.x

# Check Copilot extension
gh copilot --version
# Expected: copilot extension installed

# Check Python
python --version
# Expected: Python 3.10+

# Check Git
git --version
# Expected: git version 2.x.x
```

**In VS Code:**
- `GitHub Copilot` extension installed → check bottom status bar
- Extension is active (not greyed out)

---

## What We Build Today

We start with the `1205/todo-app/` Flask project:

```
todo-app/
├── app.py             ← Flask routes
├── todos.json         ← Data storage
├── test_app.py        ← Tests
└── templates/
    └── index.html     ← UI
```

**During the day we extend the app with:**

- [ ] Understanding the codebase with Copilot Chat
- [ ] Fixing existing bugs with /fix
- [ ] Generating tests with /tests
- [ ] Adding documentation with /doc
- [ ] Setting up `copilot-instructions.md` for consistent behavior

---

## Key Concepts: Day 1

### Ghost Text (Inline Completion)

Copilot shows suggestions in grey text as you type.  
`Tab` → Accept | `Esc` → Reject | `Alt+]` → Next suggestion

### NES – Next Edit Suggestion

Copilot suggests the next logical change (not just completion at cursor).  
Arrow key `→` or `Tab` to accept.

### Chat Modes

| Mode         | Shortcut        | Purpose                                   |
| ------------ | --------------- | ----------------------------------------- |
| Ask          | Default         | Questions, explanations, code review      |
| Edit         | Ctrl+Shift+I    | Targeted edits of selected files          |
| Agent        | `@workspace`    | Multi-step tasks, terminal access, plans  |
| Inline Chat  | Ctrl+I          | Quick edit at cursor position             |

### copilot-instructions.md

Permanent system-level instructions for Copilot.  
Located at `.github/copilot-instructions.md`.  
Active in all chats without having to attach it manually.

---

## Reference: Most Used Shortcuts

| Action                  | macOS           | Windows/Linux   |
| ----------------------- | --------------- | --------------- |
| Accept suggestion       | Tab             | Tab             |
| Reject suggestion       | Esc             | Esc             |
| Next suggestion         | Alt + ]         | Alt + ]         |
| Previous suggestion     | Alt + [         | Alt + [         |
| Open Chat               | Ctrl + Shift + I| Ctrl + Shift + I|
| Inline Chat             | Ctrl + I        | Ctrl + I        |
| Accept NES              | Tab / →         | Tab / →         |
