# Exercise: Spec-Driven Development

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Write a Spec for the Due-Dates Feature (20 min)

Create `SPEC.md` in the project root:

```
Create a SPEC.md for the "Due Dates" feature of our Flask Todo App.

The feature:
- Users should be able to set a due date when creating/editing a todo
- Due dates are displayed in the list as "Due on DD.MM.YYYY"
- Overdue todos (due_date < today) are shown in red
- Todos without due_date show nothing

Include in the spec:
1. User Story
2. Data model change (what changes in todos.json)
3. UI description (what the user sees)
4. Routes table (which routes are extended)
5. 5 specific, testable acceptance criteria
6. Out of Scope section

Keep the spec concrete and measurable – avoid vague criteria like "looks good".
```

---

## Task 2 – Implement the Feature (30 min)

Use the Copilot Chat in **Agent Mode**:

```
Implement the feature described in #file:SPEC.md.

Step 1: Extend todos.json structure (add due_date: null as default)
Step 2: Update /add route to accept due_date from form
Step 3: Update index.html – add date input to form
Step 4: Show due_date in todo list with appropriate formatting
Step 5: Highlight overdue todos in red

After each step, run: python -m pytest test_app.py -v
```

---

## Task 3 – Write Tests (20 min)

```
Generate tests for all acceptance criteria from #file:SPEC.md.

For each criterion:
1. One test for the happy path
2. One test for the edge case
3. Name format: test_{criterion}_{condition}_{expected}

Save the tests in test_app.py.
Run: python -m pytest test_app.py -v
```

---

## Task 4 – Compare Spec vs. Implementation (20 min)

```
Review #file:SPEC.md and check the current implementation.
Are all acceptance criteria met?

Show me a table:
| Criterion | Implemented? | Notes |
| --------- | ------------ | ----- |
```

---

## Checklist – Spec-Driven Development

```
Before starting:
□ SPEC.md is complete (User Story, Data Model, UI, Routes, Criteria)
□ Acceptance criteria are specific and testable
□ Out of Scope is defined

During implementation:
□ After each step: run tests
□ No step skipped
□ Backwards compatibility ensured

After completion:
□ All acceptance criteria are met
□ All tests pass
□ Spec serves as documentation
```
