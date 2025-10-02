# Aufgaben – Lab 5.1 Copilot erweitern & anpassen

1. **Eigener Copilot‑Endpoint (C#):** Implementiere eine Minimal‑API in C# (Program.cs), die einen `/info`‑Endpunkt mit Name und Beschreibung deines eigenen Agenten bereitstellt.  Der Root‑Endpunkt `/` soll eine JSON‑Anfrage mit einem Feld `question` annehmen und die Frage in die Antwort einbetten (z. B. `"answer": "Du hast gefragt: ..."`).  Teste die API mit `curl`.

2. **Express‑Agent (TypeScript):** Setze einen Node‑Agenten mit Express um, der dieselben Funktionen bietet wie oben (Info‑Endpoint und Root‑Endpoint).  Die Anfrage soll als JSON verarbeitet werden.  Starte den Server auf Port 3000 und prüfe ihn mit `curl`.

3. **GitHub‑Info abrufen (C#):** Erweitere die Minimal‑API so, dass sie den Namen und die offene Issue‑Anzahl eines GitHub‑Repositories zurückgibt.  Verwende die Bibliothek `Octokit` und lies den Repository‑Owner und -Namen aus der JSON‑Anfrage aus.  Gib eine Antwort wie `"dotnet/runtime hat 1000 offene Issues"` zurück.
