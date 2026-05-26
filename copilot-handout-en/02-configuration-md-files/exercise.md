# Exercise: Configuration & .md Files

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create copilot-instructions.md (30 min)

**Without any configuration:**

Open Copilot Chat and ask:

```
Add error handling for when todos.json doesn't exist.
```

Note down what Copilot suggests.

---

**Now create `.github/copilot-instructions.md`:**

```
Create a .github/copilot-instructions.md for my Todo App.
I use:
- Flask (Python 3.12)
- Tailwind CSS via CDN
- todos.json for storage
- pytest for tests
- Post/Redirect/Get pattern

The file should:
1. Describe the project goal
2. Include the start commands
3. Contain clear DOs and DON'Ts
Keep it under 80 lines!
```

Ask the same question again:

```
Add error handling for when todos.json doesn't exist.
```

**Compare:** Is the suggestion now more targeted?

---

## Task 2 – Create security.instructions.md (20 min)

```
Create a .github/instructions/security.instructions.md for our Flask Todo App.
It should apply to all files (applyTo: "**").

Security rules:
- No eval() or exec()
- Always validate user inputs
- No sensitive data in source code
- Use secrets.token_urlsafe() instead of random
- Always use parameterized queries (for future database work)

Short and precise – max 20 rules.
```

Add to `.vscode/settings.json`:

```json
{
  "github.copilot.chat.reviewSelection.instructions": [
    {
      "file": ".github/instructions/security.instructions.md"
    }
  ]
}
```

**Test:** Select the `/add` route, right-click → Copilot → Review and Comment.  
Does Copilot evaluate against the security rules?

---

## Task 3 – Configure .vscode/settings.json (20 min)

```
Create a .vscode/settings.json for our Flask Todo App.

It should configure:
1. codeGeneration: load python.instructions.md
2. testGeneration: use pytest, create happy path + edge case tests
3. reviewSelection: load security.instructions.md

Also: disable Ghost Text for markdown files.
```

---

## Task 4 – Try gh copilot CLI (20 min)

```bash
# Install (once):
gh extension install github/gh-copilot

# Test:
gh copilot suggest "Start Flask application in debug mode"

gh copilot explain "FLASK_DEBUG=1 python app.py"

gh copilot suggest -t shell "Show all Python files recursively"
```

**Question:** How does the CLI experience differ from VS Code Chat?
