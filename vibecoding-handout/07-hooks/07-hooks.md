# 07 - Hooks

## Ziel

Hooks automatisieren Folgeaktionen nach Angebotsgenerierung.

## Typische Hooks

- Nach Generate: Review automatisch starten
- Nach Review-Fehler: Hinweis in UI erzeugen
- Nach Freigabe: Export vorbereiten

## Sample Prompt

```text
Erstelle `.claude/hooks/notify-review.md`.
Wenn ein neues Angebot erzeugt wird, soll ein Review-Task mit
Titel, Zeitstempel und Prioritaet erstellt werden.
```

## Ergebnis

Weniger manuelle Schritte, konsistenter Team-Prozess.
