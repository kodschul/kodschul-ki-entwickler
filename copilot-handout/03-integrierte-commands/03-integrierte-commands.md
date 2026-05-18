# 03 – Integrierte Commands

**Block:** 90 min | **Tag 1**

---

## Was sind integrierte Commands?

Integrierte Commands sind **eingebaute Slash-Befehle** in Copilot Chat – keine eigenen Dateien nötig, sofort verfügbar.

```
/explain   → Code erklären
/fix       → Fehler beheben
/tests     → Tests generieren
/doc       → Dokumentation generieren
/new       → Neues Projekt/Datei scaffolden
/newNotebook → Jupyter Notebook erstellen
```

> Eingabe: einfach `/befehl` in den Chat tippen.

---

## /explain – Code verstehen

```
/explain

/explain Was macht diese Regex?

/explain #file:app.py – fokussiere auf die Fehlerbehandlung
```

**Wann nutzen:**

- Fremden Code verstehen
- Komplexe Logik analysieren
- Algorithmen erklären lassen
- Onboarding in Legacy-Code

**Mit Kontext:**

```
/explain #sym:func_load_todos
```

---

## /fix – Fehler beheben

```
/fix

/fix Der Test schlägt fehl: AssertionError: 302 != 200

/fix #terminalLastCommand
```

**Wie es funktioniert:**

1. Markiere den fehlerhaften Code (optional)
2. Tippe `/fix` + Fehlerbeschreibung
3. Copilot analysiert und schlägt eine Korrektur vor
4. Diff anzeigen → annehmen oder ablehnen

**Besonders stark bei:**

- Syntax-Fehlern
- Typ-Fehlern (TypeErrors, AttributeErrors)
- Logikfehlern mit klarem Testfehler
- Import-Problemen

---

## /tests – Tests generieren

```
/tests

/tests Schreibe pytest-Tests für alle Routes in #file:app.py

/tests Füge Edge-Cases für die /add Route hinzu
```

**Konfigurieren was /tests generiert:**

```json
// .vscode/settings.json
{
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze pytest. Schreibe immer happy path UND edge case Tests. Kommentare auf Deutsch."
    }
  ]
}
```

**Oder via `.instructions.md`:**

```markdown
---
applyTo: "**/test_*.py"
---

- Nutze pytest mit dem bestehenden `client`-Fixture
- Schreibe immer: happy path + leere Eingabe + ungültiger Wert
- Kommentare auf Deutsch
- Keine neuen Fixtures einführen
```

---

## /doc – Dokumentation generieren

```
/doc

/doc Erstelle einen Docstring für alle Funktionen in #file:app.py

/doc Schreibe eine README.md für dieses Projekt
```

**Konfigurieren:**

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "text": "Docstrings im Google-Style-Format auf Deutsch."
    }
  ]
}
```

---

## /new – Projekt oder Datei scaffolden

```
/new Flask REST API mit SQLAlchemy und pytest

/new Python-Klasse für einen Todo-Service mit CRUD-Methoden

/new GitHub Actions Workflow für Python-Tests
```

**Wie es funktioniert:**

- Copilot generiert eine **Vorschau** im Chat
- Dann: Workspace-Explorer oder direkt speichern
- Ideal für Boilerplate, neue Features, neue Microservices

---

## /newNotebook – Jupyter Notebook

```
/newNotebook Datenanalyse der todos.json Datei

/newNotebook Python Tutorial für Flask-Routen
```

→ Erstellt ein `.ipynb`-Notebook direkt im Workspace.

---

## /terminal – Terminal-Hilfe im Chat

```
/terminal Wie führe ich pytest mit Coverage aus?

/terminal Wie finde ich alle Python-Dateien die sich geändert haben?
```

→ Copilot antwortet mit erklärbarem Shell-Befehl + Erklärung.

> **Unterschied zu `gh copilot suggest`:** `/terminal` gibt Erklärungen + Befehl im Chat. `gh copilot suggest` interaktiv im Terminal.

---

## /search – Workspace durchsuchen

```
/search Wo wird der Flask-Secret-Key konfiguriert?

/search Alle Stellen wo todos.json geöffnet wird
```

→ Nutzt semantische Suche im Workspace (ähnlich wie `@workspace`).

---

## Rechtsklick-Commands (Kontextmenü)

Markiere Code → Rechtsklick → **Copilot**:

| Kontextmenü-Eintrag | Entspricht                         |
| ------------------- | ---------------------------------- |
| Explain             | `/explain` mit Selection           |
| Fix                 | `/fix` mit Selection               |
| Generate Tests      | `/tests` mit Selection             |
| Generate Docs       | `/doc` mit Selection               |
| Review and Comment  | Code-Review mit Inline-Kommentaren |
| Start Inline Chat   | `⌘ I` / `Ctrl I`                   |

---

## Copilot Review (Code-Review)

```
Markiere Datei → Rechtsklick → Copilot → Review and Comment
```

Oder in Chat:

```
Bitte führe einen Code-Review von #file:app.py durch.
Fokus: Sicherheit, Fehlerbehandlung, Code-Qualität.
Ausgabe als Markdown-Tabelle: Problem | Zeile | Schwere | Empfehlung
```

**Review-Einstellungen:**

```json
{
  "github.copilot.chat.reviewSelection.instructions": [
    {
      "file": ".github/instructions/security.instructions.md"
    }
  ]
}
```

---

## Alle Commands auf einen Blick

| Command        | Beschreibung                     | Kontext-Tipp                        |
| -------------- | -------------------------------- | ----------------------------------- |
| `/explain`     | Code erklären                    | Mit `#sym` für Funktionen           |
| `/fix`         | Fehler beheben                   | Mit `#terminalLastCommand`          |
| `/tests`       | Tests generieren                 | Mit `#file` für Scope               |
| `/doc`         | Dokumentation generieren         | Mit `#editor` für aktive Datei      |
| `/new`         | Boilerplate scaffolden           | Beschreibung so präzise wie möglich |
| `/newNotebook` | Jupyter Notebook erstellen       | Thema angeben                       |
| `/terminal`    | Shell-Befehl erklären/finden     | Fehlermeldung einfügen              |
| `/search`      | Workspace semantisch durchsuchen | Konzept statt Dateiname             |
