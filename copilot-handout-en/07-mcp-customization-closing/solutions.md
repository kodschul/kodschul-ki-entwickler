# Module 07-MCP — Solutions

---

## Solution 07-MCP.1 – mcp.json (Playwright)

`.vscode/mcp.json`:

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

**Verification prompt in Agent Mode:**

```
Open http://localhost:5000 in the browser and list all todos currently shown.
```

Expected behaviour: Copilot opens a headless Chromium instance, navigates to the app, and returns the visible todo titles. If the Flask app is not running, start it first: `FLASK_DEBUG=1 python app.py`.

---

## Solution 07-MCP.2 – gh CLI Setup

```bash
# macOS / Linux
brew install gh
gh auth login

# Windows
winget install GitHub.cli
gh auth login

# Install Copilot extension
gh extension install github/gh-copilot

# Verify
gh --version
gh copilot --version

# Register aliases
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'
```

```bash
# Quick tests
gh cs "Run Flask tests only for the /add route"
# → python -m pytest test_app.py -v -k "add"

gh ce "python -m pytest -v -k 'add'"
# → explains what the command does
```

---

## Solution 07-MCP.3 – review.sh

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

**Expected output:** Test results (pass/fail summary), a bullet list of common Flask security issues, and a suggested `git commit` command with a Conventional Commit message.

---

## Solution 07-MCP.4 – Permissions via copilot-instructions.md

```markdown
# Project: Flask Todo App

## Permissions

Copilot MAY:

- Read and edit all `.py`, `.html`, `.json`, `.md`, `.sh` files in this project
- Run `python -m pytest test_app.py` to verify changes
- Run `python app.py` to start the development server
- Use gh CLI to suggest commit messages

Copilot MUST NOT:

- Push to any Git remote without explicit approval
- Modify `.git/` contents other than hooks
- Read or write files outside this project directory
- Install packages not listed in `requirements.txt` without asking first
- Access external URLs other than `http://localhost:5000`
```

---

## Solution 07-MCP.5 – Closing Checklist

| Item                                | Status |
| ----------------------------------- | ------ |
| `.vscode/mcp.json` configured       | ✅     |
| Playwright MCP test passed          | ✅     |
| `gh copilot` installed + aliases    | ✅     |
| `review.sh` executable              | ✅     |
| Permissions defined in instructions | ✅     |
| All tests passing                   | ✅     |
