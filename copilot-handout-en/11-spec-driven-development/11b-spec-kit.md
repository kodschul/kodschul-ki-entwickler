# 11b – Spec-Kit: Automated Plan → Build → Test

**Block:** Day 3

---

## What is the Spec-Kit?

The Spec-Kit is a set of three custom prompt commands that implement the entire spec-driven workflow:

| Command       | Task                                        |
| ------------- | ------------------------------------------- |
| `/spec-plan`  | Validate spec, identify gaps, plan approach |
| `/spec-build` | Implement feature step by step              |
| `/spec-test`  | Generate tests from acceptance criteria     |

---

## How does it work under the hood?

```
User writes SPEC.md
  ↓
/spec-plan   → Copilot analyzes + asks clarifying questions
  ↓
User answers questions + refines SPEC.md
  ↓
/spec-build  → Copilot implements: Model → Route → Template → Validation
  ↓
/spec-test   → Copilot generates tests per acceptance criterion
  ↓
Review → Accept / Reject
```

---

## Why / When not?

| Why                                  | When not to             |
| ------------------------------------ | ----------------------- |
| Complex feature with multiple steps  | Trivial changes         |
| Spec serves as documentation         | Quick prototyping       |
| Multiple people work on it           | No clear requirements   |
| Reproducing the same type of feature | Exploratory development |

---

## The Three Prompt Files

### spec-plan.prompt.md

```markdown
---
mode: ask
description: "Validate and plan a feature from SPEC.md"
---

# Spec Planning

Read #file:SPEC.md and perform the following checks:

## 1. Spec Completeness

Check if all sections are present and complete:

- [ ] User Story (role, action, benefit)
- [ ] Data Model (fields, types, defaults)
- [ ] UI description
- [ ] Routes (method, path, behavior)
- [ ] Acceptance criteria (specific, testable)
- [ ] Out of scope defined

## 2. Identify Questions

List all questions that need to be answered before implementation:

- Unclear requirements
- Missing edge cases
- Undefined behavior for error scenarios

## 3. Implementation Plan

Create a step-by-step implementation plan:

1. Data model change
2. Backend route
3. Template/UI
4. Validation
5. Tests

## 4. Risk Assessment

Which parts of the spec could be problematic?

- Backwards compatibility
- Performance
- Security
```

---

### spec-build.prompt.md

```markdown
---
mode: agent
description: "Implement feature from SPEC.md step by step"
tools:
  - codebase
  - terminal
---

# Feature Implementation

Read #file:SPEC.md and implement the feature step by step.

## Step 1: Data Model

Extend todos.json structure per the spec.
Ensure backward compatibility (existing todos without new field must still work).

## Step 2: Backend

Implement all routes listed in the spec.
Follow existing code conventions (func\_ prefix, PRG pattern).

## Step 3: Frontend

Update templates to show the new fields/functionality.
Use existing Tailwind classes for consistent styling.

## Step 4: Validation

Add input validation for all new form fields.
Error messages via flash().

## Step 5: Tests

After each step, check: `python -m pytest -v`
Fix all test failures before moving to the next step.

## Final Report

✅ Implemented:

- [list of completed acceptance criteria]

❌ Not implemented (with reasons):

- [list of missing criteria]
```

---

### spec-test.prompt.md

```markdown
---
mode: agent
description: "Generate tests from SPEC.md acceptance criteria"
tools:
  - codebase
  - terminal
---

# Test Generation from Spec

Read #file:SPEC.md and generate tests for all acceptance criteria.

## Rules

1. Each acceptance criterion → at least 1 test
2. Test naming: test*{criterion}*{condition}\_{expected}
3. Happy path + error cases for each criterion
4. Tests must be independent (no shared state)
5. Mock all external dependencies

## Process

1. Read the acceptance criteria from the spec
2. For each criterion:
   - Write a test description
   - Implement the test
   - Run the test: `python -m pytest test_app.py -v -k "new_test_name"`
3. Fix failing tests
4. Show final coverage of all criteria

## Output

Show a table at the end:
| Criterion | Test name | Status |
| --------- | --------- | ------ |
| ... | ... | ✅/❌ |
```

---

## SPEC.md – Structure Example

```markdown
# Feature: [Name]

## User Story

As a [role], I want [action], so that [benefit].

## Data Model

| Field    | Type   | Default | Required |
| -------- | ------ | ------- | -------- |
| due_date | string | null    | No       |

## UI

[Description of the interface]

## Routes

| Method | Path | Action          |
| ------ | ---- | --------------- |
| POST   | /add | Save with field |

## Acceptance Criteria

- [ ] Criterion 1: [specific + measurable]
- [ ] Criterion 2: [specific + measurable]

## Out of Scope

- [What intentionally is not included]
```
