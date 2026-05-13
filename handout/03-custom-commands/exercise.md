# Übung: Custom Commands

**Zeit:** 10:45 – 12:15 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Command `/todo-review` erstellen (20 min)

**Ziel:** Einen Command bauen, der die Todo-App reviewed und eine strukturierte Checkliste ausgibt.

**Schritt 1 – Datei anlegen:**

```bash
mkdir -p .claude/commands
```

Erstelle `.claude/commands/todo-review.md`:

```markdown
# Todo-App Code Review

Führe einen vollständigen Code-Review der Todo-App durch.

## Prüfpunkte

1. Lies app.py komplett durch
2. Prüfe alle Flask-Routen auf:
   - Fehlende Input-Validierung (z.B. leere Todos)
   - Fehlende Fehlerbehandlung (try/except)
   - Sicherheitsprobleme
3. Prüfe das todos.json-Handling
4. Zähle wie viele Routen Tests in test_app.py haben

## Ausgabe

Gib das Ergebnis als Markdown-Tabelle aus:

| Problem | Datei/Route | Schwere (hoch/mittel/niedrig) | Empfehlung |
| ------- | ----------- | ----------------------------- | ---------- |
```

**Schritt 2 – Testen:**

Gib in Claude Code ein: `/todo-review`

**Fragen zum Nachdenken:**

- Was gibt Claude aus?
- Sind die Probleme korrekt?
- Was würdest du am Command ändern?

---

## Aufgabe 2 – Command `/add-feature` mit Argument (25 min)

**Ziel:** Ein Command, der zuerst eine Spec schreibt, bevor Code entsteht.

**Erstelle** `.claude/commands/add-feature.md`:

```markdown
# Neues Feature planen

Feature-Anfrage: $ARGUMENTS

## Ablauf

1. Erstelle eine neue Datei specs/$ARGUMENTS.md mit folgendem Inhalt:
   - **User Story:** Als Nutzer möchte ich [Feature], damit [Nutzen]
   - **Datenmodell:** Welche Felder in todos.json müssen sich ändern?
   - **UI:** Was sieht der Nutzer? Beschreibe es in 2-3 Sätzen
   - **Akzeptanzkriterien:** Mindestens 3 konkrete, testbare Kriterien
2. Zeige die Spec und frage: "Soll ich mit der Implementierung beginnen?"
3. Implementiere nur nach expliziter Bestätigung

## Regeln

- IMMER zuerst die Spec, nie direkt Code
- Spec-Datei im Ordner specs/ anlegen
- Ändere app.py erst nach Bestätigung
```

**Testen:**

```
/add-feature Prioritäten für Todos
```

**Erwartetes Ergebnis:**

- Datei `specs/Prioritäten für Todos.md` wird erstellt
- Claude wartet auf Bestätigung
- Danach optional: Bestätige und beobachte die Implementierung

---

## Aufgabe 3 – Eigenen Command erfinden (20 min)

**Aufgabe:** Erfinde und baue einen eigenen Command für ein Problem, das du oft hast.

**Ideen (falls keine eigene kommt):**

| Command        | Zweck                                                 |
| -------------- | ----------------------------------------------------- |
| `/cleanup`     | Findet TODOs und print-Statements im Code             |
| `/docs`        | Generiert eine README-Sektion für eine Route          |
| `/diff-review` | Beschreibt was sich seit letztem Commit verändert hat |
| `/performance` | Prüft auf offensichtliche Performance-Probleme        |

**Prompt zum Starten:**

```
Erstelle einen neuen Claude-Code-Command unter .claude/commands/<name>.md.
Der Command soll [BESCHREIBUNG DEINES COMMANDS].
Er soll folgende Schritte ausführen:
1. ...
2. ...
Die Ausgabe soll [FORMAT] sein.
```

---

## Bonus – Command ohne Datei testen

Man kann Commands auch direkt in der Konsole als langen Prompt schreiben.  
Vergleiche: Ist ein Command in einer Datei besser als ein langer Prompt? Warum?

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] `.claude/commands/todo-review.md` erstellt und getestet
- [ ] `.claude/commands/add-feature.md` mit `$ARGUMENTS` erstellt
- [ ] Eine Spec-Datei durch `/add-feature` generiert
- [ ] Einen eigenen Command nach Wahl erstellt
