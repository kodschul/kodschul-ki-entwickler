# Exercise: Custom Agents

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create the Security Reviewer Agent (25 min)

Create `.github/agents/security-reviewer.agent.md`:

```
Create a .github/agents/security-reviewer.agent.md for our Flask Todo App.

The agent should:
1. Scan all Python files for security vulnerabilities:
   - Missing input validation
   - Potential XSS (unescaped output)
   - File path issues (e.g. todos.json manipulation)
   - Hardcoded values that should be secrets
   - Use of eval()/exec()

2. Generate a prioritized report:
   - Critical: fix immediately
   - Medium: should be fixed
   - Low: informational

3. For each finding: exact location (file + line) + fix suggestion

Use tools: codebase (to read files)
Persona: security expert, direct, concrete
```

**Test:** In Agent Mode: `@security-reviewer Review app.py and test_app.py.`

---

## Task 2 – Create the Test Writer Agent (25 min)

Create `.github/agents/test-writer.agent.md`:

```
Create a .github/agents/test-writer.agent.md for our Flask Todo App.

The agent should:
1. Identify all functions without test coverage
2. For each function, generate:
   - 1 happy path test
   - 1 invalid input test
   - 1 edge case test
3. Use pytest conventions: test_what_when_expected
4. Add tests to test_app.py
5. Run pytest and fix any errors

Tools: codebase (read), terminal (run pytest)
Never change existing source code – only test_app.py.
```

**Test:** `@test-writer Write tests for all functions in app.py that have no test coverage.`

---

## Task 3 – Build Your Own Agent (30 min)

Ideas for a custom agent:

| Agent Name            | Description                                      |
| --------------------- | ------------------------------------------------ |
| `performance-auditor` | Analyze response times, unnecessary loops        |
| `docs-writer`         | Generate API documentation from routes           |
| `refactoring-guide`   | Find duplicates, suggest refactoring             |
| `dependency-checker`  | Find outdated requirements.txt entries           |
| `changelog-generator` | Generate CHANGELOG.md from Git commits           |
| `onboarding-helper`   | Explain the codebase structure to new developers |

**Template:**

```markdown
---
name: [agent-name]
description: "[When is this agent useful?]"
tools:
  - codebase
  - terminal # only if commands need to run
---

# [Agent Name]

You are [Role]. Your specialty is [Domain].

## Your Tasks When Invoked

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output Format

[How should the output look?]

## Rules

- [What should the agent not do?]
- [What style/format?]
```

---

## Task 4 – gh copilot CLI as "Agent" (10 min)

```bash
# Simulate security review via CLI
cat app.py | gh copilot explain \
  "Check this code for security vulnerabilities"

# Headless review script
cat > review.sh << 'EOF'
#!/bin/bash
echo "=== Security Review ==="
gh copilot suggest \
  "Review for OWASP Top 10 vulnerabilities" \
  --no-interaction < app.py
EOF
chmod +x review.sh
./review.sh
```
