from flask import Flask, render_template, request, redirect, url_for, jsonify
from flasgger import Swagger
from functools import wraps
import hmac
import json
import os
import threading
from datetime import date
from markupsafe import escape

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if not app.config["SECRET_KEY"]:
    raise RuntimeError("SECRET_KEY environment variable must be set")
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

API_TOKEN = os.environ.get("API_TOKEN")
if not API_TOKEN:
    raise RuntimeError("API_TOKEN environment variable must be set")

swagger_config = {
    "headers": [],
    "specs": [{"endpoint": "apispec", "route": "/apispec.json", "rule_filter": lambda rule: rule.rule.startswith("/api"), "model_filter": lambda tag: True}],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/docs",
}
swagger_template = {
    "info": {"title": "Todo API", "description": "REST API for managing todos", "version": "1.0"},
    "securityDefinitions": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header", "description": 'Enter: **Bearer &lt;token&gt;**'}},
    "security": [{"Bearer": []}],
}
swagger = Swagger(app, config=swagger_config, template=swagger_template)


def require_token(f):
    """Decorator that rejects requests lacking a valid Bearer token in the Authorization header."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        if not hmac.compare_digest(auth, f"Bearer {API_TOKEN}"):
            return jsonify({"error": "unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated


@app.after_request
def set_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.tailwindcss.com; "
        "style-src 'self' 'unsafe-inline'"
    )
    return response


def load_todos():
    """Return todos from disk, or an empty list if the file is missing or corrupt."""
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_todos(todos):
    """Persist todos to disk; raises on write failure instead of silently discarding data."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(todos, f, indent=2)
    except OSError as e:
        app.logger.error("Failed to save todos: %s", e)
        raise


def _parse_date(value):
    """Return value if it is a valid ISO-8601 date (YYYY-MM-DD), otherwise None."""
    try:
        date.fromisoformat(value)
        return value
    except (ValueError, TypeError):
        return None


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
VALID_PRIORITIES = set(PRIORITY_ORDER)


def parse_priority(value):
    """Return value if it is a recognised priority, otherwise fall back to 'medium'."""
    return value if value in VALID_PRIORITIES else "low"


_todos_lock = threading.Lock()


def mutate_todos_list(fn):
    """Load todos, apply fn(todos) under a lock, save, and return the result of fn."""
    with _todos_lock:
        todos = load_todos()
        result = fn(todos)
        save_todos(todos)
    return result


def next_id(todos):
    """Return an ID one greater than the current maximum, guaranteeing uniqueness even after deletions."""
    return max((t["id"] for t in todos), default=0) + 1


def sorted_todos(todos):
    """Return todos sorted high->medium->low using PRIORITY_ORDER; unknown priorities sort as medium."""
    return sorted(todos, key=lambda t: PRIORITY_ORDER.get(t.get("priority", "medium"), 1), reverse=True)


@app.route("/")
def index():
    """GET / — render the main page with all todos sorted by priority, no auth required."""
    todos = sorted_todos(load_todos())
    return render_template("index.html", todos=todos, today=date.today().isoformat())


@app.route("/add", methods=["POST"])
def add():
    """POST /add — create a todo from form data, silently ignore empty titles, redirect to index."""
    title = str(escape(request.form.get("title", "").strip()))[:200]
    priority = parse_priority(request.form.get("priority", "medium"))
    due_date = _parse_date(request.form.get("due_date", "").strip())
    if title:
        mutate_todos_list(lambda todos: todos.append({"id": next_id(
            todos), "title": title, "done": False, "priority": priority, "due_date": due_date}))
    return redirect(url_for("index"))


@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit(todo_id):
    """POST /edit/<todo_id> — update title and priority of an existing todo, redirect to index."""
    title = request.form.get("title", "").strip()[:200]
    priority = parse_priority(request.form.get("priority", "medium"))
    if title:
        mutate_todos_list(lambda todos: next((t.update(
            {"title": title, "priority": priority}) for t in todos if t["id"] == todo_id), None))
    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    """POST /toggle/<todo_id> — flip the done flag on a todo, redirect to index."""
    def _toggle_x(todos):
        for t_x in todos:
            if t_x["id"] == todo_id:
                t_x["done"] = not t_x["done"]
                break
    mutate_todos_list(_toggle_x)
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    """POST /delete/<todo_id> — remove a todo permanently, redirect to index."""
    def DeleteTodos(todos):
        todos[:] = [t for t in todos if t["id"] != todo_id]
    mutate_todos_list(DeleteTodos)
    return redirect(url_for("index"))


@app.route("/api/todos", methods=["POST"])
@require_token
def api_add():
    """POST /api/todos — Bearer auth required; create todo from JSON body, return 201 with new todo or 400 if title missing.
    ---
    tags: [Todos]
    security:
      - Bearer: []
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [title]
          properties:
            title:
              type: string
              example: Buy milk
            priority:
              type: string
              enum: [high, medium, low]
              example: medium
    responses:
      201:
        description: Created todo
        schema:
          type: object
          properties:
            id: {type: integer}
            title: {type: string}
            done: {type: boolean}
            priority: {type: string}
      400:
        description: title is required
      401:
        description: unauthorized
    """
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()[:200]
    priority = parse_priority(data.get("priority", "medium"))
    if not title:
        return jsonify({"error": "title is required"}), 400
    result = {}

    def _api_add(todos):
        todo = {"id": next_id(todos), "title": title,
                "done": False, "priority": priority}
        todos.append(todo)
        result.update(todo)
    mutate_todos_list(_api_add)
    return jsonify(result), 201


@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
@require_token
def api_edit(todo_id):
    """PUT /api/todos/<todo_id> — Bearer auth required; update todo fields and return updated todo, or 404 if ID not found.
    ---
    tags: [Todos]
    security:
      - Bearer: []
    consumes: [application/json]
    parameters:
      - in: path
        name: todo_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Updated title
            priority:
              type: string
              enum: [high, medium, low]
              example: high
            done:
              type: boolean
              example: true
            due_date:
              type: string
              example: 2026-05-26
    responses:
      200:
        description: Updated todo
      400:
        description: invalid input
      401:
        description: unauthorized
      404:
        description: not found
    """
    data = request.get_json(silent=True) or {}
    updates = {}

    if "title" in data:
        title = str(data.get("title", "")).strip()[:200]
        if not title:
            return jsonify({"error": "title cannot be empty"}), 400
        updates["title"] = title

    if "priority" in data:
        updates["priority"] = parse_priority(data.get("priority", "medium"))

    if "done" in data:
        if not isinstance(data["done"], bool):
            return jsonify({"error": "done must be boolean"}), 400
        updates["done"] = data["done"]

    if "due_date" in data:
        due_date = data["due_date"]
        updates["due_date"] = _parse_date(str(due_date).strip()) if due_date is not None else None

        if not updates:
                return jsonify({"error": "no valid fields to update"}), 400

    updated = {}

    def _api_edit(todos):
        for t in todos:
            if t["id"] == todo_id:
                t.update(updates)
                updated.update(t)
                return

    mutate_todos_list(_api_edit)
    if not updated:
        return jsonify({"error": "not found"}), 404
    return jsonify(updated), 200


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
@require_token
def api_delete(todo_id):
    """DELETE /api/todos/<todo_id> — Bearer auth required; return 204 on success or 404 if ID not found.
    ---
    tags: [Todos]
    security:
      - Bearer: []
    parameters:
      - in: path
        name: todo_id
        type: integer
        required: true
    responses:
      204:
        description: Deleted successfully
      401:
        description: unauthorized
      404:
        description: not found
    """
    found = []

    def _api_delete(todos):
        remaining = [t for t in todos if t["id"] != todo_id]
        if len(remaining) < len(todos):
            found.append(True)
            todos[:] = remaining
    mutate_todos_list(_api_delete)
    if not found:
        return jsonify({"error": "not found"}), 404
    return "", 204


@app.route("/api/todos/<int:todo_id>/done", methods=["POST"])
@require_token
def api_mark_done(todo_id):
    """POST /api/todos/<todo_id>/done — Bearer auth required; mark todo as done, return updated todo, or 404 if ID not found.
    ---
    tags: [Todos]
    security:
      - Bearer: []
    parameters:
      - in: path
        name: todo_id
        type: integer
        required: true
    responses:
      200:
        description: Todo marked as done
      401:
        description: unauthorized
      404:
        description: not found
    """
    updated = {}

    def mark_done(todos):
        for todo in todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                updated.update(todo)
                return

    mutate_todos_list(mark_done)
    if not updated:
        return jsonify({"error": "not found"}), 404
    return jsonify(updated), 200


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a", ""))
            b = float(request.form.get("b", ""))
            result = a + b
        except ValueError:
            result = "Invalid input"
    return render_template("calculator.html", result=result)


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, host="127.0.0.1")
