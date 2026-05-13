# Übung: MCP + Customization

**Zeit:** 15:15 – 17:00 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Playwright MCP nutzen (20 min)

Die Todo-App läuft lokal. Starte sie falls nötig:

```bash
FLASK_DEBUG=1 python app.py
```

**Prompt:**

```
Öffne die Todo-App unter http://localhost:5000.
1. Mach einen Screenshot der aktuellen Liste
2. Füge ein neues Todo mit dem Titel "MCP Test Todo" hinzu
3. Mach einen Screenshot nach dem Hinzufügen
4. Bestätige, dass das Todo in der Liste sichtbar ist
```

**Beobachten:**

- Welche MCP-Tools nutzt Claude?
- Erscheinen die Screenshots unter `.playwright-mcp/`?

---

## Aufgabe 2 – Headless Review-Skript (20 min)

**Ziel:** Ein Skript, das die App reviewed und das Ergebnis speichert – ohne User-Interaktion.

Erstelle `review.sh`:

```bash
#!/bin/bash
echo "Starte Code-Review..."

claude --print \
  "Führe einen vollständigen Code-Review von app.py durch.
   Prüfe auf: Sicherheitsprobleme, fehlende Tests, Code-Qualität.
   Ausgabe als Markdown mit Tabelle: Problem | Schwere | Empfehlung" \
  > review-output.md

echo "Review gespeichert: review-output.md"
```

Ausführen:

```bash
chmod +x review.sh
./review.sh
cat review-output.md
```

**Erweiterung – JSON-Output:**

```bash
claude --print \
  "Analysiere app.py. Ausgabe NUR als JSON-Array: [{\"problem\": \"\", \"severity\": \"\", \"line\": 0}]" \
  --output-format json \
  > review-output.json
```

---

## Aufgabe 3 – Permissions härten (15 min)

**Ziel:** `settings.local.json` so konfigurieren, dass Claude nur das Minimum darf.

```
Überarbeite die .claude/settings.local.json.
Ziel: Least-Privilege-Prinzip.

deny-Regeln hinzufügen für:
- rm (Löschen von Dateien)
- git push (kein ungewolltes Pushen)
- pip install (nur explizit erlaubte Pakete)

Erkläre jede deny-Regel mit einem Kommentar warum sie sinnvoll ist.
```

**Hinweis:** JSON unterstützt keine Kommentare – Claude soll die Erklärungen als separaten Text ausgeben.

---

## Aufgabe 4 – Freies Experimentieren (15 min)

Wähle eine der folgenden Ideen:

| Idee                   | Beschreibung                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| **Eigener MCP-Server** | Recherche: Wie baut man einen MCP-Server in Python?                                              |
| **CI-Simulation**      | `review.sh` so erweitern, dass es mit Exit-Code 1 abbricht wenn kritische Fehler gefunden werden |
| **Sandbox testen**     | `claude --sandbox` starten und prüfen was noch geht                                              |
| **Global vs. Lokal**   | `~/.claude/settings.json` öffnen und verstehen was global konfiguriert ist                       |

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] Playwright MCP genutzt um die App automatisiert zu testen
- [ ] `review.sh` für Headless-Review erstellt
- [ ] `settings.local.json` mit deny-Regeln gehärtet
- [ ] Eines der freien Experimente durchgeführt
