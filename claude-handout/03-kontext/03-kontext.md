# 03 – Kontext bereitstellen

**Block:** 90 min | **Tag 2**

---

## Wie funktioniert das unter der Haube?

```
Start
  → CLAUDE.md wird automatisch gelesen        → Projektkontext
  → Claude nutzt Tools (Read, Glob, Grep)       → holt sich weiteren Kontext selbst
  → Erste Antwort ist bereits kontextuell korrekt
```

> Anders als bei IDE-Chats mit `#file`/`#codebase`-Referenzen holt sich Claude Code Kontext meist **aktiv selbst** über seine Tools, statt dass du ihn manuell "hineinziehst".

---

## Automatischer vs. manueller Kontext

| Mechanismus           | Wie                                                                     |
| --------------------- | ----------------------------------------------------------------------- |
| Automatisch           | `CLAUDE.md` im Projektroot wird bei jedem Start gelesen                 |
| Aktiv durch Claude    | `Read`, `Glob`, `Grep` – Claude durchsucht die Codebase selbst          |
| Manuell (Pfad nennen) | Dateipfad im Prompt nennen: "Lies `app.py` und erkläre die Routen"      |
| Verzeichnis erweitern | `/add-dir <pfad>` – zusätzliche Ordner außerhalb des Projekts freigeben |
| Bild/Screenshot       | In der Zwischenablage einfügen (unterstützte Terminals)                 |
| Extern                | MCP-Server (Modul 13) – Live-Daten von außen                            |

---

## CLAUDE.md – der zentrale Kontext-Mechanismus

`CLAUDE.md` im Projektroot ist das Äquivalent zu `.github/copilot-instructions.md` bei GitHub Copilot – wird aber **nicht optional dazugeladen**, sondern bei jedem Claude-Code-Start automatisch gelesen.

```markdown
# CLAUDE.md

## Project Goal

[Ein Satz was die App tut]

## Commands

FLASK_DEBUG=1 python app.py # Dev-Server
python -m pytest test_app.py -v # Tests

## Architecture

Request → app.py (Flask) → todos.json → Jinja2-Template → Browser

## Do

- Post/Redirect/Get Pattern verwenden
- Daten in todos.json speichern

## Don't

- Kein eval() oder exec()
- Keine Passwörter im Code
```

> Vertiefung zu Konventionen/Vererbung von `CLAUDE.md` in Unterordnern: Modul 06 (Skills & Kontext-Scoping).

---

## Warum / Wann nicht?

| Warum nutzen                                           | Wann nicht                                            |
| ------------------------------------------------------ | ----------------------------------------------------- |
| Gleicher Kontext bei jedem Start                       | Einmaliger Prompt → direkt tippen                     |
| Teamkontext via Git teilbar                            | Sensible Daten → niemals in `CLAUDE.md`, immer `.env` |
| Claude muss nicht bei jeder Session neu erklärt werden | Sehr kleines Skript ohne Struktur → Overhead          |

---

## Kontext bewusst klein halten

Je mehr Dateien Claude lesen muss, desto mehr Tokens werden verbraucht (siehe Modul 10). Praxis-Tipps:

- Gezielt nach Dateien/Ordnern fragen statt "durchsuche alles"
- `CLAUDE.md` kurz halten (Faustregel: unter 100 Zeilen im Root, Details in Unterordnern, Modul 06)
- Große, generierte Ordner (z. B. `node_modules/`, `.venv/`) über `.gitignore`-ähnliche Regeln aus der Suche ausschließen
