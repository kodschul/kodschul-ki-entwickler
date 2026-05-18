# Tagesübersicht – GitHub Copilot

**Schulungszeit:** 09:00 – 17:00 Uhr

---

## Was haben wir bisher gemacht?

| Thema                     | Inhalt                                                          |
| ------------------------- | --------------------------------------------------------------- |
| GitHub Copilot Grundlagen | Installation, erste Prompts, copilot-instructions.md eingeführt |
| Todo-App aufgebaut        | Flask-App mit CRUD, JSON-Speicher, Tailwind-UI                  |
| Instructions eingeführt   | `.instructions.md` verstehen und erste Anweisungen geschrieben  |

**Unsere App:** `1205/todo-app/` – diese App bauen wir heute weiter aus.

---

## Roter Faden heute

Wir simulieren einen echten Entwicklertag:

```
Morgenbesprechung
 → Konfiguration professionell aufstellen
 → Prompt-Dateien schreiben (eigene Slash-Befehle)
 → Custom Agents bauen (spezialisierte KI-Helfer)
 → VS Code Tasks verbinden (Automation)
 → Feature spec-driven entwickeln
 → MCP anbinden
 → CLI & CI-Modus mit gh copilot
```

Jeder Block = **ein reales Problem** an der Todo-App lösen.  
Jede Übung = **ein Artefakt**, das in der App bleibt.

---

## Tagesplan

| Zeit              | Block                                  | Format         |
| ----------------- | -------------------------------------- | -------------- |
| 09:00 – 09:15     | Übersicht (dieser Block)               | Frontal        |
| 09:15 – 10:30     | Konfiguration & .md-Dateien            | Theorie + Demo |
| **10:30 – 10:45** | **Pause**                              |                |
| 10:45 – 12:15     | Custom Prompts + Custom Agents + Tasks | Demo + Übung   |
| **12:15 – 13:15** | **Mittagspause**                       |                |
| 13:15 – 15:00     | Spec-Driven Development                | Demo + Übung   |
| **15:00 – 15:15** | **Pause**                              |                |
| 15:15 – 17:00     | MCP + gh copilot CLI + Abschluss       | Demo + Retro   |

---

## Ziel am Ende des Tages

Die Todo-App hat:

- Professionelle `.github/copilot-instructions.md` + `.github/instructions/*.instructions.md`
- Eigene Slash-Commands (`.github/prompts/todo-review.prompt.md`, `/add-feature`)
- Spezialisierte Agents (`.github/agents/security-reviewer.agent.md`)
- Automatische Tasks (Tests laufen über `.vscode/tasks.json`)
- Ein neues Feature über eine Spec implementiert und getestet
- `gh copilot suggest` für CLI-Automation genutzt

---

## GitHub Copilot vs. Claude Code – Schnellvergleich

| Claude Code                   | GitHub Copilot Äquivalent                |
| ----------------------------- | ---------------------------------------- |
| `CLAUDE.md`                   | `.github/copilot-instructions.md`        |
| `~/.claude/settings.json`     | VS Code User Settings (`settings.json`)  |
| `.claude/settings.local.json` | `.vscode/settings.json`                  |
| `.claude/commands/*.md`       | `.github/prompts/*.prompt.md`            |
| `.claude/agents/*.md`         | `.github/agents/*.agent.md`              |
| `.claude/skills/*/SKILL.md`   | `.github/instructions/*.instructions.md` |
| `hooks` in settings.json      | `.vscode/tasks.json` + GitHub Actions    |
| `mcpServers` in settings.json | `.vscode/mcp.json`                       |
| `claude --print "..."`        | `gh copilot suggest "..."`               |
