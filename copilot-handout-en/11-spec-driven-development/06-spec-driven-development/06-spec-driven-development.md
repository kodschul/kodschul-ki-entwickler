# 06 – Spec-Driven Development

**Block:** 90 min | **Day 3**

---

## How does Spec-Driven Development work?

Instead of asking Copilot "just implement something", you first write a structured specification – then let Copilot implement it step by step.

```
1. Write SPEC.md (human → structure)
2. /spec-plan  (Copilot → validates plan, identifies questions)
3. /spec-build (Copilot → implements feature step by step)
4. /spec-test  (Copilot → generates tests from spec)
5. Review & Accept
```

---

## Why / When not?

| Why use it                               | When not to                     |
| ---------------------------------------- | ------------------------------- |
| New feature with multiple components     | Small, isolated change          |
| Multiple people work on the same feature | Quick fix or bugfix             |
| Complex business logic                   | One-liners or trivial functions |
| Important decision trail needed          | Prototyping / throwaway code    |

---

## Spec Template

```markdown
# Feature: [Name]

## User Story

As a [role], I want [action], so that [benefit].

## Data Model

[Which fields are added/changed?]
[What does the data structure look like?]

## UI

[What does the user interface look like?]
[Which routes are affected?]

## Routes

| Method | Path       | Action       |
| ------ | ---------- | ------------ |
| GET    | /todos     | Show list    |
| POST   | /todos/add | Add new todo |

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Out of Scope

[What intentionally is NOT included in this feature?]
```

---

## Plan → Implement → Test Workflow

### Step 1 – Write spec

```markdown
# Feature: Due Dates

## User Story

As a user, I want to set due dates for my todos so I can prioritize my tasks.

## Data Model

todos.json entry extended with:

- due_date: string (ISO 8601: YYYY-MM-DD) or null

## UI

- Input field "Due by" in the Add Todo form (type="date")
- Display in the todo list: "Due on DD.MM.YYYY" or "Overdue" in red

## Routes

| Method | Path  | Change                       |
| ------ | ----- | ---------------------------- |
| GET    | /     | Render due_date in the list  |
| POST   | /add  | Accept due_date from form    |
| POST   | /edit | Accept due_date in edit form |

## Acceptance Criteria

- [ ] User can set a due_date when creating
- [ ] Due dates are shown in the list in DD.MM.YYYY format
- [ ] Overdue todos are shown in red
- [ ] todos without due_date show nothing
- [ ] Tests: add_with_due_date, display_formatting, overdue_detection
```

### Step 2 – /spec-plan

```
/spec-plan #file:SPEC.md
```

Copilot validates: Is the spec complete? Are there missing edge cases?

### Step 3 – /spec-build

```
/spec-build #file:SPEC.md
```

Copilot implements step by step: Model → Route → Template → Tests.

### Step 4 – /spec-test

```
/spec-test #file:SPEC.md
```

Copilot generates tests based on the acceptance criteria.

---

## Automating with a Custom Prompt

**`spec-feature.prompt.md`:**

```markdown
---
mode: agent
description: "Plan, build, and test a new feature from a spec"
tools:
  - codebase
  - terminal
---

# Feature Implementation from Spec

1. Read #file:SPEC.md and validate the spec:

   - Are all acceptance criteria specific enough?
   - Are edge cases defined?
   - Is the data model complete?

2. Implement the feature step by step:

   - Data model changes
   - Backend routes
   - Frontend templates
   - Input validation

3. Generate tests for all acceptance criteria.

4. Run: `python -m pytest -v`
5. Fix failing tests.

Report at the end: which criteria are ✅ done and which ❌ are missing.
```

---

## Folder Structure

```
project/
├── SPEC.md                    ← The current specification
├── specs/
│   ├── due-dates.md           ← Archived specs
│   └── priority.md
└── .github/
    └── prompts/
        ├── spec-plan.prompt.md
        ├── spec-build.prompt.md
        └── spec-test.prompt.md
```

---

## # Reference Syntax in Prompts

| Syntax             | Effect                       |
| ------------------ | ---------------------------- |
| `#file:SPEC.md`    | Includes the spec as context |
| `#sym:funcName`    | Includes a specific function |
| `${input:feature}` | Asks for input when calling  |
| `#codebase`        | Searches the entire codebase |
