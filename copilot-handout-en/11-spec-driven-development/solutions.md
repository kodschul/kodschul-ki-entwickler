# Module 11 — Solutions

---

## Solution 11.1 – SPEC.md for Due Dates Feature

````markdown
# SPEC – Due Dates Feature

## User Story

As a user, I want to set an optional due date on a todo item so that I can track deadlines and immediately see which items are overdue.

## Data Model Change

`todos.json` entry — existing fields plus one new field:

```json
{
  "id": 1,
  "title": "Buy milk",
  "done": false,
  "due_date": null
}
```
````

`due_date` is an ISO 8601 date string (`YYYY-MM-DD`) or `null` when no due date is set. All existing todos without a due date default to `null`.

## UI Description

- **Create / Edit form:** An optional date input field labelled "Due date (optional)".
- **Todo list:** Each todo with a due date shows "Due on DD.MM.YYYY" below the title.
- **Overdue indicator:** When `due_date < today`, the todo title is rendered in red.
- **No due date:** Nothing extra is shown — no empty label or placeholder.

## Routes Table

| Route             | Change                                                       |
| ----------------- | ------------------------------------------------------------ |
| `GET /`           | Passes today's date to the template for overdue comparison   |
| `POST /add`       | Accepts optional `due_date` form field (YYYY-MM-DD or empty) |
| `GET /edit/<id>`  | Pre-fills `due_date` in the form                             |
| `POST /edit/<id>` | Saves the updated `due_date`                                 |

## Acceptance Criteria

1. A todo created with a due date stores the date in ISO format (`YYYY-MM-DD`) in `todos.json`.
2. A todo created without a due date has `"due_date": null` in `todos.json`.
3. A todo with a future due date displays "Due on DD.MM.YYYY" in the list view.
4. A todo whose `due_date` is before today is displayed with a red title in the list view.
5. Editing a todo preserves the existing `due_date` unless the user explicitly changes it.

## Out of Scope

- Recurring or repeating due dates
- Email / push notifications for upcoming deadlines
- Sorting the list by due date
- Time-of-day precision (date only)

```

---

## Solution 11.2 – Agent Mode Prompt Chain

The step-by-step prompt used in Agent Mode:

```

Implement the feature described in #file:SPEC.md.

Step 1: Update the data model — add "due_date": null as a default field to every
todo in todos.json and to the /add and /edit routes in app.py.
Step 2: Update the POST /add route to read an optional due_date from the form.
Step 3: Update index.html — add a date input to the add form.
Step 4: Show due_date in the todo list as "Due on DD.MM.YYYY" using a helper
function func_format_due_date(due_date: str | None) -> str.
Step 5: Apply a CSS class "overdue" (red text) to todos where due_date < today.

After each step run: python -m pytest test_app.py -v

````

**Key practice:** Running tests after every step catches regressions immediately rather than debugging a large diff at the end.

---

## Solution 11.3 – Tests for Acceptance Criteria

```python
from datetime import date, timedelta

# AC 1 – due_date stored in ISO format
def test_add_todo_with_due_date_stores_iso_format(client):
    future = (date.today() + timedelta(days=7)).isoformat()
    client.post("/add", data={"title": "AC1", "due_date": future})
    todos = json.loads(pathlib.Path("todos.json").read_text())
    assert todos[-1]["due_date"] == future

# AC 2 – no due_date → null
def test_add_todo_without_due_date_stores_null(client):
    client.post("/add", data={"title": "AC2"})
    todos = json.loads(pathlib.Path("todos.json").read_text())
    assert todos[-1]["due_date"] is None

# AC 3 – future due_date shown in list
def test_list_shows_due_date_for_future_todo(client):
    future = (date.today() + timedelta(days=3)).strftime("%Y-%m-%d")
    client.post("/add", data={"title": "AC3", "due_date": future})
    response = client.get("/")
    assert b"Due on" in response.data

# AC 4 – overdue todo rendered with overdue class
def test_list_marks_overdue_todo_with_css_class(client):
    past = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    client.post("/add", data={"title": "AC4", "due_date": past})
    response = client.get("/")
    assert b"overdue" in response.data

# AC 5 – edit preserves due_date
def test_edit_preserves_existing_due_date(client):
    future = (date.today() + timedelta(days=5)).isoformat()
    client.post("/add", data={"title": "AC5", "due_date": future})
    todos = json.loads(pathlib.Path("todos.json").read_text())
    todo_id = todos[-1]["id"]
    client.post(f"/edit/{todo_id}", data={"title": "AC5 updated"})
    todos = json.loads(pathlib.Path("todos.json").read_text())
    assert todos[-1]["due_date"] == future
````

---

## Solution 11.4 – Spec vs. Implementation Comparison Table

| Criterion                                     | Implemented? | Notes                                       |
| --------------------------------------------- | ------------ | ------------------------------------------- |
| 1. due_date stored in ISO format              | ✅ Yes       | Confirmed in `todos.json` after POST /add   |
| 2. null for todos without due_date            | ✅ Yes       | Default set in `/add` route                 |
| 3. "Due on DD.MM.YYYY" shown for future todos | ✅ Yes       | `func_format_due_date` used in template     |
| 4. Overdue todos displayed in red             | ✅ Yes       | `overdue` CSS class applied in `index.html` |
| 5. Edit preserves existing due_date           | ✅ Yes       | Pre-filled in the edit form                 |

**Typical gap found:** AC 5 is the most commonly missed — the edit route often overwrites `due_date` with an empty string when the date field is left blank.
