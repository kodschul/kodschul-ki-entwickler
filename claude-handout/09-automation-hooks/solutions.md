# Lösungen: Hooks & Automation

## Aufgabe 1 – Tests nach Codeänderung

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
    ]
  }
}
```

## Aufgabe 2 – Backup vor Überschreiben

```json
{
  "hooks": {
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
