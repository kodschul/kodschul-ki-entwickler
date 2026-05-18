# Übung: MCP + gh copilot CLI

**Zeit:** 15:15 – 17:00 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Playwright MCP konfigurieren (20 min)

Die Todo-App läuft lokal. Starte sie falls nötig:

```bash
FLASK_DEBUG=1 python app.py
```

**Schritt 1 – MCP-Konfiguration erstellen:**

Erstelle `.vscode/mcp.json`:

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {}
    }
  }
}
```

**Schritt 2 – Copilot Chat im Agent-Modus nutzen:**

```
Öffne die Todo-App unter http://localhost:5000.
1. Mach einen Screenshot der aktuellen Liste
2. Füge ein neues Todo mit dem Titel "MCP Test Todo" hinzu
3. Mach einen Screenshot nach dem Hinzufügen
4. Bestätige, dass das Todo in der Liste sichtbar ist
```

**Beobachten:**

- Welche MCP-Tools nutzt Copilot?
- Erscheinen die Screenshots in einem Ausgabeordner?

---

## Aufgabe 2 – gh copilot CLI einrichten (15 min)

```bash
# Copilot CLI installieren
gh extension install github/gh-copilot

# Erste Befehle testen
gh copilot suggest "Flask Development-Server im Debug-Modus starten" -t shell
gh copilot suggest "pytest mit verbose output und Kurzem Traceback ausführen" -t shell
gh copilot explain "python -m pytest test_app.py -v --tb=short"
```

**Fragen zum Nachdenken:**

- Was schlägt Copilot CLI vor?
- Ist der Vorschlag korrekt für unsere App?
- Wann würdest du `gh copilot suggest` vs. Copilot Chat im Editor nutzen?

---

## Aufgabe 3 – Review-Skript mit gh copilot CLI (20 min)

**Ziel:** Ein Skript, das die App reviewed – analog zum Claude `--print`-Modus.

```bash
# Copilot nach dem passenden Befehl fragen
gh copilot suggest "Python-Datei auf Sicherheitsprobleme prüfen und Ergebnis in Markdown-Datei speichern" -t shell
```

**Manuell erstellen** `review.sh`:

```bash
#!/bin/bash
echo "Starte Code-Review..."

# flake8 für Code-Qualität
python -m flake8 app.py --max-line-length=100 --format="%(path)s:%(row)d: %(text)s" \
  > review-output.txt 2>&1

# bandit für Sicherheit (falls installiert)
if command -v bandit &> /dev/null; then
  bandit -r app.py -f txt >> review-output.txt 2>&1
fi

echo "Review gespeichert: review-output.txt"
cat review-output.txt
```

Ausführen:

```bash
chmod +x review.sh
./review.sh
```

**Mit gh copilot CLI den Befehl erklären lassen:**

```bash
gh copilot explain "bandit -r app.py -f txt"
```

---

## Aufgabe 4 – Permissions über Instructions härten (15 min)

**Ziel:** `copilot-instructions.md` so konfigurieren, dass Copilot nur das Minimum tut.

```
Erweitere die .github/copilot-instructions.md um einen Abschnitt "Einschränkungen".

Deny-Regeln hinzufügen für:
- Keine destructiven Operationen (rm -rf, DROP TABLE, git push --force)
- Keine hardcodierten Credentials
- Kein pip install ohne requirements.txt zu aktualisieren

Erkläre jede Einschränkung mit einer kurzen Begründung.
```

**Erwartetes Ergebnis in `.github/copilot-instructions.md`:**

```markdown
## Einschränkungen

- Keine destructiven Operationen ausführen (rm -rf, DROP TABLE, git push --force)
  → Datenverlust-Prävention
- Keine hardcodierten Credentials im Code
  → Sicherheit: Secrets gehören in .env-Dateien
- requirements.txt immer aktualisieren wenn neue Pakete installiert werden
  → Reproduzierbare Builds
- Keine Datenbankmigrationen ohne explizite Bestätigung
  → Datenbankintegrität
```

---

## Aufgabe 5 – Freies Experimentieren (15 min)

Wähle eine der folgenden Ideen:

| Idee                    | Beschreibung                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| **Eigener MCP-Server**  | Recherche: Wie baut man einen MCP-Server in Python? `gh copilot suggest` nutzen            |
| **CI erweitern**        | `.github/workflows/test.yml` so erweitern, dass bei Fehlern ein Issue erstellt wird        |
| **Alias einrichten**    | `gh copilot alias` einrichten für häufige Review-Befehle                                   |
| **Global vs. Lokal**    | VS Code User Settings öffnen und verstehen was global vs. projektspezifisch konfiguriert ist |
| **gh copilot explain**  | Erkläre 3 unbekannte Befehle aus dem Projekt mit `gh copilot explain`                      |

---

## Abschluss-Checkliste

Nach diesem Tag sollte deine Todo-App haben:

- [ ] `.github/copilot-instructions.md` mit Projektkontext
- [ ] `.github/instructions/security.instructions.md`
- [ ] `.github/prompts/todo-review.prompt.md`
- [ ] `.github/prompts/add-feature.prompt.md`
- [ ] `.github/prompts/spec-plan.prompt.md`
- [ ] `.github/agents/security-reviewer.agent.md`
- [ ] `.github/agents/test-writer.agent.md`
- [ ] `.vscode/tasks.json` mit Test-Tasks
- [ ] `.vscode/mcp.json` mit Playwright
- [ ] `.github/workflows/test.yml` für CI
- [ ] `gh copilot` CLI installiert und getestet
