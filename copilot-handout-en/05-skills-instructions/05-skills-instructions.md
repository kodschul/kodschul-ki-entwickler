# 05 – Skills & .instructions.md

**Block:** 90 min | **Day 2**

---

## What are Instructions and Skills?

**Instructions** (`.instructions.md`) are persistent behavioral rules that Copilot follows automatically when working with specific files. They are the equivalent of Claude's SKILL.md files.

**Unlike Prompts (`.prompt.md`):**

| Aspect          | Prompt (`.prompt.md`)      | Instruction (`.instructions.md`) |
| --------------- | -------------------------- | -------------------------------- |
| Activation      | Manual (`/command`)        | Automatic (when file matches)    |
| Purpose         | Task to execute            | Rule to always follow            |
| Mode            | ask / edit / agent         | Passive context                  |
| Usage           | On demand                  | Always active for matching files |

---

## File Structure

```
.github/
└── instructions/
    ├── python.instructions.md      ← applyTo: **/*.py
    ├── flask.instructions.md       ← applyTo: **/app.py
    ├── testing.instructions.md     ← applyTo: **/test_*.py
    └── security.instructions.md   ← applyTo: **
```

---

## Frontmatter Fields

```yaml
---
applyTo: "**/*.py"        # Which files this applies to (glob pattern)
description: "..."        # When is this instruction used? (optional)
---
```

---

## applyTo Patterns

| Pattern          | Applies to                      |
| ---------------- | ------------------------------- |
| `**`             | All files (global)              |
| `**/*.py`        | All Python files                |
| `**/test_*.py`   | All pytest test files           |
| `src/**`         | Everything in src/              |
| `**/app.py`      | Only files named app.py         |
| `templates/**`   | All templates                   |
| `**/*.{ts,tsx}`  | TypeScript and TSX files        |

---

## copilot-instructions.md vs. .instructions.md

| Aspect              | copilot-instructions.md         | .instructions.md              |
| ------------------- | --------------------------------| ----------------------------- |
| Location            | `.github/`                      | `.github/instructions/`       |
| Read automatically  | Always                          | Only when applyTo matches     |
| Scope               | Entire project                  | File-type-specific            |
| Purpose             | Project context & general rules | Specific technology rules     |
| Recommended length  | Max 80 lines                    | 20–40 lines                   |

---

## Example 1 – Python Instructions

```markdown
---
applyTo: "**/*.py"
description: "Python code generation rules"
---

# Python Guidelines

- Use Python 3.12+ syntax (match/case, walrus operator, f-strings)
- Always add type annotations to function parameters and return values
- Prefer list comprehensions over for loops for simple transformations
- Handle all exceptions explicitly – no bare `except:`
- Use pathlib instead of os.path for file operations
```

---

## Example 2 – Flask Instructions

```markdown
---
applyTo: "**/app.py"
description: "Flask application rules"
---

# Flask Guidelines

- Always use Post/Redirect/Get (PRG) pattern for form routes
- Validate all form inputs before processing
- Use flash() for user messages
- Never expose sensitive data in responses or logs
- All routes must have a docstring
```

---

## Example 3 – Testing Instructions

```markdown
---
applyTo: "**/test_*.py"
description: "Testing conventions for pytest"
---

# Testing Guidelines

- Test naming: test_{function}_{condition}_{expected_result}
- Create at least 3 tests per function: happy path, empty input, edge case
- Use pytest fixtures for repeated setup
- Never test implementation details, only public behavior
- Mock all external dependencies (file system, APIs)
```

---

## Example 4 – Security Instructions

```markdown
---
applyTo: "**"
description: "Security rules for all files"
---

# Security Rules

- Never use eval() or exec()
- Always validate and sanitize user inputs
- No hardcoded passwords, tokens, or API keys in source code
- Use secrets.token_urlsafe() for token generation
- All file paths must be validated (no path traversal)
```

---

## Activating via settings.json

**Method 1 – File reference:**

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/instructions/python.instructions.md"
    }
  ]
}
```

**Method 2 – Inline text:**

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "text": "Always use Python 3.12+ and type annotations."
    }
  ]
}
```

**Method 3 – Combine multiple instructions:**

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/instructions/python.instructions.md" },
    { "file": ".github/instructions/flask.instructions.md" },
    { "text": "Use English for all code and comments." }
  ]
}
```

---

## Instructions Stacking

Multiple instructions can apply simultaneously:

```
Working on test_app.py
  → copilot-instructions.md (always active)
  → python.instructions.md (applyTo: **/*.py ✓)
  → testing.instructions.md (applyTo: **/test_*.py ✓)
  → security.instructions.md (applyTo: ** ✓)
  → flask.instructions.md (applyTo: **/app.py ✗)
```

→ All three active files are combined into the system prompt.

---

## When Instructions vs. Prompts

| Task                                   | Solution              |
| -------------------------------------- | --------------------- |
| "Always write type annotations"        | instruction           |
| "Run a code review now"                | prompt                |
| "Never use eval()"                     | instruction           |
| "Generate tests for this function"     | prompt or /tests      |
| "Use PRG pattern in Flask"             | instruction           |
| "Add a new feature step by step"       | prompt + agent        |
