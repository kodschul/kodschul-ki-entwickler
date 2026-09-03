# Übung: Skills & .instructions.md

**Zeit:** 90 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Python Instructions erstellen (20 min)

```bash
mkdir -p .github/instructions
```

Erstelle `.github/instructions/python.instructions.md`:

```markdown
---
applyTo: "**/*.py"
description: "Python code generation rules for this project"
---

# Python Guidelines

- Python 3.12+ Syntax (match/case, walrus operator erlaubt)
- Typ-Annotationen für alle Parameter und Rückgabewerte
- F-Strings statt .format() oder %
- Exceptions explizit behandeln: nie blankes `except:`
- `pathlib.Path` statt `os.path` für Dateipfade
```

**Testen:**

Öffne Copilot Chat und gib ein:

```
Schreibe eine Funktion die prüft ob todos.json existiert und lesbar ist.
```

**Beobachten:** Nutzt Copilot Typ-Annotationen und pathlib? Wenn ja → Instruction wirkt.

---

## Aufgabe 2 – Security Instructions erstellen (20 min)

Erstelle `.github/instructions/security.instructions.md`:

```markdown
---
applyTo: "**"
description: "Security rules - applies to all files"
---

# Security Guidelines

- Keine hardcodierten Passwörter, Tokens, API-Keys oder Secrets im Code
- `eval()` und `exec()` sind verboten
- Alle Benutzereingaben validieren bevor Verarbeitung
- Flask: `request.form.get()` statt `request.form[]` (KeyError-Sicherheit)
- Secrets aus Umgebungsvariablen: `os.environ.get("SECRET_KEY", "")`
```

**Testen:**

```
Schreibe eine Route die ein Passwort entgegennimmt und in einer Datei speichert.
```

**Beobachten:** Warnt Copilot vor dem Hardcoding? Schlägt es Umgebungsvariablen vor?

---

## Aufgabe 3 – Testing Instructions + settings.json (20 min)

Erstelle `.github/instructions/testing.instructions.md`:

```markdown
---
applyTo: "**/test_*.py"
description: "pytest rules for this project"
---

# Testing Guidelines

- Immer: happy path + leere/None Eingabe + ungültiger Wert
- Bestehende `client`-Fixture nutzen, keine neuen erstellen
- Test-Namen beschreiben das Szenario: `test_add_todo_mit_leerem_titel_gibt_400`
- Kommentare auf Deutsch
- Nach jedem Test: assert-Nachricht bei nicht-trivialen Assertions
```

Verknüpfe in `.vscode/settings.json`:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ]
}
```

Teste:

```
/tests Schreibe Tests für die /add Route.
```

---

## Aufgabe 4 – Instructions stacking beobachten (15 min)

Öffne eine neue Python-Datei `utils_new.py`.

Tippe in Copilot Chat:

```
Schreibe eine Funktion die alle Todos nach due_date sortiert.
```

**Protokolliere:** Welche Instructions sind aktiv?

- `copilot-instructions.md` → immer
- `python.instructions.md` → weil `*.py`
- `security.instructions.md` → weil `**`
- `testing.instructions.md` → NEIN (weil kein `test_*.py`)

Ist das Ergebnis von allen drei Instructions beeinflusst?

---

## Aufgabe 5 – Eigene Instruction erfinden (15 min)

Erstelle eine Instruction für einen Bereich deiner Wahl:

**Ideen:**

| Instruction             | applyTo        | Inhalt                                             |
| ----------------------- | -------------- | -------------------------------------------------- |
| `flask.instructions.md` | `**/app.py`    | Flask-Konventionen, Route-Patterns, flash() Regeln |
| `html.instructions.md`  | `templates/**` | Tailwind-Klassen nutzen, kein inline-Style         |
| `git.instructions.md`   | `**`           | Commit-Message-Format, Branch-Naming               |

**Vorlage:**

```markdown
---
applyTo: "[DEIN MUSTER]"
description: "[DEINE BESCHREIBUNG]"
---

# [TITEL]

- [Regel 1]
- [Regel 2]
- [Regel 3]
```

**Testen:** Öffne eine passende Datei und beobachte ob Copilot die Regeln befolgt.
