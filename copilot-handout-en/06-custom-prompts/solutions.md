# Module 06 — Solutions

---

## Solution 06.1 – /todo-review Prompt

```markdown
---
mode: ask
description: "Comprehensive review of the Todo App: bugs, security, code quality, and missing tests"
---

# Todo App Review

Analyze #file:app.py and #file:test_app.py.

## 1. Summary

Give a one-paragraph overview of the current state of the code (structure, coverage, overall quality).

## 2. Critical Issues

List bugs or security problems that require immediate attention.
For each: file path + line number + explanation + suggested fix.

## 3. Suggestions

List code quality improvements: overly long functions, duplicated logic, unclear naming.

## 4. Missing Tests

List functions or scenarios that have no test coverage.
```

**Expected output:** A four-section Markdown report. The `mode: ask` ensures Copilot only analyses and never modifies files.

---

## Solution 06.2 – /add-feature Prompt

```markdown
---
mode: agent
description: "Add a new feature to the Flask Todo App following existing patterns"
tools:
  - codebase
  - terminal
---

# Add Feature: ${input:feature_name}

1. Open #file:app.py and identify the right integration point for "${input:feature_name}".
2. Implement the feature following existing conventions:
   - New routes use the Post/Redirect/Get (PRG) pattern
   - Helper functions use the `func_` prefix
   - Update the `todos.json` structure only if a new field is required
3. Add tests to `test_app.py` using the `test_{function}_{condition}_{expected}` naming format.
4. Run `python -m pytest test_app.py -v` and fix any failures before finishing.
5. Report what was added, where, and whether all tests pass.
```

**Test result for "Mark todo as important":**  
Copilot adds a boolean `important` field to the data model, a `POST /important/<id>` route, and at least three tests (`test_mark_important_valid_id_sets_flag`, `test_mark_important_unknown_id_returns_404`, `test_mark_important_already_important_toggles_off`).

---

## Solution 06.3 – Example Custom Prompt (/api-doc)

```markdown
---
mode: ask
description: "Generate Markdown API documentation for all Flask routes in app.py"
---

# API Documentation

Analyze #file:app.py and produce complete API documentation for every Flask route.

For each route provide:

- **Method & URL** (e.g., `POST /add`)
- **Description** – what does it do in one sentence?
- **Inputs** – form fields, query parameters, or path variables
- **Response** – redirect target, rendered template, or JSON payload
- **Side effects** – what changes in the application state?

Format: a summary table first, then a detailed section per route.
```

---

## Solution 06.4 – gh copilot CLI

```bash
# Install the extension once
gh extension install github/gh-copilot

# Explain a file
cat app.py | gh copilot explain

# Get improvement suggestions
gh copilot suggest "How can I add error handling to this Flask app?"

# Suggest a shell command
gh copilot suggest -t shell "Run only the tests that contain 'add' in their name"
```

**Expected output for `gh copilot explain`:** A natural-language walkthrough of the Flask app structure — routes, helper functions, data persistence pattern, and how the Todo list is rendered.
