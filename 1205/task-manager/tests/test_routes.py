from models import Task


class TestIndex:
    def test_get_index_returns_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_empty_state_message(self, client):
        resp = client.get("/")
        assert b"No tasks yet" in resp.data


class TestCreateTask:
    def test_create_task_redirects(self, client):
        resp = client.post("/tasks", data={"title": "Buy milk"})
        assert resp.status_code == 302
        assert resp.headers["Location"] == "/"

    def test_created_task_appears_in_list(self, client):
        client.post("/tasks", data={"title": "Buy milk"})
        resp = client.get("/")
        assert b"Buy milk" in resp.data

    def test_empty_title_flashes_error(self, client):
        resp = client.post("/tasks", data={"title": ""}, follow_redirects=True)
        assert b"cannot be empty" in resp.data

    def test_whitespace_only_title_flashes_error(self, client):
        resp = client.post("/tasks", data={"title": "   "}, follow_redirects=True)
        assert b"cannot be empty" in resp.data

    def test_title_too_long_flashes_error(self, client):
        long_title = "x" * 201
        resp = client.post("/tasks", data={"title": long_title}, follow_redirects=True)
        assert b"200 characters" in resp.data

    def test_title_at_max_length_accepted(self, client, db, app):
        max_title = "x" * 200
        resp = client.post("/tasks", data={"title": max_title})
        assert resp.status_code == 302
        with app.app_context():
            task = Task.query.first()
            assert task is not None
            assert len(task.title) == 200

    def test_task_persists_after_redirect(self, client, app):
        client.post("/tasks", data={"title": "Persist me"})
        with app.app_context():
            task = Task.query.filter_by(title="Persist me").first()
            assert task is not None


class TestToggleTask:
    def test_toggle_marks_complete(self, client, app):
        client.post("/tasks", data={"title": "Toggle me"})
        with app.app_context():
            task = Task.query.first()
            task_id = task.id
        resp = client.post(f"/tasks/{task_id}/toggle")
        assert resp.status_code == 302
        with app.app_context():
            task = Task.query.get(task_id)
            assert task.completed is True

    def test_toggle_twice_returns_to_incomplete(self, client, app):
        client.post("/tasks", data={"title": "Toggle twice"})
        with app.app_context():
            task_id = Task.query.first().id
        client.post(f"/tasks/{task_id}/toggle")
        client.post(f"/tasks/{task_id}/toggle")
        with app.app_context():
            assert Task.query.get(task_id).completed is False

    def test_toggle_nonexistent_returns_404(self, client):
        resp = client.post("/tasks/9999/toggle")
        assert resp.status_code == 404


class TestDeleteTask:
    def test_delete_removes_task(self, client, app):
        client.post("/tasks", data={"title": "Delete me"})
        with app.app_context():
            task_id = Task.query.first().id
        client.post(f"/tasks/{task_id}/delete")
        with app.app_context():
            assert Task.query.get(task_id) is None

    def test_delete_redirects_to_index(self, client, app):
        client.post("/tasks", data={"title": "Delete redirect"})
        with app.app_context():
            task_id = Task.query.first().id
        resp = client.post(f"/tasks/{task_id}/delete")
        assert resp.status_code == 302
        assert resp.headers["Location"] == "/"

    def test_delete_last_task_shows_empty_state(self, client, app):
        client.post("/tasks", data={"title": "Last task"})
        with app.app_context():
            task_id = Task.query.first().id
        client.post(f"/tasks/{task_id}/delete")
        resp = client.get("/")
        assert b"No tasks yet" in resp.data

    def test_delete_nonexistent_returns_404(self, client):
        resp = client.post("/tasks/9999/delete")
        assert resp.status_code == 404
