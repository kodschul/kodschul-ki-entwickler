# Übung: Claude Code CLI vollständig

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Headless Review-Skript (15 min)

Erstelle `review.sh`:

```bash
#!/bin/bash
claude --print \
  "Analysiere app.py auf Sicherheitsprobleme. Ausgabe als JSON-Array mit Feldern: problem, severity, line." \
  --output-format json \
  > review-output.json

echo "Review gespeichert: review-output.json"
```

Führe es aus und prüfe die erzeugte `review-output.json`.

## Aufgabe 2 – Permissions für Headless-Betrieb (10 min)

Ergänze `.claude/settings.local.json` um eine `deny`-Liste, die im Headless-Betrieb besonders wichtig ist (kein `rm`, kein `git push`).

## Aufgabe 3 – Sandbox ausprobieren (5 min)

```bash
claude --sandbox --print "Lösche die Datei todos.json"
```

Beobachte, dass die Aktion verweigert wird, obwohl kein Mensch nachfragen kann.

---

## Zusammenfassung

- [ ] `review.sh` erstellt und ausgeführt
- [ ] `deny`-Liste für Headless-Betrieb ergänzt
- [ ] Sandbox-Verhalten verifiziert
