# Tag 1 – GitHub Copilot Grundlagen

**Schulungszeit:** 09:00 – 17:00 Uhr

---

## Ziel des Tages

Am Ende von Tag 1 kannst du GitHub Copilot als echten Coding-Assistenten nutzen:  
Inline-Vorschläge bewusst steuern, den Chat-Kontext gezielt aufbauen und mit eingebauten Commands produktiv arbeiten.

---

## Tagesplan

| Zeit              | Block                                        | Format       |
| ----------------- | -------------------------------------------- | ------------ |
| 09:00 – 09:15     | Übersicht + Setup-Check                      | Frontal      |
| 09:15 – 10:30     | Inline Completions – Ghost Text meistern     | Demo + Übung |
| **10:30 – 10:45** | **Pause**                                    |              |
| 10:45 – 12:15     | Chat-Grundlagen – Kontext & Variablen        | Demo + Übung |
| **12:15 – 13:15** | **Mittagspause**                             |              |
| 13:15 – 14:45     | Eingebaute Commands – /fix, /explain, /tests | Demo + Übung |
| **14:45 – 15:00** | **Pause**                                    |              |
| 15:00 – 17:00     | Konfiguration – copilot-instructions.md      | Demo + Übung |

---

## 3-Tages-Übersicht

| Tag   | Thema                 | Kerninhalt                                                      |
| ----- | --------------------- | --------------------------------------------------------------- |
| Tag 1 | Grundlagen            | Inline, Chat, eingebaute Commands, Konfiguration                |
| Tag 2 | Customization         | Instructions/Skills, Custom Prompts, Agents, Automation         |
| Tag 3 | Advanced & Produktion | Spec-Driven Development, Copilot CLI (Token-Sparen), MCP, CI/CD |

---

## Setup-Check

```bash
# GitHub CLI installiert?
gh --version

# GitHub Copilot CLI installiert?
gh copilot --version

# Falls nicht:
gh extension install github/gh-copilot
```

In VS Code prüfen:

- Extension `GitHub Copilot` ✓
- Extension `GitHub Copilot Chat` ✓
- Status-Bar unten: Copilot-Icon aktiv (nicht durchgestrichen) ✓

---

## Was wir heute bauen

Alle Übungen laufen auf der **Todo-App** unter `1205/todo-app/`.

Am Ende von Tag 1 hat die App:

- `FLASK_DEBUG=1 python app.py` → läuft
- `python -m pytest test_app.py` → läuft
- `.github/copilot-instructions.md` → erstellt und optimiert
