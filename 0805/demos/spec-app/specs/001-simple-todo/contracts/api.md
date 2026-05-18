# API Contract: Simple Todo App

**Base URL**: `http://localhost:5000/api`
**Format**: JSON request/response bodies

---

## GET /todos

Return all todo items ordered by `created_at` ascending.

**Response 200**:
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "completed": false,
    "created_at": "2026-05-12T10:00:00Z"
  }
]
```

---

## POST /todos

Create a new todo item.

**Request body**:
```json
{ "description": "Buy groceries" }
```

**Response 201**:
```json
{
  "id": 1,
  "description": "Buy groceries",
  "completed": false,
  "created_at": "2026-05-12T10:00:00Z"
}
```

**Response 400** (empty description):
```json
{ "error": "Description must not be empty." }
```

---

## PATCH /todos/{id}

Toggle or update the `completed` state of an existing todo.

**Request body**:
```json
{ "completed": true }
```

**Response 200**:
```json
{
  "id": 1,
  "description": "Buy groceries",
  "completed": true,
  "created_at": "2026-05-12T10:00:00Z"
}
```

**Response 404** (todo not found):
```json
{ "error": "Todo not found." }
```

---

## DELETE /todos/{id}

Delete a todo item.

**Response 204**: No content.

**Response 404** (todo not found):
```json
{ "error": "Todo not found." }
```
