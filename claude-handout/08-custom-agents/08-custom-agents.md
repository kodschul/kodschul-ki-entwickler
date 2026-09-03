# 08 – Custom Agents

**Block:** 90 min | **Tag 3**

---

## Wie funktioniert das unter der Haube?

```
Claude erhält eine Aufgabe
  → erkennt: Agent "test-writer" ist zuständig
  → startet Sub-Agent mit eigenem Kontext + eingeschränkten Tools
  → Sub-Agent arbeitet isoliert, gibt Ergebnis zurück
  → Haupt-Claude nutzt das Ergebnis weiter
```

> Ein Agent ist ein **spezialisierter Claude-Prozess** mit eigenem System-Prompt und definierten Tool-Rechten. Agents können nicht mehr tun als erlaubt – Least-Privilege-Prinzip.

**Datei:** `.claude/agents/<name>.md`

```yaml
---
name: agent-name
description: Wann wird dieser Agent verwendet?
model: sonnet # optional – welches Modell
tools: # optional – Tool-Whitelist
  - Read
  - Write
---
```

---

## Warum / Wann nicht?

| Warum nutzen                                    | Wann nicht                                             |
| ----------------------------------------------- | ------------------------------------------------------ |
| Spezialisierte Aufgabe mit klarem Scope         | Einfache Aufgabe → Command (Modul 07) reicht           |
| Tool-Beschränkung nötig (nur lesen, nur testen) | Kein Mehrwert ohne Tool-Einschränkung                  |
| Langer Workflow mit eigenen Regeln              | Aufgabe braucht vollen Tool-Zugriff → kein Agent nötig |
| Parallele Sub-Aufgaben delegieren (Modul 15)    | Zu viele Agents → Übersicht verloren                   |

---

## Vollständiges Beispiel

**`.claude/agents/security-reviewer.md`**

```markdown
---
name: security-reviewer
description: Führt einen Sicherheits-Audit der App durch. Nur lesen, kein Code ändern.
tools:
  - Read
---

# Security Reviewer

Analysiere alle Python-Dateien auf Sicherheitsprobleme.

## Prüfpunkte

- Hardcodierte Tokens oder Passwörter
- Fehlende Input-Validierung in Flask-Routen
- `eval()` oder `exec()` Aufrufe
- Fehlende Authentifizierung an sensiblen Routen
- Unsichere Dateioperationen

## Ausgabe

Markdown-Tabelle:
| Problem | Datei | Zeile | Schwere | Empfehlung |
```

**`.claude/agents/test-writer.md`**

```markdown
---
name: test-writer
description: Generiert pytest-Tests für neue oder ungetestete Routen in app.py
tools:
  - Read
  - Write(test_app.py)
---

# Test Writer

1. Lies app.py und test_app.py komplett
2. Finde alle Routen in app.py, die noch keinen Test haben
3. Schreibe für jede fehlende Route mindestens 2 Tests (Happy Path, Edge Case)
4. Nutze das bestehende `client`-Fixture aus test_app.py

## Regeln

- Keine neuen Fixtures einführen
- Bestehende Tests nicht verändern
```

## Agent aufrufen

Einfach beschreiben, was getan werden soll – Claude wählt den passenden Agent:

```
Mach einen Sicherheits-Audit der App.
```

```
Schreib Tests für alle Routen, die noch nicht getestet sind.
```

---

## Vergleich: Command vs. Skill vs. Agent

|            | Command             | Skill             | Agent                      |
| ---------- | ------------------- | ----------------- | -------------------------- |
| **Aufruf** | `/name`             | Automatisch       | Per Beschreibung delegiert |
| **Tools**  | Alle                | Alle              | Eingeschränkt definierbar  |
| **Scope**  | Workflow-Schritte   | Verhaltensregeln  | Eigenständige Teilaufgabe  |
| **Datei**  | `.claude/commands/` | `.claude/skills/` | `.claude/agents/`          |

> Vertiefung zur Delegation mehrerer Agents gleichzeitig: Modul 15 – Best Practices (Multi-Agent-Orchestrierung).
