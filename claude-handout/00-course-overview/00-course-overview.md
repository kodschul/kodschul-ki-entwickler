# Claude Code – 4-Tages-Schulung

**Ziel:** Claude Code professionell einsetzen – von den Grundlagen generativer KI über die ersten Schritte im Terminal bis zu eigenen Agents, Hooks und CI-Automation.

> **Hinweis:** Struktur und Zeiten sind 1-zu-1 an den GitHub-Copilot-Kurs (`copilot-handout/`) angelehnt, inhaltlich aber auf Claude Codes agentisches, terminal-first Arbeiten zugeschnitten. Zeiten sind Richtwerte.

---

## Inhalte

**Grundlagen (Modul 01 – 6 Unterthemen in einem Ordner)**

- Arten von KI-Integrationen (Autocomplete, Chat, Agent Terminal/headless)
- Generative KI und LLMs in a Nutshell
- Generative KI im Coding (planen, schreiben, analysieren, refactoren, testen)
- Generative KI in Softwareprojekten (Requirements, Konzeption, Styles)
- Generative KI kreativ eingesetzt (Skills, Modelle, Ausblick)
- Recht, Sicherheit & Datenschutz bei KI-generiertem Code

**Claude-Code-Praxis (Modul 02–13)**

- Erste Schritte, Kontext & CLAUDE.md, Built-in Commands, Konfiguration
- Skills, Custom Commands, Custom Agents, Hooks & Automation
- Token-Management, Claude Code CLI vollständig, Spec-Driven Development, MCP

**Abschluss (Modul 14–16)**

- Neuerungen: Checkpoints/Rewind, IDE & Web, Plan Mode, Agent Skills als Standard
- Best Practices (Modul 15 – 7 Unterthemen): Multi-Agent-Orchestrierung, Kostenoptimierung, Team-Zusammenarbeit, parallele Sessions & Delegation, große Codebases, EU-KI-Verordnung, Wissen persistieren
- Outro: Zusammenfassung & nächste Schritte

---

## Themenübersicht (alle 4 Tage)

| #   | Thema                                       | Tag   | Dauer   |
| --- | ---------------------------------------------- | ----- | ------- |
| 01  | Grundlagen (6 Unterthemen, siehe unten)          | Tag 1 | 255 min |
| 02  | Erste Schritte mit Claude Code                    | Tag 2 | 90 min  |
| 03  | Kontext bereitstellen (CLAUDE.md)                 | Tag 2 | 90 min  |
| 04  | Built-in Commands                                 | Tag 2 | 90 min  |
| 05  | Konfiguration                                     | Tag 2 | 60 min  |
| 06  | Skills & CLAUDE.md-Vertiefung                      | Tag 3 | 90 min  |
| 07  | Custom Commands                                   | Tag 3 | 90 min  |
| 08  | Custom Agents                                     | Tag 3 | 90 min  |
| 09  | Hooks & Automation                                | Tag 3 | 60 min  |
| 10  | Token-Management                                  | Tag 4 | 60 min  |
| 11  | Claude Code CLI – vollständig                      | Tag 4 | 90 min  |
| 12  | Spec-Driven Development                           | Tag 4 | 90 min  |
| 13  | MCP – Model Context Protocol                      | Tag 4 | 60 min  |
| 14  | Neuerungen                                        | Tag 4 | 60 min  |
| 15  | Best Practices (7 Unterthemen, siehe unten)        | Tag 4 | 200 min |
| 16  | Outro                                             | Tag 4 | 30 min  |

---

## Tag 1 – Grundlagen (Modul 01)

```
09:00  01a Intro: Integrationsarten  Autocomplete vs. Chat vs. Agent (Terminal/headless)
09:30  01b LLMs in a Nutshell        Tokens, Context Window, Kontext einbringen
10:30  01c KI im Coding              Planen, Schreiben, Analyse, Refactoring, Testing
13:00  01d KI in Softwareprojekten   Requirements, Konzeption, Styles & Patterns
14:00  01e KI kreativ eingesetzt     Skills, Modelle, Ausblick
15:00  01f Recht & Security          Urheberrecht, Haftung, Privacy-by-design
```

**Dateien:** `01-grundlagen/01-intro-ki-integrationsarten.md` … `01-grundlagen/06-recht-sicherheit-privacy.md`

---

## Tag 2 – Fundamentals

```
09:00  02 Erste Schritte            Installation, REPL, erste Prompts
10:45  03 Kontext & CLAUDE.md       Automatischer Kontext, CLAUDE.md-Aufbau
13:15  04 Built-in Commands         /clear /compact /cost /init /permissions /mcp
15:15  05 Konfiguration             settings.json, settings.local.json, Permissions
```

**App:** `1205/todo-app/` – Flask, pytest, Tailwind

---

## Tag 3 – Customization

```
09:00  06 Skills & CLAUDE.md-Vertiefung   SKILL.md, verschachtelte CLAUDE.md
10:45  07 Custom Commands                 .claude/commands/*.md, $ARGUMENTS
13:15  08 Custom Agents                   .claude/agents/*.md, tools, Scope
15:15  09 Hooks & Automation              settings.json hooks, PreToolUse/PostToolUse
```

---

## Tag 4 – Advanced, Produktion & Neuerungen

```
09:00  10 Token-Management          Kontext sparen, /clear, /compact
10:00  11 Claude Code CLI           --print, --output-format, Headless, Sandbox
13:15  12 Spec-Driven Development   Manuelle Spec + Spec-Kit (/spec plan/​/spec/​/spec test)
15:15  13 MCP                       mcpServers, Playwright, eigene Server
16:15  14 Neuerungen                14a Checkpoints, 14b IDE/Web, 14c Plan Mode, 14d Skills-Standard
16:45  15 Best Practices           Multi-Agent, Kosten, Team, Delegation, große Codebases, EU-KI-Verordnung, Wissen persistieren
17:45  16 Outro                     Zusammenfassung, nächste Schritte
```

**Dateien Modul 14:** `14-neuerungen/01-checkpoints-rewind.md` … `14-neuerungen/04-agent-skills-standard.md`

**Dateien Modul 15:** `15-best-practices/01-multi-agent-orchestrierung.md` … `15-best-practices/07-wissen-persistieren.md`

---

## Vollständige Dateistruktur & Mapping-Referenz

Siehe [claude-structure-reference.md](claude-structure-reference.md) für die vollständige `.claude/`-Verzeichnisstruktur und eine Mapping-Tabelle Copilot ↔ Claude Code.
