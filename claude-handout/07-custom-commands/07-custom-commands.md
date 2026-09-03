# 07 – Custom Commands

**Block:** 90 min | **Tag 3**

---

## Wie funktioniert das unter der Haube?

```
/todo-review
  → Claude Code sucht .claude/commands/todo-review.md
  → Dateiinhalt wird als Prompt gesendet
  → Claude führt die beschriebenen Schritte aus
```

> Ein Command ist eine **Textdatei als Prompt** – kein Skript, kein Code. Das Äquivalent bei GitHub Copilot heißt `.prompt.md`.

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

## Wo liegen Commands?

```
mein-projekt/
└── .claude/
    └── commands/
        ├── todo-review.md     → aufrufbar mit /todo-review
        ├── add-feature.md     → aufrufbar mit /add-feature
        └── run-tests.md       → aufrufbar mit /run-tests
```

Oder global (für alle Projekte): `~/.claude/commands/daily-review.md`

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

**Platzhalter:**

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
2. Prüfe alle Flask-Routen auf fehlende Input-Validierung, fehlende
   Fehlerbehandlung, Sicherheitsprobleme (z. B. keine Auth)
3. Prüfe todos.json-Handling auf Race-Conditions
4. Erstelle eine Checkliste mit Problemen (kritisch / mittel / niedrig)

## Ausgabe

Markdown-Tabelle: | Problem | Datei | Schwere | Empfehlung |
```

**Aufrufen:** `/todo-review`

---

## Beispiel 2 – Command mit Argument

**Datei:** `.claude/commands/add-feature.md`

```markdown
# Neues Feature zur Todo-App hinzufügen

Feature-Anfrage: $ARGUMENTS

## Schritte

1. Erstelle eine Spec-Datei unter specs/$ARGUMENTS.md (User Story,
   Datenmodell-Änderungen, UI-Anforderungen, mind. 3 Akzeptanzkriterien)
2. Zeige die Spec und warte auf Bestätigung
3. Implementiere das Feature erst nach Bestätigung

## Regeln

- Schreibe IMMER zuerst die Spec, nie direkt Code
- Erstelle nach der Implementierung Tests in test_app.py
```

**Aufrufen:** `/add-feature Prioritäten für Todos`

---

## Vergleich: Command vs. Skill vs. Agent

|            | Command             | Skill               | Agent                        |
| ---------- | ------------------- | ------------------- | ---------------------------- |
| **Aufruf** | `/command-name`     | Automatisch erkannt | Per Aufgabe delegiert        |
| **Wann**   | Explizite Aktion    | Kontextbasiert      | Spezialisierte Teilaufgabe   |
| **Tools**  | Alle verfügbaren    | Alle verfügbaren    | Eingeschränkt definierbar    |
| **Datei**  | `.claude/commands/` | `.claude/skills/`   | `.claude/agents/` (Modul 08) |
