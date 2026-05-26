# Exercise: Chat & Context Variables – TypeScript Angular

**Time:** 90 min | **Project:** Angular Todo App

---

## Task 1 – Explore Context Variables (20 min)

Open Copilot Chat. Try the following prompts and observe the quality of responses:

**Without context:**

```
Explain how the todos are stored.
```

**With #file:**

```
Explain how the todos are stored. #file:src/app/services/todo.service.ts
```

**With #sym:**

```
Explain #sym:funcLoadTodos and #sym:funcSaveTodo
```

**Compare:** How do the answers differ?

---

## Task 2 – Using @workspace (20 min)

```
@workspace Where are todos loaded and where are they saved?
```

```
@workspace Which Angular routes exist and which ones have unit tests?
```

```
@workspace Are there code duplicates between todo.service.ts and the components?
```

**Observe:** What does `@workspace` find that a normal prompt doesn't?

---

## Task 3 – Inline Chat (20 min)

1. Open `src/app/components/todo-form/todo-form.component.ts`
2. Select the `funcSubmit()` method
3. Press `⌘ I` / `Ctrl I`
4. Enter:

```
Add Reactive Forms validation: title must not be empty
and not longer than 200 characters. Show an error message below
the input field when validation fails.
```

5. Check the diff – are all changes in `.ts` and `.html` correct?
6. `⌘ Enter` to accept or `Esc` to reject

---

## Task 4 – #terminalLastCommand (15 min)

```bash
# Run in terminal:
ng test --watch=false --browsers=ChromeHeadless
```

If tests fail → in Copilot Chat:

```
#terminalLastCommand
Why is this test failing? How do I fix it?
```

If all tests pass → intentionally break one test:

```typescript
// todo.service.spec.ts – temporarily change:
it("should load todos", () => {
  expect(true).toBe(false); // Intentional failure
});
```

---

## Task 5 – #changes for Code Review (15 min)

Add a new field in `src/app/models/todo.model.ts`:

```typescript
export interface Todo {
  id: number;
  title: string;
  completed: boolean;
  dueDate: string | null;
  tags?: string[]; // ← NEW
}
```

Then in Copilot Chat:

```
Do a brief code review of my changes. #changes
Are all places that use Todo updated?
```

---

## Task 6 – Edit Mode vs. Ask Mode (15 min)

**Ask Mode:**

```
How do I implement a DarkMode toggle in Angular without an external library?
```

**Edit Mode** (open todo-list.component.ts, then select Edit mode):

```
Add a toggle button that shows and hides completed todos.
Use a local boolean signal: showCompleted.
```

**Observe:**

- Ask mode: explains, does not write code directly into the file
- Edit mode: directly changes the selected files
