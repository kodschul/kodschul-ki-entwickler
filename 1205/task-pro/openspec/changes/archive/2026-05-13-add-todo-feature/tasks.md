## 1. Project Setup

- [x] 1.1 Initialize a React + TypeScript project (e.g., `npm create vite@latest task-pro -- --template react-ts`)
- [x] 1.2 Remove Vite boilerplate (default styles, App.tsx placeholder content)

## 2. Data Model

- [x] 2.1 Define the `Todo` interface (`id`, `title`, `completed`, `createdAt`) in `src/types/todo.ts`

## 3. State & Persistence

- [x] 3.1 Create a `useTodos` custom hook in `src/hooks/useTodos.ts` that initializes state from localStorage
- [x] 3.2 Implement `addTodo(title: string)` in the hook — generates a UUID, creates the todo, prepends it to the list, and writes to localStorage

## 4. UI Components

- [x] 4.1 Create `TodoInput` component (`src/components/TodoInput.tsx`) with a controlled text input and submit button
- [x] 4.2 Implement empty-title guard in `TodoInput` — do not call `addTodo` if title is blank/whitespace
- [x] 4.3 Clear and focus the input after a successful submission
- [x] 4.4 Create `TodoList` component (`src/components/TodoList.tsx`) that renders the list of todos

## 5. Wiring

- [x] 5.1 Integrate `useTodos`, `TodoInput`, and `TodoList` in `App.tsx`
- [ ] 5.2 Verify end-to-end: add a todo, reload the page, confirm it persists
