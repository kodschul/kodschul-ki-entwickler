# Exercise: Built-in Commands – TypeScript Angular

**Time:** 90 min | **Project:** Angular Todo App

---

## Task 1 – /explain with #sym (15 min)

Open Copilot Chat:

```
/explain #sym:funcLoadTodos
```

```
/explain #sym:funcSaveTodo
```

**Questions:**

- What edge cases exist?
- Where could errors occur?
- What happens if localStorage is unavailable?

---

## Task 2 – /fix with #terminalLastCommand (20 min)

Intentionally introduce a bug in `todo.service.ts`:

```typescript
// Remove null check
funcGetById(id: number): Todo {
  return this.todos.find(t => t.id === id)!; // ← possible undefined
}
```

Run in the terminal:

```bash
ng test --watch=false 2>&1 | tail -20
```

In Copilot Chat:

```
/fix #terminalLastCommand
```

**Observe:** Does Copilot suggest adding `| undefined` to the return type?

---

## Task 3 – /tests with settings.json (20 min)

First configure `.vscode/settings.json`:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Use Angular TestBed with Jasmine. Always generate: 1 happy path test, 1 empty input test, 1 edge case test. Test names in the format 'should [expectation] when [condition]'."
    }
  ]
}
```

Then:

```
/tests #sym:funcValidateTodo
```

**Observe:**

- Are the tests using Jasmine `describe/it` correctly?
- Does TestBed get set up properly?
- Would they actually pass?

---

## Task 4 – /doc with JSDoc (15 min)

```
/doc #sym:funcLoadTodos
Use JSDoc with @param, @returns, and @throws annotations.
```

**Check:**

- Are the TypeScript types correct?
- Are return values documented?
- Are exceptions mentioned?

---

## Task 5 – /new (20 min)

**Subtask A – New Angular Service:**

```
/new Angular service TodoFilterService with methods:
filterByStatus(todos, showCompleted), filterByDueDate(todos, date), sortByPriority(todos).
All methods pure (no side effects), typed with the Todo interface.
```

**Subtask B – GitHub Actions:**

```
/new GitHub Actions workflow that runs ng test --watch=false on every push to main.
Node.js 20, install dependencies, fail on test error.
```

---

## Task 6 – Right-Click Review (10 min)

1. Select `funcAddTodo()` in `todo.service.ts`
2. Right-click → Copilot → **Review and Comment**
3. Observe the inline comments
4. Select all of `todo.service.ts`
5. Right-click → Copilot → **Review and Comment**

**Question:** What does Copilot flag?
