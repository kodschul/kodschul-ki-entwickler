# .claude – Vollständige Struktur & Referenz

---

## Verzeichnisstruktur

```
mein-projekt/
├── CLAUDE.md                     ← Projektkontext (Modul 03)
└── .claude/
    ├── settings.json              ← Team-weite Konfiguration (eingecheckt, Modul 05)
    ├── settings.local.json        ← Persönliche/lokale Konfiguration (nicht eingecheckt)
    ├── commands/
    │   ├── todo-review.md         ← /todo-review (Modul 07)
    │   ├── add-feature.md         ← /add-feature
    │   └── run-tests.md           ← /run-tests
    ├── agents/
    │   ├── security-reviewer.md   ← Sicherheits-Audit Agent (Modul 08)
    │   └── test-writer.md         ← Test-Generierungs Agent
    └── skills/
        ├── feature-builder/
        │   └── SKILL.md            ← Modul 06
        ├── api-designer/
        │   └── SKILL.md
        └── bug-finder/
            └── SKILL.md

~/.claude/
├── settings.json                  ← Globale Konfiguration (alle Projekte)
└── commands/
    └── daily-review.md            ← Globaler Command
```

---

## Copilot vs. Claude Code – Mapping-Referenz

| GitHub Copilot                                       | Claude Code                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| `.github/copilot-instructions.md`                    | `CLAUDE.md`                                                  |
| `.github/instructions/*.instructions.md` (`applyTo`) | Verschachtelte `CLAUDE.md` pro Unterordner (Modul 06)        |
| `.github/skills/*/SKILL.md`                          | `.claude/skills/*/SKILL.md` (hier der Ursprung des Konzepts) |
| `.github/prompts/*.prompt.md`                        | `.claude/commands/*.md`                                      |
| `.github/agents/*.agent.md`                          | `.claude/agents/*.md`                                        |
| `.github/chatmodes/*.chatmode.md`                    | Plan Mode (Modul 14, kein separates Datei-Format)            |
| `.vscode/tasks.json` + GitHub Actions                | `hooks` in `.claude/settings.json` (Modul 09)                |
| `.vscode/mcp.json`                                   | `mcpServers` in `.claude/settings.json` (Modul 13)           |
| `gh copilot suggest "..."`                           | `claude --print "..."` (Modul 11)                            |
| VS Code User `settings.json`                         | `~/.claude/settings.json`                                    |
| GitHub Copilot Coding Agent                          | Claude Code Headless/Web-Zugang (Modul 11, 14)               |

---

## Vollständige Dateistruktur am Ende des Kurses

```
.claude/
├── settings.json                    ← Team-Konfiguration (Thema 05)
├── settings.local.json              ← Lokale Berechtigungen & Hooks (Thema 05, 09)
├── skills/
│   ├── feature-builder/SKILL.md
│   ├── api-designer/SKILL.md
│   └── bug-finder/SKILL.md          ← Thema 06
├── commands/
│   ├── todo-review.md               ← /todo-review (Thema 07)
│   └── add-feature.md               ← /add-feature
└── agents/
    ├── security-reviewer.md         ← Sicherheits-Audit (Thema 08)
    └── test-writer.md               ← Test-Generierung

CLAUDE.md                             ← Projektkontext (Thema 03)
review.sh                             ← Headless CI-Skript (Thema 11)

specs/
├── due-dates.md                      ← manuelle Spec (Thema 12)
└── due-dates-spec.md                 ← Spec-Kit-Ausgabe
```
