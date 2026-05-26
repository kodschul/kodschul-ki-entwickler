# Exercise: MCP, Customization & Closing

**Time:** 60 min | **Project:** `1205/todo-app/`

---

## Task 1 – Configure Playwright MCP (15 min)

Install Playwright MCP and configure it:

```bash
npx @playwright/mcp@latest --help
```

Create `.vscode/mcp.json`:

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {}
    }
  }
}
```

Start the Flask app:

```bash
FLASK_DEBUG=1 python app.py
```

In Copilot Chat (Agent Mode):

```
Open http://localhost:5000 in the browser.
Add a todo "MCP Test" and verify it appears in the list.
```

**Observe:** Copilot controls the browser?

---

## Task 2 – Set Up gh copilot CLI (10 min)

```bash
# Install (once)
gh extension install github/gh-copilot

# Test:
gh copilot suggest "Run Flask app in debug mode on port 8080"

gh copilot explain "FLASK_DEBUG=1 python app.py"

# Set up aliases
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Test aliases:
gh cs "Run all pytest tests and show coverage"
```

---

## Task 3 – Create a Review Script (15 min)

```
Create a shell script review.sh that:
1. Runs python -m pytest -v and saves output
2. Sends the test output to gh copilot for analysis
3. Asks for a code review of app.py
4. Shows all results clearly formatted

Use gh copilot suggest --no-interaction for headless operation.
```

**Test:**

```bash
chmod +x review.sh
./review.sh
```

---

## Task 4 – Harden Permissions via Instructions (10 min)

Create `.github/instructions/permissions.instructions.md`:

```
Create .github/instructions/permissions.instructions.md.

Rules:
- NEVER change todos.json directly (only via func_save_todos)
- NEVER add imports without asking
- NEVER change the HTML structure in templates (only content within existing elements)
- NEVER delete existing functions
- Ask the user if you're unsure

applyTo: **
```

**Test:** Ask Copilot to delete `func_load_todos`. Does it refuse?

---

## Task 5 – Free Experimentation (10 min)

Try something you've wanted to explore during the training:

Ideas:

- `@security-reviewer` on the full app
- `@test-writer` for all uncovered functions
- `/spec-plan` for a new feature idea
- `gh copilot suggest -t github-actions "Deploy Flask to Railway"`

---

## Closing Checklist

```
✅ Day 1:
□ copilot-instructions.md created
□ .vscode/settings.json configured
□ Inline completions + shortcuts mastered
□ /fix, /explain, /tests, /doc used

✅ Day 2:
□ .instructions.md files created (python, security, testing)
□ /todo-review custom prompt created
□ /add-feature with ${input:} created
□ @security-reviewer agent created
□ tasks.json with auto-test set up
□ GitHub Actions workflow created

✅ Day 3:
□ Token strategies understood
□ gh copilot CLI installed and used
□ SPEC.md written and used
□ Spec-Kit prompts created
□ MCP configured (Playwright)
□ Closing checklist complete 🎉
```
