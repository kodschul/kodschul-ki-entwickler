import json
import os
import tempfile
import pytest
from app import app, DATA_FILE, sorted_todos, PRIORITY_ORDER


@pytest.fixture
def client(tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr("app.DATA_FILE", str(data_file))
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_add_todo_with_priority(client):
    client.post("/add", data={"title": "Buy milk", "priority": "high"})
    resp = client.get("/")
    assert b"Buy milk" in resp.data
    assert b"High" in resp.data


def test_add_todo_defaults_to_medium(client):
    client.post("/add", data={"title": "Read book"})
    resp = client.get("/")
    assert b"Medium" in resp.data


def test_invalid_priority_falls_back_to_medium(client):
    client.post("/add", data={"title": "Hack", "priority": "critical"})
    import app as app_module
    todos = json.loads(open(app_module.DATA_FILE).read())
    assert todos[0]["priority"] == "medium"


def test_sorted_todos_order():
    todos = [
        {"id": 1, "title": "Low task", "priority": "low"},
        {"id": 2, "title": "High task", "priority": "high"},
        {"id": 3, "title": "Medium task", "priority": "medium"},
    ]
    result = sorted_todos(todos)
    assert [t["priority"] for t in result] == ["high", "medium", "low"]


def test_index_renders_in_priority_order(client):
    client.post("/add", data={"title": "Low task", "priority": "low"})
    client.post("/add", data={"title": "High task", "priority": "high"})
    client.post("/add", data={"title": "Medium task", "priority": "medium"})
    resp = client.get("/")
    html = resp.data.decode()
    assert html.index("High task") < html.index("Medium task") < html.index("Low task")


def test_edit_updates_priority(client):
    client.post("/add", data={"title": "Task", "priority": "low"})
    import app as app_module
    todos = json.loads(open(app_module.DATA_FILE).read())
    todo_id = todos[0]["id"]
    client.post(f"/edit/{todo_id}", data={"title": "Task", "priority": "high"})
    todos = json.loads(open(app_module.DATA_FILE).read())
    assert todos[0]["priority"] == "high"


def test_backfill_missing_priority(client, monkeypatch, tmp_path):
    data_file = tmp_path / "todos.json"
    data_file.write_text(json.dumps([{"id": 1, "title": "Old todo", "done": False}]))
    monkeypatch.setattr("app.DATA_FILE", str(data_file))
    resp = client.get("/")
    assert b"Medium" in resp.data
