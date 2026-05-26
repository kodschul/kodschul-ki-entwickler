# 02 – Chat & Context Variables

**Block:** 90 min | **Day 1**

---

## Opening Chat

| Action                  | macOS         | Windows/Linux  |
| ----------------------- | ------------- | -------------- |
| Open Chat               | `⌃ ⌘ I`       | `Ctrl Alt I`   |
| Inline Chat (in editor) | `⌘ I`         | `Ctrl I`       |
| Quick Chat              | `⌘ Shift I`   | `Ctrl Shift I` |
| Clear Chat              | `+` icon top  | `+` icon top   |

---

## Chat Modes

| Mode      | Symbol | When to use                                               |
| --------- | ------ | --------------------------------------------------------- |
| **Ask**   | 💬     | Questions, explanations, code review without changes      |
| **Edit**  | ✏️     | Edit files directly (shows diff)                          |
| **Agent** | 🤖     | Multi-step tasks, terminal commands, multiple files       |

> **Switch:** Dropdown at the bottom left of the chat input field.

---

## Context Variables (`#`)

Add files, symbols, or the entire workspace as context:

| Variable               | Description                                        |
| ---------------------- | -------------------------------------------------- |
| `#file`                | Select a file and add it as context                |
| `#codebase`            | Search the entire codebase (semantic search)       |
| `#selection`           | Currently selected text                            |
| `#editor`              | Content of the active editor file                  |
| `#terminalSelection`   | Selected text in the terminal                      |
| `#terminalLastCommand` | Last command + output in the terminal              |
| `#sym`                 | Select a symbol (function, class)                  |
| `#changes`             | Git changes (staged + unstaged)                    |
| `#testFailure`         | Failed test + stack trace                          |

**Examples:**

```
Explain #file:app.py to me

What does the function #sym:func_load_todos do?

Why does #testFailure fail?

Create a code review for #changes
```

---

## Agents (`@`)

Agents are specialized chat participants with access to specific data:

| Agent        | Access to                                        |
| ------------ | ------------------------------------------------ |
| `@workspace` | All files in the workspace (semantic search)     |
| `@github`    | GitHub repos, issues, PRs, commits, code search  |
| `@vscode`    | VS Code settings, commands, documentation        |
| `@terminal`  | Terminal context and command suggestions          |

**Examples:**

```
@workspace Where is todos.json read?

@github What open issues are there for this project?

@vscode How do I set the Python interpreter?

@terminal Why does the last command fail?
```

---

## Building Context Efficiently

### Too much context → worse answers

```
❌ "Analyze my entire project and explain everything"
✅ "Explain #file:app.py – focus on the /add route"
```

### Precise references instead of vague descriptions

```
❌ "Look at the todo logic"
✅ "Look at #sym:func_load_todos and #sym:func_save_todos"
```

### Use context for follow-up questions

```
First question:  "Explain #file:app.py"
Follow-up:       "How would I add a delete route?"
                 → Copilot still has app.py in context
```

---

## Inline Chat – directly in code

`⌘ I` / `Ctrl I` opens chat directly at the cursor:

```python
def func_load_todos():
    # ← Cursor here, press ⌘ I
    # Prompt: "Add error handling for when the file doesn't exist"
```

**Inline Chat Shortcuts:**

| Action              | Key        |
| ------------------- | ---------- |
| Accept changes      | `⌘ Enter`  |
| Reject changes      | `Esc`      |
| Next change         | `F7`       |
| Previous change     | `Shift F7` |

---

## Quick Chat – fast questions without opening Chat

`⌘ Shift I` / `Ctrl Shift I` → type → `Enter` → answer appears briefly.

Ideal for:

- Quick explanations
- Looking up a command
- Short question about current file
