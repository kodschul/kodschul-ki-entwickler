# 01 – Inline Completions

**Block:** 90 min | **Day 1**

---

## What are Inline Completions?

Inline Completions (Ghost Text) are the grey suggestions Copilot displays directly in the editor – before you press `Enter`. Copilot analyzes:

- The code **before** the cursor (primary)
- The code **after** the cursor (secondary)
- Open files in the editor (context window)
- The file name and language

```python
# Copilot sees everything from here upward as context
def func_calculate_total(items):
    # Ghost Text appears here ↓
    |
```

---

## Keyboard Shortcuts

| Action                  | macOS                | Windows/Linux           |
| ----------------------- | -------------------- | ----------------------- |
| Accept suggestion       | `Tab`                | `Tab`                   |
| Dismiss suggestion      | `Esc`                | `Esc`                   |
| Accept **word by word** | `⌘ →`                | `Ctrl →`                |
| Next suggestion         | `⌥ ]`                | `Alt ]`                 |
| Previous suggestion     | `⌥ [`                | `Alt [`                 |
| Show all suggestions    | `⌥ Enter`            | `Alt Enter`             |
| Toggle completions      | `⌘ Shift P` → Toggle | `Ctrl Shift P` → Toggle |

> **Tip:** `⌥ Enter` opens the Completions panel with up to 10 alternatives side by side.

---

## Controlling Context Deliberately

### What Copilot sees

```
✅ The code ABOVE the cursor (most important context)
✅ The code BELOW the cursor
✅ All currently open tabs (up to token limit)
✅ File name + extension
✅ .github/copilot-instructions.md
✅ Matching .instructions.md (via applyTo)
❌ Closed files
❌ Files in .gitignore (usually)
```

### Improving context – techniques

**1. Comment as instruction:**

```python
# Validates a todo title: not empty, max 200 characters, no HTML
def func_validate_title(title):
    |
```

**2. Show example patterns (Few-Shot):**

```python
# Example pattern: validate_email returns (bool, str)
def func_validate_email(email):
    if not email:
        return False, "Email must not be empty"
    ...

# Now Copilot follows the same pattern:
def func_validate_title(title):
    |
```

**3. Import as hint:**

```python
from datetime import datetime, timezone
# Copilot now knows which datetime functions are available
```

**4. Write docstring first:**

```python
def func_get_overdue_todos(todos):
    """
    Returns all todos whose due_date is before today.

    Args:
        todos: List of todo dicts with optional 'due_date' (ISO format)
    Returns:
        List of overdue todos
    """
    |  # Copilot generates the implementation from the docstring
```

---

## Why is there no suggestion?

| Problem                      | Solution                                         |
| ---------------------------- | ------------------------------------------------ |
| Cursor in empty file         | Add filename/comment                             |
| Too little context           | Rename function/class, add comment               |
| Copilot disabled             | Check status bar icon (bottom right)             |
| Wrong cursor area            | Start a new line instead of typing in the middle |
| Completion disabled for type | Check `settings.json`: `copilot.enable`          |

---

## Disabling Copilot selectively

```json
// .vscode/settings.json
{
  "github.copilot.enable": {
    "*": true,
    "markdown": false, // No Ghost Text in .md files
    "plaintext": false, // No Ghost Text in .txt
    "yaml": true
  }
}
```

---

## Next Edit Suggestions (NES)

Copilot detects when you make a change and automatically suggests the **next logical change**:

```python
# You change:
def func_add_todo(title):           # was: add_item(name)
#                  ↑ Copilot suggests also updating the parameter
#                    and all call sites
```

→ `Tab` to accept, `Esc` to reject – Copilot jumps to the next change.
