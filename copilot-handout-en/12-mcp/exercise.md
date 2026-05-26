# Exercise: MCP, gh CLI & Closing

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Set Up Playwright MCP (20 min)

Create `.vscode/mcp.json`:

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "type": "stdio"
    }
  }
}
```

Test in Agent Mode:

```
Open http://localhost:5000 in the browser and show me all todos currently in the list.
```

**Then:**

```
Add a new todo "Test MCP" via the browser form and confirm it appears in the list.
```

---

## Task 2 – Set Up gh CLI (15 min)

```bash
# Install (if not done yet)
brew install gh
gh auth login
gh extension install github/gh-copilot

# Verify:
gh --version
gh copilot --version

# Aliases:
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'
```

Test:

```bash
gh cs "Run Flask tests only for /add route"
gh ce "python -m pytest -v -k 'add'"
```

---

## Task 3 – Build a Review Script (20 min)

Create `review.sh`:

```bash
#!/bin/bash
echo "=== Running Tests ==="
python -m pytest test_app.py -v 2>&1 | tail -20

echo ""
echo "=== Code Review ==="
gh copilot suggest --no-interaction \
  "What security issues do Flask apps with file-based storage typically have?"

echo ""
echo "=== Next Steps ==="
gh copilot suggest -t git --no-interaction \
  "Create a commit for my current changes with a Conventional Commit message"
```

```bash
chmod +x review.sh
./review.sh
```

---

## Task 4 – Define Permissions via Instructions (15 min)

Extend `.github/copilot-instructions.md` with a Permissions section:

```markdown
## Allowed Actions

The agent may:
- Read and modify Python files
- Run tests: `python -m pytest`
- Run linting: `ruff check .`

## Prohibited

The agent must NOT:
- Execute `git push` without approval
- Install new packages without approval
- Access files outside this project

## Always Ask First

- Deleting files
- Changes to todos.json (production data)
```

Test in Agent Mode: Give the agent an instruction that would require `git push`.

---

## Task 5 – Free Experimentation (20 min)

Choose one:

**Option A – MCP Extension:**
Add GitHub MCP server to `mcp.json` and let the agent create a GitHub issue.

**Option B – Custom Spec-Kit:**
Create a spec for a new feature (e.g. tags/labels) and test the full spec-plan → spec-build → spec-test workflow.

**Option C – CLI Scripting:**
Build a complete `ci.sh` that runs tests, linting, and a code review – fully automated.

---

## Closing Checklist

```
Inline Completions:
□ Ghost Text with Tab accepted
□ NES (Next Edit Suggestion) understood
□ Context control with comments/docstrings used

Chat & Context:
□ Context variables used (#file, #sym, etc.)
□ Inline Chat (Ctrl+I) used
□ #terminalLastCommand used

Configuration:
□ copilot-instructions.md created
□ At least one .instructions.md file created
□ settings.json configured

Custom Commands & Agents:
□ At least one .prompt.md file created
□ At least one .agent.md file created
□ Both tested in real workflow

Automation:
□ tasks.json with at least one task
□ CLI aliases set up
□ (Optional) Spec-Kit implemented

Advanced:
□ Token management strategies understood
□ CLI as fallback for terminal tasks used
□ MCP server tested
```
