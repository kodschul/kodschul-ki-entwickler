import json
import os
import secrets
from datetime import datetime, timezone
from flask import Flask, redirect, render_template_string, request, session, url_for

App = Flask(__name__)
App.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

DataFile = os.path.join(os.path.dirname(__file__), "data", "todos.json")

MaxTitleLength = 200
MaxTodos = 500

HtmlTemplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Todo App</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen py-10">
    <div class="max-w-xl mx-auto">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-8">My Todos</h1>

        {% if Error %}
        <p class="mb-4 text-center text-red-600 font-medium">{{ Error }}</p>
        {% endif %}

        <!-- Add todo form -->
        <form action="/add" method="post" class="flex gap-2 mb-8">
            <input type="hidden" name="csrf_token" value="{{ CsrfToken }}" />
            <input
                type="text"
                name="title"
                placeholder="What needs to be done?"
                maxlength="{{ MaxTitleLength }}"
                required
                class="flex-1 border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
            <button
                type="submit"
                class="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-5 py-2 rounded"
            >
                Add
            </button>
        </form>

        <!-- Todo list -->
        <ul class="space-y-3">
            {% for Todo in Todos %}
            <li class="bg-white rounded shadow px-4 py-3 flex items-center justify-between gap-4">
                <div class="flex-1 min-w-0">
                    <p class="font-medium text-gray-800 {% if Todo.done %}line-through text-gray-400{% endif %} truncate">
                        {{ Todo.title }}
                    </p>
                    <p class="text-xs text-gray-400 mt-1">{{ Todo.created_at[:10] }}</p>
                </div>
                <div class="flex gap-2 shrink-0">
                    <form action="/done/{{ Todo.id }}" method="post">
                        <input type="hidden" name="csrf_token" value="{{ CsrfToken }}" />
                        <button
                            type="submit"
                            class="text-sm px-3 py-1 rounded {% if Todo.done %}bg-yellow-100 hover:bg-yellow-200 text-yellow-700{% else %}bg-green-100 hover:bg-green-200 text-green-700{% endif %}"
                        >
                            {% if Todo.done %}Undo{% else %}Done{% endif %}
                        </button>
                    </form>
                    <form action="/delete/{{ Todo.id }}" method="post">
                        <input type="hidden" name="csrf_token" value="{{ CsrfToken }}" />
                        <button
                            type="submit"
                            class="text-sm px-3 py-1 rounded bg-red-100 hover:bg-red-200 text-red-700"
                        >
                            Delete
                        </button>
                    </form>
                </div>
            </li>
            {% else %}
            <li class="text-center text-gray-400 py-10">No todos yet. Add one above!</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""


def LoadTodos():
    if not os.path.exists(DataFile):
        return []
    try:
        with open(DataFile, "r", encoding="utf-8") as F:
            return json.load(F)
    except (json.JSONDecodeError, OSError):
        return []


def SaveTodos(Todos):
    os.makedirs(os.path.dirname(DataFile), exist_ok=True)
    with open(DataFile, "w", encoding="utf-8") as F:
        json.dump(Todos, F, indent=2)


def GetCsrfToken():
    if "CsrfToken" not in session:
        session["CsrfToken"] = secrets.token_hex(32)
    return session["CsrfToken"]


def ValidateCsrfToken():
    return request.form.get("csrf_token") == session.get("CsrfToken")


@App.route("/")
def Index():
    Todos = LoadTodos()
    return render_template_string(HtmlTemplate, Todos=Todos, CsrfToken=GetCsrfToken(), MaxTitleLength=MaxTitleLength, Error=None)


@App.route("/add", methods=["POST"])
def AddTodo():
    if not ValidateCsrfToken():
        return "Forbidden", 403
    Todos = LoadTodos()
    Title = request.form.get("title", "").strip()
    if not Title:
        return redirect(url_for("Index"))
    if len(Title) > MaxTitleLength:
        Todos = LoadTodos()
        return render_template_string(HtmlTemplate, Todos=Todos, CsrfToken=GetCsrfToken(), MaxTitleLength=MaxTitleLength, Error=f"Title must be {MaxTitleLength} characters or fewer."), 422
    if len(Todos) >= MaxTodos:
        Todos = LoadTodos()
        return render_template_string(HtmlTemplate, Todos=Todos, CsrfToken=GetCsrfToken(), MaxTitleLength=MaxTitleLength, Error=f"Todo limit of {MaxTodos} reached. Delete some todos first."), 422
    NewId = max((T["id"] for T in Todos), default=0) + 1
    Todos.append({
        "id": NewId,
        "title": Title,
        "done": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })
    SaveTodos(Todos)
    return redirect(url_for("Index"))


@App.route("/done/<int:TodoId>", methods=["POST"])
def ToggleDone(TodoId):
    if not ValidateCsrfToken():
        return "Forbidden", 403
    Todos = LoadTodos()
    for Todo in Todos:
        if Todo["id"] == TodoId:
            Todo["done"] = not Todo["done"]
            break
    SaveTodos(Todos)
    return redirect(url_for("Index"))


@App.route("/delete/<int:TodoId>", methods=["POST"])
def DeleteTodo(TodoId):
    if not ValidateCsrfToken():
        return "Forbidden", 403
    Todos = LoadTodos()
    Todos = [T for T in Todos if T["id"] != TodoId]
    SaveTodos(Todos)
    return redirect(url_for("Index"))


if __name__ == "__main__":
    DebugMode = os.environ.get("DEBUG", "false").lower() == "true"
    App.run(debug=DebugMode)
