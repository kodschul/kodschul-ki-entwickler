# Übung: Spec-Driven Development

**Zeit:** 13:15 – 15:00 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Spec schreiben (20 min)

**Ziel:** Spec für das Feature "Fälligkeitsdatum" erstellen, bevor Code geschrieben wird.

**Prompt (in Copilot Chat – Agent-Modus):**

```
Erstelle eine Spec-Datei unter specs/due-dates.md für das Feature
"Fälligkeitsdatum für Todos".

Die Spec muss enthalten:
- User Story
- Datenmodell-Änderung in todos.json (neues Feld due_date, ISO-Format, optional)
- UI-Anforderungen (Eingabefeld + Anzeige in Liste + visuelle Markierung bei Überfälligkeit)
- Betroffene Routen (/add POST, / GET)
- Mindestens 4 Akzeptanzkriterien als Checkboxen

Schreibe NUR die Spec. Keinen Code. Warte auf mein OK.
```

**Danach:** Lies die Spec durch.

- Fehlt etwas?
- Ist ein Kriterium unklar?
- Verbessere die Spec bevor du weitermachst.

---

## Aufgabe 2 – Feature implementieren (25 min)

**Erst wenn die Spec fertig ist – Spec mit `#` referenzieren:**

```
Implementiere das Feature aus #specs/due-dates.md.
- Ändere app.py (Route /add und /)
- Ändere das Template templates/index.html
- Halte dich genau an die Spec
- Informiere mich bei Unklarheiten, bevor du entscheidest
```

**Prüfen:**

```bash
FLASK_DEBUG=1 python app.py
```

Öffne `http://localhost:5000` – funktioniert das Datum-Feld?

---

## Aufgabe 3 – Tests schreiben (20 min)

**Nutze den `test-writer` Agent oder den `/spec-test` Prompt:**

```
Schreibe Tests für das Due-Dates-Feature.
Orientiere dich an den Akzeptanzkriterien in #specs/due-dates.md.
Nutze das bestehende client-Fixture aus test_app.py.
```

Ausführen:

```bash
python -m pytest test_app.py -v --tb=short
```

Ziel: Alle Tests grün.

---

## Aufgabe 4 – Spec vs. Implementierung (15 min)

```
Vergleiche die aktuelle Implementierung in #app.py und #templates/index.html
mit der Spec in #specs/due-dates.md.

Erstelle eine kurze Tabelle:
| Akzeptanzkriterium | Implementiert? | Abweichung |
```

**Diskussion:**

- Wo weicht Copilot von der Spec ab?
- War die Spec präzise genug?
- Was würdest du an der Spec verbessern?

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] `specs/due-dates.md` geschrieben und reviewed
- [ ] Feature Due-Dates in `app.py` + Template implementiert
- [ ] Tests für das Feature geschrieben
- [ ] Implementierung gegen die Spec verglichen
