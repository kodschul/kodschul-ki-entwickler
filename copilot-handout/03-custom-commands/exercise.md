# Übung: Custom Prompts (Slash Commands)

**Zeit:** 10:45 – 12:15 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Prompt `/todo-review` erstellen (20 min)

**Ziel:** Einen Custom Prompt bauen, der die Todo-App reviewed und eine strukturierte Checkliste ausgibt.

**Schritt 1 – Verzeichnis anlegen:**

```bash
mkdir -p .github/prompts
```

**Schritt 2 – Datei erstellen:** `.github/prompts/todo-review.prompt.md`

```markdown
---
mode: ask
description: "Vollständiger Code-Review der Todo-App mit Checkliste"
tools:
  - codebase
---

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

**Schritt 3 – Testen:**

Öffne Copilot Chat und gib ein: `/todo-review`

**Fragen zum Nachdenken:**

- Was gibt Copilot aus?
- Sind die Probleme korrekt?
- Was würdest du am Prompt ändern?

---

## Aufgabe 2 – Prompt `/add-feature` mit Eingabe (25 min)

**Ziel:** Ein Prompt, der zuerst eine Spec schreibt, bevor Code entsteht.

**Erstelle** `.github/prompts/add-feature.prompt.md`:

```markdown
---
mode: agent
description: "Neues Feature planen – Spec zuerst, dann Implementierung"
tools:
  - codebase
  - terminal
---

# Neues Feature planen

Feature-Anfrage: ${input:featureName}

## Ablauf

1. Erstelle eine neue Datei specs/${input:featureName}.md mit folgendem Inhalt:
   - **User Story:** Als Nutzer möchte ich [Feature], damit [Nutzen]
   - **Datenmodell:** Welche Felder in todos.json müssen sich ändern?
   - **UI:** Was sieht der Nutzer? Beschreibe es in 2-3 Sätzen
   - **Akzeptanzkriterien:** Mindestens 3 konkrete, testbare Kriterien
2. Zeige die Spec und frage: "Soll ich mit der Implementierung beginnen?"
3. Implementiere nur nach expliziter Bestätigung

## Regeln

- IMMER zuerst die Spec, nie direkt Code
- Spec-Datei im Ordner specs/ anlegen
- app.py erst nach Bestätigung ändern
```

**Testen:**

Öffne Copilot Chat und gib ein: `/add-feature`

Copilot fragt: Gib `Prioritäten für Todos` ein.

**Erwartetes Ergebnis:**

- Datei `specs/Prioritäten für Todos.md` wird erstellt
- Copilot wartet auf Bestätigung
- Danach optional: Bestätige und beobachte die Implementierung

---

## Aufgabe 3 – Eigenen Prompt erfinden (20 min)

**Aufgabe:** Erfinde und baue einen eigenen Custom Prompt für ein Problem, das du oft hast.

**Ideen (falls keine eigene kommt):**

| Idee               | Dateiname                         | Beschreibung                                        |
| ------------------ | --------------------------------- | --------------------------------------------------- |
| Dokumentation      | `generate-docs.prompt.md`         | Erstellt Docstrings für alle Funktionen in einer Datei |
| Changelog          | `update-changelog.prompt.md`      | Schreibt einen Changelog-Eintrag aus Git-Commits    |
| Refactoring        | `refactor-check.prompt.md`        | Prüft Code auf Refactoring-Potenzial                |
| Deployment-Check   | `deploy-checklist.prompt.md`      | Erstellt eine Checkliste vor einem Deployment       |

**Vorlage:**

```markdown
---
mode: ask
description: "[DEINE BESCHREIBUNG]"
tools:
  - codebase
---

# [DEIN COMMAND-TITEL]

[Was soll Copilot tun?]

## Schritte

1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]
```

**Testen und reflektieren:**

- Rufe deinen Command mit `/dein-command` auf
- Funktioniert der Workflow wie erwartet?
- Was müsstest du am Prompt verbessern?

---

## Aufgabe 4 – gh copilot CLI für Reviews (10 min)

```bash
# Code-Review über die CLI anstoßen
gh copilot suggest "Sicherheitsprobleme in app.py finden und als Markdown ausgeben"

# Ergebnis in Datei speichern (nach Copilot-Vorschlag ausführen)
gh copilot suggest -t shell "Python-Code auf Sicherheitsprobleme prüfen und Ergebnis speichern"
```

**Diskussion:** Wann nutzt du `gh copilot suggest` vs. Copilot Chat im Editor?
