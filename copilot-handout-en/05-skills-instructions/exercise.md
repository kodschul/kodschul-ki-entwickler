# Exercise: Skills & .instructions.md

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create Python Instructions (20 min)

Create `.github/instructions/python.instructions.md`:

```
Create a .github/instructions/python.instructions.md for our Flask Todo App.

applyTo: **/*.py

Rules:
- Python 3.12+ syntax
- Always add type annotations
- Use pathlib instead of os.path
- Prefer list comprehensions
- No bare except:
- All functions with docstring

Keep it under 30 lines.
```

**Test:** Open `app.py` → ask Copilot to add a new function.  
Does it automatically use type annotations?

---

## Task 2 – Create Security Instructions (20 min)

Create `.github/instructions/security.instructions.md`:

```
Create a .github/instructions/security.instructions.md.

applyTo: **  (applies to all files)

Security rules:
- No eval() or exec()
- Always validate user inputs
- No hardcoded passwords/tokens
- File paths must be validated
- Use secrets.token_urlsafe() for tokens
- No sensitive data in logs
```

**Test:** Ask Copilot Chat:

```
Generate a function that reads a file at a user-specified path.
```

Does Copilot automatically add path validation?

---

## Task 3 – Create Testing Instructions + settings.json (20 min)

Create `.github/instructions/testing.instructions.md`:

```
Create .github/instructions/testing.instructions.md.

applyTo: **/test_*.py

Rules:
- Naming: test_{function}_{condition}_{expected}
- At least 3 tests per function: happy path, empty input, edge case
- Use pytest fixtures for shared setup
- Mock all file system operations
- Test only public behavior, not implementation details
```

Add to `.vscode/settings.json`:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ]
}
```

**Test:** `/tests #sym:func_validate_title`  
Do the generated tests follow the naming convention?

---

## Task 4 – Observe Stacking (15 min)

With all three instruction files active:

Open `test_app.py` and ask:

```
Add tests for func_format_due_date.
```

**Check:**
- Are type annotations present? (Python instructions)
- Are security checks mentioned? (Security instructions)
- Is the test naming convention followed? (Testing instructions)

**Trace the stacking:**

```
Working on test_app.py:
→ copilot-instructions.md       active? ___
→ python.instructions.md        active? ___ (why?)
→ security.instructions.md      active? ___ (why?)
→ testing.instructions.md       active? ___ (why?)
→ flask.instructions.md         active? ___ (why? if you have one)
```

---

## Task 5 – Invent Your Own Instruction (15 min)

Choose an idea from this table or invent one:

| Idea                   | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `api.instructions.md`  | REST API conventions for Flask endpoints         |
| `logging.instructions.md` | Always use structured logging                 |
| `performance.instructions.md` | Avoid N+1 queries, unnecessary loops      |
| `docs.instructions.md` | Google Docstring style, always document raises  |
| `typing.instructions.md` | Advanced typing: TypedDict, Protocol, etc.    |

**Template:**

```markdown
---
applyTo: "[pattern]"
description: "[When is this instruction used?]"
---

# [Name]

- [Rule 1]
- [Rule 2]
- [Rule 3]
```
