# Übung: Konfiguration & .md-Dateien

**Zeit:** 09:15 – 10:30 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – CLAUDE.md verbessern (15 min)

Öffne die bestehende `CLAUDE.md` der Todo-App.  
Sie ist bereits vorhanden, aber zu kurz für eine echte Schulungsumgebung.

**Ziel:** Claude soll nach dem Lesen wissen:

- Was diese App tut
- Wie sie gestartet und getestet wird
- Welche Patterns verwendet werden
- Was sie NICHT tun soll

**Prompt zum Ausprobieren:**

```
Lies die aktuelle CLAUDE.md und verbessere sie so, dass:
- Der Projektkontext in 2-3 Sätzen klar ist
- Alle wichtigen Befehle (start, test) eingetragen sind
- Mindestens 5 Do-Regeln und 5 Don't-Regeln vorhanden sind
- Einen Abschnitt "Architecture" gibt, der erklärt wie Daten fließen (Request → app.py → todos.json → Template)
```

**Erwartetes Ergebnis:** `CLAUDE.md` mit den neuen Abschnitten

---

## Aufgabe 2 – Eigenen Skill schreiben (20 min)

Wir brauchen einen neuen Skill: **`bug-finder`**  
Er soll Claude anweisen, Code auf typische Python-Fehler zu prüfen.

**Ziel:** Datei `.claude/skills/bug-finder/SKILL.md` erstellen

**Manuell erstellen – Vorlage:**

```markdown
---
name: bug-finder
description: [HIER EINTRAGEN: Wann wird dieser Skill genutzt?]
---

# Bug Finder

Prüfe den Code auf folgende Probleme:

- [HIER EINTRAGEN: Regel 1]
- [HIER EINTRAGEN: Regel 2]
- [HIER EINTRAGEN: Regel 3]
```

**Oder per Prompt:**

```
Erstelle einen neuen Skill unter .claude/skills/bug-finder/SKILL.md.
Der Skill soll Claude anweisen, Python-Code zu analysieren und auf folgende Probleme zu prüfen:
- Unbehandelte Exceptions
- Fehlende Input-Validierung bei Flask-Routen
- Hardcodierte Werte (Passwörter, Tokens, Ports)
- Fehlende Tests für neue Funktionen
Der Skill soll aktiviert werden, wenn jemand nach Fehlern oder Problemen im Code fragt.
```

**Erwartetes Ergebnis:** `.claude/skills/bug-finder/SKILL.md`

---

## Aufgabe 3 – settings.local.json erweitern (15 min)

Die aktuelle `settings.local.json` erlaubt bereits einige Befehle.  
Füge folgende Erlaubnisse hinzu:

**Gewünschte Erweiterungen:**

- `python -m pytest test_app.py -v --tb=short` (ausführliche Test-Ausgabe)
- `cat todos.json` (JSON-Datei anzeigen)
- `python app.py` (App direkt starten)

**Manuell** – Datei öffnen und `allow`-Array ergänzen:

```json
"Bash(python -m pytest test_app.py -v --tb=short)",
"Bash(cat todos.json)",
"Bash(python app.py)"
```

**Oder per Prompt:**

```
Erweitere die .claude/settings.local.json so, dass Claude folgende
Befehle ohne Rückfrage ausführen darf:
- pytest mit verbose Output und kurzem Traceback
- cat todos.json zum Anzeigen des aktuellen Datenstands
- python app.py zum direkten Starten der App

Erkläre mir danach, warum permissions.deny sinnvoll ist und
ergänze dort eine Regel, die verhindert, dass todos.json gelöscht wird.
```

**Erwartetes Ergebnis:** Erweiterte `settings.local.json`

---

## Bonus – Skill testen (5 min)

Rufe den neuen `bug-finder`-Skill in Claude Code auf:

```
Schau dir app.py an und prüfe den Code auf mögliche Fehler und Probleme.
```

Beobachte: Verhält sich Claude anders als ohne den Skill?

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] Eine verbesserte `CLAUDE.md` mit Architecture-Abschnitt
- [ ] Einen neuen Skill `bug-finder` unter `.claude/skills/`
- [ ] Erweiterte `settings.local.json` mit neuen Erlaubnissen
