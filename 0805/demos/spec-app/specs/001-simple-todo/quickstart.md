# Quickstart: Simple Todo App

## Prerequisites

- Python 3.11+
- pip

## Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend starts on `http://localhost:5000`.

## Open the UI

Open `frontend/index.html` directly in a browser, or serve it:

```bash
python -m http.server 3000 --directory frontend
```

Then visit `http://localhost:3000`.

## Run Tests

```bash
cd backend
pytest ../tests/
```

## API Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/todos` | List all todos |
| POST | `/api/todos` | Create a todo |
| PATCH | `/api/todos/{id}` | Toggle complete |
| DELETE | `/api/todos/{id}` | Delete a todo |

See `contracts/api.md` for full request/response schemas.
