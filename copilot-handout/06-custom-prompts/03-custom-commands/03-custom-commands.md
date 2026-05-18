# Custom Prompts (Slash Commands)

**Block:** 10:45 – 12:15 Uhr

---

## Wie funktioniert das unter der Haube?

```
/todo-review
  → Copilot sucht .github/prompts/todo-review.prompt.md
  → Dateiinhalt wird als Prompt gesendet
  → Copilot führt die beschriebenen Schritte aus
```

> Eine Prompt-Datei ist eine **Textdatei als Prompt** – kein Skript, kein Code.

**`${input:variablenname}`:**

```
/add-feature mit ${input:featureName}  →  Copilot fragt nach dem Feature-Namen
```

**Scope:** `.github/prompts/` → für dieses Projekt (via Git teilbar)

---

## Warum / Wann nicht?

| Warum nutzen                    | Wann nicht                                          |
| ------------------------------- | --------------------------------------------------- |
| Gleicher Workflow, immer gleich | Einmalige Aufgabe → direkt tippen                   |
| Teamstandard via Git            | Sehr langer Workflow (>20 Schritte) → lieber Agent  |
| Onboarding: `/setup` und los    | Sensible Daten als Argument → nie                   |
| Versionierbar im Repo           | Zu viele Varianten → mehrere Prompt-Dateien anlegen |

---

## Was sind Custom Prompts?

Custom Prompts sind **eigene Slash-Befehle** in GitHub Copilot Chat.  
Wenn du `/mein-prompt` eintippst, führt Copilot den definierten Workflow aus.

**Wann sinnvoll?**

- Aufgaben, die du **regelmäßig** machst (Code-Review, Test generieren, Dokumentation)
- Workflows, die **immer gleich** ablaufen sollen
- Abkürzungen für lange Prompts

---

## Wo liegen Prompt-Dateien?

```
mein-projekt/
└── .github/
    └── prompts/
        ├── todo-review.prompt.md     → aufrufbar mit /todo-review
        ├── add-feature.prompt.md     → aufrufbar mit /add-feature
        └── run-tests.prompt.md       → aufrufbar mit /run-tests
```

---

## Aufbau einer Prompt-Datei

```markdown
---
mode: ask # "ask" | "edit" | "agent"
description: "Beschreibung was dieser Command tut"
tools:
  - codebase
  - terminal
---

# Command-Titel

[Beschreibung was dieser Command tut]

## Schritte

1. Schritt 1 – was Copilot als erstes tun soll
2. Schritt 2 – nächste Aktion
3. Schritt 3 – Ausgabe oder Ergebnis

## Regeln

- Regel A
- Regel B
```

**Frontmatter-Optionen:**

| Feld          | Bedeutung                                                        |
| ------------- | ---------------------------------------------------------------- |
| `mode`        | `ask` (nur lesen/antworten), `edit` (Datei bearbeiten), `agent`  |
| `description` | Wird in der Slash-Command-Liste angezeigt                        |
| `tools`       | Liste der erlaubten Tools (`codebase`, `terminal`, `githubRepo`) |

**Variablen:**

| Platzhalter          | Bedeutung                                |
| -------------------- | ---------------------------------------- |
| `${input:name}`      | Copilot fragt den Nutzer nach einem Wert |
| `${file}`            | Aktuell geöffnete Datei                  |
| `${selection}`       | Aktuell markierter Code                  |
| `${workspaceFolder}` | Pfad zum Projektordner                   |

---

## Beispiel 1 – Einfacher Review-Command

**Datei:** `.github/prompts/todo-review.prompt.md`

```markdown
---
mode: ask
description: "Vollständiger Code-Review der Todo-App"
tools:
  - codebase
---

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

**Aufrufen:** `/todo-review` in Copilot Chat eingeben.

---

## Beispiel 2 – Command mit Eingabe

**Datei:** `.github/prompts/add-feature.prompt.md`

```markdown
---
mode: agent
description: "Neues Feature planen und implementieren"
tools:
  - codebase
  - terminal
---

# Neues Feature zur Todo-App hinzufügen

Feature-Anfrage: ${input:featureName}

## Schritte

1. Erstelle eine Spec-Datei unter specs/${input:featureName}.md mit:
   - User Story (Als Nutzer möchte ich...)
   - Datenmodell-Änderungen (falls nötig)
   - UI-Anforderungen
   - Akzeptanzkriterien (mindestens 3)
2. Zeige die Spec und warte auf Bestätigung
3. Implementiere das Feature erst nach Bestätigung

## Regeln

- IMMER zuerst die Spec, nie direkt Code
- Spec-Datei im Ordner specs/ anlegen
- app.py erst nach Bestätigung ändern
```

**Aufrufen:** `/add-feature` → Copilot fragt nach dem Feature-Namen.

---

## gh copilot CLI – Commands im Terminal

```bash
# Befehl für ein bestimmtes Ziel vorschlagen
gh copilot suggest "Code-Review von app.py als Markdown ausgeben"

# Zieltyp angeben
gh copilot suggest -t shell "Tests ausführen und Ergebnis in Datei speichern"
gh copilot suggest -t git "Alle geänderten Python-Dateien committen"
gh copilot suggest -t gh "Pull Request für das Feature branch erstellen"

# Befehl direkt ausführen lassen (nach Bestätigung)
gh copilot suggest "pytest mit verbose output" --execute
```
