# Feature: Create and delete todos

## User Story

As a user, I want to add a new todo and delete an existing todo, so that I can keep a simple running list of things to do.

## Data model

`todos.json` — a JSON array of todo objects, stored at the repo root:

```json
[
  { "id": "3f2a1b", "text": "Buy milk", "done": false }
]
```

- `id`: string, generated with `uuid.uuid4().hex[:6]` (short, unique, URL-safe)
- `text`: string, the todo's content (required, non-empty after trimming)
- `done`: boolean, defaults to `false` (reserved for a future toggle feature; not editable by this feature)

If `todos.json` does not exist, treat it as an empty list (create it on first write).

## Routes (Flask, `app.py`)

- `GET /` — reads `todos.json`, renders `index.html` with the list of todos and a form to add a new one.
- `POST /add` — reads `text` from the form body, trims it, appends a new todo (skips if empty after trim), writes `todos.json`, then redirects to `/` (PRG pattern).
- `POST /delete/<id>` — removes the todo with matching `id` from the list, writes `todos.json`, then redirects to `/` (PRG pattern).

All logic stays in `app.py`. No REST API, no JSON responses, no JS — plain HTML forms with full page reloads, per CLAUDE.md.

## UI requirements (`templates/index.html`, Tailwind via CDN)

- A text input + "Add" submit button, posting to `/add`.
- A list of existing todos, each showing its text and a "Delete" button that posts to `/delete/<id>`.
- Empty state message ("No todos yet") when the list is empty.
- Minimal, clean styling using Tailwind utility classes — no custom CSS files.

## Acceptance criteria

1. Submitting the add form with non-empty text creates a new todo, redirects to `/`, and the new todo appears in the list.
2. Submitting the add form with blank/whitespace-only text does not create a todo.
3. Clicking "Delete" on a todo removes it from `todos.json` and it no longer appears on the page after redirect.
4. Restarting the Flask dev server preserves todos (they persist in `todos.json` across restarts).
5. Deleting a non-existent id (e.g. stale link, double-submit) does not error — it redirects to `/` with the list unchanged.
