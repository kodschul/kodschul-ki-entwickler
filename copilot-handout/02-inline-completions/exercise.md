# Übung: Inline Completions

**Zeit:** 90 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Shortcuts kennenlernen (20 min)

Öffne `app.py`. Gehe ans Ende der Datei und schreibe:

```python
# Hilfsfunktion: Gibt alle Todos zurück die heute fällig sind
def func_get_due_today(todos):
```

**Ausprobieren:**

1. Warte auf Ghost Text
2. `⌥ ]` / `Alt ]` – nächster Vorschlag
3. `⌥ [` / `Alt [` – vorheriger Vorschlag
4. `⌥ Enter` / `Alt Enter` – alle Vorschläge im Panel
5. `⌘ →` / `Ctrl →` – Wort für Wort annehmen

**Fragen:**

- Wie viele verschiedene Vorschläge bietet Copilot an?
- Welcher ist am sinnvollsten?

---

## Aufgabe 2 – Kontext mit Kommentar steuern (20 min)

Schreibe drei Varianten der gleichen Funktion und beobachte wie der Kommentar den Vorschlag ändert:

**Variante A – kein Kommentar:**

```python
def func_validate_todo(title):
    |
```

**Variante B – kurzer Kommentar:**

```python
# Validiert den Todo-Titel
def func_validate_todo(title):
    |
```

**Variante C – präziser Kommentar:**

```python
# Validiert den Todo-Titel: nicht leer, max 200 Zeichen,
# gibt (True, "") bei Erfolg oder (False, Fehlermeldung) zurück
def func_validate_todo(title):
    |
```

**Beobachten:** Wie unterscheiden sich die Vorschläge?

---

## Aufgabe 3 – Docstring-First (20 min)

Schreibe zuerst den Docstring, dann lässt du Copilot die Implementierung generieren:

```python
def func_format_due_date(due_date_str):
    """
    Formatiert ein ISO-Datum (YYYY-MM-DD) für die Anzeige.

    - Gibt "Kein Datum" zurück wenn due_date_str leer/None ist
    - Gibt "Überfällig" zurück wenn das Datum in der Vergangenheit liegt
    - Sonst: gibt "Fällig am DD.MM.YYYY" zurück

    Args:
        due_date_str: ISO-Datumsstring oder None
    Returns:
        Formatierter String für die UI
    """
    |
```

Akzeptiere den Vorschlag. Schreibe dann einen Test:

```python
def test_format_due_date():
    |  # Copilot sollte aus dem Docstring Tests ableiten
```

---

## Aufgabe 4 – Next Edit Suggestion (15 min)

1. Öffne `app.py`
2. Benenne eine Route um: ändere `/add` in `/todo/add`
3. Beobachte: Schlägt Copilot vor, alle Referenzen zu aktualisieren?
4. Drücke `Tab` um jeden Vorschlag anzunehmen

**Alternativ:**

```python
# Ändere den Parameter-Namen in einer Funktion
# und beobachte ob Copilot die Aufrufe anpasst
```

---

## Aufgabe 5 – Completions gezielt deaktivieren (15 min)

Füge in `.vscode/settings.json` hinzu:

```json
{
  "github.copilot.enable": {
    "*": true,
    "markdown": false,
    "plaintext": false
  }
}
```

Öffne `todos.json` – erscheint noch Ghost Text?  
Öffne `app.py` – erscheint Ghost Text?
