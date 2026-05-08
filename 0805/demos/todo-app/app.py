import json
import uuid
from datetime import date, datetime
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "todo-demo-secret"

TODOS_FILE = Path("todos.json")

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def load_todos() -> list[dict]:
    if not TODOS_FILE.exists():
        return []
    with open(TODOS_FILE) as f:
        return json.load(f)


def save_todos(todos: list[dict]) -> None:
    with open(TODOS_FILE, "w") as f:
        json.dump(todos, f, indent=2)


@app.route("/")
def index():
    todos = load_todos()
    sort = request.args.get("sort", "date")

    if sort == "priority":
        todos.sort(key=lambda t: PRIORITY_ORDER[t["priority"]])
    elif sort == "name":
        todos.sort(key=lambda t: t["title"].lower())
    else:
        todos.sort(key=lambda t: t["created_at"], reverse=True)

    return render_template("index.html", todos=todos, sort=sort, today=date.today().isoformat())


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("index"))

    todos = load_todos()
    todos.append({
        "id": str(uuid.uuid4()),
        "title": title,
        "done": False,
        "priority": request.form.get("priority", "medium"),
        "due_date": request.form.get("due_date") or None,
        "created_at": datetime.now().isoformat(),
    })
    save_todos(todos)
    return redirect(url_for("index"))


@app.route("/toggle/<todo_id>", methods=["POST"])
def toggle(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    save_todos(todos)
    return redirect(url_for("index", sort=request.args.get("sort", "date")))


@app.route("/delete/<todo_id>", methods=["POST"])
def delete(todo_id):
    todos = [t for t in load_todos() if t["id"] != todo_id]
    save_todos(todos)
    return redirect(url_for("index", sort=request.args.get("sort", "date")))


if __name__ == "__main__":
    app.run(debug=True)
