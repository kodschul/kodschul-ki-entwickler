# 10 – Copilot CLI – vollständige Referenz

**Block:** 90 min | **Tag 3**

---

## Installation & Setup

```bash
# 1. GitHub CLI installieren
brew install gh                          # macOS
winget install GitHub.cli                # Windows
sudo apt install gh                      # Ubuntu/Debian

# 2. Authentifizieren
gh auth login
# → Wähle: GitHub.com → HTTPS → mit Browser

# 3. Copilot Extension installieren
gh extension install github/gh-copilot

# 4. Prüfen
gh copilot --version
gh copilot --help
```

---

## Die zwei Haupt-Befehle

### `gh copilot suggest` – Befehle finden

```bash
gh copilot suggest [BESCHREIBUNG] [FLAGS]
```

Schlägt einen Shell-Befehl für eine natürlichsprachliche Beschreibung vor.

### `gh copilot explain` – Befehle verstehen

```bash
gh copilot explain [BEFEHL] [FLAGS]
```

Erklärt was ein Befehl tut – inkl. aller Flags und Argumente.

---

## `gh copilot suggest` – alle Optionen

### Basis-Verwendung

```bash
# Einfache Anfrage
gh copilot suggest "alle Python-Dateien auflisten"

# Ergebnis interaktiv:
# → Copilot schlägt vor: find . -name "*.py"
# → Optionen: [e]xecute / [r]evise / [e]xplain / [c]opy / [q]uit
```

### Zieltyp mit `-t` / `--target`

```bash
# Shell-Befehl (Standard)
gh copilot suggest -t shell "Tests ausführen und Ergebnis speichern"

# Git-Befehl
gh copilot suggest -t git "alle Änderungen der letzten 3 Commits anzeigen"

# GitHub CLI-Befehl
gh copilot suggest -t gh "Pull Request für aktuellen Branch erstellen"
```

| `-t` Wert | Beschreibung                        |
| --------- | ----------------------------------- |
| `shell`   | Allgemeine Shell-Befehle (Standard) |
| `git`     | Git-Befehle                         |
| `gh`      | GitHub CLI-Befehle                  |

### Ohne Interaktion (für Skripte)

```bash
# Kein interaktives Menü
gh copilot suggest "pytest ausführen" --no-interaction

# Hinweis: Gibt nur den Befehl aus (ohne Erklärung)
```

### Interaktives Menü – was sind die Optionen?

Nach einem Vorschlag:

```
? What would you like to do?
  ▸ Execute command      → Befehl direkt ausführen
    Revise command       → Prompt verfeinern
    Explain command      → Was macht dieser Befehl?
    Copy command         → In Zwischenablage
    Exit                 → Beenden
```

---

## `gh copilot explain` – alle Optionen

### Basis-Verwendung

```bash
# Befehl direkt übergeben
gh copilot explain "python -m pytest test_app.py -v --tb=short"

# Git-Befehl erklären
gh copilot explain "git rebase -i HEAD~3"

# Komplexe Pipeline
gh copilot explain "find . -name '*.py' | xargs grep -l 'import os' | head -20"
```

### Ausgabe-Format

```bash
# Standard: Markdown-Erklärung
gh copilot explain "docker compose up -d --build"

# Beispiel-Output:
# ## docker compose up -d --build
# Startet alle Services in docker-compose.yml
# **-d**: Detached Mode (im Hintergrund)
# **--build**: Images vor dem Start neu bauen
```

---

## Aliase einrichten (Token sparen – Tippen sparen)

```bash
# Kurze Aliases definieren
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Danach nutzbar als:
gh cs "Tests ausführen"
gh ce "git cherry-pick --abort"

# Alle Aliases anzeigen
gh alias list

# Alias löschen
gh alias delete cs
```

**Shell-Alias (noch kürzer):**

```bash
# In ~/.zshrc oder ~/.bashrc:
alias gcs='gh copilot suggest'
alias gce='gh copilot explain'
alias gcss='gh copilot suggest -t shell'
alias gcsg='gh copilot suggest -t git'
alias gcgh='gh copilot suggest -t gh'

# Reload
source ~/.zshrc
```

---

## Workflow-Beispiele

### Code-Review im Terminal

```bash
# Sicherheitsprobleme finden
gh copilot suggest -t shell "Python-Dateien auf hardcodierte Secrets scannen"
# → Vorschlag: grep -r "password\|secret\|api_key" . --include="*.py"

# Ergebnis direkt ausführen
gh copilot suggest "grep nach Passwörtern in Python-Dateien" --execute 2>/dev/null
```

### Git-Workflow automatisieren

```bash
# Branch erstellen
gh copilot suggest -t git "feature branch für due-dates erstellen"

# Änderungen committen
gh copilot suggest -t git "alle Python-Dateien committen mit Nachricht Feature: Add due dates"

# Pull Request
gh copilot suggest -t gh "Pull Request erstellen für due-dates branch"
```

### CI/CD Debugging

```bash
# Letzten Fehler erklären
gh copilot explain "$(python -m pytest test_app.py 2>&1 | tail -20)"

# Oder: Fehlermeldung direkt hineinkopieren
gh copilot explain "ModuleNotFoundError: No module named 'flask'"
```

### Headless Review-Skript

```bash
#!/bin/bash
# review.sh – Nutzung von gh copilot suggest für Automation

echo "=== Code Quality Check ==="
# flake8 für Style
python -m flake8 app.py --max-line-length=100

echo ""
echo "=== Nächster Schritt empfohlen von Copilot ==="
gh copilot suggest -t shell \
  "Python-Datei app.py auf häufige Sicherheitsprobleme prüfen" \
  --no-interaction
```

---

## Token-Sparen mit der CLI

Die CLI läuft **komplett außerhalb** des VS Code Chat-Kontexts:

```
VS Code Chat:        Shared Token-Budget mit Chat-Verlauf + Instructions
gh copilot CLI:      Eigenes Budget, kein Verlauf, minimaler Kontext
```

**Faustregel:**

- Terminal-Befehle finden/erklären → **CLI**
- Code verstehen/schreiben/reviewen → **Editor Chat**

```bash
# Diese Dinge immer in der CLI:
gh copilot suggest "pytest coverage report als HTML generieren"
gh copilot suggest -t git "staging area zurücksetzen ohne commits zu verlieren"
gh copilot explain "chmod 755 review.sh"
gh copilot suggest -t gh "alle offenen PRs auflisten"
```

---

## Vollständige Flag-Übersicht

### `gh copilot suggest`

| Flag               | Kurz | Beschreibung                  |
| ------------------ | ---- | ----------------------------- |
| `--target`         | `-t` | Zieltyp: `shell`, `git`, `gh` |
| `--no-interaction` |      | Keine interaktive Auswahl     |
| `--help`           | `-h` | Hilfe anzeigen                |

### `gh copilot explain`

| Flag     | Kurz | Beschreibung   |
| -------- | ---- | -------------- |
| `--help` | `-h` | Hilfe anzeigen |

### Globale Copilot-Flags

```bash
gh copilot --version    # Installierte Version
gh copilot --help       # Alle Befehle
```

---

## Copilot CLI vs. Editor Chat – wann was?

| Aufgabe                    | CLI                   | Editor Chat         |
| -------------------------- | --------------------- | ------------------- |
| Shell-Befehl finden        | ✅ Ideal              | Möglich             |
| Git-Befehl finden          | ✅ Ideal              | Möglich             |
| Befehl erklären            | ✅ Ideal              | Möglich             |
| Code schreiben / ändern    | ❌                    | ✅ Ideal            |
| Code reviewen              | Eingeschränkt         | ✅ Ideal            |
| Multi-File-Aufgaben        | ❌                    | ✅ Agent-Modus      |
| In Skripten automatisieren | ✅ `--no-interaction` | ❌                  |
| Token-Budget sparen        | ✅ Kein Chat-Verlauf  | Verlauf akkumuliert |
