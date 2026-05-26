# 07 – Custom Agents

**Block:** 90 min | **Day 2**

---

## How do Custom Agents work?

Custom Agents are specialized AI assistants that operate in **Agent mode** and have access to defined tools:

```
User invokes @security-reviewer
  → VS Code reads .github/agents/security-reviewer.agent.md
  → Frontmatter defines: name, description, available tools
  → Content defines the agent's behavior
  → Agent can: read files, run commands, search codebase, access GitHub
  → Agent works autonomously until the task is complete
```

---

## Why / When not?

| Why use them                      | When not to                          |
| --------------------------------- | ------------------------------------ |
| Specialized, recurring task       | One-time task → use Chat             |
| Needs multiple tools (read + run) | Simple question → Ask/Edit mode      |
| Team needs standardized workflow  | Task that varies greatly each time   |
| Specific persona/role for Copilot | Already covered by built-in commands |

---

## Prompt vs. Instruction vs. Agent

| Aspect      | Prompt (`.prompt.md`) | Instruction (`.instructions.md`) | Agent (`.agent.md`)          |
| ----------- | --------------------- | -------------------------------- | ---------------------------- |
| Purpose     | Reusable task         | Persistent behavior rule         | Specialized assistant        |
| Activation  | `/command-name`       | Automatically for matching files | `@agent-name`                |
| Mode        | ask / edit / agent    | Always active                    | Agent (with tools)           |
| Tool access | Optional              | No                               | Yes (defined in frontmatter) |
| Context     | Explicit (in prompt)  | Automatic (via applyTo)          | Agent decides                |

---

## Available Tools

| Tool         | Access to                                     |
| ------------ | --------------------------------------------- |
| `codebase`   | All files in the workspace (read, search)     |
| `terminal`   | Run commands in the integrated terminal       |
| `githubRepo` | GitHub API: issues, PRs, commits, code search |
| `search`     | Web search (Bing)                             |
| `extensions` | Installed VS Code extensions                  |

---

## File Location & Structure

```
.github/
└── agents/
    ├── security-reviewer.agent.md
    └── test-writer.agent.md
```

**Frontmatter:**

```yaml
---
name: security-reviewer
description: "Reviews code for security vulnerabilities"
tools:
  - codebase
  - terminal
---
```

---

## Example 1 – Security Reviewer Agent

```markdown
---
name: security-reviewer
description: "Audits the codebase for security vulnerabilities"
tools:
  - codebase
  - terminal
---

# Security Reviewer

You are a security expert specializing in Python Flask web applications.

## Your Tasks When Invoked

1. Scan all Python files for security vulnerabilities:

   - Unvalidated user inputs
   - Missing CSRF protection
   - Direct use of user data in file paths
   - Hardcoded secrets or passwords
   - Use of eval() or exec()
   - Missing rate limiting

2. Check tests for missing security test cases.

3. Generate a prioritized security report:
   ## Critical Findings
   [Vulnerabilities that need immediate fixing]
   ## Medium Priority
   [Should be fixed soon]
   ## Low Priority / Informational
   [Best practices to consider]

## Style

- Be direct and specific (exact file + line number)
- Always provide a concrete suggestion for fixing
- Rate each finding by severity (Critical / High / Medium / Low)
```

---

## Example 2 – Test Writer Agent

```markdown
---
name: test-writer
description: "Generates comprehensive test cases for Python functions"
tools:
  - codebase
  - terminal
---

# Test Writer

You are a test automation expert for Python/pytest.

## Your Tasks When Invoked

1. Identify functions without test coverage in the codebase.
2. For each uncovered function, generate tests:

   - 1 happy path test
   - 1 empty/null input test
   - 1 edge case test (boundary values)
   - 1 error case test (invalid inputs)

3. Test naming convention: `test_{function}_{condition}_{expected}`
4. Save the tests to the appropriate test file.
5. Run `python -m pytest -v` and fix failing tests.

## Rules

- Never change the existing source code
- Use pytest fixtures where appropriate
- Never test implementation details, only behavior
```

---

## How to Invoke Agents

In Copilot Chat (must be in **Agent mode** 🤖):

```
@security-reviewer Review the entire codebase.

@test-writer Generate tests for all functions without coverage.

@security-reviewer Focus on the /add route in app.py.
```

> **Important:** Select **Agent** mode in the dropdown (not Ask or Edit).

---

## gh copilot CLI – Agent-like Workflows

```bash
# Review via CLI
cat app.py | gh copilot explain "Are there security issues in this code?"

# Headless workflow
gh copilot suggest --no-interaction \
  "Run pytest and show me which tests are failing and why"

# Multi-step via shell script
#!/bin/bash
echo "=== Security Review ==="
gh copilot suggest "Check this Flask app for OWASP Top 10 vulnerabilities" \
  < app.py
```
