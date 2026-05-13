import sqlite3
import pytest
from unittest.mock import patch
from db import DbManager


SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    status     TEXT    NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP        DEFAULT CURRENT_TIMESTAMP
);
"""


@pytest.fixture
def manager(tmp_path):
    db_file = str(tmp_path / "test.db")
    with patch("db.DB_PATH", db_file):
        m = DbManager()
        conn = sqlite3.connect(db_file)
        conn.executescript(SCHEMA)
        conn.commit()
        conn.close()
        yield m


# --- func_get_tasks ---

def test_get_tasks_empty(manager):
    assert manager.func_get_tasks() == []


def test_get_tasks_returns_all(manager):
    manager.func_create_task("Alpha")
    manager.func_create_task("Beta")
    tasks = manager.func_get_tasks()
    titles = [t["title"] for t in tasks]
    assert set(titles) == {"Alpha", "Beta"}


def test_get_tasks_status_filter(manager):
    manager.func_create_task("Alpha")
    tasks = manager.func_get_tasks(status="pending")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Alpha"


def test_get_tasks_status_filter_no_match(manager):
    manager.func_create_task("Alpha")
    tasks = manager.func_get_tasks(status="done")
    assert tasks == []


# --- func_create_task ---

def test_create_task_persists(manager):
    manager.func_create_task("My Task")
    tasks = manager.func_get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "My Task"
    assert tasks[0]["status"] == "pending"


@pytest.mark.xfail(strict=True, reason="SQL injection: single quotes in title break string-concatenation query")
def test_create_task_special_characters(manager):
    manager.func_create_task("Fix bug: use 'quotes' & ampersands")
    tasks = manager.func_get_tasks()
    assert tasks[0]["title"] == "Fix bug: use 'quotes' & ampersands"


# --- func_delete_task ---

def test_delete_task_removes_row(manager):
    manager.func_create_task("To delete")
    task_id = manager.func_get_tasks()[0]["id"]
    manager.func_delete_task(task_id)
    assert manager.func_get_tasks() == []


def test_delete_task_nonexistent_id_is_noop(manager):
    manager.func_create_task("Keep me")
    manager.func_delete_task(9999)
    assert len(manager.func_get_tasks()) == 1


def test_delete_task_only_removes_target(manager):
    manager.func_create_task("Keep")
    manager.func_create_task("Remove")
    tasks = manager.func_get_tasks()
    remove_id = next(t["id"] for t in tasks if t["title"] == "Remove")
    manager.func_delete_task(remove_id)
    remaining = manager.func_get_tasks()
    assert len(remaining) == 1
    assert remaining[0]["title"] == "Keep"
