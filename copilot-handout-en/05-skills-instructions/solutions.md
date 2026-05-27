# Module 05 — Solutions

---

## Solution 05.1 – python.instructions.md

```markdown
---
applyTo: "**/*.py"
description: "Python code generation rules"
---

# Python Guidelines

- Use Python 3.12+ syntax (match/case, walrus operator, f-strings)
- Always add type annotations to function parameters and return values
- Use pathlib instead of os.path for file operations
- Prefer list comprehensions over for loops for simple transformations
- No bare `except:` – catch a specific exception type
- Every function must include a one-line docstring
```

**Expected effect:** When you open `app.py` and ask Copilot to add a function, the generated code automatically includes type annotations and docstrings.

---

## Solution 05.2 – security.instructions.md

```markdown
---
applyTo: "**"
description: "Security rules for all files"
---

# Security Rules

- Never use eval() or exec()
- Always validate and sanitize user-supplied inputs before use
- No hardcoded passwords, tokens, or API keys in source code
- Validate all file paths against a base directory to prevent path traversal
- Use secrets.token_urlsafe() for token generation
- Never log sensitive data (passwords, tokens, personal information)
```

**Expected effect:** When you ask Copilot to generate a function that reads a file at a user-specified path, it automatically adds path validation:

```python
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

def read_user_file(filename: str) -> str:
    """Read a file from the data directory; rejects path traversal attempts."""
    target = (BASE_DIR / filename).resolve()
    if not str(target).startswith(str(BASE_DIR)):
        raise ValueError("Path traversal detected")
    return target.read_text()
```

---

## Solution 05.3 – testing.instructions.md + settings.json

```markdown
---
applyTo: "**/test_*.py"
description: "Testing conventions for pytest"
---

# Testing Guidelines

- Naming: test*{function}*{condition}\_{expected}
- At least 3 tests per function: happy path, empty input, edge case
- Use pytest fixtures for shared setup (e.g., test client)
- Mock all file system operations with unittest.mock.patch
- Test only public behavior, not implementation details
```

**.vscode/settings.json:**

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ]
}
```

**Expected effect:** Running `/tests #sym:func_validate_title` produces tests like:

```python
def test_func_validate_title_valid_input_returns_title():
    assert func_validate_title("Buy milk") == "Buy milk"

def test_func_validate_title_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        func_validate_title("")

def test_func_validate_title_whitespace_only_raises_value_error():
    with pytest.raises(ValueError):
        func_validate_title("   ")
```

---

## Solution 05.4 – Stacking Trace

When working on `test_app.py`, the following instructions are active simultaneously:

```
Working on test_app.py
  → copilot-instructions.md      (always active – project-wide rules)
  → python.instructions.md       (applyTo: **/*.py ✓)
  → security.instructions.md     (applyTo: ** ✓)
  → testing.instructions.md      (applyTo: **/test_*.py ✓)
  → flask.instructions.md        (applyTo: **/app.py ✗ – does NOT apply)
```

**Result for "Add tests for func_format_due_date":**  
Copilot combines all three active instruction sets and generates tests that:

- Use the `test_{function}_{condition}_{expected}` naming convention (testing)
- Include type annotations in helper fixtures (python)
- Mock file I/O where needed (testing)
- Avoid exposing internal state (security)

---

## Solution 05.5 – Example Custom Instruction

```markdown
---
applyTo: "**/templates/**"
description: "Jinja2 template security and structure rules"
---

# Template Guidelines

- Always escape user-provided data with {{ value | e }} or use {{ value }} (Jinja2 auto-escapes by default in Flask)
- Never use {{ value | safe }} on user input
- Keep templates free of business logic – only display logic
- Use {% block %} / {% extends %} for layout inheritance
- Add aria-label attributes to all interactive elements
```

---

## Solution 05.6 – SKILL.md Example

```markdown
---
name: flask-test-runner
description: "Run the Flask test suite and report results. Use when asked to run tests, check coverage, or verify the app works."
argument-hint: "test file or function to run (optional)"
---

# Flask Test Runner

## When to Use

When the user asks to run tests, check coverage, or verify that changes haven't broken anything.

## Procedure

1. Run `python -m pytest test_app.py -v` and capture the output.
2. If any test fails, read the failure message and suggest a fix.
3. Report: total tests, passed, failed, duration.

## Rules

- Never modify source code to make tests pass.
- If the failure is in the test itself, point that out explicitly.
```
