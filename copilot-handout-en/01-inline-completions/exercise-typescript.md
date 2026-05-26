# Exercise: Inline Completions – TypeScript Angular

**Time:** 90 min | **Project:** Angular Todo App

---

## Project Setup

```bash
ng new todo-app-angular --standalone --routing --style=css
cd todo-app-angular
ng generate service services/todo
ng generate component components/todo-list
ng generate component components/todo-form
ng generate interface models/todo
```

---

## Task 1 – Learn the Shortcuts (20 min)

Open `src/app/services/todo.service.ts`. Write at the end:

```typescript
// Returns all todos that are due today
funcGetDueToday(todos: Todo[]): Todo[] {
```

**Try it out:**

1. Wait for Ghost Text
2. `⌥ ]` / `Alt ]` – next suggestion
3. `⌥ [` / `Alt [` – previous suggestion
4. `⌥ Enter` / `Alt Enter` – all suggestions in panel
5. `⌘ →` / `Ctrl →` – accept word by word

**Questions:**

- How many different suggestions does Copilot offer?
- Does Copilot use `Date` correctly for the comparison?

---

## Task 2 – Control Context with Comments (20 min)

Write three variants in `todo.service.ts` and observe how the comment changes the suggestion:

**Variant A – no comment:**

```typescript
funcValidateTodo(title: string): boolean {
  |
}
```

**Variant B – short comment:**

```typescript
// Validates the todo title
funcValidateTodo(title: string): boolean {
  |
}
```

**Variant C – precise comment:**

```typescript
// Validates the todo title: not empty, max 200 characters.
// Returns { valid: true } on success or { valid: false, error: string } on failure.
funcValidateTodo(title: string): { valid: boolean; error?: string } {
  |
}
```

**Observe:** How do the return types in the suggestions differ?

---

## Task 3 – JSDoc-First (20 min)

Write the JSDoc first, then let Copilot generate the implementation:

```typescript
/**
 * Formats an ISO date string (YYYY-MM-DD) for display in the UI.
 *
 * - Returns 'No date' if dueDateStr is empty or null
 * - Returns 'Overdue' if the date is in the past
 * - Otherwise returns 'Due on DD.MM.YYYY'
 *
 * @param dueDateStr - ISO date string or null
 * @returns Formatted string for display
 */
funcFormatDueDate(dueDateStr: string | null): string {
  |
}
```

Accept the suggestion. Then write a test:

```typescript
describe('funcFormatDueDate', () => {
  it('should return |  // Copilot derives tests from the JSDoc
```

---

## Task 4 – Next Edit Suggestion (15 min)

1. Open `src/app/models/todo.model.ts`
2. Add a new required field: `priority: 'low' | 'medium' | 'high'`
3. Observe: Does Copilot suggest updating all places where `Todo` is used?
4. Press `Tab` to accept each suggestion

**Alternatively:**

```typescript
// todo.model.ts – before the change:
export interface Todo {
  id: number;
  title: string;
  completed: boolean;
  dueDate: string | null;
}

// Change to:
export interface Todo {
  id: number;
  title: string;
  completed: boolean;
  dueDate: string | null;
  priority: "low" | "medium" | "high"; // ← NEW
}
```

**Observe:** Does Copilot suggest updates in `todo.service.ts` and `todo-form.component.ts`?

---

## Task 5 – Copilot vs. Manual Implementation (15 min)

Implement the function manually:

```typescript
funcFilterByStatus(todos: Todo[], showCompleted: boolean): Todo[] {
  // Manual: return todos filtered by completed status
}
```

Delete the implementation. Write only the comment and let Copilot suggest.

**Comparison:**

- Is Copilot's suggestion more idiomatic (e.g. does it use `filter()`)?
- Does it use the `showCompleted` parameter sensibly?
