## Why

Rescheduling several todos one at a time — opening the edit form and re-picking a date for each — is tedious when a user wants to defer a batch of them (e.g. at the end of a week, pushing everything not done to next week). A bulk action lets them select several todos and move them all at once.

## What Changes

- Each todo row gains a checkbox for bulk selection.
- A new "Push to next week" button (part of a form wrapping the todo list) submits the selected todo ids.
- A new `POST /push-week` route adds 7 days to the `due_date` of every selected todo, leaving unselected todos untouched, then redirects back to `/`.
- No selection is made by default; submitting with no todo selected is a no-op.

## Capabilities

### New Capabilities
- `bulk-reschedule`: Selecting multiple todos and shifting their due dates forward by one week in a single action.

### Modified Capabilities
(none — this reuses the existing `due_date` field defined by `due-dates`; it does not change that capability's requirements, only adds a new way to update the field)

## Impact

- `app.py`: new `POST /push-week` route; reads a list of selected todo ids from the form body, shifts each matching todo's `due_date` by 7 days (`date.fromisoformat(...) + timedelta(days=7)`), writes `todos.json`, redirects to `/`.
- `templates/index.html`: each todo row gains a `<input type="checkbox" name="ids" value="{{ todo.id }}">`; the todo list is wrapped in a `<form action="/push-week" method="post">` with a "Push to next week" submit button. Individual per-row Edit/Delete forms remain separate, unchanged forms nested appropriately (see design.md for how overlapping forms are handled, since HTML forms cannot nest).
- No changes to `todos.json` schema (still just shifts the existing `due_date` string), no new dependencies.
