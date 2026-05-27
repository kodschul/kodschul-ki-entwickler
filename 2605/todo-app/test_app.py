import json
import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(__file__))
import app as TodoApp


# ---------------------------------------------------------------------------
# Helpers & shared data
# ---------------------------------------------------------------------------

SampleTodos = [
    {"id": 1, "title": "Buy milk", "done": False, "created_at": "2026-01-01T00:00:00+00:00"},
    {"id": 2, "title": "Walk dog", "done": True,  "created_at": "2026-01-02T00:00:00+00:00"},
]


def _Write(DataFile, Todos):
    with open(DataFile, "w", encoding="utf-8") as F:
        json.dump(Todos, F)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def TempDataFile(tmp_path, monkeypatch):
    DataFile = str(tmp_path / "todos.json")
    monkeypatch.setattr(TodoApp, "DataFile", DataFile)
    return DataFile


@pytest.fixture
def Client(TempDataFile):
    TodoApp.App.config["TESTING"] = True
    with TodoApp.App.test_client() as C:
        yield C


# ---------------------------------------------------------------------------
# LoadTodos
# ---------------------------------------------------------------------------

def test_LoadTodos_fileExists_returnsList(TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Result = TodoApp.LoadTodos()
    assert len(Result) == 2
    assert Result[0]["title"] == "Buy milk"


def test_LoadTodos_fileNotExist_returnsEmptyList(TempDataFile):
    Result = TodoApp.LoadTodos()
    assert Result == []


def test_LoadTodos_emptyJsonArray_returnsEmptyList(TempDataFile):
    _Write(TempDataFile, [])
    Result = TodoApp.LoadTodos()
    assert Result == []


def test_LoadTodos_invalidJson_raisesException(TempDataFile):
    with open(TempDataFile, "w") as F:
        F.write("not valid json {{")
    with pytest.raises(Exception):
        TodoApp.LoadTodos()


# ---------------------------------------------------------------------------
# SaveTodos
# ---------------------------------------------------------------------------

def test_SaveTodos_validTodos_persistsToFile(TempDataFile):
    TodoApp.SaveTodos(SampleTodos)
    with open(TempDataFile, "r", encoding="utf-8") as F:
        Saved = json.load(F)
    assert len(Saved) == 2
    assert Saved[1]["title"] == "Walk dog"


def test_SaveTodos_emptyList_writesEmptyArray(TempDataFile):
    TodoApp.SaveTodos([])
    with open(TempDataFile, "r", encoding="utf-8") as F:
        Saved = json.load(F)
    assert Saved == []


def test_SaveTodos_dirNotExist_createsDirAndFile(tmp_path, monkeypatch):
    DataFile = str(tmp_path / "newdir" / "todos.json")
    monkeypatch.setattr(TodoApp, "DataFile", DataFile)
    TodoApp.SaveTodos([SampleTodos[0]])
    assert os.path.exists(DataFile)


def test_SaveTodos_specialCharacters_preservedCorrectly(TempDataFile):
    Todos = [{"id": 1, "title": "Ünïcödé & <script>", "done": False, "created_at": "2026-01-01T00:00:00+00:00"}]
    TodoApp.SaveTodos(Todos)
    with open(TempDataFile, "r", encoding="utf-8") as F:
        Saved = json.load(F)
    assert Saved[0]["title"] == "Ünïcödé & <script>"


# ---------------------------------------------------------------------------
# GET /
# ---------------------------------------------------------------------------

def test_Index_withTodos_rendersTitles(Client, TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Response = Client.get("/")
    assert Response.status_code == 200
    assert b"Buy milk" in Response.data
    assert b"Walk dog" in Response.data


def test_Index_noTodos_rendersEmptyStateMessage(Client):
    Response = Client.get("/")
    assert Response.status_code == 200
    assert b"No todos yet" in Response.data


def test_Index_manyTodos_rendersAllItems(Client, TempDataFile):
    ManyTodos = [
        {"id": I, "title": f"Task {I}", "done": False, "created_at": "2026-01-01T00:00:00+00:00"}
        for I in range(1, 21)
    ]
    _Write(TempDataFile, ManyTodos)
    Response = Client.get("/")
    assert Response.status_code == 200
    assert b"Task 20" in Response.data


def test_Index_corruptedStorage_raisesException(Client, TempDataFile):
    with open(TempDataFile, "w") as F:
        F.write("corrupted")
    with pytest.raises(Exception):
        Client.get("/")


# ---------------------------------------------------------------------------
# POST /add
# ---------------------------------------------------------------------------

def test_AddTodo_validTitle_todoSavedAndRedirects(Client, TempDataFile):
    Response = Client.post("/add", data={"title": "New Task"})
    assert Response.status_code == 302
    assert any(T["title"] == "New Task" for T in TodoApp.LoadTodos())


def test_AddTodo_emptyTitle_noTodoAdded(Client, TempDataFile):
    Client.post("/add", data={"title": ""})
    assert TodoApp.LoadTodos() == []


def test_AddTodo_whitespaceOnlyTitle_noTodoAdded(Client, TempDataFile):
    Client.post("/add", data={"title": "   "})
    assert TodoApp.LoadTodos() == []


def test_AddTodo_noTitleField_noTodoAdded(Client, TempDataFile):
    Response = Client.post("/add", data={})
    assert Response.status_code == 302
    assert TodoApp.LoadTodos() == []


# ---------------------------------------------------------------------------
# POST /done/<id>
# ---------------------------------------------------------------------------

def test_ToggleDone_doneIsFalse_setsTrueAndRedirects(Client, TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Response = Client.post("/done/1")
    assert Response.status_code == 302
    Todo = next(T for T in TodoApp.LoadTodos() if T["id"] == 1)
    assert Todo["done"] is True


def test_ToggleDone_noTodos_redirectsWithoutCrash(Client):
    Response = Client.post("/done/1")
    assert Response.status_code == 302


def test_ToggleDone_toggleTwice_restoresOriginalState(Client, TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Client.post("/done/1")
    Client.post("/done/1")
    Todo = next(T for T in TodoApp.LoadTodos() if T["id"] == 1)
    assert Todo["done"] is False


def test_ToggleDone_nonExistentId_redirectsWithoutCrash(Client, TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Response = Client.post("/done/999")
    assert Response.status_code == 302
    assert len(TodoApp.LoadTodos()) == 2


# ---------------------------------------------------------------------------
# POST /delete/<id>
# ---------------------------------------------------------------------------

def test_DeleteTodo_existingId_removesTodAndRedirects(Client, TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Response = Client.post("/delete/1")
    assert Response.status_code == 302
    assert not any(T["id"] == 1 for T in TodoApp.LoadTodos())


def test_DeleteTodo_noTodos_redirectsWithoutCrash(Client):
    Response = Client.post("/delete/1")
    assert Response.status_code == 302


def test_DeleteTodo_lastTodo_listBecomesEmpty(Client, TempDataFile):
    _Write(TempDataFile, [SampleTodos[0]])
    Client.post("/delete/1")
    assert TodoApp.LoadTodos() == []


def test_DeleteTodo_nonExistentId_noTodoRemoved(Client, TempDataFile):
    _Write(TempDataFile, SampleTodos)
    Response = Client.post("/delete/999")
    assert Response.status_code == 302
    assert len(TodoApp.LoadTodos()) == 2
