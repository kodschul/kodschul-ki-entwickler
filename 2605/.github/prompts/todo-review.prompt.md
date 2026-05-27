---
name: todo-review
description: "Review Todo app code for bugs, input validation security, quality issues, and missing tests"
argument-hint: "Optional focus area (e.g., API routes, auth, validation)"
agent: ask
model: GPT-5.3-Codex (copilot)
---

# Todo Review

Run a read-only review of the Todo app codebase. Do not make code changes.

Context:

- #file:app.py
- #file:test_app.py

If provided, prioritize this extra focus area: ${input:focus_area}

Review checklist:

1. Check app.py and test_app.py for bugs.
2. Verify security of user input validation.
3. Check code quality (function length, duplicates).
4. List missing tests.

Output structure:

- Summary
- Critical Issues
- Suggestions
- Missing Tests

Requirements:

- Use concrete file and line references whenever possible.
- Prioritize correctness and security over style.
- If no critical issues are found, state that explicitly.
