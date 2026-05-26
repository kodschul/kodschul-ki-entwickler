# Exercise: Automation & Tasks

**Time:** 60 min | **Project:** `1205/todo-app/`

---

## Task 1 – Set Up Auto-Test Task (20 min)

```
Create a .vscode/tasks.json for our Flask Todo App.

The task "Run Tests" should:
1. Run: python -m pytest test_app.py -v
2. Be the default test task (⌘ Shift P → Run Test Task)
3. Show output in the terminal (reveal: always)
4. Be the default task for the "test" group

Also create a second task "Start Flask" that:
1. Runs: FLASK_DEBUG=1 python app.py
2. Runs in the background (isBackground: true)
3. Belongs to the "build" group
```

**Test:** `⌘ Shift P` → "Run Test Task" → are tests running?

---

## Task 2 – Backup via Git Hook (15 min)

Create `.git/hooks/pre-commit`:

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

Make the file executable:

```bash
chmod +x .git/hooks/pre-commit
```

**Test:** Intentionally break a test → `git commit` → does the commit get blocked?

---

## Task 3 – Full tasks.json (15 min)

Expand your `tasks.json` with:

```
Add the following tasks to our tasks.json:

1. "Lint" – runs: python -m flake8 app.py (if flake8 is available, otherwise skip)
2. "Format" – runs: python -m black app.py (if black is available)
3. "Full Pipeline" – depends on: Run Tests
   (and Lint/Format if available)
4. "Clean JSON" – runs: python -c "import json; open('todos.json','w').write('[]')"
   (Reset todos.json to empty)
```

---

## Task 4 – GitHub Actions Workflow (10 min)

```
Create a .github/workflows/test.yml for our Flask Todo App.

The workflow should:
1. Run on every push to main and on pull requests
2. Use ubuntu-latest
3. Set up Python 3.12
4. Install: pip install -r requirements.txt
5. Run: python -m pytest test_app.py -v
6. Fail on test errors (exit code != 0)

Also add a name for each step.
```

**Check:** Does the YAML have the right indentation?
