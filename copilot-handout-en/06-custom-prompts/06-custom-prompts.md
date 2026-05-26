# 06 – Custom Prompts (Slash Commands)

**Block:** 90 min | **Day 2**

---

## How do Custom Prompts work under the hood?

When you type `/todo-review` in Copilot Chat, Copilot does this internally:

```
User types /todo-review
  → VS Code reads .github/prompts/todo-review.prompt.md
  → Frontmatter is parsed (mode, tools)
  → Content becomes part of the system prompt
  → Copilot executes the task as if you typed the entire prompt manually
```

> Custom Prompts are **reusable prompt templates** that Copilot uses like a slash command.

---

## Why / When not?

| Why use them                     | When not to                         |
| -------------------------------- | ----------------------------------- |
| Same task repeated regularly     | One-time task → type it directly    |
| Complex prompts (10+ lines)      | Simple question                     |
| Team-wide standardized workflows | Highly context-dependent (use chat) |
| Parameterizable templates        | Tasks that vary greatly each time   |

---

## What are Custom Prompts?

- Markdown files with frontmatter
- Located in `.github/prompts/`
- Available as `/filename` (without `.prompt.md`)
- Can be parameterized with `${input:label}`
- Optionally access tools (codebase, terminal, etc.)

---

## File Location & Naming

```
.github/
└── prompts/
    ├── todo-review.prompt.md    → /todo-review
    ├── add-feature.prompt.md   → /add-feature
    ├── run-tests.prompt.md     → /run-tests
    └── security-check.prompt.md → /security-check
```

---

## .prompt.md Structure

```markdown
---
mode: ask # "ask" | "edit" | "agent"
description: "..." # What does this command do?
tools: # Optional: allowed tools
  - codebase
  - terminal
---

# Command Title

Instructions and context for Copilot.
Can reference variables: ${input:feature_name}
Can reference files: #file:app.py
```

---

## Frontmatter Options

| Key           | Values                   | Effect                             |
| ------------- | ------------------------ | ---------------------------------- |
| `mode`        | `ask` / `edit` / `agent` | Chat mode when calling the command |
| `description` | String                   | Shown as tooltip in command list   |
| `tools`       | List of tool names       | Which tools the agent may use      |

---

## Variables

| Variable             | Example                     | Effect                       |
| -------------------- | --------------------------- | ---------------------------- |
| `${input:label}`     | `${input:feature_name}`     | Asks for input when calling  |
| `#file:path`         | `#file:app.py`              | Includes the file as context |
| `#sym:symbol`        | `#sym:func_load_todos`      | Includes a specific symbol   |
| `${workspaceFolder}` | `${workspaceFolder}/app.py` | Absolute path to workspace   |

---

## Example 1 – /todo-review

```markdown
---
mode: ask
description: "Code review for the Todo App"
---

# Todo App Code Review

Analyze the code of our Todo App:

1. **Correctness:** Does all CRUD logic work correctly?
2. **Edge cases:** Are empty inputs, missing files, and invalid data handled?
3. **Security:** Is user input validated? Could XSS or injection attacks occur?
4. **Code quality:** Are functions too long (>20 lines)? Is code duplicated?
5. **Tests:** Are the important cases tested?

Output format:

## Summary

[Overall assessment]

## Critical Issues

[Bugs that need immediate fixing]

## Suggestions

[Non-critical improvements]

#file:app.py
#file:test_app.py
```

---

## Example 2 – /add-feature with Input

```markdown
---
mode: agent
description: "Add a new feature to the Todo App"
tools:
  - codebase
  - terminal
---

# Add Feature: ${input:feature_name}

1. Analyze the existing code (#file:app.py) and find the right place.
2. Implement the feature "${input:feature_name}":
   - Add the route in app.py
   - Update todos.json structure if needed
   - Add test cases in test_app.py
3. Ensure the implementation is consistent with the existing pattern.
4. Run the tests: `python -m pytest test_app.py -v`
```

---

## gh copilot CLI – Reviews via Command Line

```bash
# Review entire file
cat app.py | gh copilot explain

# Suggest improvements
gh copilot suggest "How can I improve the security of this Flask app?"

# Headless review (for CI/CD)
gh copilot suggest --no-interaction "Review for SQL injection vulnerabilities"
```
