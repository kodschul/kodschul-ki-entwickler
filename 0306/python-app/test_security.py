"""
Security regression tests for the Flask todo app (app.py).

Each test corresponds to a specific security vulnerability and checks whether it
has been FIXED or is still PRESENT.  A passing test means the app behaves
securely for that concern; a failing test flags a live vulnerability.

Run with:
    python -m pytest test_security.py -v

Vulnerability categories covered:
  CRITICAL  – hardcoded token fallback, missing SECRET_KEY, timing-safe comparison
  HIGH      – stored XSS, unbounded input on /add, missing security headers, hmac source check
  MEDIUM    – date injection on /add, token in Swagger spec, invalid JSON, unbounded API edit
  LOW       – empty Bearer token
"""

import inspect
import os

# ---------------------------------------------------------------------------
# Environment bootstrap — MUST happen before 'app' is imported, because
# API_TOKEN and SECRET_KEY are read at module-load time.
# ---------------------------------------------------------------------------
os.environ.setdefault("API_TOKEN", "test-token-for-tests")
os.environ.setdefault("SECRET_KEY", "test-secret-key")

import app as app_module  # noqa: E402  (import after env setup is intentional)
from app import app as flask_app  # noqa: E402

import pytest  # noqa: E402

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TOKEN = "test-token-for-tests"          # matches the env-var set above
AUTH_HEADERS = {"Authorization": f"Bearer {TOKEN}"}


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def isolated_todos(tmp_path, monkeypatch):
    """Redirect DATA_FILE to a fresh temp file for every test so tests do not
    pollute or depend on each other's persisted state."""
    temp_file = tmp_path / "todos.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(app_module, "DATA_FILE", str(temp_file))
    yield


@pytest.fixture
def client():
    """Provide a Flask test client with TESTING mode enabled."""
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as test_client:
        yield test_client


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def add_todo_via_form(client, title="Test todo", priority="medium", due_date=""):
    """POST /add with the given form fields and follow the redirect to GET /."""
    return client.post(
        "/add",
        data={"title": title, "priority": priority, "due_date": due_date},
        follow_redirects=True,
    )


# ---------------------------------------------------------------------------
# CRITICAL – 1: Hardcoded API token fallback
# ---------------------------------------------------------------------------


def test_hardcoded_api_token_fallback_is_removed():
    """CRITICAL: When API_TOKEN env var is not set, 'secret-token-1234' must NOT be the fallback.

    The module source is inspected to assert that the os.environ.get() call for
    API_TOKEN does not supply a hardcoded default value.  The fix requires removing
    the default and raising RuntimeError when the env var is absent.

    Current state: app.py line 12 still reads
        API_TOKEN = os.environ.get("API_TOKEN", "secret-token-1234")
    so this test is expected to FAIL until the fallback is removed.
    """
    source = inspect.getsource(app_module)
    for line in source.splitlines():
        stripped = line.strip()
        # Target only the assignment line, not comments or other occurrences
        if (
            stripped.startswith("API_TOKEN")
            and "os.environ.get" in stripped
            and "=" in stripped
        ):
            assert "secret-token-1234" not in stripped, (
                "VULNERABILITY NOT FIXED: API_TOKEN still falls back to the hardcoded value "
                "'secret-token-1234' when API_TOKEN env var is absent.  "
                "Replace with:\n"
                "    API_TOKEN = os.environ.get('API_TOKEN')\n"
                "    if not API_TOKEN:\n"
                "        raise RuntimeError('API_TOKEN environment variable must be set')"
            )


# ---------------------------------------------------------------------------
# CRITICAL – 2: SECRET_KEY must be configured
# ---------------------------------------------------------------------------


def test_secret_key_is_configured():
    """CRITICAL: app.config['SECRET_KEY'] must be set to a non-empty, non-None value.

    Flask uses SECRET_KEY to sign session cookies.  An unset key means sessions are
    unsigned and can be forged by any client.

    Current state: app.py never reads SECRET_KEY from the environment into
    app.config, so Flask leaves it as None.  This test is expected to FAIL until
    the app explicitly sets app.config['SECRET_KEY'].
    """
    secret = flask_app.config.get("SECRET_KEY")
    assert secret, (
        "VULNERABILITY NOT FIXED: SECRET_KEY is not configured in the Flask app.  "
        "Add the following to app.py (after the Flask() constructor):\n"
        "    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')\n"
        "    if not app.config['SECRET_KEY']:\n"
        "        raise RuntimeError('SECRET_KEY environment variable must be set')"
    )


# ---------------------------------------------------------------------------
# CRITICAL – 3a / 3b: Timing-safe token comparison — behavioural checks
# ---------------------------------------------------------------------------


def test_timing_safe_comparison_wrong_value_returns_401(client):
    """CRITICAL (behavioural): A token with the correct prefix but a wrong value must return 401.

    This confirms that the auth check is correct even when the token string
    shares a long common prefix with the real token.
    """
    # Craft a token that starts identically to TOKEN but has a wrong suffix
    wrong_token = TOKEN + "_WRONG_SUFFIX"
    resp = client.post(
        "/api/todos",
        json={"title": "payload"},
        headers={"Authorization": f"Bearer {wrong_token}"},
    )
    assert resp.status_code == 401, (
        "Expected 401 for a token with correct prefix but wrong value, "
        "got %d instead." % resp.status_code
    )


def test_timing_safe_comparison_short_token_returns_401(client):
    """CRITICAL (behavioural): A token shorter than the real token must return 401.

    Ensures there is no short-circuit that would accidentally accept a prefix
    of the real token.
    """
    resp = client.post(
        "/api/todos",
        json={"title": "payload"},
        headers={"Authorization": "Bearer x"},
    )
    assert resp.status_code == 401, (
        "Expected 401 for a very short/invalid token, "
        "got %d instead." % resp.status_code
    )


# ---------------------------------------------------------------------------
# HIGH – 4: Stored XSS sanitisation
# ---------------------------------------------------------------------------


def test_xss_script_tag_not_rendered_unescaped(client):
    """HIGH: A todo title containing a <script> tag must NOT appear unescaped in GET /.

    Jinja2 autoescaping protects {{ todo.title }} in the template, so this test
    currently PASSES.  It acts as a regression guard: if a developer ever marks
    the output as |safe, or disables autoescaping, this test will catch the regression.
    """
    xss_payload = "<script>alert('xss')</script>"
    add_todo_via_form(client, title=xss_payload)

    resp = client.get("/")
    html = resp.data.decode("utf-8")

    assert "<script>alert" not in html, (
        "VULNERABILITY NOT FIXED: Raw unescaped <script> tag found in the GET / HTML response.  "
        "Ensure Jinja2 autoescaping is active and that no template uses '| safe' on user input."
    )


# ---------------------------------------------------------------------------
# HIGH – 5: Input length limiting on /add
# ---------------------------------------------------------------------------


def test_input_length_limiting_on_add_route(client):
    """HIGH: POST /add with a title > 200 characters must be truncated before storage.

    The /edit route and all API routes apply [:200] truncation; the /add route
    does not.  This test is expected to FAIL until the truncation is added there.
    """
    long_title = "A" * 5000
    add_todo_via_form(client, title=long_title)

    # Read the stored todos directly (avoids HTML-parsing complexity)
    stored_todos = app_module.load_todos()
    assert stored_todos, "Setup failed: no todo was created by /add"

    stored_title = stored_todos[0]["title"]
    assert len(stored_title) <= 200, (
        "VULNERABILITY NOT FIXED: /add stored a title of %d characters (max allowed: 200).  "
        "Add [:200] truncation in the /add route, matching the /edit route and the API routes."
        % len(stored_title)
    )


# ---------------------------------------------------------------------------
# HIGH – 6a / 6b / 6c: Security headers
# ---------------------------------------------------------------------------


def test_security_header_x_content_type_options(client):
    """HIGH: Every response must include the header 'X-Content-Type-Options: nosniff'.

    Without this header, older browsers may MIME-sniff responses and execute
    unexpected content types as scripts.  This test is expected to FAIL until the
    header is added (e.g. via an after_request hook or Flask-Talisman).
    """
    resp = client.get("/")
    value = resp.headers.get("X-Content-Type-Options")
    assert value == "nosniff", (
        "VULNERABILITY NOT FIXED: 'X-Content-Type-Options: nosniff' header is missing "
        "(got: %r).  Add it via an @app.after_request hook." % value
    )


def test_security_header_x_frame_options(client):
    """HIGH: Every response must include the header 'X-Frame-Options: DENY'.

    Without this header, the page can be embedded in an iframe on another origin,
    enabling clickjacking attacks.  This test is expected to FAIL.
    """
    resp = client.get("/")
    value = resp.headers.get("X-Frame-Options")
    assert value == "DENY", (
        "VULNERABILITY NOT FIXED: 'X-Frame-Options: DENY' header is missing "
        "(got: %r).  Add it via an @app.after_request hook." % value
    )


def test_security_header_content_security_policy(client):
    """HIGH: Every response must include a 'Content-Security-Policy' header.

    A CSP restricts where scripts, styles, and other resources may be loaded from,
    substantially reducing the impact of any XSS that slips through.
    This test is expected to FAIL.
    """
    resp = client.get("/")
    value = resp.headers.get("Content-Security-Policy")
    assert value is not None, (
        "VULNERABILITY NOT FIXED: 'Content-Security-Policy' header is absent.  "
        "Add a restrictive CSP via an @app.after_request hook or Flask-Talisman."
    )


# ---------------------------------------------------------------------------
# HIGH – 7: API auth – hmac.compare_digest in require_token (source inspection)
# ---------------------------------------------------------------------------


def test_require_token_uses_hmac_compare_digest():
    """HIGH: The require_token decorator must use hmac.compare_digest for token comparison.

    Plain string equality (== / !=) leaks timing information: Python's comparison
    short-circuits at the first differing byte, so an attacker can enumerate valid
    token prefixes via response-time measurement.  hmac.compare_digest always
    takes constant time regardless of where strings differ.

    This test inspects the source of require_token directly.
    Expected to FAIL until the fix is applied.
    """
    source = inspect.getsource(app_module.require_token)
    assert "hmac.compare_digest" in source, (
        "VULNERABILITY NOT FIXED: require_token uses plain string equality instead of "
        "hmac.compare_digest.  Replace:\n"
        "    if auth != f'Bearer {API_TOKEN}':\n"
        "with:\n"
        "    if not hmac.compare_digest(auth, f'Bearer {API_TOKEN}'):\n"
        "Note: hmac is already imported in app.py."
    )


# ---------------------------------------------------------------------------
# MEDIUM – 8: Date validation on /add
# ---------------------------------------------------------------------------


def test_date_validation_rejects_injection_string(client):
    """MEDIUM: POST /add with a non-ISO-8601 due_date must not persist the raw string.

    Storing an arbitrary string as due_date is benign in the current JSON backend,
    but leaves the door open when the storage layer changes (e.g. a SQL database).
    The fix is to validate that due_date matches YYYY-MM-DD before storing it.

    This test is expected to FAIL: the app currently stores whatever string is
    submitted without validation.
    """
    injected = "; DROP TABLE todos"
    add_todo_via_form(client, title="Legitimate task", due_date=injected)

    stored_todos = app_module.load_todos()
    assert stored_todos, "Setup failed: no todo was created"

    stored_due = stored_todos[0].get("due_date")
    assert stored_due != injected, (
        "VULNERABILITY NOT FIXED: /add persisted the raw injection string %r as due_date.  "
        "Validate due_date with a regex or datetime.date.fromisoformat() and reject/clear "
        "any value that does not match the YYYY-MM-DD format." % injected
    )


# ---------------------------------------------------------------------------
# MEDIUM – 9: Swagger UI / API spec must not expose the hardcoded token
# ---------------------------------------------------------------------------


def test_swagger_spec_does_not_expose_hardcoded_token(client):
    """MEDIUM: The machine-readable API spec at /apispec.json must not contain 'secret-token-1234'.

    The swagger_template in app.py currently embeds the hardcoded token in the
    Bearer security definition description, publishing credentials to anyone who
    browses the docs.  This test is expected to FAIL.
    """
    resp = client.get("/apispec.json")
    assert resp.status_code == 200, (
        "Could not reach /apispec.json (status %d); adjust the route if the spec "
        "is served elsewhere." % resp.status_code
    )
    body = resp.data.decode("utf-8")
    assert "secret-token-1234" not in body, (
        "VULNERABILITY NOT FIXED: The API spec at /apispec.json contains the hardcoded "
        "token 'secret-token-1234'.  Remove the example token from the 'description' field "
        "in swagger_template['securityDefinitions']['Bearer']."
    )


# ---------------------------------------------------------------------------
# MEDIUM – 10: API JSON parse error handling — must return 400, not 500
# ---------------------------------------------------------------------------


def test_api_invalid_json_body_returns_400_not_500(client):
    """MEDIUM: POST /api/todos with a syntactically invalid JSON body must return 400.

    get_json(silent=True) already swallows the parse error and returns None, which
    the route then treats as a missing title → 400.  This test currently PASSES and
    acts as a regression guard to ensure that behaviour is never accidentally broken
    (e.g. by switching to force=True or silent=False).
    """
    resp = client.post(
        "/api/todos",
        data=b"{not valid json}",
        content_type="application/json",
        headers=AUTH_HEADERS,
    )
    assert resp.status_code == 400, (
        "Expected HTTP 400 for an invalid JSON body, got %d.  "
        "Ensure request.get_json(silent=True) is used so malformed payloads are "
        "handled gracefully rather than crashing with 500." % resp.status_code
    )


# ---------------------------------------------------------------------------
# MEDIUM – 11: Unbounded input on API PUT /api/todos/<id>
# ---------------------------------------------------------------------------


def test_api_edit_truncates_long_title_to_200_chars(client):
    """MEDIUM: PUT /api/todos/<id> with a title longer than 200 chars must store at most 200 chars.

    The API edit route already applies [:200] truncation, so this test currently
    PASSES.  It acts as a regression guard ensuring the truncation is never removed.
    """
    # Create a todo via the form first so we have a real ID to target
    add_todo_via_form(client, title="Seed todo for edit test")
    todos = app_module.load_todos()
    assert todos, "Setup failed: no todo created to seed the edit test"
    todo_id = todos[0]["id"]

    long_title = "C" * 5000
    resp = client.put(
        f"/api/todos/{todo_id}",
        json={"title": long_title},
        headers=AUTH_HEADERS,
    )
    assert resp.status_code == 200, (
        "Expected HTTP 200 when updating an existing todo via the API, "
        "got %d instead." % resp.status_code
    )

    stored_todos = app_module.load_todos()
    stored_title = next(
        (t["title"] for t in stored_todos if t["id"] == todo_id), None
    )
    assert stored_title is not None, "Todo was not found in storage after the PUT request"
    assert len(stored_title) <= 200, (
        "VULNERABILITY NOT FIXED: API edit stored a title of %d characters (max 200).  "
        "Ensure the [:200] slice is present in api_edit()." % len(stored_title)
    )


# ---------------------------------------------------------------------------
# LOW – 12: Empty Bearer token must be rejected
# ---------------------------------------------------------------------------


def test_empty_bearer_token_returns_401(client):
    """LOW: Authorization header 'Bearer ' (present but with an empty token) must return 401.

    An absent or whitespace-only token is not a valid credential and must never
    be accepted, even if the configured API_TOKEN happens to be an empty string.
    This test currently PASSES because the empty-token string never equals the
    configured TOKEN.
    """
    resp = client.post(
        "/api/todos",
        json={"title": "probe"},
        headers={"Authorization": "Bearer "},
    )
    assert resp.status_code == 401, (
        "Expected HTTP 401 for an empty Bearer token (Authorization: 'Bearer '), "
        "got %d instead." % resp.status_code
    )
