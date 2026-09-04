import hmac
import json
import os

from flask import Blueprint, jsonify, request, send_from_directory, url_for

API_TOKEN = os.environ.get("API_TOKEN", "dev-secret-token")
SPECS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs")
TODOS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load_todos():
    if not os.path.exists(TODOS_FILE):
        return []
    with open(TODOS_FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    with open(TODOS_FILE, "w") as f:
        json.dump(todos, f, indent=2)

api_bp = Blueprint("api", __name__, url_prefix="/api")

PUBLIC_PATHS = {"/api/docs", "/api/openapi.yaml"}


@api_bp.before_request
def require_bearer_token():
    if request.path in PUBLIC_PATHS:
        return None

    auth = request.headers.get("Authorization", "")
    scheme, _, token = auth.partition(" ")
    if scheme != "Bearer" or not hmac.compare_digest(token, API_TOKEN):
        response = jsonify({"error": "Unauthorized"})
        response.status_code = 401
        response.headers["WWW-Authenticate"] = "Bearer"
        return response


@api_bp.route("/openapi.yaml")
def openapi_spec():
    return send_from_directory(SPECS_DIR, "todos-api.yaml", mimetype="text/yaml")


@api_bp.route("/docs")
def swagger_ui():
    return """<!DOCTYPE html>
<html>
<head>
  <title>Todo API Docs</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.17.14/swagger-ui.min.css">
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.17.14/swagger-ui-bundle.min.js"></script>
  <script>
    window.onload = () => {
      window.ui = SwaggerUIBundle({
        url: '/api/openapi.yaml',
        dom_id: '#swagger-ui',
      });
    };
  </script>
</body>
</html>"""


def find_todo(todos, id):
    return next((t for t in todos if t["id"] == id), None)


@api_bp.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(load_todos())


@api_bp.route("/todos/<id>", methods=["GET"])
def get_todo(id):
    todo = find_todo(load_todos(), id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)


@api_bp.route("/todos", methods=["POST"])
def create_todo():
    import uuid

    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    due_date = (data.get("due_date") or "").strip()
    if not text or not due_date:
        return jsonify({"error": "text and due_date are required"}), 400

    todo = {"id": uuid.uuid4().hex[:6], "text": text, "done": False, "due_date": due_date}
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)

    response = jsonify(todo)
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_todo", id=todo["id"])
    return response


@api_bp.route("/todos/<id>", methods=["PUT"])
def update_todo(id):
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    due_date = (data.get("due_date") or "").strip()
    if not text or not due_date:
        return jsonify({"error": "text and due_date are required"}), 400

    todos = load_todos()
    todo = find_todo(todos, id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todo["text"] = text
    todo["due_date"] = due_date
    if "done" in data:
        todo["done"] = bool(data["done"])
    save_todos(todos)
    return jsonify(todo)


@api_bp.route("/todos/<id>/toggle", methods=["PATCH"])
def toggle_todo(id):
    todos = load_todos()
    todo = find_todo(todos, id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todo["done"] = not todo["done"]
    save_todos(todos)
    return jsonify(todo)


@api_bp.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    todos = load_todos()
    todo = find_todo(todos, id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todos = [t for t in todos if t["id"] != id]
    save_todos(todos)
    return "", 204
