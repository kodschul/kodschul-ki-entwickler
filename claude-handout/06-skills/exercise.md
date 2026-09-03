# Übung: Skills & CLAUDE.md-Vertiefung

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Eigenen Skill schreiben (20 min)

Erstelle `.claude/skills/bug-finder/SKILL.md`, der Claude anweist, Code auf typische Python-Fehler zu prüfen.

**Prompt:**

```
Erstelle einen neuen Skill unter .claude/skills/bug-finder/SKILL.md.
Der Skill soll Claude anweisen, Python-Code zu analysieren und auf folgende
Probleme zu prüfen: unbehandelte Exceptions, fehlende Input-Validierung bei
Flask-Routen, hardcodierte Werte (Passwörter, Tokens, Ports), fehlende Tests
für neue Funktionen. Der Skill soll aktiviert werden, wenn jemand nach
Fehlern oder Problemen im Code fragt.
```

Teste ihn danach:

```
Schau dir app.py an und prüfe den Code auf mögliche Fehler und Probleme.
```

## Aufgabe 2 – Verschachtelte CLAUDE.md (10 min)

Falls die App in `templates/` und restlichem Code unterschiedliche Konventionen hat: Lege `templates/CLAUDE.md` mit 2–3 Regeln an, die nur für Templates gelten (z. B. "Nur Tailwind-Klassen, kein eigenes CSS").

---

## Zusammenfassung

- [ ] Skill `bug-finder` erstellt und getestet
- [ ] Verschachtelte `CLAUDE.md` für einen Unterordner angelegt
