# 11 – Skills & .instructions.md

**Block:** 90 min | **Tag 2**

---

## Was sind Instructions / Skills?

Instructions sind **persistente Verhaltensregeln** für Copilot – geladen bei jeder Antwort, ohne dass du sie jedes Mal tippen musst.

```
Copilot antwortet
  → lädt copilot-instructions.md (immer)
  → prüft alle *.instructions.md auf applyTo-Match
  → fügt passende Instructions dem System-Prompt hinzu
  → antwortet mit vollem Kontext
```

> Instructions sind **nicht** dasselbe wie Skills. GitHub Copilot kennt inzwischen beide Konzepte parallel: `.instructions.md` für Regeln, **Agent Skills** (`SKILL.md`) für ganze Fähigkeitspakete – siehe eigener Abschnitt weiter unten.

**Analogie:** Instructions sind wie ein Briefing, das jeder neue Mitarbeiter bekommt, bevor er eine Aufgabe beginnt.

---

## Dateistruktur

```
.github/
├── copilot-instructions.md          ← gilt für ALLES (immer geladen)
└── instructions/
    ├── python.instructions.md       ← gilt für *.py
    ├── flask.instructions.md        ← gilt für app.py
    ├── security.instructions.md    ← gilt für **
    └── testing.instructions.md     ← gilt für test_*.py
```

---

## Frontmatter – alle Felder

```yaml
---
applyTo: "**/*.py" # Glob: welche Dateien lösen diese Instruction aus
description: "..." # Optional: erscheint in VS Code UI
---
```

**`applyTo`-Muster:**

| Muster         | Bedeutung                             |
| -------------- | ------------------------------------- |
| `**`           | Alle Dateien (global)                 |
| `**/*.py`      | Alle Python-Dateien                   |
| `**/test_*.py` | Alle Test-Dateien                     |
| `**/app.py`    | Nur app.py (überall im Projekt)       |
| `templates/**` | Alle Dateien im templates-Ordner      |
| `src/**/*.ts`  | Alle TypeScript-Dateien im src-Ordner |

---

## copilot-instructions.md vs. .instructions.md

| Aspekt          | `copilot-instructions.md` | `*.instructions.md`       |
| --------------- | ------------------------- | ------------------------- |
| Ort             | `.github/`                | `.github/instructions/`   |
| Geltungsbereich | Immer, für alle Dateien   | Nur bei `applyTo`-Match   |
| Frontmatter     | Keins                     | `applyTo` + `description` |
| Zweck           | Globaler Projektkontext   | Dateispecifische Regeln   |
| Länge           | 1–2 Seiten                | Kompakt, fokussiert       |

---

## Beispiele

### python.instructions.md

```markdown
---
applyTo: "**/*.py"
description: "Python code generation rules"
---

# Python Guidelines

- Python 3.12+ Syntax verwenden
- Typ-Annotationen für alle Funktions-Parameter und Rückgabewerte
- Exceptions immer explizit behandeln – kein blankes `except:`
- F-Strings statt `.format()` oder `%`
- `pathlib.Path` statt `os.path`
```

### flask.instructions.md

```markdown
---
applyTo: "**/app.py"
description: "Flask application conventions"
---

# Flask Guidelines

- Post/Redirect/Get Pattern für alle Form-Submissions
- `flash()` für Nutzer-Feedback verwenden
- Alle Formular-Eingaben validieren bevor Speichern
- `url_for()` statt hartkodierten URLs
- Error-Handler für 404 und 500 definieren
```

### testing.instructions.md

```markdown
---
applyTo: "**/test_*.py"
description: "pytest test generation rules"
---

# Testing Guidelines

- Immer: happy path + leere Eingabe + ungültiger Wert
- Bestehende Fixtures nutzen – keine neuen einführen
- Kommentare auf Deutsch
- Test-Namen beschreiben was getestet wird: `test_add_todo_mit_leerem_titel`
- `assert`-Nachrichten bei komplexen Assertions
```

### security.instructions.md

```markdown
---
applyTo: "**"
description: "Security rules for all files"
---

# Security Guidelines

- Keine hardcodierten Passwörter, Tokens oder API-Keys
- `eval()` und `exec()` sind verboten
- Alle User-Inputs validieren und sanitizen
- Parameterisierte Queries bei Datenbankoperationen
- Secrets nur aus Umgebungsvariablen (`os.environ.get(...)`)
```

---

## Instructions aktivieren (settings.json)

Instructions werden automatisch geladen, aber du kannst steuern wofür:

```json
// .vscode/settings.json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/instructions/python.instructions.md" },
    { "file": ".github/instructions/security.instructions.md" }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": ".github/instructions/security.instructions.md" }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Commit-Messages auf Englisch, Format: type(scope): message" }
  ]
}
```

**Direkt als Text (kein File):**

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "text": "Schreibe immer Docstrings. Nutze camelCase für Variablen." }
  ]
}
```

---

## Instructions stacking (Schichten)

Mehrere Instructions werden **kombiniert** – nicht überschrieben:

```
copilot-instructions.md         → Projektkontext (immer)
  + python.instructions.md      → Python-Regeln (bei *.py)
  + security.instructions.md   → Sicherheitsregeln (bei allen)
  = Vollständiger System-Prompt
```

**Reihenfolge:** Zuerst `copilot-instructions.md`, dann `.instructions.md` nach `applyTo`.

---

## Wann Instructions, wann Prompts?

| Instructions (`.instructions.md`) | Prompts (`.prompt.md`)            |
| --------------------------------- | --------------------------------- |
| Dauerhaftes Verhalten             | Einmaliger Workflow               |
| "Mach immer X"                    | "Führe jetzt Schritt A, B, C aus" |

---

## Agent Skills (`SKILL.md`) – eigenständiges Konzept

Instructions sind schlanke **Regeln**. Ein **Agent Skill** ist ein ganzes **Fähigkeitspaket**: eine `SKILL.md` mit Beschreibung, wann sie greift, plus optional beigelegte Referenzdateien, Scripts oder Beispiele – Copilot lädt sie nur bei Bedarf nach (Progressive Disclosure), statt sie dauerhaft in den Kontext zu packen.

**Datei:** `.github/skills/<name>/SKILL.md`

```yaml
---
name: pdf-report-generator
description: "Erzeuge PDF-Reports aus Rohdaten. Nutzen, wenn nach 'Report' oder 'PDF' gefragt wird."
---

# PDF Report Generator

1. Rohdaten aus `data/*.csv` einlesen
2. Mit der beigelegten `template.html` rendern
3. Mit dem beigelegten Script `render.py` nach PDF konvertieren
```

| Aspekt          | `.instructions.md`               | `SKILL.md` (Agent Skill)                    |
| --------------- | --------------------------------- | -------------------------------------------- |
| Inhalt          | Kurze Verhaltensregeln            | Ganzer Workflow inkl. Dateien/Scripts         |
| Ladeverhalten   | Immer bei `applyTo`-Match geladen | Nur bei Bedarf nachgeladen (Token-schonend)   |
| Typischer Zweck | "Schreibe Code so"                | "Führe diese komplexe Aufgabe so aus"         |
| Stil, Konventionen, Verbote       | Reviews, Features, Analyse        |
| Passiv (automatisch aktiviert)    | Aktiv (muss aufgerufen werden)    |
