# Exercise: Custom Commands (Slash Commands)

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create /todo-review (20 min)

Create `.github/prompts/todo-review.prompt.md`:

```
Create a .github/prompts/todo-review.prompt.md for the Todo App.

The command /todo-review should:
1. Check app.py and test_app.py for bugs
2. Verify security of user input validation
3. Check code quality (function length, duplicates)
4. List missing tests

Output structured in:
- Summary
- Critical Issues
- Suggestions
- Missing Tests

Use mode: ask (only analyze, don't change anything)
Include #file:app.py and #file:test_app.py as context.
```

**Test:** In Chat: `/todo-review` → is the response well-structured?

---

## Task 2 – Create /add-feature with Input (20 min)

Create `.github/prompts/add-feature.prompt.md`:

```
Create .github/prompts/add-feature.prompt.md for our Todo App.

The command /add-feature should:
1. Ask for a feature name via ${input:feature_name}
2. Analyze app.py and identify the right integration point
3. Implement the feature:
   - Route in app.py
   - Update to todos.json structure if needed
   - Test cases in test_app.py
4. Follow the existing pattern (Post/Redirect/Get, func_ prefix)
5. Run tests automatically

Use mode: agent with tools: codebase, terminal.
```

**Test:** `/add-feature` → enter "Mark todo as important" → check the result.

---

## Task 3 – Invent Your Own Prompt (30 min)

Choose a prompt idea from this table or invent one:

| Idea                  | Description                                             |
| --------------------- | ------------------------------------------------------- |
| `/bug-fix`            | Analyze error in terminal, suggest fix                  |
| `/refactor-function`  | Refactor selected function with better structure        |
| `/api-doc`            | Document all routes as API docs (Markdown)              |
| `/performance-check`  | Identify performance bottlenecks                        |
| `/dependency-check`   | Review all imports and dependencies                     |
| `/changelog`          | Generate CHANGELOG from Git commits                     |

**Template:**

```markdown
---
mode: ask | edit | agent
description: "..."
tools: # optional
  - codebase
---

# [Name]

[Your instructions here]
[What should Copilot do step by step?]
[What context does it need?]
```

---

## Task 4 – Code Review via gh copilot CLI (20 min)

```bash
# Install (if not done yet)
gh extension install github/gh-copilot

# Pipe file to Copilot
cat app.py | gh copilot explain

# Get specific suggestions
gh copilot suggest "How can I add error handling to this Flask app?"

# More targeted:
gh copilot suggest "Review for missing input validation in Flask forms"
```

**Question:** What differences do you notice compared to `/todo-review` in VS Code?
