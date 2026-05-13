# Übung: Hooks

**Zeit:** 10:45 – 12:15 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Auto-Test Hook einrichten (15 min)

**Ziel:** Tests laufen automatisch, wenn Claude `app.py` ändert.

Öffne `.claude/settings.local.json` und füge einen `hooks`-Block hinzu:

```json
{
  "permissions": {
    "allow": [...]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(app.py)",
        "hooks": [
          {
            "type": "command",
            "command": "python -m pytest test_app.py -q --tb=line"
          }
        ]
      }
    ]
  }
}
```

**Testen – Claude zu einer Änderung bringen:**

```
Füge einen Kommentar am Anfang von app.py hinzu.
```

Beobachte: Laufen die Tests automatisch im Terminal?

---

## Aufgabe 2 – Backup Hook für todos.json (15 min)

**Ziel:** Bevor `todos.json` überschrieben wird, entsteht ein Backup.

Erweitere `hooks` um einen `PreToolUse`-Eintrag:

```json
"PreToolUse": [
  {
    "matcher": "Write(todos.json)",
    "hooks": [
      {
        "type": "command",
        "command": "cp todos.json todos.backup.json 2>/dev/null || true"
      }
    ]
  }
]
```

**Testen:**

```
Füge ein Test-Todo direkt in todos.json ein.
```

Prüfe: Existiert danach `todos.backup.json`?

```bash
ls -la todos*.json
```

---

## Aufgabe 3 – Stop Hook (10 min)

**Ziel:** Am Ende jeder Claude-Session erscheint eine Bestätigung.

```json
"Stop": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "echo '--- Session beendet: $(date) ---'"
      }
    ]
  }
]
```

**Testen:** Beende die aktuelle Claude-Konversation – erscheint die Meldung?

---

## Aufgabe 4 – Vollständige settings.local.json (10 min)

Am Ende sollte die Datei alle drei Hooks enthalten.

**Prompt zum Zusammenführen:**

```
Zeig mir die aktuelle .claude/settings.local.json und stelle sicher,
dass alle drei Hooks korrekt eingebunden sind:
1. PostToolUse für Write(app.py) → pytest ausführen
2. PreToolUse für Write(todos.json) → Backup erstellen
3. Stop → Echo mit Timestamp
```

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] Auto-Test-Hook: pytest läuft nach jeder `app.py`-Änderung
- [ ] Backup-Hook: `todos.backup.json` wird vor jedem Überschreiben erstellt
- [ ] Stop-Hook: Bestätigung am Session-Ende
- [ ] Vollständige `settings.local.json` mit permissions + hooks
