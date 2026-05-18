# Data Model: Simple Todo App

**Phase**: 1 — Design
**Date**: 2026-05-12

## Entities

### Todo

Represents a single task managed by the user.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTO INCREMENT | Unique identifier |
| `description` | TEXT | NOT NULL, non-empty | Task text entered by the user |
| `completed` | BOOLEAN | NOT NULL, default `False` | Whether the task is done |
| `created_at` | DATETIME | NOT NULL, default `now()` | Timestamp of creation |

### Validation Rules

- `description` must not be empty or whitespace-only (enforced at the API layer before persistence).
- `completed` defaults to `False` on creation.
- No maximum length constraint defined in spec; apply a practical limit of 1000 characters.

### State Transitions

```text
[created] → completed=False
    │
    ▼ (mark complete)
completed=True
    │
    ▼ (unmark)
completed=False
    │
    ▼ (delete)
[removed]
```

## SQLAlchemy Model (reference)

```python
class Todo(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    completed   = db.Column(db.Boolean, nullable=False, default=False)
    created_at  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
```
