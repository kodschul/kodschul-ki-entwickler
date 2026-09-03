# 05 – Konfiguration

**Block:** 60 min | **Tag 2**

---

## Überblick: Welche Datei macht was?

| Datei                        | Wo               | Zweck                                          |
| ------------------------------ | ------------------ | ------------------------------------------------- |
| `CLAUDE.md`                     | Projektroot        | Kontext & Regeln für Claude in diesem Projekt (Modul 03) |
| `.claude/settings.local.json`   | Projekt, `.claude/` | Projektspezifische Berechtigungen & Hooks (nicht eingecheckt) |
| `.claude/settings.json`         | Projekt, `.claude/` | Team-weite, eingecheckte Projekt-Konfiguration     |
| `~/.claude/settings.json`       | Home-Verzeichnis   | Globale Konfiguration für alle Projekte            |

**Hierarchie:** Globale Settings (`~/.claude/`) werden von projektweiten (`.claude/settings.json`) überschrieben, diese wiederum von lokalen (`.claude/settings.local.json`).

---

## settings.json – die wichtigsten Felder

```jsonc
{
  "model": "claude-sonnet-4-5",
  "theme": "dark",

  "permissions": {
    "allow": [
      "Bash(python -m pytest *)",
      "Bash(pip install *)",
      "Read",
      "Write"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push *)",
      "Bash(git reset --hard *)",
      "Write(/etc/*)",
      "Write(~/.ssh/*)"
    ]
  },

  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

| Feld                | Bedeutung                                                      |
| --------------------- | ------------------------------------------------------------------ |
| `model`                | Standardmodell für diese Konfigurationsebene                       |
| `permissions.allow`    | Bash-Befehle/Tools, die ohne Rückfrage ausgeführt werden dürfen     |
| `permissions.deny`     | Komplett gesperrte Befehle – **wichtigste Sicherheitsleitplanke**   |
| `mcpServers`           | Angebundene MCP-Server (Modul 13)                                   |

> **Least Privilege:** Lieber gezielt einzelne Befehle erlauben (`Bash(python -m pytest *)`) als pauschal alles (`autoApprove`) – gerade weil Claude Code eigenständig Befehle ausführen kann.

---

## Warum / Wann nicht?

| Warum nutzen                             | Wann nicht                                            |
| ------------------------------------------- | --------------------------------------------------------- |
| Immer gleiche Berechtigungen im Team         | Sehr kleines Experiment/Wegwerf-Skript                    |
| Gefährliche Befehle technisch sperren        | -                                                          |
| Team-weite Defaults über Git teilen          | Persönliche Präferenzen gehören in `settings.local.json`, nicht ins Team-File |

---

## settings.local.json vs. settings.json

`.claude/settings.local.json` ist für **persönliche, nicht geteilte** Einstellungen gedacht (z. B. lokale Testbefehle) – gehört typischerweise in `.gitignore`. `.claude/settings.json` dagegen wird eingecheckt und gilt für das ganze Team.

```
Ich will etwas nur für mich lokal erlauben
  → .claude/settings.local.json (nicht eingecheckt)

Ich will einen Team-Standard für alle setzen
  → .claude/settings.json (eingecheckt)

Ich will etwas für alle meine Projekte konfigurieren
  → ~/.claude/settings.json
```
