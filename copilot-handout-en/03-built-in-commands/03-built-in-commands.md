# 03 – Built-in Commands

**Block:** 90 min | **Day 1**

---

## /explain – Understand Code

Use `/explain` to understand code you didn't write – or your own code after a while.

**How it works:**

```
Select code → /explain
or
/explain #sym:func_load_todos
or
/explain #file:app.py
```

**Example prompts:**

```
/explain #sym:func_load_todos
What does this function do? What are edge cases?

/explain #file:app.py
Explain the data flow from form submission to storage.
```

---

## /fix – Fix Bugs

Copilot analyzes code and suggests fixes. Works best when combined with error messages.

**Best practice – with error context:**

```
/fix #terminalLastCommand
```

or select the error directly:

```
/fix #selection
Error: "KeyError: 'title'" – what's wrong?
```

**Example:**

```python
# Bug: missing .get() with default value
todo = {
    "title": request.form["title"],   # ← KeyError if field missing
    "done": False
}
```

```
/fix → suggestion: request.form.get("title", "")
```

---

## /tests – Generate Tests

Copilot generates test cases automatically.

**Important:** First configure which test framework to use.

**Configure in `.vscode/settings.json`:**

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Use pytest. Always create: 1 happy path test, 1 empty input test, 1 edge case test. Use descriptive test names (test_what_when_then)."
    }
  ]
}
```

**Use:**

```
/tests #sym:func_validate_title
```

or select a function:

```
/tests → generates tests for the selected function
```

**Tip:** Write tests **before** implementing a function – Copilot can generate tests even from the docstring.

---

## /doc – Add Documentation

Generates docstrings, type annotations, and inline comments.

```
/doc #sym:func_load_todos
```

**Result:**

```python
def func_load_todos() -> list[dict]:
    """
    Loads all todos from todos.json.

    Returns:
        list[dict]: List of todo dicts.
                   Empty list if the file doesn't exist.

    Raises:
        json.JSONDecodeError: If todos.json is malformed.
    """
```

---

## /new – Generate New Files & Structures

Creates complete new files, folder structures, or scaffolding.

**Examples:**

```
/new GitHub Actions workflow that runs pytest on every push to main
```

```
/new Python class for managing todos with CRUD methods
```

```
/new Flask Blueprint for a user authentication module
```

---

## /newNotebook – Create Jupyter Notebook

```
/newNotebook Analyze the todos.json file: average title length,
how many are completed, when most todos are created.
```

---

## /terminal – Command Help

Explains and suggests commands in the terminal:

```
/terminal Start Flask in debug mode on port 8080
```

```
/terminal Run only tests that contain "todo" in the name
```

---

## /search – Workspace Search

Searches the codebase for relevant places:

```
/search Where are todos validated?
```

```
/search All places where the file is written
```

---

## Right-Click Context Menu

Select code → right-click → **Copilot**:

| Action              | Effect                                                 |
| ------------------- | ------------------------------------------------------ |
| Explain             | Explain selected code                                  |
| Fix                 | Fix bugs in selection                                  |
| Generate Tests      | Create tests for selection                             |
| Review and Comment  | Code review with inline comments                       |
| Generate Docs       | Add docstrings/comments                                |
| Start Inline Chat   | Open Inline Chat at selection position                 |
