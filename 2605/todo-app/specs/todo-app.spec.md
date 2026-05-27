# Spec: Simple Python Todo App with Flask

## Overview

A dead-simple todo app built with Python and Flask. No database — file storage only. UI is raw HTML in a single file following the KISS principle.

## Goals

- Scaffold a minimal Flask todo application
- Single-file approach (one `app.py`, everything in one place)
- Pure HTML UI, no JavaScript frameworks, no CSS frameworks

## Features

- View all todos
- Add a new todo
- Mark a todo as done
- Delete a todo

## Tech Stack

- Python 3.12+
- Flask (no DB, file storage only)
- Raw HTML + Tailwind CSS (via CDN)

## Constraints

- KISS principle — keep it as simple as possible
- Everything in one file
- PascalCase naming convention

## Out of Scope

- User authentication
- Database integration
- REST API / JSON endpoints
- JavaScript frameworks

## Notes

- Todos are persisted to a local JSON file
- Todo fields: `id`, `title`, `done`, `created_at`
- Storage file: `data/todos.json` (relative to app root)

---

## EXECUTION PLAN

### Step 1 — Project structure

Create the following layout inside `todo-app/`:

```
todo-app/
  app.py          ← single Flask app file (routes + HTML template)
  data/
    todos.json    ← persisted todo list (created on first run)
```

### Step 2 — Data layer (inside app.py)

Implement two helper functions:

- `LoadTodos()` — reads `data/todos.json`; returns `[]` if file does not exist
- `SaveTodos(todos)` — writes the list to `data/todos.json` (creates `data/` dir if needed)

Each todo is a dict with keys: `id` (int), `title` (str), `done` (bool), `created_at` (ISO-8601 string).

### Step 3 — Flask routes (inside app.py)

| Method | Path           | Action                                                          |
| ------ | -------------- | --------------------------------------------------------------- |
| GET    | `/`            | Load todos, render HTML page                                    |
| POST   | `/add`         | Read form field `title`, append new todo, save, redirect to `/` |
| POST   | `/done/<id>`   | Toggle `done` on matching todo, save, redirect to `/`           |
| POST   | `/delete/<id>` | Remove matching todo, save, redirect to `/`                     |

### Step 4 — HTML template (inline in app.py)

Render via `flask.render_template_string`. One page only:

- Load Tailwind CSS via CDN `<script src="https://cdn.tailwindcss.com"></script>`
- `<form>` to add a new todo (POST `/add`)
- `<ul>` listing all todos showing title, created date, done status
- Per-item forms for "Mark done / Undo" (POST `/done/<id>`) and "Delete" (POST `/delete/<id>`)
- Styled with Tailwind utility classes, no custom CSS

### Step 5 — Entry point

```python
if __name__ == "__main__":
    App.run(debug=True)
```

### Step 6 — Dependencies

`requirements.txt` with a single line: `flask`

Tailwind CSS is loaded via CDN — no npm or build step required.

### Acceptance Criteria

- [ ] App starts with `python app.py` without errors
- [ ] Todos survive a server restart (persisted to JSON)
- [ ] All four CRUD actions work end-to-end in the browser
- [ ] UI is styled with Tailwind CSS (CDN)

---

## EXECUTION DETAILS

### Files Created

**`todo-app/app.py`** — single-file Flask application containing:

- `DataFile` — path constant pointing to `data/todos.json` relative to `app.py`
- `HtmlTemplate` — inline Jinja2 HTML string with Tailwind CSS (CDN), add-todo form, and todo list
- `LoadTodos()` — reads `data/todos.json`; returns `[]` if file does not exist
- `SaveTodos(Todos)` — writes the list to `data/todos.json`, creates `data/` dir if missing
- `Index()` — `GET /` — loads todos, renders HTML page
- `AddTodo()` — `POST /add` — reads `title` form field, appends new todo (auto-incremented id, ISO-8601 `created_at`), saves, redirects to `/`
- `ToggleDone(TodoId)` — `POST /done/<id>` — toggles `done` on matching todo, saves, redirects to `/`
- `DeleteTodo(TodoId)` — `POST /delete/<id>` — removes matching todo, saves, redirects to `/`
- Entry point: `if __name__ == "__main__": App.run(debug=True)`

**`todo-app/requirements.txt`** — single dependency: `flask`

### Conventions Applied

- PascalCase used for all variables, functions, and the Flask app instance (`App`)
- Tailwind CSS loaded via CDN — no build step required
- No database; todos persisted exclusively to `data/todos.json`
- Todo shape: `{ "id": int, "title": str, "done": bool, "created_at": ISO-8601 string }`
