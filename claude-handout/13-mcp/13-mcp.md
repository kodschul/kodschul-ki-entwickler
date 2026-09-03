# 13 – MCP (Model Context Protocol)

**Block:** 60 min | **Tag 4**

---

## Wie funktioniert das unter der Haube?

```
Claude Code startet
  → liest mcpServers aus settings.json
  → verbindet sich zu jedem Server (stdio oder SSE)
  → Server registriert Tools (z. B. browser_navigate)
  → Claude kann diese Tools wie eigene nutzen
```

> MCP ist ein offenes Protokoll (ursprünglich von Anthropic veröffentlicht, inzwischen von mehreren Anbietern übernommen). Jeder kann einen MCP-Server bauen. Claude sieht MCP-Tools genauso wie eingebaute Tools (`Read`, `Write`, `Bash`).

---

## Warum / Wann nicht?

| Warum nutzen                    | Wann nicht                                        |
| ------------------------------- | ------------------------------------------------- |
| Browser-Automation (Playwright) | Server nicht vertrauenswürdig → Sicherheitsrisiko |
| Externe Datenquellen anbinden   | Latenz kritisch → stdio-Server bevorzugen         |
| Eigene Firma-Tools in Claude    | Nur ein Tool nötig → Bash reicht oft              |
| Parallelisierte Sub-Aufgaben    | MCP-Server nicht stabil → bremst Claude           |

---

## Konfiguration in `settings.json`

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {}
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/pfad/zum/projekt"
      ]
    }
  }
}
```

Nur der angegebene Pfad ist beim `filesystem`-Server zugänglich – Claude kann außerhalb nichts lesen oder schreiben. Bei eigenen Servern immer `${VAR}`-Referenzen statt echter Secrets verwenden:

```json
"custom-server": {
  "command": "python",
  "args": ["mcp_server.py"],
  "env": { "DATABASE_URL": "${DATABASE_URL}" }
}
```

---

## Playwright MCP – Beispiel

```
Öffne die Todo-App unter http://localhost:5000, füge ein Todo mit
dem Titel "MCP Test" hinzu und mach einen Screenshot.
```

Claude nutzt dann automatisch:

- `mcp__playwright__browser_navigate`
- `mcp__playwright__browser_fill_form`
- `mcp__playwright__browser_take_screenshot`

---

## MCP-Status prüfen

```
> /mcp
```

Zeigt verbundene Server und deren verfügbare Tools (Modul 04).

---

## Sicherheitshinweis

MCP-Server laufen als eigenständige Prozesse mit eigenem Zugriff (z. B. auf das Dateisystem oder das Netzwerk). Nur Server aus vertrauenswürdigen Quellen einbinden – ein kompromittierter MCP-Server kann theoretisch alles tun, wozu seine Tools befähigt sind (siehe auch Modul 01 – Recht & Security).
