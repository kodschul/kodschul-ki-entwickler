# Hooks

**Block:** 10:45 – 12:15 Uhr (zusammen mit Commands & Agents)

---

## Wie funktioniert das unter der Haube?

```
Claude führt eine Aktion aus (z.B. Datei schreiben)
  → Hook-Event wird ausgelöst (z.B. PostToolUse)
  → Claude Code führt den konfigurierten Shell-Befehl aus
  → Ausgabe erscheint im Terminal
```

> Hooks sind **Shell-Befehle**, die automatisch vor oder nach bestimmten Claude-Aktionen laufen.  
> Konfiguriert in `settings.local.json` unter `hooks`.

**Hook-Typen:**

| Event          | Wann                                     |
| -------------- | ---------------------------------------- |
| `PreToolUse`   | Bevor Claude ein Tool benutzt            |
| `PostToolUse`  | Nachdem Claude ein Tool benutzt hat      |
| `Stop`         | Wenn Claude fertig ist (Session-Ende)    |
| `Notification` | Wenn Claude eine Benachrichtigung sendet |

---

## Warum / Wann nicht?

| Warum nutzen                        | Wann nicht                                               |
| ----------------------------------- | -------------------------------------------------------- |
| Tests automatisch nach Codeänderung | Hook-Befehl dauert sehr lang → blockiert                 |
| Backup vor Überschreiben            | Zu komplexe Logik → lieber Skript separat                |
| Formatierung erzwingen (linting)    | Vertrauliche Daten in Hook-Output → sichtbar im Terminal |
| Benachrichtigung bei Fertigstellung | Hook schlägt fehl → Claude wird gestoppt                 |

---

## Aufbau in `settings.local.json`

```json
{
  "permissions": { ... },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "python -m pytest test_app.py -q"
          }
        ]
      }
    ]
  }
}
```

**`matcher`** – Welches Tool löst den Hook aus:

| Matcher         | Beschreibung                               |
| --------------- | ------------------------------------------ |
| `Write`         | Jedes Mal, wenn Claude eine Datei schreibt |
| `Write(app.py)` | Nur wenn `app.py` geschrieben wird         |
| `Bash`          | Nach jedem Bash-Aufruf                     |
| `*`             | Immer (alle Tools)                         |

---

## Beispiel 1 – Tests nach Codeänderung

```json
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
```

→ Jedes Mal wenn Claude `app.py` ändert, laufen die Tests automatisch.

---

## Beispiel 2 – Backup vor Überschreiben

```json
"hooks": {
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
}
```

→ Bevor `todos.json` überschrieben wird, entsteht automatisch `todos.backup.json`.

---

## Mehrere Hooks verwalten

### Kein YAML, keine .md – nur JSON

Hooks gibt es **ausschließlich in `settings.local.json`** (oder `~/.claude/settings.json` global).  
Es gibt kein YAML-Format und keine separate Hook-Datei.

### Mehrere Hooks pro Event

Mehrere Matchers unter demselben Event-Typ als Array:

```json
"hooks": {
  "PostToolUse": [
    {
      "matcher": "Write(app.py)",
      "hooks": [{ "type": "command", "command": "python -m pytest test_app.py -q" }]
    },
    {
      "matcher": "Write(*.py)",
      "hooks": [{ "type": "command", "command": "python -m flake8 $TOOL_INPUT_PATH 2>/dev/null || true" }]
    },
    {
      "matcher": "Write(*.html)",
      "hooks": [{ "type": "command", "command": "echo 'Template geändert: $TOOL_INPUT_PATH'" }]
    }
  ],
  "PreToolUse": [
    {
      "matcher": "Write(todos.json)",
      "hooks": [{ "type": "command", "command": "cp todos.json todos.backup.json 2>/dev/null || true" }]
    }
  ]
}
```

### Mehrere Befehle pro Matcher

Ein Matcher kann mehrere `hooks` hintereinander ausführen:

```json
{
  "matcher": "Write(app.py)",
  "hooks": [
    {
      "type": "command",
      "command": "python -m flake8 app.py --max-line-length=120 2>/dev/null || true"
    },
    {
      "type": "command",
      "command": "python -m pytest test_app.py -q --tb=line"
    },
    { "type": "command", "command": "echo '✅ Lint + Tests fertig'" }
  ]
}
```

> Befehle laufen **sequenziell**. Schlägt einer fehl, stoppt die Kette.  
> Mit `|| true` am Ende läuft die Kette weiter, auch bei Fehler.

### Bei vielen Hooks: Auslagern in ein Skript

Ab ~5 Hooks wird die JSON-Datei unübersichtlich.  
Lösung: Logik in ein Shell-Skript auslagern, Hook ruft nur das Skript auf.

**`.claude/hooks/post-write.sh`:**

```bash
#!/bin/bash
FILE=$1

case "$FILE" in
  *.py)
    python -m flake8 "$FILE" --max-line-length=120 2>/dev/null || true
    python -m pytest test_app.py -q --tb=line
    ;;
  *.html)
    echo "Template geändert: $FILE"
    ;;
  todos.json)
    echo "Datendatei geändert"
    ;;
esac
```

**`settings.local.json` – nur noch ein Eintrag:**

```json
"PostToolUse": [
  {
    "matcher": "Write",
    "hooks": [
      { "type": "command", "command": "bash .claude/hooks/post-write.sh $TOOL_INPUT_PATH" }
    ]
  }
]
```

### Verfügbare Variablen in Hook-Befehlen

| Variable             | Inhalt                                             |
| -------------------- | -------------------------------------------------- |
| `$TOOL_INPUT_PATH`   | Dateipfad der gerade geschriebenen/gelesenen Datei |
| `$TOOL_NAME`         | Name des Tools (z.B. `Write`, `Bash`)              |
| `$CLAUDE_SESSION_ID` | ID der aktuellen Session                           |

---

## Beispiel 3 – Benachrichtigung bei Fertigstellung

```json
"hooks": {
  "Stop": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "echo '✅ Claude ist fertig'"
        }
      ]
    }
  ]
}
```
