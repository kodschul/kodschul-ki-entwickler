## Context

Task-Pro is a new application with no existing code. This design establishes the foundational architecture for the todo feature, which is the core user-facing capability.

## Goals / Non-Goals

**Goals:**
- Define the data model for a todo item
- Establish UI interaction pattern for adding a todo (input + submit)
- Persist todos in component state (or localStorage for durability across refreshes)

**Non-Goals:**
- Editing or deleting todos (separate features)
- Backend/API integration — local state only for now
- User authentication or multi-user support

## Decisions

**Framework: React with TypeScript**
- Standard choice for interactive UI; TypeScript prevents runtime type errors on the data model.

**State: useState hook (component-local)**
- Simplest approach for a single-feature MVP; avoids premature introduction of a global store (Redux, Zustand) before it's needed.

**Persistence: localStorage**
- Zero-dependency durability; todos survive page refresh without a backend.
- Alternative (in-memory only) rejected — loses data on refresh, poor UX.

**Todo ID: `crypto.randomUUID()`**
- Collision-free, no library needed, supported in all modern browsers.

**Data model:**
```ts
interface Todo {
  id: string;
  title: string;
  completed: boolean;
  createdAt: string; // ISO timestamp
}
```

## Risks / Trade-offs

- **localStorage size limit (~5 MB)** → Acceptable for a todo list; can add eviction logic later if needed.
- **No server sync** → Data is device-local; fine for MVP, revisit when multi-device support is needed.
