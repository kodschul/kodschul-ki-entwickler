# 05 – Skills & .instructions.md

**Block:** 90 min | **Day 2**

---

## What are Instructions and Skills?

**Instructions** (`.instructions.md`) are persistent behavioral rules that Copilot follows automatically when working with specific files.

**Skills** (`SKILL.md`) are on-demand, bundled workflows that the agent discovers and loads when relevant. They live alongside scripts, templates, and reference files in a dedicated folder.

**Unlike Prompts (`.prompt.md`):**

| Aspect     | Prompt (`.prompt.md`) | Instruction (`.instructions.md`) |
| ---------- | --------------------- | -------------------------------- |
| Activation | Manual (`/command`)   | Automatic (when file matches)    |
| Purpose    | Task to execute       | Rule to always follow            |
| Mode       | ask / edit / agent    | Passive context                  |
| Usage      | On demand             | Always active for matching files |

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
applyTo: "**/*.py" # Which files this applies to (glob pattern)
description: "..." # When is this instruction used? (optional)
---
```

---

## applyTo Patterns

| Pattern         | Applies to               |
| --------------- | ------------------------ |
| `**`            | All files (global)       |
| `**/*.py`       | All Python files         |
| `**/test_*.py`  | All pytest test files    |
| `src/**`        | Everything in src/       |
| `**/app.py`     | Only files named app.py  |
| `templates/**`  | All templates            |
| `**/*.{ts,tsx}` | TypeScript and TSX files |

---

## copilot-instructions.md vs. .instructions.md

| Aspect             | copilot-instructions.md         | .instructions.md          |
| ------------------ | ------------------------------- | ------------------------- |
| Location           | `.github/`                      | `.github/instructions/`   |
| Read automatically | Always                          | Only when applyTo matches |
| Scope              | Entire project                  | File-type-specific        |
| Purpose            | Project context & general rules | Specific technology rules |
| Recommended length | Max 80 lines                    | 20–40 lines               |

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

- Test naming: test*{function}*{condition}\_{expected_result}
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

---

## SKILL.md – On-Demand Agent Skills

**Skills** package reusable, domain-specific workflows that the agent loads only when needed.

### Folder Structure

```
.github/
└── skills/
    └── <skill-name>/
        ├── SKILL.md        ← Required; name must match folder
        ├── scripts/        ← Executable helpers (optional)
        ├── references/     ← Docs the agent can load (optional)
        └── assets/         ← Templates, boilerplate (optional)
```

### SKILL.md Frontmatter

```yaml
---
name: skill-name            # Required: lowercase alphanumeric + hyphens, matches folder
description: "When and why to use this skill. Be keyword-rich so the agent can discover it."
argument-hint: "Optional hint shown when invoked as /skill-name"
user-invocable: true        # true = appears as /skill-name slash command (default)
disable-model-invocation: false  # false = agent auto-loads when relevant (default)
---

# Skill Body

Describe what the skill does, step by step.
Link to bundled resources: [run tests](./scripts/run-tests.sh)
```

### Instructions vs. Skills

| Aspect           | `.instructions.md`               | `SKILL.md`                            |
| ---------------- | -------------------------------- | ------------------------------------- |
| Activation       | Automatic (when applyTo matches) | On-demand (model or `/slash-command`) |
| Purpose          | Always-on coding rules           | Packaged, repeatable workflow         |
| Can carry assets | No                               | Yes (scripts, templates, references)  |
| Location         | `.github/instructions/`          | `.github/skills/<name>/`              |
| Scope            | File-type-specific               | Task-specific                         |

### Example – Flask-Deploy Skill

```markdown
---
name: flask-deploy
description: "Deploy the Flask app locally and run smoke tests. Use when asked to start, deploy, or verify the application."
argument-hint: "environment (local | staging)"
---

# Flask Deploy

## When to Use

When the user asks to run, start, or deploy the Flask Todo App.

## Procedure

1. Run `python -m pytest test_app.py -q` – stop if any test fails.
2. Start the server: `FLASK_DEBUG=1 python app.py`
3. Open http://localhost:5000 and confirm the todo list loads.
4. Report: test results + server URL.
```

### How the Agent Discovers Skills

1. **Discovery** – Agent reads only `name` + `description` (~100 tokens)
2. **Load** – When relevant, it loads the `SKILL.md` body (<5000 tokens)
3. **Resources** – Additional files are fetched only when the body references them

Keep the `SKILL.md` body under 500 lines. Put detailed procedures in `references/`.

→ All three active files are combined into the system prompt.

---

## When Instructions vs. Prompts

| Task                               | Solution         |
| ---------------------------------- | ---------------- |
| "Always write type annotations"    | instruction      |
| "Run a code review now"            | prompt           |
| "Never use eval()"                 | instruction      |
| "Generate tests for this function" | prompt or /tests |
| "Use PRG pattern in Flask"         | instruction      |
| "Add a new feature step by step"   | prompt + agent   |
