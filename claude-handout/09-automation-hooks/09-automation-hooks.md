# 09 – Hooks & Automation

**Block:** 60 min | **Tag 3**

---

## Wie funktioniert das unter der Haube?

```
Claude führt eine Aktion aus (z. B. Datei schreiben)
  → Hook-Event wird ausgelöst (z. B. PostToolUse)
  → Claude Code führt den konfigurierten Shell-Befehl aus
  → Ausgabe erscheint im Terminal
```

> Hooks sind **Shell-Befehle**, die automatisch vor oder nach bestimmten Claude-Aktionen laufen. Konfiguriert in `settings.local.json` (oder `settings.json`) unter `hooks`. Das entspricht in seiner Funktion GitHub Actions/Tasks bei Copilot – nur direkt in Claude Codes eigenem Lebenszyklus verankert.

**Hook-Typen:**

| Event            | Wann                                       |
| ------------------ | --------------------------------------------- |
| `PreToolUse`         | Bevor Claude ein Tool benutzt                  |
| `PostToolUse`        | Nachdem Claude ein Tool benutzt hat            |
| `Stop`               | Wenn Claude fertig ist (Session-Ende)          |
| `Notification`       | Wenn Claude eine Benachrichtigung sendet       |

---

## Warum / Wann nicht?

| Warum nutzen                          | Wann nicht                                                |
| ---------------------------------------- | ---------------------------------------------------------- |
| Tests automatisch nach Codeänderung        | Hook-Befehl dauert sehr lang → blockiert                    |
| Backup vor Überschreiben                   | Zu komplexe Logik → lieber Skript separat auslagern         |
| Formatierung erzwingen (Linting)           | Vertrauliche Daten in Hook-Output → sichtbar im Terminal    |
| Benachrichtigung bei Fertigstellung        | Hook schlägt fehl → Claude wird gestoppt                     |

---

## Aufbau in `settings.local.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(app.py)",
        "hooks": [
          { "type": "command", "command": "python -m pytest test_app.py -q --tb=line" }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Write(todos.json)",
        "hooks": [
          { "type": "command", "command": "cp todos.json todos.backup.json 2>/dev/null || true" }
        ]
      }
    ]
  }
}
```

**`matcher`** – welches Tool löst den Hook aus:

| Matcher            | Beschreibung                                |
| --------------------- | ---------------------------------------------- |
| `Write`                | Jedes Mal, wenn Claude eine Datei schreibt       |
| `Write(app.py)`        | Nur wenn `app.py` geschrieben wird               |
| `Bash`                 | Nach jedem Bash-Aufruf                          |
| `*`                    | Immer (alle Tools)                              |

---

## Mehrere Hooks verwalten

Es gibt **kein YAML, keine `.md`** für Hooks – nur JSON in `settings.local.json`/`settings.json`. Mehrere Matchers pro Event als Array, mehrere Befehle pro Matcher sequenziell:

```json
{
  "matcher": "Write(app.py)",
  "hooks": [
    { "type": "command", "command": "python -m flake8 app.py --max-line-length=120 2>/dev/null || true" },
    { "type": "command", "command": "python -m pytest test_app.py -q --tb=line" }
  ]
}
```

> Befehle laufen sequenziell. Schlägt einer fehl, stoppt die Kette – mit `|| true` läuft sie trotzdem weiter.

**Ab ~5 Hooks:** Logik in ein Shell-Skript auslagern (`.claude/hooks/post-write.sh`), der Hook ruft nur noch das Skript auf.

### Verfügbare Variablen in Hook-Befehlen

| Variable                | Inhalt                                             |
| -------------------------- | ------------------------------------------------------ |
| `$TOOL_INPUT_PATH`          | Dateipfad der gerade geschriebenen/gelesenen Datei       |
| `$TOOL_NAME`                | Name des Tools (z. B. `Write`, `Bash`)                  |
| `$CLAUDE_SESSION_ID`        | ID der aktuellen Session                                |

---

## Beispiel: Benachrichtigung bei Fertigstellung

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [{ "type": "command", "command": "echo '✅ Claude ist fertig'" }] }
    ]
  }
}
```
