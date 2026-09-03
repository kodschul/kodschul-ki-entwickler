# Übung: Hooks & Automation

**Zeit:** ca. 20 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Tests nach Codeänderung (10 min)

Ergänze in `.claude/settings.local.json` einen `PostToolUse`-Hook, der nach jeder Änderung an `app.py` automatisch `pytest` ausführt.

## Aufgabe 2 – Backup vor Überschreiben (10 min)

Ergänze einen `PreToolUse`-Hook, der vor jeder Änderung an `todos.json` automatisch ein Backup `todos.backup.json` anlegt.

Teste: Lass Claude ein Todo hinzufügen und prüfe, ob das Backup entsteht.

---

## Zusammenfassung

- [ ] `PostToolUse`-Hook für automatische Tests eingerichtet
- [ ] `PreToolUse`-Hook für Backup eingerichtet und verifiziert
