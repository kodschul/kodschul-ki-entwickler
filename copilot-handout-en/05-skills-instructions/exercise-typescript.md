# Exercise: Skills & .instructions.md – TypeScript Angular

**Time:** 90 min | **Project:** Angular Todo App

---

## Task 1 – Create Angular Instructions (20 min)

Create `.github/instructions/angular.instructions.md`:

```
Create .github/instructions/angular.instructions.md for our Angular Todo App.

applyTo: **/*.ts

Rules:
- Angular 17+ Standalone Components (no NgModules)
- Use Angular Signals instead of BehaviorSubjects
- All Observables must be unsubscribed with takeUntilDestroyed()
- All public methods with explicit return types
- No "any" – use "unknown" or specific types
- Interfaces for all data models (no classes for pure data)

Keep it under 30 lines.
```

**Test:** Open `todo.service.ts` → ask Copilot to add a method.  
Does it automatically use Signals?

---

## Task 2 – Create Security Instructions (20 min)

Create `.github/instructions/security.instructions.md`:

```
Create .github/instructions/security.instructions.md.

applyTo: **  (all files)

Security rules:
- Never use eval() or Function()
- Sanitize all user inputs before processing
- No hardcoded API keys or tokens
- Use HttpClient with typed responses (no "any")
- Mark sensitive fields in interfaces
```

**Test:** Ask Copilot:

```
Generate a function that evaluates a user-entered expression.
```

Does Copilot warn against using `eval()`?

---

## Task 3 – Create Testing Instructions + settings.json (20 min)

Create `.github/instructions/testing.instructions.md`:

```
Create .github/instructions/testing.instructions.md.

applyTo: **/*.spec.ts

Rules:
- Angular TestBed with Jasmine
- Naming: 'should [expectation] when [condition]'
- At least 3 tests: happy path, invalid input, edge case
- Mock all HTTP calls with HttpClientTestingModule
- Test only public behavior, not private methods
- Always check for ngOnDestroy side effects
```

Add to `.vscode/settings.json`:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ]
}
```

---

## Task 4 – Understand applyTo Patterns (15 min)

Write a table that describes what each pattern matches:

| Pattern             | Which files match? |
| ------------------- | ------------------ |
| `**/*.ts`           |                    |
| `**/*.spec.ts`      |                    |
| `src/app/**`        |                    |
| `**/*.component.ts` |                    |
| `**/*.service.ts`   |                    |
| `**`                |                    |

Now create a `flask.instructions.md` → wrong project!  
**Question:** Why doesn't `applyTo: **` make sense for every instruction?

---

## Task 5 – Stack Instructions (15 min)

With all three instruction files active:

Open `todo.service.spec.ts` and ask:

```
Add tests for funcValidateTodo.
```

**Trace the stacking:**

```
Working on todo.service.spec.ts:
→ copilot-instructions.md         active? ___
→ angular.instructions.md         active? ___ (why?)
→ security.instructions.md        active? ___ (why?)
→ testing.instructions.md         active? ___ (why?)
```

**Check the generated tests:**

- Is TestBed set up correctly?
- Does the naming convention follow "should ... when ..."?
- Are there 3 test cases?
