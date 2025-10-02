# Python Flask & API Style Guide

This style guide provides best practices for writing modern Python code using Flask and building HTTP APIs. It covers code structure, naming conventions, API design, validation, error handling, security, testing, and delivery.

---

## 1. General Python Best Practices

- **Follow PEP 8** for code style. Enforce with formatters/linters.
- Target **Python 3.10+** to leverage typing, pattern matching, and `|` unions.
- Prefer **virtual environments** (`venv`, `poetry`, or `pipenv`).
- Use **black** (format), **ruff** (lint/imports), and **mypy** (types) in CI.
- Write **docstrings** for public modules, classes, and functions (Google or NumPy style).
- Use **type hints** for all function signatures and public variables.
- Avoid wildcard imports (`from module import *`).
- Keep functions and classes **small and single-purpose**. Extract helpers.
- Fail fast with explicit errors; avoid silent `except`.

---

## 2. Project Structure

Organize Flask projects using the application factory pattern and blueprints. Example layout:

```text
project/
  app/
    __init__.py           # create_app factory, extensions registration
    api/
      __init__.py         # blueprint registration
      v1/
        __init__.py
        users.py          # routes/controllers
        auth.py
        schemas.py        # request/response models
        errors.py         # API error mappers
    core/
      config.py           # settings via environs/pydantic
      extensions.py       # db, cache, limiter, cors, etc.
      logging.py
    services/
      user_service.py     # domain logic
    repositories/
      user_repo.py        # data access layer
    models/
      user.py             # ORM models (SQLAlchemy)
    tasks/
      __init__.py
      user_tasks.py       # celery/rq tasks
  migrations/             # alembic
  tests/
    conftest.py
    integration/
    unit/
  .env.example
  pyproject.toml          # black/ruff/mypy/pytest config
  README.md
```

---

## 3. Application Factory & Configuration

- Use an `create_app(config: BaseSettings) -> Flask` factory to enable testing and multiple configs.
- Keep configuration pure-data and environment-driven. Never hardcode secrets.
- Prefer **Pydantic Settings** or **environs** to load environment variables with validation.
- Separate configs per environment: `Development`, `Testing`, `Production`.

```python
from flask import Flask
from .core.extensions import db, cors
from .core.config import settings

def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping({
        "SQLALCHEMY_DATABASE_URI": settings.database_url,
        "JSON_SORT_KEYS": False,
    })
    if config:
        app.config.update(config)

    db.init_app(app)
    cors.init_app(app)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
```

---

## 4. Blueprints & Routing

- Group endpoints by domain within a versioned blueprint (e.g., `api/v1/users`).
- Use nouns for resources and HTTP verbs for actions.
- Keep route functions thin; delegate to services.

```python
from flask import Blueprint, request
from .schemas import UserCreateIn, UserOut
from ...services.user_service import UserService

bp = Blueprint("users", __name__)

@bp.post("/users")
def create_user():
    payload = UserCreateIn.model_validate_json(request.get_data())
    user = UserService().create_user(payload)
    return UserOut.model_validate(user).model_dump(), 201
```

---

## 5. Request/Response Models

- Use **Pydantic** models for validation and serialization.
- Separate input and output schemas; never expose internal fields.
- Validate in controllers; never trust client data.

```python
from pydantic import BaseModel, EmailStr, Field

class UserCreateIn(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
```

---

## 6. Error Handling

- Define a consistent error envelope: `{ "error": { "code": str, "message": str, "details": Any } }`.
- Raise domain errors in services; map them to HTTP errors at the API layer.
- Register error handlers on the blueprint/app.

```python
from flask import jsonify
from werkzeug.exceptions import HTTPException

class AppError(Exception):
    code = "internal_error"
    status = 500
    def __init__(self, message: str, *, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

def to_response(error: AppError | HTTPException):
    if isinstance(error, HTTPException):
        status = error.code or 500
        code = getattr(error, "name", "http_error").lower()
        message = error.description
    else:
        status = error.status
        code = error.code
        message = error.message
    return jsonify({"error": {"code": code, "message": message, "details": getattr(error, "details", {})}}), status
```

---

## 7. Naming Conventions

- Modules, packages: `snake_case`.
- Classes, schemas: `PascalCase`.
- Functions, variables: `snake_case`.
- Constants: `UPPER_SNAKE_CASE`.
- Endpoints: `kebab-case` for URL segments; `snake_case` for JSON keys.

---

## 8. Authentication & Authorization

- Prefer **JWT** or **session cookies** depending on client type and threat model.
- Store secrets and keys only in environment variables or secret managers.
- For JWTs: short-lived access tokens, refresh tokens, clock skew tolerance, `aud` and `iss` validation.
- Enforce authorization in a dedicated layer (decorators or middleware) using roles/permissions from the domain.

---

## 9. Database & Persistence

- Use **SQLAlchemy** for ORM; keep models simple and documented.
- Encapsulate data access in repository classes; services call repositories.
- Use **Alembic** for schema migrations; one migration per PR if possible.
- Avoid N+1 queries; prefer eager loading or batch operations.

---

## 10. Caching & Rate Limiting

- Use **Flask-Caching** backed by Redis for hot paths; set explicit TTLs.
- Cache idempotent GETs; invalidate on write.
- Apply **Flask-Limiter** per endpoint and per identity.

---

## 11. Pagination, Filtering, Sorting

- Use cursor-based pagination for large datasets; otherwise page/limit.
- Validate limits (e.g., `1 <= limit <= 100`).
- Return pagination metadata: `total` (optional/expensive), `next`, `prev`, `count`.

---

## 12. OpenAPI/Swagger

- Generate OpenAPI automatically from schemas and routes (e.g., `flask-smorest`, `apispec`).
- Version your API (`/api/v1/...`).
- Document auth methods, error shapes, and rate limits.

---

## 13. Logging & Observability

- Use **structured logging** (JSON) at INFO in prod, DEBUG in dev.
- Correlate logs with request IDs; propagate `X-Request-ID`.
- Emit metrics (requests, latency, errors) and traces if available.

---

## 14. Security

- Enforce HTTPS; set HSTS.
- Validate and sanitize inputs; avoid passing raw values to SQL.
- Set secure cookies: `HttpOnly`, `Secure`, `SameSite=Lax/Strict`.
- Enable **CORS** narrowly; avoid `*` on credentials endpoints.
- Limit file uploads by size/type; scan when necessary.
- Keep dependencies updated; pin versions.

---

## 15. Testing

- Use **pytest** with fixtures for app, client, and database.
- Separate unit, integration, and end-to-end tests; keep them fast and deterministic.
- Cover services and error paths; assert error envelopes and status codes.

---

## 16. Performance

- Profile critical endpoints; set SLOs for latency and error budgets.
- Stream large responses when possible; use gzip/br.
- Avoid heavy sync I/O in request thread; offload to background tasks.

---

## 17. Background Tasks

- Use **Celery** or **RQ** for asynchronous processing; set timeouts and retries.
- Pass minimal context to jobs (IDs, not full objects).
- Monitor queues; implement dead-letter handling.

---

## 18. Deployment & Configuration

- Containerize with a minimal base image (e.g., `python:3.12-slim`).
- Use `gunicorn` with sensible workers/threads based on CPU and blocking I/O.
- Twelve-Factor config via environment variables; provide `.env.example`.

---

## 19. CI/CD & Quality Gates

- Mandatory checks: format (black), lint (ruff), types (mypy), tests (pytest), security scan (pip-audit, bandit).
- Block merges on failing checks; require code review.
- Use conventional commits and automated changelogs.

---

## 20. Versioning & Deprecation

- Version APIs via URL (`/v1`) or header; never break existing contracts within a version.
- Add deprecation headers/notices and timelines; provide migration guides.
- Remove deprecated endpoints in the next major version only.

---

## 21. Example Configurations

`pyproject.toml` minimal setup:

```toml
[tool.black]
line-length = 100
target-version = ["py310"]

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "UP", "B", "SIM", "N"]
ignore = ["E203", "W503"]

[tool.mypy]
python_version = "3.10"
disallow_untyped_defs = true
warn_unused_ignores = true
warn_redundant_casts = true
strict_optional = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"
```

---

## 22. API Design Checklist

- Clear resource naming and versioning
- Consistent request/response schemas (Pydantic)
- Validated inputs; descriptive errors
- Idempotency for PUT/DELETE; use idempotency keys for transfers
- Pagination and filters specified and validated
- AuthN/AuthZ enforced and documented
- Observability: request IDs, logs, metrics
- OpenAPI kept in sync and published

---

## 23. Code Review Guidelines

- Readability and maintainability over cleverness
- Clear separation of concerns (controller/service/repo)
- Adequate tests and documentation
- No leaking internals in responses
- Performance and security considerations addressed

---

## 24. Ready-to-Use App Skeleton (Excerpt)

```python
# app/__init__.py
from flask import Flask
from .core.extensions import db, cors
from .api import api_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_app(app)
    cors.init_app(app)
    app.register_blueprint(api_bp, url_prefix="/api/v1")
    return app
```

```python
# app/api/__init__.py
from flask import Blueprint
from .v1.users import bp as users_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(users_bp)
```

```python
# app/api/v1/users.py
from flask import Blueprint, request
from .schemas import UserCreateIn, UserOut

bp = Blueprint("users", __name__)

@bp.post("/users")
def create_user():
    data = UserCreateIn.model_validate_json(request.get_data())
    # call service, persist, return output
    return UserOut(id=1, email=data.email, name=data.name).model_dump(), 201
```

---

## 25. Further Reading

- Flask docs: `https://flask.palletsprojects.com/`
- Pydantic: `https://docs.pydantic.dev/`
- SQLAlchemy: `https://docs.sqlalchemy.org/`
- Alembic: `https://alembic.sqlalchemy.org/`
- OWASP ASVS: `https://owasp.org/www-project-application-security-verification-standard/`

# Python Flask & API Style Guide

This style guide provides best practices for writing modern Python code using Flask and APIs. It covers code structure, naming conventions, API design, error handling, and more.

---

## 1. General Python Best Practices

- **Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)** for code style.
- Use **Python 3.8+** for modern features (e.g., type hints, f-strings).
- Prefer **virtual environments** (e.g., `venv`, `pipenv`, `poetry`).
- Use **black** or **ruff** for code formatting and linting.
- Write **docstrings** for all public modules, classes, and functions.
- Use **type hints** for function signatures and variables.
- Avoid wildcard imports (`from module import *`).
- Keep functions and classes small and focused.

---

## 2. Project Structure

Organize your Flask project as follows:
