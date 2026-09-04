## Context

`GET /` (`app.py:index`) already loads `todos.json` and computes an `overdue` flag per todo before rendering `templates/index.html`. CLAUDE.md forbids JavaScript fetch calls, a REST/JSON layer for the UI, and a database — the popup has to be plain server-rendered HTML, computed fresh on every request, with no dismissal state persisted anywhere. See proposal.md - Why.

## Goals / Non-Goals

**Goals:**
- Show a native, dismissible popup on `GET /` when incomplete todos are due today.
- Keep all logic in `app.py` and `templates/index.html`, no new files or routes.

**Non-Goals:**
- Remembering that the user dismissed the popup across reloads (explicitly out of scope per spec's "No JavaScript or persisted dismissal state" requirement).
- Notifying about upcoming (not-yet-due) or overdue-from-the-past todos — that's the existing `overdue` styling, unchanged by this design.

## Decisions

- **Use the native `<dialog open>` element, closed via `<form method="dialog">`.** The HTML `<dialog>` element supports a submit button with `method="dialog"` that closes the dialog using built-in browser behavior — no `<script>` tag required. This satisfies the "no JavaScript" constraint while still giving an actual modal popup (browser-native backdrop, focus handling) rather than an inline banner.
  - Alternative considered: a plain `<div>` banner at the top of the page. Rejected because the request specifically asks for a "popup," and a banner can't be dismissed without JS or a server round-trip.
  - Alternative considered: CSS `:target` show/hide trick. Rejected as more fragile and less semantic than `<dialog>`, which is purpose-built for this.
- **Compute `due_today` in `index()` alongside the existing `overdue` computation.** Same loop, same pattern already used for `overdue`, so no new helper function is needed:
  ```python
  today = date.today().isoformat()
  due_today = [t for t in todos if t["due_date"] == today and not t["done"]]
  ```
- **Render unconditionally in the template, gated by `{% if due_today %}`.** No query param, no session, no cookie — matches the "no persisted dismissal state" requirement and keeps the app database-free.

## Risks / Trade-offs

- [Popup reappears every time the page is reloaded, even seconds after dismissal] → Accepted by design; the spec explicitly calls for this (no persistence), and it's consistent with the app's stateless, full-page-reload model.
- [`<dialog>` `open` attribute support requires a reasonably modern browser] → Acceptable for a learning project; no polyfill needed since CLAUDE.md forbids adding JS anyway.
