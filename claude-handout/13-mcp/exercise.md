# Übung: MCP

**Zeit:** ca. 20 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Playwright MCP verbinden (10 min)

Ergänze `.claude/settings.local.json` bzw. `~/.claude/settings.json` um den Playwright-Server:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Prüfe die Verbindung:

```
> /mcp
```

## Aufgabe 2 – Browser-Automation testen (10 min)

Starte die Todo-App lokal, dann:

```
Öffne die Todo-App unter http://localhost:5000, füge ein Todo mit
dem Titel "MCP Test" hinzu und mach einen Screenshot.
```

---

## Zusammenfassung

- [ ] Playwright-MCP-Server verbunden und mit `/mcp` verifiziert
- [ ] Browser-Automation über MCP erfolgreich ausgeführt
