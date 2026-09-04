import json
import os
import uuid
from datetime import date

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

TODOS_FILE = "todos.json"

# NOTE: registered at the bottom of this file, after load_todos/save_todos
# are defined, to avoid a circular import with api.py.


def load_todos():
    if not os.path.exists(TODOS_FILE):
        return []
    with open(TODOS_FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    with open(TODOS_FILE, "w") as f:
        json.dump(todos, f, indent=2)


@app.route("/")
def index():
    todos = load_todos()
    today = date.today().isoformat()
    for todo in todos:
        todo["overdue"] = todo["due_date"] < today and not todo["done"]
    due_today = [t for t in todos if t["due_date"] == today and not t["done"]]
    edit_id = request.args.get("edit")
    return render_template("index.html", todos=todos, due_today=due_today, edit_id=edit_id)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    due_date = request.form.get("due_date", "").strip()
    if text and due_date:
        todos = load_todos()
        todos.append(
            {"id": uuid.uuid4().hex[:6], "text": text, "done": False, "due_date": due_date}
        )
        save_todos(todos)
    return redirect(url_for("index"))


@app.route("/edit/<id>", methods=["POST"])
def edit(id):
    text = request.form.get("text", "").strip()
    due_date = request.form.get("due_date", "").strip()
    if text and due_date:
        todos = load_todos()
        for todo in todos:
            if todo["id"] == id:
                todo["text"] = text
                todo["due_date"] = due_date
        save_todos(todos)
    return redirect(url_for("index"))


@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != id]
    save_todos(todos)
    return redirect(url_for("index"))


from api import api_bp  # noqa: E402  (imported late to avoid circular import)

app.register_blueprint(api_bp)


if __name__ == "__main__":
    app.run(debug=True)
