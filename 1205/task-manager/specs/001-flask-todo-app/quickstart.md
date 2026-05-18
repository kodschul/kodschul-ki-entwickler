# Quickstart: Flask Todo App

**Date**: 2026-05-13

---

## Prerequisites

- Python 3.11+
- pip

---

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
flask run
# or: python app.py
```

The app will be available at `http://127.0.0.1:5000`.

The SQLite database (`instance/todos.db`) is created automatically on first run.

---

## Running Tests

```bash
pytest
# or with coverage:
pytest --tb=short -v
```

Tests use an in-memory SQLite database — no database file is created.

---

## Project Layout

```
app.py              # Flask app + routes
models.py           # SQLAlchemy Task model
templates/
  base.html         # Tailwind layout shell
  index.html        # Todo list view
instance/
  todos.db          # SQLite DB (auto-created, gitignored)
tests/
  conftest.py       # Fixtures
  test_routes.py    # Route tests
  test_models.py    # Model tests
requirements.txt
```

---

## Key URLs

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:5000/` | Main todo list |
