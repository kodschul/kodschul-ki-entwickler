import json
import pytest
import app as app_module
from app import app, sorted_todos, API_TOKEN


@pytest.fixture
def client(tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def todos_from_file(monkeypatch_data_file):
    with open(monkeypatch_data_file) as f:
        return json.load(f)


def test_add_todo_with_priority(client, tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Buy milk", "priority": "high"})
    todos = todos_from_file(data_file)
    assert todos[0]["priority"] == "high"


def test_add_todo_defaults_to_medium(client, tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Read book"})
    todos = todos_from_file(data_file)
    assert todos[0]["priority"] == "medium"


def test_invalid_priority_falls_back_to_medium(client, tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Hack", "priority": "critical"})
    todos = todos_from_file(data_file)
    assert todos[0]["priority"] == "medium"


def test_sorted_todos_order():
    todos = [
        {"id": 1, "title": "Low task", "priority": "low"},
        {"id": 2, "title": "High task", "priority": "high"},
        {"id": 3, "title": "Medium task", "priority": "medium"},
    ]
    result = sorted_todos(todos)
    assert [t["priority"] for t in result] == ["high", "medium", "low"]


def test_index_renders_in_priority_order(client, tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Low task", "priority": "low"})
    client.post("/add", data={"title": "High task", "priority": "high"})
    client.post("/add", data={"title": "Medium task", "priority": "medium"})
    resp = client.get("/")
    html = resp.data.decode()
    assert html.index("High task") < html.index("Medium task") < html.index("Low task")


def test_edit_updates_priority(client, tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Task", "priority": "low"})
    todo_id = todos_from_file(data_file)[0]["id"]
    client.post(f"/edit/{todo_id}", data={"title": "Task", "priority": "high"})
    assert todos_from_file(data_file)[0]["priority"] == "high"


def test_priority_badge_shown_in_html(client, tmp_path, monkeypatch):
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Urgent", "priority": "high"})
    resp = client.get("/")
    assert b"High" in resp.data


# ---------------------------------------------------------------------------
# Sicherheitstests – dokumentieren bekannte Schwachstellen der Anwendung
# ---------------------------------------------------------------------------


def test_hardcoded_token_is_default():
    """Sicherheitslücke: Wenn die Umgebungsvariable API_TOKEN nicht gesetzt ist,
    verwendet die App den hart codierten Standardwert 'secret-token-1234'.
    Jeder, der den Quellcode kennt, kann sich damit authentifizieren."""
    assert API_TOKEN == "secret-token-1234"


def test_swagger_docs_exposes_token(client):
    """Sicherheitslücke: Die öffentlich erreichbare API-Spezifikation unter /apispec.json
    enthält den Klartext-Token 'secret-token-1234' in der Beschreibung der
    securityDefinitions. Damit ist der Token ohne Authentifizierung einsehbar."""
    resp = client.get("/apispec.json")
    assert resp.status_code == 200
    assert b"secret-token-1234" in resp.data


def test_api_accessible_with_known_default_token(client):
    """Sicherheitslücke: Der hart codierte Standardtoken 'secret-token-1234'
    gewährt vollen Zugriff auf die API. Da der Token öffentlich bekannt ist
    (Quellcode, Swagger-UI), kann jeder Angreifer Todos anlegen."""
    resp = client.post(
        "/api/todos",
        json={"title": "Angreifer-Todo", "priority": "high"},
        headers={"Authorization": "Bearer secret-token-1234"},
    )
    assert resp.status_code == 201
    daten = resp.get_json()
    assert daten["title"] == "Angreifer-Todo"


def test_csrf_delete_no_token_required(client, tmp_path, monkeypatch):
    """Sicherheitslücke: Die Route POST /delete/<id> ist nicht durch einen
    CSRF-Token geschützt. Eine fremde Website kann im Namen des eingeloggten
    Nutzers Todos löschen, ohne dass ein Geheimnis benötigt wird."""
    # Vorbereitung: Todo anlegen
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Zu löschendes Todo", "priority": "medium"})
    todo_id = todos_from_file(data_file)[0]["id"]

    # Löschanfrage ohne CSRF-Token – muss trotzdem erfolgreich sein (302)
    resp = client.post(f"/delete/{todo_id}")
    assert resp.status_code == 302

    # Todo wurde tatsächlich entfernt
    verbleibende = todos_from_file(data_file)
    assert all(t["id"] != todo_id for t in verbleibende)


def test_csrf_add_no_token_required(client):
    """Sicherheitslücke: Die Route POST /add prüft keinen CSRF-Token.
    Eine präparierte externe Seite kann beliebige Todos im Namen des Nutzers
    erstellen, solange der Browser die Session-Cookies mitsendet."""
    resp = client.post("/add", data={"title": "CSRF-Todo", "priority": "low"})
    # Ohne CSRF-Schutz wird die Anfrage normal verarbeitet und leitet weiter
    assert resp.status_code == 302


def test_csrf_toggle_no_token_required(client, tmp_path, monkeypatch):
    """Sicherheitslücke: Die Route POST /toggle/<id> ist ebenfalls ohne
    CSRF-Schutz erreichbar. Der Status eines Todos kann so von einer externen
    Seite manipuliert werden."""
    # Vorbereitung: Todo anlegen
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Toggle-Todo", "priority": "low"})
    todo_id = todos_from_file(data_file)[0]["id"]

    # Toggle-Anfrage ohne CSRF-Token – muss trotzdem erfolgreich sein (302)
    resp = client.post(f"/toggle/{todo_id}")
    assert resp.status_code == 302

    # Status wurde tatsächlich umgeschaltet (done: True)
    aktualisiert = todos_from_file(data_file)
    toggle_todo = next(t for t in aktualisiert if t["id"] == todo_id)
    assert toggle_todo["done"] is True


# ---------------------------------------------------------------------------
# Neue Sicherheitstests – dokumentieren weitere Schwachstellen
# ---------------------------------------------------------------------------


def test_api_rejects_missing_auth_header(client):
    """Sicherheitslücke: POST /api/todos ohne Authorization-Header muss 401 zurückgeben."""
    # Anfrage vollständig ohne Authorization-Header
    resp = client.post("/api/todos", json={"title": "Kein Header"})
    assert resp.status_code == 401


def test_api_rejects_wrong_token(client):
    """Sicherheitslücke: POST /api/todos mit falschem Bearer-Token muss 401 zurückgeben."""
    # Falscher Token – darf keinen Zugriff gewähren
    resp = client.post(
        "/api/todos",
        json={"title": "Falscher Token"},
        headers={"Authorization": "Bearer wrong-token"},
    )
    assert resp.status_code == 401


def test_api_rejects_malformed_auth(client):
    """Sicherheitslücke: POST /api/todos ohne 'Bearer '-Präfix muss 401 zurückgeben,
    da das Format des Authorization-Headers nicht dem erwarteten Schema entspricht."""
    # Token ohne "Bearer "-Präfix – kein gültiges Format
    resp = client.post(
        "/api/todos",
        json={"title": "Kein Bearer Präfix"},
        headers={"Authorization": "secret-token-1234"},
    )
    assert resp.status_code == 401


def test_token_comparison_uses_constant_time():
    """Fix bestätigt: require_token verwendet hmac.compare_digest statt '!=',
    womit Timing-Angriffe auf den Token verhindert werden."""
    import inspect

    quellcode = inspect.getsource(app_module.require_token)
    assert "compare_digest" in quellcode


def test_edit_csrf_no_token_required(client, tmp_path, monkeypatch):
    """Sicherheitslücke: POST /edit/<id> prüft keinen CSRF-Token – externe Seiten
    können den Titel eines Todos im Namen des Nutzers ändern."""
    # Vorbereitung: Todo anlegen
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))
    client.post("/add", data={"title": "Originaltitel", "priority": "low"})
    todo_id = todos_from_file(data_file)[0]["id"]

    # Edit-Anfrage ohne CSRF-Token – muss trotzdem erfolgreich sein (302)
    resp = client.post(f"/edit/{todo_id}", data={"title": "Manipulierter Titel", "priority": "low"})
    assert resp.status_code == 302

    # Titel wurde tatsächlich geändert, obwohl kein CSRF-Token gesendet wurde
    aktualisiert = todos_from_file(data_file)
    bearbeitetes_todo = next(t for t in aktualisiert if t["id"] == todo_id)
    assert bearbeitetes_todo["title"] == "Manipulierter Titel"


# ---------------------------------------------------------------------------
# Neue Sicherheitstests – XSS, Debug-Modus, Fehlerbehandlung, Eingabelänge
# ---------------------------------------------------------------------------


def test_xss_title_is_escaped_in_html(client):
    """Jinja2-Auto-Escaping verhindert gespeichertes XSS: <script>-Tags im Titel dürfen nie roh gerendert werden."""
    # XSS-Nutzlast als Todo-Titel einsenden
    xss_payload = "<script>alert(1)</script>"
    client.post("/add", data={"title": xss_payload, "priority": "low"})

    # Startseite abrufen und auf rohes Script-Tag prüfen
    resp = client.get("/")
    html = resp.data.decode()

    # Entweder ist das Tag HTML-kodiert oder komplett abwesend – niemals roh vorhanden
    assert "<script>alert(1)</script>" not in html


def test_debug_mode_off_in_testing(client):
    """app.debug muss im Test-Kontext False sein, damit keine Stack-Traces an Nutzer geleakt werden."""
    # TESTING=True darf debug nicht einschalten
    assert app.debug is False


def test_api_delete_returns_404_for_nonexistent_id(client):
    """DELETE /api/todos/<id> mit gültigem Token und unbekannter ID muss 404 zurückgeben, nicht 500 oder 200."""
    # Nicht vorhandene ID – Fehlerbehandlung darf keine internen Details preisgeben
    resp = client.delete(
        "/api/todos/99999",
        headers={"Authorization": "Bearer secret-token-1234"},
    )
    assert resp.status_code == 404


def test_title_length_capped_at_200(client, tmp_path, monkeypatch):
    """POST /add mit einem 500-Zeichen-Titel darf maximal 200 Zeichen in der Datenbank und im HTML speichern."""
    data_file = tmp_path / "todos.json"
    monkeypatch.setattr(app_module, "DATA_FILE", str(data_file))

    # Titel mit 500 Zeichen erzeugen
    langer_titel = "A" * 500
    client.post("/add", data={"title": langer_titel, "priority": "low"})

    # Direkt in der JSON-Datei prüfen: Titel wurde auf 200 Zeichen gekürzt
    todos = todos_from_file(data_file)
    assert len(todos[0]["title"]) <= 200

    # Auch im gerenderten HTML darf der rohe 500-Zeichen-String nicht auftauchen
    resp = client.get("/")
    html = resp.data.decode()
    assert langer_titel not in html


def test_toggle_nonexistent_id_does_not_crash(client):
    """POST /toggle/<id> mit unbekannter ID muss mit 302 (Weiterleitung) antworten, nicht mit 500."""
    # Keine Todos vorhanden – graceful no-op erwartet
    resp = client.post("/toggle/99999")
    assert resp.status_code == 302
