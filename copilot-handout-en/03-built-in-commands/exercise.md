# Exercise: Built-in Commands

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – /explain with #sym (15 min)

Open Copilot Chat:

```
/explain #sym:func_load_todos
```

```
/explain #sym:func_save_todos
```

**Questions:**

- What edge cases exist?
- Where could errors occur?
- What happens if `todos.json` has an incorrect format?

---

## Task 2 – /fix with #terminalLastCommand (20 min)

Intentionally introduce a bug in `app.py`:

```python
# In the /add route – remove .get():
todo = {
    "title": request.form["title"],   # ← Bug: KeyError if form field missing
    "done": False
}
```

Run in the terminal:

```bash
curl -X POST http://localhost:5000/add -d ""
```

In Copilot Chat:

```
/fix #terminalLastCommand
```

**Observe:** Does Copilot recognize the problem and suggest `.get()`?

---

## Task 3 – /tests with settings.json (20 min)

First configure `.vscode/settings.json`:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Use pytest. Always generate: 1 happy path test, 1 empty input test, 1 edge case test. Test names in the format test_what_when_expected."
    }
  ]
}
```

Then:

```
/tests #sym:func_validate_title
```

**Observe:**

- How many test cases are generated?
- Are they in the right format?
- Would they actually pass?

---

## Task 4 – /doc with Google Style (15 min)

```
/doc #sym:func_load_todos
Use Google Docstring style with type annotations.
```

**Check:**

- Are the types correct?
- Are the return values documented?
- Are exceptions mentioned?

---

## Task 5 – /new (20 min)

**Subtask A – Scaffold a class:**

```
/new Python class TodoManager for the Todo App.
It should have all CRUD methods: load, save, add, delete, toggle, filter_by_status.
Use todos.json for storage.
```

**Subtask B – GitHub Actions:**

```
/new GitHub Actions workflow that runs pytest on every push to main.
Python 3.12, install requirements.txt, fail on test error.
```

---

## Task 6 – Right-Click Review (10 min)

1. Select the `/add` route in `app.py`
2. Right-click → Copilot → **Review and Comment**
3. Observe the inline comments
4. Select all of `app.py`
5. Right-click → Copilot → **Review and Comment**

**Question:** What does Copilot flag?
