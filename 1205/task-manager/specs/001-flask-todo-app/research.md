# Research: Flask Todo App

**Date**: 2026-05-13

---

## Decision 1: Web Framework

**Decision**: Flask 3.x

**Rationale**: User specified Flask explicitly. Flask is minimal, well-documented, and ideal for simple CRUD web apps. Jinja2 templating is built-in.

**Alternatives considered**: Django (too heavy for a single-model app), FastAPI (API-first, not ideal for server-rendered HTML).

---

## Decision 2: CSS Approach

**Decision**: Tailwind CSS via CDN (Play CDN for development)

**Rationale**: User specified Tailwind CSS. Using the CDN avoids a Node.js build step, keeping the project pure Python. For production, the Tailwind CLI can generate a purged stylesheet.

**Alternatives considered**: Custom CSS (more work, less consistent), Bootstrap (not requested).

---

## Decision 3: Database / Persistence

**Decision**: SQLite via Flask-SQLAlchemy

**Rationale**: The spec requires persistence across page reloads. SQLite is zero-config, file-based, and ships with Python. SQLAlchemy provides a clean ORM that makes model definition and querying straightforward.

**Alternatives considered**:
- Raw SQLite (`sqlite3` module): More verbose, no ORM benefits
- PostgreSQL: Overkill for a single-user app
- File-based JSON: No query support, fragile on concurrent writes

---

## Decision 4: Rendering Strategy

**Decision**: Server-side rendering with Jinja2; form submissions via standard HTML POST

**Rationale**: Keeps the stack simple (no JavaScript framework, no REST API). Each form action posts to a Flask route which redirects (PRG pattern — Post/Redirect/Get) to prevent duplicate submissions on refresh.

**Alternatives considered**: React/Vue SPA + REST API (over-engineered for this scope), HTMX (lighter than a SPA but adds a dependency not requested by user).

---

## Decision 5: Testing Strategy

**Decision**: pytest + pytest-flask with an in-memory SQLite database for tests

**Rationale**: pytest is the de-facto standard for Python. pytest-flask provides a test client fixture. Using an in-memory SQLite database for tests ensures isolation and speed.

**Alternatives considered**: unittest (more verbose), no tests (violates quality standards).

---

## Resolved Clarifications

All spec clarifications resolved via reasonable defaults:

| Topic | Resolution |
|-------|------------|
| Task name max length | 200 characters (FR-008) — enforced at model + form level |
| Whitespace-only names | Stripped and rejected server-side |
| Empty state | Simple centered message: "No tasks yet. Add one above!" |
| Completion toggle | Checkbox per task; POST to `/tasks/<id>/toggle` |
| Delete confirmation | No modal — single click delete (simple scope) |
