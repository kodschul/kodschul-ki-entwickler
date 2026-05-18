# Route Contracts: Flask Todo App

**Date**: 2026-05-13

This app is server-rendered. "Contracts" here are the HTTP route interfaces exposed to the browser.

---

## Routes

### GET `/`

**Purpose**: Display all tasks

**Response**: HTML page with task list (or empty-state message)

**Behaviour**: Queries all tasks ordered by `created_at` descending.

---

### POST `/tasks`

**Purpose**: Create a new task

**Form fields**:
| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `title` | string | Yes | Non-empty after strip; max 200 chars |

**Success**: Redirect to `GET /` (PRG pattern)

**Failure**: Redirect to `GET /` with flash error message

---

### POST `/tasks/<int:id>/toggle`

**Purpose**: Toggle the completed status of a task

**URL params**: `id` — integer task ID

**Success**: Redirect to `GET /`

**Failure (not found)**: 404 response

---

### POST `/tasks/<int:id>/delete`

**Purpose**: Permanently delete a task

**URL params**: `id` — integer task ID

**Success**: Redirect to `GET /`

**Failure (not found)**: 404 response

---

## Notes

- All mutations use `POST` (HTML forms do not support `PUT`/`DELETE` natively)
- All successful mutations redirect to `GET /` to follow the PRG pattern (prevents double-submit on refresh)
- Flash messages are used for user-visible validation errors
