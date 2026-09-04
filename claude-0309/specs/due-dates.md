# Feature: Due dates

## User Story

As a user, I want to set and edit a due date on my todos, so that I know when something needs to get done and can see at a glance what's overdue.

## Data model

`todos.json` — existing JSON array, each todo gains a `due_date` field:

```json
[
  { "id": "3f2a1b", "text": "Buy milk", "done": false, "due_date": "2026-09-10" }
]
```

- `due_date`: string, ISO format `YYYY-MM-DD` (matches HTML `<input type="date">` output). **Required** — every todo must have one.

## Routes (Flask, `app.py`)

- `GET /` — unchanged behavior, but now also computes an `overdue` flag per todo (`due_date < today and not done`) and passes it to the template. Supports an optional `?edit=<id>` query param: when present and matching a todo, that todo is rendered in edit mode instead of view mode.
- `POST /add` — reads `text` and `due_date` from the form body. Both required (non-empty after trim for `text`; non-empty for `due_date`). Skips creation if either is missing. Appends `{"id": ..., "text": ..., "done": False, "due_date": ...}`, writes `todos.json`, redirects to `/`.
- `POST /edit/<id>` *(new)* — reads `text` and `due_date` from the form body. Both required, same validation as add. Finds the todo by `id`, updates its `text` and `due_date` in place, writes `todos.json`, redirects to `/`. If `id` doesn't exist, no-op redirect to `/`.
- `POST /delete/<id>` — unchanged.

All logic stays in `app.py`. No REST API, no JSON responses, no JS — plain HTML forms with full page reloads and query-param-driven edit mode, per CLAUDE.md.

## UI requirements (`templates/index.html`, Tailwind via CDN)

- Add form gains a required `<input type="date" name="due_date" required>` next to the text input.
- Each todo row shows its due date next to its text.
- Rows where `overdue` is true get a visual cue — e.g. red border/text (`border-red-300`, `text-red-600`) — applied only when not done.
- Each row gets an "Edit" link (`<a href="{{ url_for('index') }}?edit={{ todo.id }}">`) alongside "Delete".
- When a row's `id` matches the `edit` query param, that row renders as a form instead: text input (pre-filled), date input (pre-filled), "Save" button posting to `/edit/<id>`, and a "Cancel" link back to `/` (no query param).
- Empty state and overall layout otherwise unchanged.

## Implementation steps

1. Update `templates/index.html`: add due-date input to the add form.
2. Update `app.py` `/add`: require and store `due_date`.
3. Add `/edit/<id>` route in `app.py`.
4. Update `GET /` in `app.py`: compute `overdue` per todo and read `edit` query param, pass both to template.
5. Update `templates/index.html`: render due date + overdue styling in view mode; render inline edit form when row matches `edit` param.
6. Manual test pass (add with due date, edit text/date, overdue styling, delete unaffected).
7. Document completion in this spec.

No timeline needed — single-session implementation.

## Acceptance criteria

1. Adding a todo without a due date does not create it (form requires the field; server also rejects empty).
2. Adding a todo with text + due date creates it and both fields appear in the list.
3. Clicking "Edit" on a todo shows an inline form pre-filled with its current text and due date.
4. Saving an edit updates the todo's text and due date, persists to `todos.json`, and returns to view mode.
5. Clicking "Cancel" while editing discards no data and returns to view mode.
6. A todo whose due date is in the past and is not done is visually marked overdue.
7. A todo whose due date is in the past but is done is not marked overdue.
8. Editing a non-existent id (stale link) does not error — redirects to `/` with the list unchanged.

## Implementation status: Done

Implemented as designed:

- `app.py`: `/add` now requires and stores `due_date`; new `POST /edit/<id>` route updates `text`/`due_date`; `GET /` computes `overdue` (`due_date < today and not done`) per todo and reads the `edit` query param.
- `templates/index.html`: add form gained a required date input; each row shows its due date (red + bold when overdue) and an "Edit" link; the row matching `?edit=<id>` renders an inline pre-filled edit form (Save/Cancel) instead of the view row.
- `test_app.py`: existing add/delete tests updated to pass `due_date`; added tests for missing due date, edit (success + nonexistent id), and overdue flag (shown when past-due and not done, hidden when done). All 11 tests pass.
- Manually smoke-tested via the running dev server (add overdue + future todo, edit form pre-fill and save, stale-id edit no-op, delete) — verified via `curl` against `/`, `/add`, `/edit/<id>`, `/delete/<id>` and inspecting `todos.json`.
