# 14a – Checkpoints & Rewind

**Seit wann:** Als Funktion "Rewind"/Checkpoints im Laufe von 2025 in Claude Code eingeführt, um einzelne Agent-Schritte rückgängig machen zu können.

> Vor dem Unterrichten den genauen Namen/Shortcut in der aktuell installierten Claude-Code-Version prüfen (`/help`) – Details ändern sich zwischen Versionen.

---

## Was ist neu?

Claude Code legt während einer Session automatisch **Checkpoints** an, bevor größere Änderungen vorgenommen werden. Damit lässt sich der Zustand vor einer bestimmten Aktion wiederherstellen, ohne manuell `git reset` bemühen zu müssen.

```
Claude ändert app.py (Schritt 1)
Claude ändert templates/index.html (Schritt 2)
  → Ergebnis gefällt nicht
  → Rewind auf Checkpoint vor Schritt 2
  → app.py bleibt geändert, templates/index.html wird zurückgesetzt
```

## Warum wichtig?

- Senkt die Hemmschwelle, Claude größere, mehrschrittige Aufgaben anzuvertrauen – Fehler sind einfach rückgängig zu machen
- Ergänzt, ersetzt aber nicht Git: Checkpoints sind für die **Session**, Commits für die **dauerhafte Historie**

## Abgrenzung zu Git

| Checkpoints (Claude Code)                   | Git-Commits                           |
| ------------------------------------------- | ------------------------------------- |
| Automatisch während der Session             | Manuell/bewusst gesetzt               |
| Nur innerhalb der laufenden Session         | Dauerhaft, teambar über Remote        |
| Für schnelles Undo einzelner Agent-Schritte | Für nachvollziehbare Projekt-Historie |
