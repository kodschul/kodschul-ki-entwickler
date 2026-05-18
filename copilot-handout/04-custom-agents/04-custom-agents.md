# Custom Agents

**Block:** 10:45 – 12:15 Uhr (zusammen mit Prompts & Tasks)

---

## Wie funktioniert das unter der Haube?

```
Copilot erhält eine Aufgabe im Agent-Modus
  → erkennt: Agent "security-reviewer" ist zuständig
  → startet mit eigenem System-Prompt + definierten Tools
  → Agent arbeitet isoliert, gibt Ergebnis zurück
  → Copilot nutzt das Ergebnis weiter
```

> Ein Agent ist ein **spezialisierter Copilot-Prozess** mit eigenem System-Prompt und definierten Tool-Rechten.  
> Agents können nicht mehr tun als erlaubt – Least-Privilege-Prinzip.

**Datei:** `.github/agents/<name>.agent.md`  
**Felder im Frontmatter:**

```yaml
---
name: agent-name
description: "Wann wird dieser Agent verwendet?"
tools: # Tool-Whitelist
  - codebase
  - terminal
---
```

---

## Warum / Wann nicht?

| Warum nutzen                                    | Wann nicht                                             |
| ----------------------------------------------- | ------------------------------------------------------ |
| Spezialisierte Aufgabe mit klarem Scope         | Einfache Aufgabe → Prompt reicht                       |
| Tool-Beschränkung nötig (nur lesen, nur testen) | Kein Mehrwert ohne Tool-Einschränkung                  |
| Langer Workflow mit eigenen Regeln              | Aufgabe braucht vollen Tool-Zugriff → kein Agent nötig |
| Wiederverwendbarer Spezialist                   | Zu viele Agents → Übersicht verloren                   |

---

## Vergleich: Prompt vs. Instruction vs. Agent

|            | Prompt (`.prompt.md`) | Instruction (`.instructions.md`) | Agent (`.agent.md`)       |
| ---------- | --------------------- | -------------------------------- | ------------------------- |
| **Aufruf** | `/name` in Chat       | Automatisch bei Datei-Match      | Per Beschreibung / Aufruf |
| **Tools**  | Konfigurierbar        | Keine Tools                      | Eingeschränkt definierbar |
| **Scope**  | Workflow-Schritte     | Verhaltensregeln                 | Eigenständige Aufgabe     |
| **Datei**  | `.github/prompts/`    | `.github/instructions/`          | `.github/agents/`         |

---

## Verfügbare Tools für Agents

| Tool         | Beschreibung                                       |
| ------------ | -------------------------------------------------- |
| `codebase`   | Codebase durchsuchen und Dateien lesen             |
| `terminal`   | Terminal-Befehle ausführen                         |
| `githubRepo` | GitHub Repository-Daten abrufen (Issues, PRs etc.) |
| `search`     | Web-Suche durchführen                              |
| `extensions` | VS Code Extensions nutzen                          |

---

## Aufbau – Vollständiges Beispiel

**`.github/agents/security-reviewer.agent.md`**

```markdown
---
name: security-reviewer
description: "Führt einen Sicherheits-Audit der App durch. Nur lesen, kein Code ändern."
tools:
  - codebase
---

# Security Reviewer

Analysiere alle Python-Dateien auf Sicherheitsprobleme.

## Prüfpunkte

- Hardcodierte Tokens oder Passwörter
- Fehlende Input-Validierung in Flask-Routen
- eval() oder exec() Aufrufe
- Fehlende Authentifizierung an sensiblen Routen
- Unsichere Dateioperationen

## Ausgabe

Markdown-Tabelle:
| Problem | Datei | Zeile | Schwere | Empfehlung |
```

---

**`.github/agents/test-writer.agent.md`**

```markdown
---
name: test-writer
description: "Generiert pytest-Tests für neue oder ungetestete Routen in app.py"
tools:
  - codebase
  - terminal
---

# Test Writer

1. Lies app.py und test_app.py komplett
2. Finde alle Routen in app.py, die noch keinen Test haben
3. Schreibe für jede fehlende Route mindestens 2 Tests:
   - Happy path (normaler Aufruf)
   - Edge case (leere Eingabe, ungültiger Wert)
4. Nutze das bestehende client-Fixture aus test_app.py
5. Schreibe nur in test_app.py – keine anderen Dateien ändern

## Regeln

- Keine neuen Fixtures einführen
- Bestehende Tests nicht verändern
- Kommentare auf Deutsch
```

---

## Agent aufrufen

Im **Agent-Modus** von Copilot Chat (`@agent` oder Modus-Umschalter):

```
Mach einen Sicherheits-Audit der App.
```

```
Schreib Tests für alle Routen, die noch nicht getestet sind.
```

Oder direkt im Chat mit Verweis auf den Agent:

```
@security-reviewer Analysiere app.py auf Sicherheitsprobleme.
```

---

## gh copilot CLI – Agent-ähnliche Workflows

```bash
# Security-Scan über CLI anstoßen
gh copilot suggest "Python-Dateien auf Sicherheitsprobleme scannen und Bericht erstellen"

# Test-Generierung über CLI
gh copilot suggest -t shell "pytest-Tests für alle Routes in app.py generieren"
```
