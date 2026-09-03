# Übung: Copilot CLI

**Zeit:** 90 min | **Projekt:** `1205/todo-app/`

---

## Setup (5 min)

```bash
# Sicherstellen dass alles installiert ist
gh --version
gh copilot --version

# Falls noch nicht:
gh extension install github/gh-copilot
```

---

## Aufgabe 1 – suggest: Shell-Befehle finden (20 min)

Finde mit `gh copilot suggest` die richtigen Befehle:

```bash
# 1. Flask App starten im Debug-Modus
gh copilot suggest "Flask App im Debug-Modus starten"

# 2. Alle Tests ausführen mit verbose output
gh copilot suggest "pytest mit verbose output und kurzem Traceback"

# 3. Nur Tests ausführen die fehlgeschlagen sind
gh copilot suggest "pytest nur fehlgeschlagene Tests erneut ausführen" -t shell

# 4. Python-Dateien auf Zeilenlänge > 100 prüfen
gh copilot suggest "Python-Dateien auf Zeilen prüfen die länger als 100 Zeichen sind" -t shell

# 5. todos.json formatiert ausgeben
gh copilot suggest "JSON-Datei formatiert im Terminal anzeigen" -t shell
```

**Für jeden Vorschlag:**

- Wähle `[e]xplain` um zu verstehen was der Befehl tut
- Wähle `[e]xecute` um ihn direkt auszuführen
- Wähle `[r]evise` um ihn zu verfeinern

---

## Aufgabe 2 – suggest -t git (15 min)

```bash
# Git-Befehle über CLI finden:

# 1. Alle geänderten Dateien anzeigen
gh copilot suggest -t git "zeige alle Dateien die sich geändert haben"

# 2. Änderungen in einer Datei rückgängig machen
gh copilot suggest -t git "Änderungen in app.py rückgängig machen ohne commit zu verlieren"

# 3. Feature-Branch erstellen
gh copilot suggest -t git "neuen Branch für das Feature due-dates erstellen"

# 4. Letzten Commit rückgängig machen (soft)
gh copilot suggest -t git "letzten Commit rückgängig machen aber Änderungen behalten"
```

---

## Aufgabe 3 – explain: Befehle verstehen (15 min)

```bash
# 1. Pytest-Flags erklären
gh copilot explain "python -m pytest test_app.py -v --tb=short -x"

# 2. Find-Befehl erklären
gh copilot explain "find . -name '*.py' -not -path './.git/*' -newer requirements.txt"

# 3. Git Log erklären
gh copilot explain "git log --oneline --graph --decorate --all"

# 4. Eigenen Befehl erklären (aus dem Terminal-Verlauf holen):
history | tail -5
# → Letzten Befehl mit gh copilot explain analysieren
```

---

## Aufgabe 4 – Aliases einrichten (10 min)

```bash
# GitHub CLI Aliases
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'
gh alias list  # überprüfen

# Shell-Aliases (wähle deine Shell)
# zsh:
echo "alias gcs='gh copilot suggest'" >> ~/.zshrc
echo "alias gce='gh copilot explain'" >> ~/.zshrc
echo "alias gcss='gh copilot suggest -t shell'" >> ~/.zshrc
echo "alias gcsg='gh copilot suggest -t git'" >> ~/.zshrc
source ~/.zshrc

# bash:
echo "alias gcs='gh copilot suggest'" >> ~/.bashrc
source ~/.bashrc
```

**Testen:**

```bash
gcs "flake8 auf alle Python-Dateien ausführen"
gcsg "aktuellen Branch zu origin pushen"
gce "grep -r 'SECRET' . --include='*.py'"
```

---

## Aufgabe 5 – Review-Skript bauen (20 min)

Erstelle `review.sh` das ohne User-Interaktion läuft:

```bash
#!/bin/bash
set -e

echo "=============================="
echo "Code Quality Report"
echo "=============================="
echo ""

echo "--- flake8 (Style) ---"
python -m flake8 app.py --max-line-length=100 --statistics 2>&1 || true

echo ""
echo "--- Tests ---"
python -m pytest test_app.py -q --tb=line 2>&1

echo ""
echo "--- Copilot empfiehlt als nächsten Schritt ---"
gh copilot suggest -t shell \
  "häufigste Python-Sicherheitsprobleme in app.py finden" \
  --no-interaction 2>/dev/null || echo "(Copilot CLI nicht verfügbar)"

echo ""
echo "=============================="
echo "Review abgeschlossen"
echo "=============================="
```

```bash
chmod +x review.sh
./review.sh
```

---

## Aufgabe 6 – CLI vs. Chat Vergleich (5 min)

Stelle dieselbe Frage in beiden Orten:

**Im Terminal:**

```bash
gh copilot suggest "pytest mit HTML Coverage-Report ausführen" -t shell
```

**Im Editor-Chat:**

```
Wie führe ich pytest mit HTML Coverage-Report aus?
```

**Beobachten:**

- Welche Antwort ist präziser?
- Welche ist schneller?
- Wann würdest du welche nutzen?
