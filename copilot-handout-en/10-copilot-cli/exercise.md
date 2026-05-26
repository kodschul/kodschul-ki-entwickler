# Exercise: Copilot CLI – Complete Reference

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – suggest for Shell Commands (15 min)

```bash
# Install (if not done yet)
gh extension install github/gh-copilot

# Basic suggest:
gh copilot suggest "Run Flask tests and show only failures"
gh copilot suggest "Show all Python files modified in the last hour"
gh copilot suggest "Count lines of code in app.py"

# Try the interactive menu:
# → Copy command, Explain command, Execute command
```

**Question:** What does the interactive menu offer?

---

## Task 2 – suggest -t git (20 min)

```bash
# Git-specific commands:
gh copilot suggest -t git "Stage only Python files"

gh copilot suggest -t git "Show commits from today"

gh copilot suggest -t git "Create a branch 'feature/due-dates'"

gh copilot suggest -t git "Undo last commit but keep changes"
```

**Question:** Does `-t git` give better git suggestions than without?

---

## Task 3 – explain Commands (15 min)

```bash
# Explain common commands:
gh copilot explain "python -m pytest -v --tb=short"

gh copilot explain "git log --oneline --graph --decorate --all"

gh copilot explain "find . -name '*.py' | xargs grep -l 'def func_'"

# Explain your own command:
gh copilot explain "FLASK_DEBUG=1 python app.py"
```

---

## Task 4 – Set Up Aliases (10 min)

```bash
# gh aliases:
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Test:
gh cs "Show all open ports on this machine"
gh ce "lsof -i -P -n | grep LISTEN"

# Shell aliases in ~/.zshrc:
echo "alias ghcs='gh copilot suggest'" >> ~/.zshrc
echo "alias ghce='gh copilot explain'" >> ~/.zshrc
source ~/.zshrc

# Test:
ghcs "Start Flask app with auto-reload"
```

---

## Task 5 – Build a Review Script (20 min)

Create `review.sh`:

```bash
#!/bin/bash
# review.sh – Automated code review

set -e

echo "========================================="
echo "  Todo App Code Review"
echo "========================================="

echo ""
echo "--- Running Tests ---"
python -m pytest test_app.py -v 2>&1 | tail -20

echo ""
echo "--- Security Review ---"
cat app.py | gh copilot explain \
  "Check this Flask code for security vulnerabilities. Be specific."

echo ""
echo "--- Next Steps ---"
gh copilot suggest \
  "Based on a Flask app with todos, what should I check next?"
```

```bash
chmod +x review.sh
./review.sh
```

---

## Task 6 – CLI vs. Chat Comparison (10 min)

Answer the same question with CLI and with Copilot Chat:

**Question:** "How do I run only the tests that test the /add route?"

**CLI:**

```bash
gh copilot suggest "Run only pytest tests that test the /add route"
```

**Chat:**

```
How do I run only the pytest tests for the /add route? #file:test_app.py
```

**Fill in the comparison table:**

| Aspect           | CLI                    | Chat                   |
| ---------------- | ---------------------- | ---------------------- |
| Speed            |                        |                        |
| Context quality  | No file context        | With #file             |
| Tokens used      | 0 Copilot tokens       | ~500 tokens            |
| Best for         | Terminal questions      | Code analysis          |
