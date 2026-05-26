# Exercise: Inline Completions

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Learn the Shortcuts (20 min)

Open `app.py`. Go to the end of the file and write:

```python
# Helper function: Returns all todos that are due today
def func_get_due_today(todos):
```

**Try it out:**

1. Wait for Ghost Text
2. `⌥ ]` / `Alt ]` – next suggestion
3. `⌥ [` / `Alt [` – previous suggestion
4. `⌥ Enter` / `Alt Enter` – all suggestions in panel
5. `⌘ →` / `Ctrl →` – accept word by word

**Questions:**

- How many different suggestions does Copilot offer?
- Which one makes the most sense?

---

## Task 2 – Control Context with Comments (20 min)

Write three variants of the same function and observe how the comment changes the suggestion:

**Variant A – no comment:**

```python
def func_validate_todo(title):
    |
```

**Variant B – short comment:**

```python
# Validates the todo title
def func_validate_todo(title):
    |
```

**Variant C – precise comment:**

```python
# Validates the todo title: not empty, max 200 characters,
# returns (True, "") on success or (False, error_message) on failure
def func_validate_todo(title):
    |
```

**Observe:** How do the suggestions differ?

---

## Task 3 – Docstring-First (20 min)

Write the docstring first, then let Copilot generate the implementation:

```python
def func_format_due_date(due_date_str):
    """
    Formats an ISO date (YYYY-MM-DD) for display.

    - Returns "No date" if due_date_str is empty/None
    - Returns "Overdue" if the date is in the past
    - Otherwise: returns "Due on DD.MM.YYYY"

    Args:
        due_date_str: ISO date string or None
    Returns:
        Formatted string for the UI
    """
    |
```

Accept the suggestion. Then write a test:

```python
def test_format_due_date():
    |  # Copilot should derive tests from the docstring
```

---

## Task 4 – Next Edit Suggestion (15 min)

1. Open `app.py`
2. Rename a route: change `/add` to `/todo/add`
3. Observe: Does Copilot suggest updating all references?
4. Press `Tab` to accept each suggestion

**Alternatively:**

```python
# Change the parameter name in a function
# and observe if Copilot updates the call sites
```

---

## Task 5 – Disable Completions Selectively (15 min)

Add to `.vscode/settings.json`:

```json
{
  "github.copilot.enable": {
    "*": true,
    "markdown": false,
    "plaintext": false
  }
}
```

Open `todos.json` – does Ghost Text still appear?  
Open `app.py` – does Ghost Text appear?
