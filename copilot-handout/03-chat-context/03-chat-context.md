# 03 – Chat & Kontext-Variablen

**Block:** 90 min | **Tag 1**

---

## Chat öffnen

| Aktion                  | macOS         | Windows/Linux  |
| ----------------------- | ------------- | -------------- |
| Chat öffnen             | `⌃ ⌘ I`       | `Ctrl Alt I`   |
| Inline Chat (im Editor) | `⌘ I`         | `Ctrl I`       |
| Quick Chat              | `⌘ Shift I`   | `Ctrl Shift I` |
| Chat leeren             | `+` Icon oben | `+` Icon oben  |

---

## Chat-Modi

| Modus     | Symbol | Wann nutzen                                            |
| --------- | ------ | ------------------------------------------------------ |
| **Ask**   | 💬     | Fragen, Erklärungen, Code-Review ohne Änderungen       |
| **Edit**  | ✏️     | Dateien direkt bearbeiten (zeigt Diff)                 |
| **Agent** | 🤖     | Multi-Step-Aufgaben, Terminal-Befehle, mehrere Dateien |

> **Wechseln:** Dropdown links unten im Chat-Eingabefeld.

---

## Kontext-Variablen (`#`)

Füge gezielt Dateien, Symbole oder den gesamten Workspace als Kontext hinzu:

| Variable               | Beschreibung                                     |
| ---------------------- | ------------------------------------------------ |
| `#file`                | Datei auswählen und als Kontext hinzufügen       |
| `#codebase`            | Gesamte Codebase durchsuchen (semantische Suche) |
| `#selection`           | Aktuell markierter Text                          |
| `#editor`              | Inhalt der aktiven Editor-Datei                  |
| `#terminalSelection`   | Markierter Text im Terminal                      |
| `#terminalLastCommand` | Letzter Befehl + Output im Terminal              |
| `#sym`                 | Symbol (Funktion, Klasse) auswählen              |
| `#changes`             | Git-Änderungen (staged + unstaged)               |
| `#testFailure`         | Fehlgeschlagener Test + Stack Trace              |

**Beispiele:**

```
Erkläre mir #file:app.py

Was macht die Funktion #sym:func_load_todos?

Warum schlägt #testFailure fehl?

Erstelle einen Code-Review für #changes
```

---

## Agents (`@`)

Agents sind spezialisierte Chat-Teilnehmer mit Zugriff auf bestimmte Daten:

| Agent        | Zugriff auf                                     |
| ------------ | ----------------------------------------------- |
| `@workspace` | Alle Dateien im Workspace (semantische Suche)   |
| `@github`    | GitHub-Repos, Issues, PRs, Commits, Code Search |
| `@vscode`    | VS Code Einstellungen, Befehle, Dokumentation   |
| `@terminal`  | Terminal-Kontext und Befehlsvorschläge          |

**Beispiele:**

```
@workspace Wo wird todos.json gelesen?

@github Welche offenen Issues gibt es zu diesem Projekt?

@vscode Wie stelle ich den Python-Interpreter ein?

@terminal Warum schlägt der letzte Befehl fehl?
```

---

## Kontext effizient aufbauen

### Zu viel Kontext → schlechtere Antworten

```
❌ "Analysiere mein gesamtes Projekt und erkläre alles"
✅ "Erkläre #file:app.py – fokussiere auf die Route /add"
```

### Präzise Referenzen statt vage Beschreibungen

```
❌ "Schau dir die Todo-Logik an"
✅ "Schau dir #sym:func_load_todos und #sym:func_save_todos an"
```

### Kontext für Follow-up-Fragen nutzen

```
Erste Frage:  "Erkläre #file:app.py"
Follow-up:    "Wie würde ich eine Lösch-Route hinzufügen?"
              → Copilot hat app.py noch im Kontext
```

---

## Inline Chat – direkt im Code

`⌘ I` / `Ctrl I` öffnet Chat direkt am Cursor:

```python
def func_load_todos():
    # ← Cursor hier, ⌘ I drücken
    # Prompt: "Füge Error-Handling hinzu wenn die Datei nicht existiert"
```

**Inline Chat Shortcuts:**

| Aktion              | Taste      |
| ------------------- | ---------- |
| Änderungen accept   | `⌘ Enter`  |
| Änderungen ablehnen | `Esc`      |
| Nächste Änderung    | `F7`       |
| Vorherige Änderung  | `Shift F7` |

---

## Quick Chat – schnelle Fragen ohne Chat zu öffnen

`⌘ Shift I` / `Ctrl Shift I` → Eingabe → `Enter` → Antwort erscheint kurz.

Ideal für:

- Schnelle Erklärungen
- Befehl nachschlagen
- Kurze Frage zu aktuellem File
