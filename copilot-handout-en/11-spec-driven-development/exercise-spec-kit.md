# Exercise: Spec-Kit – Plan, Build, Test

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create the Spec-Kit Prompts (15 min)

Create the folder `.github/prompts/` and set up the three prompt files:

**`spec-plan.prompt.md`** – validate spec and plan implementation  
**`spec-build.prompt.md`** – implement feature step by step  
**`spec-test.prompt.md`** – generate tests from acceptance criteria

Each file needs:

```markdown
---
mode: ask | agent
description: "..."
tools:
  - codebase
  - terminal
---
```

---

## Task 2 – /spec-plan (20 min)

Create `SPEC.md` for the priority feature:

```markdown
# Feature: Priority

## User Story

As a user, I want to prioritize my todos (High / Medium / Low)
so I can focus on the most important tasks.

## Data Model

todos.json entry extended with:
- priority: string ("high", "medium", "low"), default: "medium"

## UI

- Dropdown in the Add Todo form: High / Medium / Low
- Colored badge in the list: 🔴 High, 🟡 Medium, 🟢 Low

## Routes

| Method | Path  | Change                          |
| ------ | ----- | ------------------------------- |
| POST   | /add  | Accept priority from form       |
| POST   | /edit | Accept priority in edit form    |

## Acceptance Criteria

- [ ] User can set priority when creating
- [ ] Priority is shown as colored badge in the list
- [ ] Default priority is "medium"
- [ ] Invalid values are rejected
- [ ] Tests for: add_with_priority, default_priority, invalid_priority

## Out of Scope

- Sorting by priority (separate feature)
- Priority change without editing
```

Run:

```
/spec-plan #file:SPEC.md
```

**Question:** What gaps or questions does Copilot identify?

---

## Task 3 – /spec-build (25 min)

Run after completing the spec:

```
/spec-build #file:SPEC.md
```

Observe:
- Does Copilot go step by step?
- Does it run tests after each step?
- Are all acceptance criteria covered?

---

## Task 4 – /spec-test (20 min)

```
/spec-test #file:SPEC.md
```

Check:
- Is every acceptance criterion covered by a test?
- Do edge cases have their own tests?
- Are the test names clear?

Run: `python -m pytest test_app.py -v`

---

## Task 5 – Comparison: Spec-Kit vs. Manual (10 min)

Fill in the comparison table:

| Aspect              | Without Spec-Kit            | With Spec-Kit              |
| ------------------- | --------------------------- | -------------------------- |
| Context quality     |                             |                            |
| Number of questions |                             |                            |
| Test coverage       |                             |                            |
| Reproducibility     |                             |                            |
| Time invested       |                             |                            |

**When would you use Spec-Kit in your projects?**
