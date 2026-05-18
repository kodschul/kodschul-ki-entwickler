# Data Model: Flask Todo App

**Date**: 2026-05-13

---

## Entity: Task

Represents a single to-do item created by the user.

### Fields

| Field | Type | Constraints | Notes |
|-------|------|-------------|-------|
| `id` | Integer | Primary key, auto-increment | Internal identifier |
| `title` | String(200) | NOT NULL, non-empty after strip | The task name entered by the user |
| `completed` | Boolean | NOT NULL, default `False` | Tracks completion state |
| `created_at` | DateTime | NOT NULL, default `utcnow` | Timestamp of creation |

### Validation Rules

- `title` must not be empty or whitespace-only after stripping
- `title` maximum length: 200 characters
- `completed` defaults to `False` on creation

### State Transitions

```
[Created] ──toggle──► [Completed]
[Completed] ──toggle──► [Created]
[Any state] ──delete──► [Deleted / removed]
```

### SQLAlchemy Model (reference)

```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
```

---

## Storage

- **Engine**: SQLite
- **File**: `instance/todos.db` (auto-created by Flask-SQLAlchemy on first run)
- **Test isolation**: In-memory SQLite (`sqlite:///:memory:`) used in pytest fixtures
