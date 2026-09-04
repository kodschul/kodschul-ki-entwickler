import json
import os
from datetime import date

import pytest

import app as app_module


@pytest.fixture
def client(tmp_path, monkeypatch):
    todos_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "TODOS_FILE", str(todos_file))
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def read_todos(client):
    with app_module.app.app_context():
        return app_module.load_todos()


def test_index_empty(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"No todos yet" in resp.data


def test_add_creates_todo(client):
    resp = client.post(
        "/add", data={"text": "Buy milk", "due_date": "2099-01-01"}, follow_redirects=True
    )
    assert resp.status_code == 200
    assert b"Buy milk" in resp.data
    todos = read_todos(client)
    assert len(todos) == 1
    assert todos[0]["text"] == "Buy milk"
    assert todos[0]["done"] is False
    assert todos[0]["due_date"] == "2099-01-01"
    assert "id" in todos[0]


def test_add_blank_text_ignored(client):
    client.post("/add", data={"text": "   ", "due_date": "2099-01-01"})
    assert read_todos(client) == []


def test_add_missing_due_date_ignored(client):
    client.post("/add", data={"text": "Buy milk"})
    assert read_todos(client) == []


def test_delete_removes_todo(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2099-01-01"})
    todo_id = read_todos(client)[0]["id"]

    resp = client.post(f"/delete/{todo_id}", follow_redirects=True)
    assert resp.status_code == 200
    assert b"Buy milk" not in resp.data
    assert read_todos(client) == []


def test_todos_persist_across_loads(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2099-01-01"})
    todos_first = read_todos(client)

    todos_second = app_module.load_todos()
    assert todos_second == todos_first


def test_delete_nonexistent_id_no_error(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2099-01-01"})
    resp = client.post("/delete/doesnotexist", follow_redirects=True)
    assert resp.status_code == 200
    assert b"Buy milk" in resp.data
    assert len(read_todos(client)) == 1


def test_edit_updates_text_and_due_date(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2099-01-01"})
    todo_id = read_todos(client)[0]["id"]

    resp = client.post(
        f"/edit/{todo_id}",
        data={"text": "Buy oat milk", "due_date": "2099-02-02"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    todos = read_todos(client)
    assert todos[0]["text"] == "Buy oat milk"
    assert todos[0]["due_date"] == "2099-02-02"


def test_edit_nonexistent_id_no_error(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2099-01-01"})
    resp = client.post(
        "/edit/doesnotexist",
        data={"text": "Ignored", "due_date": "2099-01-01"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert read_todos(client)[0]["text"] == "Buy milk"


def test_overdue_flag_shown_for_past_due_incomplete_todo(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2000-01-01"})
    resp = client.get("/")
    assert b"Buy milk" in resp.data
    assert b"text-red-600" in resp.data


def test_overdue_flag_not_shown_for_done_todo(client):
    client.post("/add", data={"text": "Buy milk", "due_date": "2000-01-01"})
    todos = read_todos(client)
    todos[0]["done"] = True
    with app_module.app.app_context():
        app_module.save_todos(todos)

    resp = client.get("/")
    assert b"text-red-600" not in resp.data


def test_due_today_popup_shown_for_incomplete_todo_due_today(client):
    today = date.today().isoformat()
    client.post("/add", data={"text": "Buy milk", "due_date": today})
    resp = client.get("/")
    assert b"Due today" in resp.data
    assert b"Buy milk" in resp.data


def test_due_today_popup_excludes_done_todo(client):
    today = date.today().isoformat()
    client.post("/add", data={"text": "Buy milk", "due_date": today})
    todos = read_todos(client)
    todos[0]["done"] = True
    with app_module.app.app_context():
        app_module.save_todos(todos)

    resp = client.get("/")
    assert b"Due today" not in resp.data


def test_due_today_popup_not_shown_when_nothing_due_today(client):
    client.post("/add", data={"text": "Past due", "due_date": "2000-01-01"})
    client.post("/add", data={"text": "Future", "due_date": "2099-01-01"})
    resp = client.get("/")
    assert b"Due today" not in resp.data
