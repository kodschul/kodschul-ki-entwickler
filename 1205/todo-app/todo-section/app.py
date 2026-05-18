import json
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
VALID_PRIORITIES = set(PRIORITY_ORDER)


def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        todos = json.load(f)
    # backfill priority for todos created before this feature
    for todo in todos:
        todo.setdefault("priority", "medium")
    return todos


def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def sorted_todos(todos):
    return sorted(todos, key=lambda t: PRIORITY_ORDER.get(t.get("priority", "medium"), 1))


@app.route("/")
def index():
    todos = sorted_todos(load_todos())
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    priority = request.form.get("priority", "medium")
    if priority not in VALID_PRIORITIES:
        priority = "medium"
    if title:
        todos = load_todos()
        todos.append({"id": len(todos) + 1, "title": title, "done": False, "priority": priority})
        save_todos(todos)
    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    save_todos(todos)
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todos = [t for t in load_todos() if t["id"] != todo_id]
    save_todos(todos)
    return redirect(url_for("index"))


@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    todos = load_todos()
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return redirect(url_for("index"))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", "medium")
        if priority not in VALID_PRIORITIES:
            priority = "medium"
        if title:
            todo["title"] = title
            todo["priority"] = priority
            save_todos(todos)
        return redirect(url_for("index"))
    return render_template("edit.html", todo=todo)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
