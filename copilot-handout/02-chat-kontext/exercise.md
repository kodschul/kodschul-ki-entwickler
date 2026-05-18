# Übung: Chat & Kontext-Variablen

**Zeit:** 90 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Kontext-Variablen erkunden (20 min)

Öffne Copilot Chat. Probiere folgende Prompts aus und beobachte die Antwortqualität:

**Ohne Kontext:**

```
Erkläre wie die Todos gespeichert werden.
```

**Mit #file:**

```
Erkläre wie die Todos gespeichert werden. #file:app.py
```

**Mit #sym:**

```
Erkläre #sym:func_load_todos und #sym:func_save_todos
```

**Vergleich:** Wie unterscheiden sich die Antworten?

---

## Aufgabe 2 – @workspace nutzen (20 min)

```
@workspace Wo wird todos.json gelesen und wo wird es geschrieben?
```

```
@workspace Welche Flask-Routen existieren und welche haben Tests?
```

```
@workspace Gibt es Code-Duplikate zwischen app.py und utils.py?
```

**Beobachten:** Was findet `@workspace` dass ein normaler Prompt nicht findet?

---

## Aufgabe 3 – Inline Chat (20 min)

1. Öffne `app.py`
2. Gehe zur Route `/add`
3. Drücke `⌘ I` / `Ctrl I`
4. Gib ein:

```
Füge Input-Validierung hinzu: Titel darf nicht leer sein und nicht länger als 200 Zeichen.
Bei Fehler: flash-Meldung und Redirect zurück zum Formular.
```

5. Prüfe den Diff – ist er korrekt?
6. `⌘ Enter` zum Annehmen oder `Esc` zum Ablehnen

---

## Aufgabe 4 – #terminalLastCommand (15 min)

```bash
# Im Terminal ausführen:
python -m pytest test_app.py -v
```

Falls Tests fehlschlagen → in Copilot Chat:

```
#terminalLastCommand
Warum schlägt dieser Test fehl? Wie behebe ich es?
```

Falls alle Tests grün → einen Test absichtlich kaputt machen:

```python
# test_app.py – temporär ändern:
def test_add_todo(client):
    assert False, "Absichtlicher Fehler"
```

---

## Aufgabe 5 – #changes für Code-Review (15 min)

Mache eine kleine Änderung in `app.py` (z.B. Kommentar hinzufügen).  
Dann in Copilot Chat:

```
Mache einen kurzen Code-Review meiner Änderungen. #changes
Gibt es Probleme oder Verbesserungsvorschläge?
```

---

## Bonus – @github (falls Repo auf GitHub)

```
@github Welche offenen Issues gibt es zu diesem Repository?

@github Was wurde zuletzt geändert in diesem Projekt?

@github Erstelle eine Zusammenfassung der letzten 5 Commits.
```
