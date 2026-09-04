## Context

`templates/index.html` currently renders each todo as an `<li>` containing, in view mode, an "Edit" link and a standalone `<form action="/delete/<id>" method="post">` for the delete button. `app.py` has three POST routes (`/add`, `/edit/<id>`, `/delete/<id>`), each reading fields with `request.form.get(...)`, loading/saving the whole `todos.json` array via `load_todos`/`save_todos`. See proposal.md - Why for the motivation.

HTML forms cannot be nested, so a bulk-selection `<form>` wrapping the entire `<li>` list would conflict with each row's existing per-row delete `<form>`. This needs a design decision (below), not just an implementation detail, since it shapes the template structure other tasks build on.

## Goals / Non-Goals

**Goals:**
- Let a user check any subset of todos and push all of their due dates forward by 7 days in one submit, without JavaScript.
- Keep every existing route (`/add`, `/edit/<id>`, `/delete/<id>`) and its current form untouched.

**Non-Goals:**
- Persisting the checkbox selection across page reloads (it's a single in-page action, not saved state).
- Any other bulk action (bulk delete, bulk mark-done) — only rescheduling, per the proposal.

## Decisions

- **Use the HTML5 `form="<id>"` attribute on each checkbox instead of wrapping the list in a `<form>`.** Declare one empty-bodied `<form id="push-week-form" action="/push-week" method="post">` (holding just the submit button) placed above the todo list, and give each row's checkbox `<input type="checkbox" name="ids" value="{{ todo.id }}" form="push-week-form">`. The `form` attribute associates a control with a form anywhere in the document, so the checkboxes can live inside each `<li>` — alongside the existing standalone delete `<form>` — without nesting any `<form>` inside another. This is plain HTML, not JavaScript, so it fits CLAUDE.md's constraints.
  - Alternative considered: wrap the whole `<ul>` in the bulk form and move the delete button's action to a per-button `formaction`/`formmethod` override. Rejected — mixing two different submit targets (`/delete/<id>` vs `/push-week`) inside one form via `formaction` on buttons works but is harder to read and riskier to get right in a beginner-friendly codebase than the `form=` attribute approach.
- **New dedicated route `POST /push-week`,** not a reuse of `/edit/<id>` (which only updates one todo at a time and requires `text`). `/push-week` reads `request.form.getlist("ids")`, loads all todos, and for each todo whose `id` is in that list, sets `due_date = (date.fromisoformat(todo["due_date"]) + timedelta(days=7)).isoformat()`. Unmatched ids in the submitted list are simply ids with no corresponding todo in the loop — skipped implicitly.
- **7-day shift is relative to each todo's own current `due_date`**, not to today's date — per the user's explicit choice when this change was proposed (a todo due in 3 weeks moves to 3 weeks + 7 days, not to a fixed date next week).

## Risks / Trade-offs

- [A user selects todos, then the underlying data changes in another tab before they submit] → Accepted; this is a single-user learning app with no concurrency controls elsewhere (same as existing `/edit/<id>` and `/delete/<id>`).
- [`form="push-week-form"` is a valid but easy-to-miss HTML feature; a future contributor might not immediately see why checkboxes work despite being outside the `<form>` tag] → Mitigated by keeping the `<form id="push-week-form">` and its checkboxes visually adjacent in the template and documented in this design doc.
