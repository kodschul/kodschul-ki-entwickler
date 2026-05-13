# Custom Commands

**Block:** 10:45 – 12:15 Uhr

---

## Wie funktioniert das unter der Haube?

```
/todo-review
  → Claude Code sucht .claude/commands/todo-review.md
  → Dateiinhalt wird als Prompt gesendet
  → Claude führt die beschriebenen Schritte aus
```

> Ein Command ist eine **Textdatei als Prompt** – kein Skript, kein Code.

**`$ARGUMENTS`:**

```
/add-feature Prioritäten         → $ARGUMENTS = "Prioritäten"
```

**Scope:** `.claude/commands/` → nur dieses Projekt | `~/.claude/commands/` → global

---

## Warum / Wann nicht?

| Warum nutzen                    | Wann nicht                                         |
| ------------------------------- | -------------------------------------------------- |
| Gleicher Workflow, immer gleich | Einmalige Aufgabe → direkt tippen                  |
| Teamstandard via Git            | Sehr langer Workflow (>20 Schritte) → lieber Agent |
| Onboarding: `/setup` und los    | Sensible Daten als Argument → nie                  |
| Versionierbar im Repo           | Zu viele Varianten → mehrere Commands anlegen      |

---

## Was sind Custom Commands?

Custom Commands sind **eigene Slash-Befehle** in Claude Code.  
Wenn du `/mein-command` eintippst, führt Claude den definierten Workflow aus.

**Wann sinnvoll?**

- Aufgaben, die du **regelmäßig** machst (Code-Review, Test generieren, Dokumentation)
- Workflows, die **immer gleich** ablaufen sollen
- Abkürzungen für lange Prompts

---

## Wo liegen Commands?

```
mein-projekt/
└── .claude/
    └── commands/
        ├── todo-review.md     → aufrufbar mit /todo-review
        ├── add-feature.md     → aufrufbar mit /add-feature
        └── run-tests.md       → aufrufbar mit /run-tests
```

**Oder global** (für alle Projekte):

```
~/.claude/commands/
└── daily-review.md
```

---

## Aufbau einer Command-Datei

```markdown
# Command-Titel

[Beschreibung was dieser Command tut]

## Schritte

1. Schritt 1 – was Claude als erstes tun soll
2. Schritt 2 – nächste Aktion
3. Schritt 3 – Ausgabe oder Ergebnis

## Regeln

- Regel A
- Regel B
```

**Sonderzeichen / Platzhalter:**

| Platzhalter     | Bedeutung                                                      |
| --------------- | -------------------------------------------------------------- |
| `$ARGUMENTS`    | Alles, was der Nutzer nach `/command text hier` eingegeben hat |
| `$CURRENT_FILE` | Der aktuell geöffnete Dateiname                                |
| `$CURRENT_DIR`  | Das aktuelle Verzeichnis                                       |

---

## Beispiel 1 – Einfacher Review-Command

**Datei:** `.claude/commands/todo-review.md`

```markdown
# Todo-App Code Review

Führe einen vollständigen Code-Review der Todo-App durch.

## Prüfpunkte

1. Lies app.py komplett
2. Prüfe alle Flask-Routen auf:
   - Fehlende Input-Validierung
   - Fehlende Fehlerbehandlung
   - Sicherheitsprobleme (z.B. keine Auth)
3. Prüfe todos.json-Handling auf Race-Conditions
4. Erstelle eine Checkliste mit Problemen (kritisch / mittel / niedrig)

## Ausgabe

Gib die Ergebnisse als Markdown-Tabelle aus:
| Problem | Datei | Schwere | Empfehlung |
```

**Aufrufen:** Einfach `/todo-review` in Claude Code eingeben.

---

## Beispiel 2 – Command mit Argument

**Datei:** `.claude/commands/add-feature.md`

```markdown
# Neues Feature zur Todo-App hinzufügen

Feature-Anfrage: $ARGUMENTS

## Schritte

1. Erstelle eine Spec-Datei unter specs/$ARGUMENTS.md mit:
   - User Story (Als Nutzer möchte ich...)
   - Datenmodell-Änderungen (falls nötig)
   - UI-Anforderungen
   - Akzeptanzkriterien (mindestens 3)
2. Zeige die Spec und warte auf Bestätigung
3. Implementiere das Feature erst nach Bestätigung

## Regeln

- Schreibe IMMER zuerst die Spec, nie direkt Code
- Halte die Implementierung minimal und fokussiert
- Erstelle nach der Implementierung Tests in test_app.py
```

**Aufrufen:** `/add-feature Prioritäten für Todos`

---

## Beispiel 3 – Test-Runner Command

**Datei:** `.claude/commands/run-tests.md`

```markdown
# Tests ausführen und auswerten

1. Führe aus: `python -m pytest test_app.py -v --tb=short`
2. Analysiere die Ausgabe
3. Bei Fehlern: Erkläre jeden Fehler in einem Satz auf Deutsch
4. Schlage konkrete Fixes vor, ohne sie direkt umzusetzen
```

**Aufrufen:** `/run-tests`

---

## Vergleich: Command vs. Skill vs. Agent

|              | Command             | Skill               | Agent                     |
| ------------ | ------------------- | ------------------- | ------------------------- |
| **Aufruf**   | `/command-name`     | Automatisch erkannt | Per Name aufgerufen       |
| **Wann**     | Explizite Aktion    | Kontextbasiert      | Spezialisierte Aufgabe    |
| **Tools**    | Alle verfügbaren    | Alle verfügbaren    | Eingeschränkt definierbar |
| **Beispiel** | `/run-tests`        | Feature bauen       | Security-Audit            |
| **Datei**    | `.claude/commands/` | `.claude/skills/`   | `.claude/agents/`         |
