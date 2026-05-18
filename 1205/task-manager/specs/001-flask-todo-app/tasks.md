# Tasks: Flask Todo App

**Input**: Design documents from `specs/001-flask-todo-app/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/routes.md

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no shared dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and directory/file structure

- [x] T001 Create project directory structure: `app.py`, `models.py`, `templates/`, `static/`, `tests/`, `instance/` (gitignored)
- [x] T002 Create `requirements.txt` with Flask, Flask-SQLAlchemy, pytest, pytest-flask
- [x] T003 [P] Create `.gitignore` excluding `instance/`, `__pycache__/`, `.venv/`, `*.pyc`
- [x] T004 [P] Create virtual environment setup note in `quickstart.md` (verify existing quickstart is accurate)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core app factory, database, and base template — MUST complete before any user story

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Flask app factory with SQLAlchemy config in `app.py` (SQLite URI: `instance/todos.db`, secret key for flash messages)
- [x] T006 Define `Task` model in `models.py` with fields: `id`, `title` (String 200), `completed` (Boolean, default False), `created_at` (DateTime, default utcnow)
- [x] T007 Create `templates/base.html` with Tailwind CSS CDN (Play CDN script tag), flash message display block, and `{% block content %}` slot
- [x] T008 Create `tests/conftest.py` with pytest fixtures: `app` (test config, in-memory SQLite, `TESTING=True`), `client` (Flask test client), `db` (creates all tables, yields, drops all)

**Checkpoint**: App starts (`flask run`), SQLite DB auto-creates, base template renders — ready for user stories

---

## Phase 3: User Story 1 - Create and View Tasks (Priority: P1) 🎯 MVP

**Goal**: User can add a new task via a form and see all tasks listed on the page.

**Independent Test**: Run the app, navigate to `http://127.0.0.1:5000/`, enter a task name, submit — task appears in list. Refresh — task still appears.

### Implementation

- [x] T009 [US1] Implement `GET /` route in `app.py`: query all tasks ordered by `created_at` desc, render `templates/index.html`
- [x] T010 [US1] Implement `POST /tasks` route in `app.py`: strip title, validate non-empty and ≤200 chars, create `Task`, commit, redirect to `/` (PRG pattern); flash error on validation failure
- [x] T011 [US1] Create `templates/index.html` extending `base.html`: task creation form (text input + submit button styled with Tailwind), task list rendering each task title
- [x] T012 [US1] Add empty-state message to `templates/index.html`: display "No tasks yet. Add one above!" when task list is empty
- [x] T013 [US1] Write route tests in `tests/test_routes.py`: GET `/` returns 200, POST `/tasks` with valid title redirects to `/`, POST `/tasks` with empty title returns error flash, task persists after redirect

**Checkpoint**: User Story 1 fully functional — create and view tasks works end-to-end

---

## Phase 4: User Story 2 - Mark Tasks as Complete (Priority: P2)

**Goal**: User can toggle a task's completion status; completed tasks display with visual distinction.

**Independent Test**: Run the app with existing tasks, click the complete checkbox/button — task visually changes. Click again — reverts to pending.

### Implementation

- [x] T014 [US2] Implement `POST /tasks/<int:id>/toggle` route in `app.py`: fetch task by id (404 if not found), flip `completed`, commit, redirect to `/`
- [x] T015 [US2] Update `templates/index.html` to add toggle form per task: checkbox or button that POSTs to `/tasks/<id>/toggle`; apply Tailwind `line-through` and muted color class to completed task titles
- [x] T016 [US2] Write toggle tests in `tests/test_routes.py`: POST to toggle sets `completed=True`, second toggle sets `completed=False`, toggle on nonexistent id returns 404

**Checkpoint**: User Stories 1 AND 2 work independently — tasks can be created, viewed, and toggled

---

## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: User can permanently remove a task; when no tasks remain, empty-state message is shown.

**Independent Test**: Run the app, click delete on a task — task disappears. Delete all tasks — empty-state message appears.

### Implementation

- [x] T017 [US3] Implement `POST /tasks/<int:id>/delete` route in `app.py`: fetch task by id (404 if not found), delete from DB, commit, redirect to `/`
- [x] T018 [US3] Update `templates/index.html` to add delete form per task: small delete button (e.g., red "×") that POSTs to `/tasks/<id>/delete`
- [x] T019 [US3] Write delete tests in `tests/test_routes.py`: POST to delete removes task from DB, redirects to `/`, deleting nonexistent id returns 404, deleting last task shows empty-state

**Checkpoint**: All three user stories functional — full CRUD (create, toggle, delete) works

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: UI polish, edge-case hardening, and final validation

- [x] T020 [P] Polish `templates/index.html` with Tailwind: responsive layout, max-width container, hover states on buttons, consistent spacing
- [x] T021 [P] Add `static/` directory placeholder or minimal custom CSS file if needed (`static/style.css`)
- [x] T022 Validate long task name (200 chars) is accepted; 201+ chars triggers validation error — add/verify test in `tests/test_routes.py`
- [x] T023 Validate whitespace-only task title is rejected — add/verify test in `tests/test_routes.py`
- [x] T024 [P] Run full test suite (`pytest -v`) and confirm all tests pass
- [x] T025 [P] Verify `quickstart.md` setup steps work end-to-end from a clean environment

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 — blocks all user stories
- **Phase 3 (US1 - Create/View)**: Depends on Phase 2 completion
- **Phase 4 (US2 - Toggle)**: Depends on Phase 2; integrates with US1 templates
- **Phase 5 (US3 - Delete)**: Depends on Phase 2; integrates with US1/US2 templates
- **Phase 6 (Polish)**: Depends on all user story phases complete

### User Story Dependencies

- **US1 (P1)**: Can start after Phase 2 — no story dependencies
- **US2 (P2)**: Can start after Phase 2 — builds on US1 template (T011); coordinate on `index.html`
- **US3 (P3)**: Can start after Phase 2 — builds on US1/US2 template; coordinate on `index.html`

### Within Each Story

- Routes before templates (routes define what data templates receive)
- Template changes per story build incrementally on the same `index.html`
- Tests written alongside or after each route/template task

### Parallel Opportunities

- T003, T004 can run in parallel with T002 (Phase 1)
- T006, T007, T008 can run in parallel after T005 is scaffolded (Phase 2)
- T020, T021, T024, T025 can run in parallel (Phase 6)

---

## Parallel Example: Phase 2 Foundational

```bash
# After T005 (app.py scaffold) is done:
Task T006: "Define Task model in models.py"
Task T007: "Create templates/base.html with Tailwind CDN"
Task T008: "Create tests/conftest.py with fixtures"
# All three touch different files — fully parallel
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (T009–T013)
4. **STOP and VALIDATE**: `flask run`, add a task, refresh — confirm persistence
5. Ship MVP

### Incremental Delivery

1. Phase 1 + 2 → Foundation ready
2. Phase 3 → Create & View tasks → Demo MVP
3. Phase 4 → Toggle completion → Demo
4. Phase 5 → Delete tasks → Demo full feature
5. Phase 6 → Polish → Production-ready

---

## Notes

- [P] tasks touch different files — safe to run in parallel
- All story tasks share `templates/index.html` — coordinate edits to avoid conflicts
- `instance/todos.db` must be gitignored; created automatically on `flask run`
- Tests use in-memory SQLite — no DB file created during test runs
- PRG (Post/Redirect/Get) pattern prevents double-submit on refresh for all POST routes
