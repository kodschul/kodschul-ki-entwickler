# Übung: Custom Agents

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Security-Reviewer-Agent (15 min)

Erstelle `.claude/agents/security-reviewer.md` nach Handout-Vorlage (nur `Read`-Tool!) und rufe ihn auf:

```
Mach einen Sicherheits-Audit der App.
```

## Aufgabe 2 – Test-Writer-Agent (15 min)

Erstelle `.claude/agents/test-writer.md` (nur `Read` und `Write(test_app.py)`) und rufe ihn auf:

```
Schreib Tests für alle Routen, die noch nicht getestet sind.
```

Prüfe: Hat der Agent wirklich nur `test_app.py` verändert?

---

## Zusammenfassung

- [ ] `security-reviewer`-Agent erstellt und getestet
- [ ] `test-writer`-Agent erstellt, Tool-Beschränkung verifiziert
