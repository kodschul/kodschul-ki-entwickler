## Why

Task-Pro needs a core capability to let users create todos. Without the ability to add a todo, the application has no primary function — this is the foundational feature that everything else builds on.

## What Changes

- Introduce a form or input field for entering a new todo title
- On submission, the new todo is added to a displayed list
- Each todo is persisted in application state (in-memory or localStorage)
- A todo has at minimum: an id, title, and completed status

## Capabilities

### New Capabilities

- `add-todo`: Allows a user to type a todo title and submit it, creating a new todo entry in the list

### Modified Capabilities

<!-- None — this is the initial capability being introduced -->

## Impact

- New UI component: todo input form
- New state management: todo list stored in component state or a store
- New data model: `Todo` type with `id`, `title`, `completed`
