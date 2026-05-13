# Konfiguration & .md-Dateien

**Block:** 09:15 – 10:30 Uhr

---

## Wie funktioniert das unter der Haube?

Beim Start liest Claude Code automatisch definierte Dateien und baut daraus den **System-Prompt** – unsichtbar, vor jeder Antwort.

```
Start
  → CLAUDE.md       → Projektkontext
  → .claude/skills/ → verfügbare Skills
  → settings.json   → erlaubte Tools & Befehle
  → Erste Antwort ist bereits kontextuell korrekt
```

> Diese Dateien sind kein Code – sie sind **Kontext**. Claude liest sie wie ein Briefing.

---

## Warum / Wann nicht?

| Warum nutzen                      | Wann nicht                                      |
| --------------------------------- | ----------------------------------------------- |
| Gleicher Kontext bei jedem Start  | Einmaliger Prompt → direkt tippen               |
| Teamkontext via Git teilbar       | Sensible Daten → niemals in `.md`, immer `.env` |
| Befehle erlauben / sperren        | Zu viele Skills (>10) → Claude wird ungenau     |
| Lange Prompts als Datei speichern | Sehr spezifische Ausnahme → Kommentar im Code   |

---

## Überblick: Welche Datei macht was?

| Datei                 | Wo                       | Zweck                                              |
| --------------------- | ------------------------ | -------------------------------------------------- |
| `CLAUDE.md`           | Projektroot              | Kontext & Regeln für Claude in diesem Projekt      |
| `SKILL.md`            | `.claude/skills/<name>/` | Wiederverwendbare Arbeitsanweisung für einen Skill |
| `commands/<name>.md`  | `.claude/commands/`      | Slash-Command (`/name`) mit eigenem Workflow       |
| `agents/<name>.md`    | `.claude/agents/`        | Spezialisierter Sub-Agent mit eigenen Tools/Regeln |
| `settings.local.json` | `.claude/`               | Projektspezifische Berechtigungen & Hooks          |
| `settings.json`       | `~/.claude/`             | Globale Konfiguration (alle Projekte)              |

---

## CLAUDE.md – Projektkontext

Claude liest `CLAUDE.md` **automatisch** beim Start jeder Session.  
Hier steht alles, was Claude über das Projekt wissen muss.

**Aufbau:**

```markdown
# CLAUDE.md

## Project Goal

[Ein Satz – was macht diese App?]

## Commands

[Wie starte/teste ich die App?]

## Do

[Was soll Claude tun?]

## Don't

[Was soll Claude NICHT tun?]
```

**Beispiel – unsere Todo-App:**

```markdown
# CLAUDE.md

## Project Goal

Minimale Todo-Web-App zum Lernen – Flask + HTML-Forms.
Nutzer können Todos anlegen, bearbeiten, abhaken, löschen.

## Commands

FLASK_DEBUG=1 python app.py # Dev-Server starten
python -m pytest test_app.py # Tests ausführen

## Do

- HTML-Form-POSTs mit Redirect verwenden (Post/Redirect/Get)
- Alle Daten in todos.json speichern
- Tailwind CDN für Styling nutzen

## Don't

- Keine REST-API oder JavaScript fetch
- Keine Datenbank oder ORM
- Keine zusätzlichen Python-Dateien
```

**Tipp:** Je präziser die CLAUDE.md, desto weniger muss man Claude erklären.

---

## SKILL.md – Wiederverwendbare Skills

Ein Skill ist eine **Anleitung für eine bestimmte Aufgabe**, die Claude immer gleich ausführen soll.

**Aufbau:**

```markdown
---
name: skill-name
description: Wann wird dieser Skill verwendet?
---

# Titel

- Schritt 1
- Schritt 2
- Regel A
- Regel B
```

**Beispiele aus unserer App:**

```markdown
# .claude/skills/feature-builder/SKILL.md

---

name: feature-builder
description: Use when building a new feature in the app

---

- Denke an 3 mögliche Umsetzungsstrategien und frage den Nutzer,
  welche er bevorzugt, bevor du anfängst
- Nach der Implementierung schreibe Tests, um das Feature zu prüfen
```

```markdown
# .claude/skills/api-designer/SKILL.md

---

name: api-designer
description: Use when designing a new API for the app

---

- Nutze REST-API Prinzipien
- Swagger für Dokumentation und Tests einbinden
- Statisches Bearer-Token für Authentifizierung
```

**Skill aufrufen:** Einfach in der Konversation beschreiben, was man tun will – Claude erkennt den passenden Skill über `description`.

---

## settings.local.json – Projektberechtigungen

Die Datei liegt unter `.claude/settings.local.json` und gilt nur für **dieses Projekt**.

**Aufbau:**

```json
{
  "permissions": {
    "allow": ["Bash(python -m pytest test_app.py -v)", "Bash(pip install *)"],
    "deny": []
  },
  "hooks": {}
}
```

**Unsere Todo-App – vollständiges Beispiel:**

```json
{
  "permissions": {
    "allow": [
      "Bash(FLASK_APP=app.py python3 -m flask run --port 5001)",
      "Bash(curl -s http://localhost:5001)",
      "mcp__playwright__browser_navigate",
      "mcp__playwright__browser_take_screenshot",
      "mcp__playwright__browser_fill_form",
      "mcp__playwright__browser_click",
      "Bash(pip install *)",
      "Bash(python -m pytest test_app.py -v)"
    ]
  }
}
```

**Wichtige Felder:**

| Feld                | Bedeutung                                                     |
| ------------------- | ------------------------------------------------------------- |
| `permissions.allow` | Diese Bash-Befehle/Tools darf Claude ohne Rückfrage ausführen |
| `permissions.deny`  | Diese Befehle sind komplett gesperrt                          |
| `hooks`             | Automationsregeln (→ Block Hooks)                             |

---

## settings.json – Globale Konfiguration

Liegt unter `~/.claude/settings.json` – gilt für **alle Projekte**.

**Typische Felder:**

```json
{
  "model": "claude-sonnet-4-5",
  "theme": "dark",
  "permissions": {
    "allow": [],
    "deny": ["Bash(rm -rf *)"]
  },
  "mcpServers": {}
}
```

---

## Entscheidungshilfe: Welche Datei brauche ich?

```
Ich will Claude erklären, was mein Projekt tut
  → CLAUDE.md

Ich will eine Aufgabe immer gleich erledigt haben (z.B. API designen)
  → SKILL.md

Ich will einen eigenen /slash-command
  → .claude/commands/<name>.md

Ich will einen spezialisierten Helfer mit eigenen Regeln
  → .claude/agents/<name>.md

Ich will bestimmte Befehle erlauben oder sperren
  → .claude/settings.local.json

Ich will etwas für alle meine Projekte konfigurieren
  → ~/.claude/settings.json
```
