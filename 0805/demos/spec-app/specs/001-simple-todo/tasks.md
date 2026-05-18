# Tasks: Simple Todo App

**Input**: Design documents from `specs/001-simple-todo/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and directory structure

- [ ] T001 Create directory structure: `backend/`, `frontend/`, `tests/`
- [ ] T002 Create `backend/requirements.txt` with Flask 3.x, SQLAlchemy 2.x, Flask-CORS, pytest, pytest-flask
- [ ] T003 [P] Create `tests/conftest.py` with pytest fixtures (Flask test client, in-memory SQLite DB)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core backend infrastructure required by all user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create `backend/database.py` — SQLAlchemy `db` instance and `init_db()` helper function
- [ ] T005 Create `backend/models.py` — `Todo` model with `id`, `description`, `completed`, `created_at` fields (per data-model.md)
- [ ] T006 Create `backend/app.py` — Flask app factory with CORS enabled, SQLAlchemy wired to SQLite at `backend/todos.db`, `/api` blueprint registered
- [ ] T007 [P] Create `frontend/index.html` — HTML skeleton with Tailwind CSS CDN script tag, a heading, an input form, and an empty `<ul id="todo-list">` placeholder
- [ ] T008 [P] Create `frontend/app.js` — empty module with `BASE_URL = 'http://localhost:5000/api'` constant

**Checkpoint**: Foundation ready — Flask starts and serves `GET /api/todos` returning `[]`; frontend HTML opens in browser

---

## Phase 3: User Story 1 — Create and View Todos (Priority: P1) 🎯 MVP

**Goal**: Users can add a new todo item and see all existing todos listed on the page.

**Independent Test**: Open `frontend/index.html`, type a task, submit → item appears in the list; reload page → item still shown.

### Implementation for User Story 1

- [ ] T009 [US1] Add `GET /api/todos` route in `backend/app.py` — query all `Todo` rows ordered by `created_at`, return JSON array
- [ ] T010 [US1] Add `POST /api/todos` route in `backend/app.py` — validate non-empty description (return 400 on failure), insert new `Todo`, return 201 with JSON
- [ ] T011 [US1] Implement `loadTodos()` in `frontend/app.js` — fetch `GET /api/todos`, render each item as an `<li>` in `#todo-list`
- [ ] T012 [US1] Implement form submit handler in `frontend/app.js` — POST new todo, clear input, call `loadTodos()`
- [ ] T013 [US1] Style the input form and todo list in `frontend/index.html` using Tailwind utility classes (responsive layout, clean spacing)
- [ ] T014 [US1] Write integration tests for `GET /api/todos` and `POST /api/todos` in `tests/test_api.py` (valid create, empty-description 400)

**Checkpoint**: User Story 1 fully functional — create and view todos, persisted across reloads

---

## Phase 4: User Story 2 — Mark Todos as Complete (Priority: P2)

**Goal**: Users can toggle a todo between pending and completed states; completed todos appear visually distinct (strikethrough).

**Independent Test**: Add a task → click complete toggle → item shows strikethrough → click again → strikethrough removed.

### Implementation for User Story 2

- [ ] T015 [US2] Add `PATCH /api/todos/<int:id>` route in `backend/app.py` — accept `{"completed": true/false}`, update `Todo.completed`, return updated JSON or 404
- [ ] T016 [US2] Add toggle checkbox/button per todo item in `frontend/app.js` `renderTodo()` helper — clicking calls `PATCH /api/todos/<id>` then re-renders list
- [ ] T017 [US2] Apply Tailwind `line-through` and `text-gray-400` classes to completed items in `frontend/app.js`
- [ ] T018 [US2] Write integration tests for `PATCH /api/todos/<id>` in `tests/test_api.py` (mark complete, unmark, 404 on missing)

**Checkpoint**: User Stories 1 and 2 both independently functional

---

## Phase 5: User Story 3 — Delete a Todo (Priority: P3)

**Goal**: Users can remove a todo item; it disappears from the list immediately.

**Independent Test**: Add a task → click delete button → item removed from list; reload — item still gone.

### Implementation for User Story 3

- [ ] T019 [US3] Add `DELETE /api/todos/<int:id>` route in `backend/app.py` — delete the row, return 204 or 404
- [ ] T020 [US3] Add delete button per todo item in `frontend/app.js` `renderTodo()` helper — clicking calls `DELETE /api/todos/<id>` then re-renders list
- [ ] T021 [US3] Style delete button with Tailwind (e.g., red text, hover effect) in `frontend/app.js`
- [ ] T022 [US3] Write integration test for `DELETE /api/todos/<id>` in `tests/test_api.py` (success 204, 404 on missing)

**Checkpoint**: All three user stories functional and independently testable

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: UX improvements and validation across all stories

- [ ] T023 [P] Add client-side validation in `frontend/app.js` — prevent submitting empty/whitespace-only descriptions; show inline error message
- [ ] T024 [P] Ensure responsive layout in `frontend/index.html` — Tailwind `max-w`, `mx-auto`, `px-4` for mobile and desktop
- [ ] T025 Add `backend/README.md` with setup and run instructions (per quickstart.md)
- [ ] T026 Run full test suite (`pytest tests/`) and confirm all tests pass
- [ ] T027 Manually walk through quickstart.md validation scenarios end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 completion — blocks all user stories
- **User Stories (Phases 3–5)**: All depend on Foundational completion; can proceed in priority order P1 → P2 → P3
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **US1 (P1)**: No dependencies on other user stories
- **US2 (P2)**: Logically extends US1 (toggles existing items); can be independently testable
- **US3 (P3)**: Logically extends US1 (deletes existing items); can be independently testable

### Parallel Opportunities

- T003 (conftest), T007 (HTML skeleton), T008 (app.js stub) can run in parallel during Phase 1/2
- Within each user story, backend route and frontend JS can be developed in parallel
- T023 and T024 in Phase 6 can run in parallel

---

## Parallel Example: User Story 1

```bash
# Backend route and frontend JS in parallel:
Task: "Add GET /api/todos route in backend/app.py"
Task: "Implement loadTodos() in frontend/app.js"

# After both complete:
Task: "Add POST /api/todos route in backend/app.py"
Task: "Implement form submit handler in frontend/app.js"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (create & view todos)
4. **STOP and VALIDATE**: open browser, add a todo, reload
5. Proceed to Phase 4 if MVP confirmed

### Incremental Delivery

1. Setup + Foundational → blank page with empty list
2. US1 → create & view todos (MVP!)
3. US2 → mark complete/incomplete
4. US3 → delete todos
5. Polish → responsive UI + edge-case validation

---

## Notes

- [P] tasks = different files, no shared state dependencies
- No authentication needed — single-user app
- Tailwind CSS loaded via CDN — no build step
- SQLite DB file stored at `backend/todos.db`
- Test DB uses in-memory SQLite (configured in `tests/conftest.py`)
