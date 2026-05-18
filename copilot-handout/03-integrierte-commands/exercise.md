# Übung: Integrierte Commands

**Zeit:** 90 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – /explain (15 min)

**Schritt 1:** Öffne `app.py` und markiere die Funktion `func_load_todos`.

**Schritt 2:** Tippe in Copilot Chat:

```
/explain #sym:func_load_todos
```

**Schritt 3:** Frage nach Details:

```
Was passiert wenn todos.json nicht existiert? Ist das sicher?
```

**Schritt 4:** Erkläre etwas Komplexes:

```
/explain Warum nutzen wir redirect(url_for(...)) statt render_template direkt?
```

---

## Aufgabe 2 – /fix (20 min)

**Schritt 1 – Absichtlichen Fehler einbauen:**

Ändere in `app.py` temporär:

```python
# Statt:
todos = func_load_todos()
# Schreibe:
todos = load_todos()  # falsche Funktion
```

**Schritt 2:** Führe die Tests aus:

```bash
python -m pytest test_app.py -q
```

**Schritt 3:** In Copilot Chat:

```
/fix #terminalLastCommand
```

**Schritt 4:** Unterschied testen – mit vs. ohne Fehler-Output:

```
/fix Die App startet nicht – warum?
```

vs.

```
/fix #terminalLastCommand
Fehler: NameError: name 'load_todos' is not defined
```

**Beobachten:** Welche Variante gibt bessere Fixes?

---

## Aufgabe 3 – /tests (20 min)

**Schritt 1:** Generiere Tests für eine bestimmte Route:

```
/tests Schreibe pytest-Tests für die /add Route in #file:app.py.
Nutze das bestehende client-Fixture. Happy path + leere Eingabe.
```

**Schritt 2:** Füge in `.vscode/settings.json` Test-Instructions hinzu:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze pytest. Immer happy path + edge case. Kommentare auf Deutsch. Kein neues Fixture."
    }
  ]
}
```

**Schritt 3:** Generiere erneut – merkst du einen Unterschied?

```
/tests #file:app.py
```

**Schritt 4:** Tests ausführen:

```bash
python -m pytest test_app.py -v --tb=short
```

---

## Aufgabe 4 – /doc (15 min)

**Schritt 1:**

```
/doc Erstelle Docstrings für alle Funktionen in #file:app.py
```

**Schritt 2:** Spezifischen Stil anfordern:

```
/doc Schreibe einen Google-Style Docstring für #sym:func_load_todos
Sprache: Deutsch
```

**Schritt 3:** README generieren:

```
/doc Erstelle eine README.md für diese Todo-App mit:
- Projektbeschreibung
- Installation (pip install -r requirements.txt)
- Starten (FLASK_DEBUG=1 python app.py)
- Tests ausführen
```

---

## Aufgabe 5 – /new (20 min)

**Scaffold eine neue Hilfsklasse:**

```
/new Python-Klasse TodoService für die Todo-App.
Methoden: get_all(), get_by_id(id), add(title), delete(id), toggle(id)
Datenspeicherung in todos.json
Keine Flask-Abhängigkeit
```

**Scaffold einen GitHub Actions Workflow:**

```
/new GitHub Actions Workflow der bei jedem Push pytest ausführt.
Python 3.12, Ubuntu, requirements.txt installieren.
```

**Beobachten:** Wie präzise ist das Scaffolding? Was müsstest du noch anpassen?

---

## Aufgabe 6 – Rechtsklick Review (10 min)

1. Öffne `app.py`
2. `Strg+A` / `⌘ A` – alles markieren
3. Rechtsklick → **Copilot** → **Review and Comment**

Copilot fügt Inline-Kommentare direkt in den Code ein.

**Fragen:** Welche Probleme findet Copilot? Sind sie alle korrekt?
