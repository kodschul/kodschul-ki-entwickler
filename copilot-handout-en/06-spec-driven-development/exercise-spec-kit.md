# Exercise: Spec-Kit – Automated Spec Workflow

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Create the Three Spec-Kit Prompts (20 min)

```
Create three prompt files for the Spec-Kit:

1. .github/prompts/spec-plan.prompt.md
   - mode: ask
   - Validates SPEC.md for completeness
   - Lists open questions
   - Creates an implementation plan

2. .github/prompts/spec-build.prompt.md
   - mode: agent, tools: codebase, terminal
   - Implements the feature step by step (Model → Route → Template → Tests)
   - Runs pytest after each step
   - Reports which criteria are done (✅) or missing (❌)

3. .github/prompts/spec-test.prompt.md
   - mode: agent, tools: codebase, terminal
   - Generates one test per acceptance criterion
   - Names tests test_{criterion}_{condition}_{expected}
   - Creates a coverage table at the end

Use the SPEC.md from the previous exercise (Due Dates feature).
```

---

## Task 2 – Use /spec-plan (15 min)

Make sure `SPEC.md` is in the project root.

In Copilot Chat:

```
/spec-plan
```

**Observe:**

- Are open questions identified?
- Are missing acceptance criteria found?
- Is the implementation plan clear?

**Improve your SPEC.md** based on the feedback.

---

## Task 3 – Use /spec-build (25 min)

In Copilot Chat (Agent Mode):

```
/spec-build
```

**Observe the step-by-step process:**

1. Does Copilot start with the data model?
2. Are the routes implemented in the right order?
3. Does it run tests after each step?
4. Are all errors fixed before moving to the next step?

---

## Task 4 – Use /spec-test (15 min)

In Copilot Chat (Agent Mode):

```
/spec-test
```

**Check the coverage table:**

| Criterion | Test name | Status |
| --------- | --------- | ------ |
| ?         | ?         | ?      |

Are all acceptance criteria covered?

---

## Task 5 – Comparison: Manual vs. Spec-Kit (15 min)

Fill out this comparison table:

| Aspect                       | Manual (Task 1–4 from prev. exercise) | Spec-Kit (/spec-plan/build/test) |
| ---------------------------- | ------------------------------------- | --------------------------------- |
| Time to implement            |                                       |                                   |
| Quality of tests             |                                       |                                   |
| Coverage of criteria         |                                       |                                   |
| Effort for spec              |                                       |                                   |
| Documentation after the fact |                                       |                                   |
| Suitable for team work       |                                       |                                   |
