import sqlite3
import pytest
from unittest.mock import patch
import app as flask_app


SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    status     TEXT    NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP        DEFAULT CURRENT_TIMESTAMP
);
"""


@pytest.fixture
def client(tmp_path):
    db_file = str(tmp_path / "test.db")
    with patch("db.DB_PATH", db_file):
        conn = sqlite3.connect(db_file)
        conn.executescript(SCHEMA)
        conn.commit()
        conn.close()

        flask_app.app.config["TESTING"] = True
        with flask_app.app.test_client() as client:
            yield client


# --- GET /tasks ---

def test_get_tasks_empty_renders_html(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert b"<html" in resp.data.lower()


def test_get_tasks_shows_created_task(client):
    client.post("/tasks", data={"title": "Visible task"})
    resp = client.get("/tasks")
    assert b"Visible task" in resp.data


def test_get_tasks_status_filter(client):
    client.post("/tasks", data={"title": "Pending task"})
    resp = client.get("/tasks?status=pending")
    assert resp.status_code == 200
    assert b"Pending task" in resp.data


def test_get_tasks_status_filter_no_match(client):
    client.post("/tasks", data={"title": "Pending task"})
    resp = client.get("/tasks?status=done")
    assert resp.status_code == 200
    assert b"Pending task" not in resp.data


# --- POST /tasks ---

def test_create_task_returns_html(client):
    resp = client.post("/tasks", data={"title": "New task"})
    assert resp.status_code == 200
    assert b"New task" in resp.data


def test_create_task_empty_title_returns_400(client):
    resp = client.post("/tasks", data={"title": ""})
    assert resp.status_code == 400
    assert resp.get_json()["error"] == "Title is required"


def test_create_task_whitespace_only_returns_400(client):
    resp = client.post("/tasks", data={"title": "   "})
    assert resp.status_code == 400


def test_create_task_missing_title_returns_400(client):
    resp = client.post("/tasks", data={})
    assert resp.status_code == 400


# --- DELETE /tasks/<id> ---

def test_delete_task_returns_json(client):
    client.post("/tasks", data={"title": "To delete"})
    resp_list = client.get("/tasks")
    # parse id from the db directly via another POST round-trip isn't ideal;
    # use id=1 since it's the first inserted row in a fresh db
    resp = client.delete("/tasks/1")
    assert resp.status_code == 200
    assert resp.get_json() == {"deleted": 1}


def test_delete_task_removes_from_list(client):
    client.post("/tasks", data={"title": "Gone"})
    client.delete("/tasks/1")
    resp = client.get("/tasks")
    assert b"Gone" not in resp.data


def test_delete_nonexistent_task_is_noop(client):
    resp = client.delete("/tasks/9999")
    assert resp.status_code == 200
    assert resp.get_json() == {"deleted": 9999}
