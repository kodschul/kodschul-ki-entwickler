# Übung: Copilot CLI – TypeScript Angular

**Zeit:** 90 min | **Projekt:** Angular Todo App

---

## Setup (5 min)

```bash
gh --version
gh copilot --version

# Falls noch nicht installiert:
gh extension install github/gh-copilot
```

---

## Aufgabe 1 – suggest: Angular-Befehle finden (20 min)

```bash
# 1. Angular Dev-Server starten
gh copilot suggest "Angular Dev-Server im development-Modus starten"

# 2. Komponente generieren (standalone)
gh copilot suggest "Angular standalone Komponente namens todo-item generieren" -t shell

# 3. Tests im Headless-Modus ausführen
gh copilot suggest "Angular Tests mit ChromeHeadless ohne Watch ausführen" -t shell

# 4. Nur fehlgeschlagene Tests wiederholen
gh copilot suggest "ng test nur fehlgeschlagene Specs erneut ausführen" -t shell

# 5. Bundle-Größe analysieren
gh copilot suggest "Angular Build-Größe analysieren mit source-map-explorer" -t shell
```

**Für jeden Vorschlag:**
- Wähle `[e]xplain` um zu verstehen was der Befehl tut
- Wähle `[e]xecute` um ihn direkt auszuführen
- Wähle `[r]evise` um ihn zu verfeinern

---

## Aufgabe 2 – suggest -t git (15 min)

```bash
# Git-Befehle für Angular-Workflow:

# 1. Alle geänderten Dateien anzeigen
gh copilot suggest -t git "zeige alle Dateien die sich geändert haben"

# 2. Nur TypeScript-Dateien stagen
gh copilot suggest -t git "nur .ts Dateien zum nächsten Commit stagen"

# 3. Feature-Branch erstellen
gh copilot suggest -t git "neuen Branch für das Feature todo-filtering erstellen"

# 4. Letzten Commit rückgängig machen (soft)
gh copilot suggest -t git "letzten Commit rückgängig machen aber Änderungen behalten"
```

---

## Aufgabe 3 – explain: Angular-Befehle verstehen (15 min)

```bash
# 1. ng generate Befehl erklären
gh copilot explain "ng generate component components/todo-item --standalone --skip-tests"

# 2. ng test Flags erklären
gh copilot explain "ng test --watch=false --browsers=ChromeHeadless --code-coverage"

# 3. TypeScript strict mode erklären
gh copilot explain "tsc --strict --noImplicitAny --strictNullChecks src/app/services/todo.service.ts"

# 4. Eigenen Befehl erklären:
history | tail -5
# → Letzten ng-Befehl mit gh copilot explain analysieren
```

---

## Aufgabe 4 – Aliases einrichten (10 min)

```bash
# GitHub CLI Aliases
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'
gh alias list

# Shell-Aliases (zsh):
echo "alias gcs='gh copilot suggest'" >> ~/.zshrc
echo "alias gce='gh copilot explain'" >> ~/.zshrc
echo "alias gcss='gh copilot suggest -t shell'" >> ~/.zshrc
echo "alias gcsg='gh copilot suggest -t git'" >> ~/.zshrc
source ~/.zshrc

# Testen:
gcs "Angular Komponente generieren"
gcsg "aktuellen Branch zu origin pushen"
gce "ng build --configuration=production --stats-json"
```

---

## Aufgabe 5 – Review-Skript für Angular (20 min)

Erstelle `review.sh`:

```bash
#!/bin/bash
set -e

echo "=============================="
echo "Angular Code Quality Report"
echo "=============================="
echo ""

echo "--- TypeScript Kompilierung ---"
npx tsc --noEmit 2>&1 || true

echo ""
echo "--- ESLint ---"
npx eslint "src/**/*.ts" --max-warnings=0 2>&1 || true

echo ""
echo "--- Tests ---"
ng test --watch=false --browsers=ChromeHeadless --no-progress 2>&1 | tail -20

echo ""
echo "--- Copilot empfiehlt als nächsten Schritt ---"
gh copilot suggest -t shell \
  "häufige Angular-Performance-Probleme in einem Projekt analysieren" \
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

## Aufgabe 6 – CLI vs. Chat Vergleich (10 min)

**Im Terminal:**

```bash
gh copilot suggest "Angular Service mit HttpClient und error handling generieren" -t shell
```

**Im Editor-Chat:**

```
Zeige mir wie ich einen Angular Service mit HttpClient und
zentralem Error-Handling schreibe.
```

**Beobachten:**
- CLI: gibt Shell-Befehle zurück (z.B. `ng generate service...`)
- Chat: gibt TypeScript-Code zurück mit Erklärung
- Wann nutzt du welches Tool?
