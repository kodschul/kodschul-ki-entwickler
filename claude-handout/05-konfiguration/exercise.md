# Übung: Konfiguration

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – settings.local.json erweitern (15 min)

Füge folgende Erlaubnisse hinzu:

- `python -m pytest test_app.py -v --tb=short`
- `cat todos.json`
- `python app.py`

**Prompt:**

```
Erweitere .claude/settings.local.json so, dass Claude folgende Befehle
ohne Rückfrage ausführen darf: pytest mit verbose Output, cat todos.json,
python app.py. Ergänze außerdem eine deny-Regel, die verhindert,
dass todos.json gelöscht wird.
```

## Aufgabe 2 – Team-Settings vs. lokale Settings (10 min)

Lege `.claude/settings.json` (Team-weit, eingecheckt) mit einer sinnvollen `deny`-Liste an und erkläre in eigenen Worten, warum diese Regeln nicht in `settings.local.json` gehören.

## Aufgabe 3 – Modellwahl (5 min)

```
Wechsle für diese Session auf ein schnelleres Modell und erkläre,
für welche Aufgaben sich das eignet.
```

---

## Zusammenfassung

- [ ] `settings.local.json` um neue Erlaubnisse und eine `deny`-Regel erweitert
- [ ] Team-weite `settings.json` mit Sicherheits-Defaults angelegt
- [ ] Modellwechsel ausprobiert
