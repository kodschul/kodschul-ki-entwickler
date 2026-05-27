# Module 08 — Solutions

---

## Solution 08.1 – tasks.json (Run Tests + Start Flask)

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "python",
      "args": ["-m", "pytest", "test_app.py", "-v"],
      "group": {
        "kind": "test",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "shared",
        "clear": true
      },
      "problemMatcher": []
    },
    {
      "label": "Start Flask",
      "type": "shell",
      "command": "python",
      "args": ["app.py"],
      "options": {
        "env": { "FLASK_DEBUG": "1" }
      },
      "group": "build",
      "isBackground": true,
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    }
  ]
}
```

**Verification:** `Ctrl+Shift+P` → "Run Test Task" runs `pytest` in the terminal. The exit code determines whether the task succeeds or fails.

---

## Solution 08.2 – pre-commit Hook

`.git/hooks/pre-commit`:

```bash
#!/bin/bash
echo "Running tests before commit..."
python -m pytest test_app.py -q

if [ $? -ne 0 ]; then
  echo ""
  echo "❌ Tests failed! Commit aborted."
  echo "Fix the tests first."
  exit 1
fi

echo "✅ Tests passed. Committing..."
exit 0
```

```bash
chmod +x .git/hooks/pre-commit
```

**Verification:** Break a test deliberately (e.g., change an assertion), run `git commit -m "test"` → the commit is blocked with the failure message.

---

## Solution 08.3 – Full tasks.json

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "python",
      "args": ["-m", "pytest", "test_app.py", "-v"],
      "group": { "kind": "test", "isDefault": true },
      "presentation": { "reveal": "always", "panel": "shared", "clear": true },
      "problemMatcher": []
    },
    {
      "label": "Start Flask",
      "type": "shell",
      "command": "python",
      "args": ["app.py"],
      "options": { "env": { "FLASK_DEBUG": "1" } },
      "group": "build",
      "isBackground": true,
      "presentation": { "reveal": "always", "panel": "new" },
      "problemMatcher": []
    },
    {
      "label": "Lint",
      "type": "shell",
      "command": "python",
      "args": ["-m", "flake8", "app.py"],
      "group": "build",
      "presentation": { "reveal": "always", "panel": "shared" },
      "problemMatcher": []
    },
    {
      "label": "Format",
      "type": "shell",
      "command": "python",
      "args": ["-m", "black", "app.py"],
      "group": "build",
      "presentation": { "reveal": "always", "panel": "shared" },
      "problemMatcher": []
    },
    {
      "label": "Full Pipeline",
      "dependsOrder": "sequence",
      "dependsOn": ["Lint", "Format", "Run Tests"],
      "group": { "kind": "build", "isDefault": true },
      "problemMatcher": []
    },
    {
      "label": "Clean JSON",
      "type": "shell",
      "command": "python",
      "args": ["-c", "import json; open('todos.json','w').write('[]')"],
      "presentation": { "reveal": "always", "panel": "shared" },
      "problemMatcher": []
    }
  ]
}
```

---

## Solution 08.4 – GitHub Actions Workflow

`.github/workflows/test.yml`:

```yaml
name: Run Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run pytest
        run: python -m pytest test_app.py -v
```

**Key points:**

- Triggers on every push to `main` and on all pull requests targeting `main`.
- Uses the same Python version as local development (3.12).
- `pip install -r requirements.txt` ensures Flask and pytest are available.
- A non-zero exit code from pytest automatically fails the workflow run.
