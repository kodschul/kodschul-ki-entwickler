# Exercise: Configuration

**Time:** 60 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create copilot-instructions.md (20 min)

```
Create a .github/copilot-instructions.md for our Flask Todo App.

Project:
- Flask web app for managing todos
- Python 3.12, Tailwind CDN
- Storage in todos.json (no database)
- pytest for testing
- Post/Redirect/Get pattern

Include:
1. Project goal (1 sentence)
2. Start command: FLASK_DEBUG=1 python app.py
3. Test command: python -m pytest test_app.py -v
4. DOs: Tailwind CDN, PRG pattern, todos.json
5. DON'Ts: no database, no REST API, no eval()

Important: Maximum 80 lines!
```

**Check:** Open file → count lines → trim if necessary.

---

## Task 2 – Configure .vscode/settings.json (20 min)

```
Create a .vscode/settings.json for our Flask Todo App.

Configure:
1. codeGeneration: load .github/instructions/python.instructions.md
2. testGeneration: use pytest, test_what_when_expected format,
   always 3 test cases (happy path, empty input, edge case)
3. commitMessageGeneration: Conventional Commits, max 72 chars,
   reference issue number if available
4. localeOverride: "en"
5. Disable Ghost Text for markdown and plaintext files
```

---

## Task 3 – Test Commit Message Generator (10 min)

1. Open Source Control panel (`⌘ Shift G`)
2. Make a small change in `app.py` (add a comment)
3. Stage the file
4. Click the ✨ icon in the commit message field
5. Observe: Does Copilot follow the Conventional Commits format?

---

## Task 4 – Reflection – Which rule goes where? (10 min)

Fill out this table based on the exercise:

| Rule                                          | Where does it belong?               |
| --------------------------------------------- | ----------------------------------- |
| "Use pytest"                                  | settings.json / testGeneration      |
| "No database – only todos.json"               | copilot-instructions.md             |
| "Always write type annotations for *.py"      | python.instructions.md (applyTo)    |
| "No eval() or exec()"                         | security.instructions.md            |
| "Commit messages in Conventional Commits format" | settings.json / commitMessageGeneration |
| "Validate all user inputs"                    | security.instructions.md            |

**Discuss:** When would you put a rule in settings.json vs. in a .md file?
