# Spec: Login Feature — TaskFlow

## 1. Goal

Add session-based authentication to the TaskFlow app so that only registered users can view or manage tasks.

**Actor:** End user (task owner)
**Problem solved:** Currently all routes are publicly accessible with no identity or ownership concept; any visitor can read, create, or delete any task.

---

## 2. Functional Requirements

- **The system shall** provide a registration page where a new user can create an account with a username and password.
- **The system shall** provide a login page where an existing user can authenticate with their credentials.
- **The system shall** create a server-side session upon successful login and set a session cookie in the browser.
- **The system shall** redirect unauthenticated requests to `/tasks` (and all other protected routes) to the login page.
- **The system shall** provide a logout endpoint that destroys the session and redirects to the login page.
- **The system shall** display the logged-in username somewhere in the task list UI.
- **The system shall** scope tasks to the authenticated user — a user may only see and manage their own tasks.

---

## 3. Non-Functional Requirements

- **Security:** Passwords must be stored as bcrypt hashes; plaintext storage is not acceptable. Session secret must be configurable via environment variable, not hardcoded.
- **Security:** All new DB queries must use parameterized queries (no string interpolation) — consistent with fixing the existing known issues rather than extending them.
- **Input validation:** Username and password fields must be validated server-side (non-empty, max length ≤ 64 chars).
- **Reliability:** Failed login attempts must return a clear error message without leaking whether the username or password was wrong (generic "Invalid credentials").
- **Maintainability:** Auth logic lives in a dedicated module (`auth.py` or similar), not inlined into `app.py`.

---

## 4. API / Interface Contract

### `GET /login`
Returns the login form (HTML).

### `POST /login`
| Field | Type | Notes |
|---|---|---|
| `username` | `string` | form field |
| `password` | `string` | form field |

- **200** — renders task list (redirect to `GET /tasks`)
- **401** — re-renders login page with error "Invalid credentials"

### `GET /register`
Returns the registration form (HTML).

### `POST /register`
| Field | Type | Notes |
|---|---|---|
| `username` | `string` | form field, must be unique |
| `password` | `string` | form field |

- **302** — redirects to `GET /login` on success
- **400** — re-renders registration page with error (e.g. "Username already taken", "Fields required")

### `POST /logout`
- **302** — destroys session, redirects to `GET /login`
- No request body needed.

### `GET /tasks` (modified)
- **302** if not authenticated → redirect to `/login`
- **200** if authenticated → existing behavior, scoped to `user_id`

---

## 5. Data Model Changes

### New table: `users`

```sql
CREATE TABLE IF NOT EXISTS users (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    username     TEXT    NOT NULL UNIQUE,
    password_hash TEXT   NOT NULL,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Modified table: `tasks`

Add a foreign key to associate tasks with their owner:

```sql
ALTER TABLE tasks ADD COLUMN user_id INTEGER REFERENCES users(id);
```

> Note: existing rows will have `user_id = NULL`. A migration strategy (assign to a default user, or delete orphans) must be decided before deployment.

---

## 6. Out of Scope

- Password reset / "forgot password" flow
- Email verification
- OAuth / third-party login (Google, GitHub, etc.)
- Role-based access control (admin vs. regular user)
- Rate limiting / brute-force protection
- Remember-me / persistent sessions
- Fixing the existing intentional SQL injection vulnerabilities in `db.py` (those are documented as intentional for workshop purposes)

---

## 7. Open Questions

1. **Existing data:** What happens to tasks already in the DB when `user_id` is added? Should they be deleted, assigned to a seed admin account, or left as orphans?
2. **Registration open or invite-only?** Can anyone register, or should new accounts require an admin to create them?
3. **Session backend:** Flask's default cookie-based sessions (signed, not encrypted) or a server-side session store (e.g. `flask-session` + SQLite/Redis)?
4. **Password policy:** Any minimum length or complexity requirements beyond "non-empty"?
5. **Username format:** Case-sensitive? Allow spaces or special characters?

---

## 8. Acceptance Criteria

- [ ] Visiting `/tasks` without a session redirects to `/login`
- [ ] A user can register with a username and password; their password is stored as a bcrypt hash
- [ ] A registered user can log in and is redirected to `/tasks`
- [ ] A logged-in user sees only their own tasks
- [ ] A logged-in user can create and delete only their own tasks
- [ ] Logging out destroys the session and redirects to `/login`
- [ ] Entering wrong credentials on the login form shows "Invalid credentials" without revealing which field was wrong
- [ ] Duplicate username registration returns an error, not a 500
- [ ] All new SQL queries in `db.py` use parameterized queries
