## Why

Todos due today are only visible by scanning the full list and checking each due date, so a user can open the board and easily miss something due right now. A notification shown when the board opens surfaces today's due items immediately, without requiring the user to hunt for them.

## What Changes

- When `GET /` is requested and one or more incomplete todos have `due_date` equal to today, the page opens with a popup notification listing those todos.
- The popup is native HTML (a `<dialog open>` element with a `<form method="dialog">` close button) — no JavaScript, consistent with the project's full-page-reload design.
- The popup does not appear when there are no todos due today, or when all of today's due todos are already done.
- No new route, no persisted "dismissed" state — the popup is computed fresh from `todos.json` on every page load, per CLAUDE.md's no-database/no-JS constraints.

## Capabilities

### New Capabilities
- `due-today-notification`: Computing which incomplete todos are due today and presenting them as a popup when the todo board loads.

### Modified Capabilities
(none — `due-dates` already defines `due_date` and `overdue`; this change only adds a new read-time view over existing data, it does not change `due-dates` requirements)

## Impact

- `app.py`: `GET /` (`index` view) gains a computed `due_today` list passed to the template, alongside the existing `overdue` computation.
- `templates/index.html`: gains a conditionally rendered `<dialog>` popup block.
- No changes to `todos.json` schema, no new dependencies, no new routes.
