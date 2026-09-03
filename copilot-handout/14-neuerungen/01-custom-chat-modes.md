# 14a – Custom Chat Modes (`.chatmode.md`)

**Seit wann:** VS Code 1.101 (Mai-Release, veröffentlicht 12. Juni 2025), zunächst als **Preview**.

> Datum wie üblich gegen die aktuellen [VS Code Release Notes](https://code.visualstudio.com/updates) prüfen – Preview-Features werden regelmäßig zu GA weiterentwickelt oder umbenannt.

---

## Was ist neu?

Ergänzt Custom Agents (Modul 08) um einen zweiten Anpassungsmechanismus: ein **Chat-Modus** statt eines aufrufbaren Agenten. Ein Chat-Mode ersetzt den eingebauten Ask/Agent-Modus komplett durch einen eigenen System-Prompt, eine feste Tool-Auswahl und optional ein festes Modell – direkt im Mode-Dropdown auswählbar.

**Datei:** `.github/chatmodes/<name>.chatmode.md`

```yaml
---
description: "Review-Fokus: nur lesen, nie editieren"
tools: ["codebase", "search"]
model: GPT-5
---
Du bist ein reiner Code-Reviewer. Schlage niemals Datei-Änderungen vor,
sondern liste Findings mit Datei:Zeile und Begründung auf.
```

| Aspekt          | Custom Agent (`.agent.md`, Modul 08)             | Custom Chat Mode (`.chatmode.md`)              |
| --------------- | ------------------------------------------------ | ---------------------------------------------- |
| Aufruf          | Wird von Copilot bei Bedarf delegiert            | Manuell im Mode-Dropdown ausgewählt            |
| Geltungsbereich | Läuft als abgekapselter Sub-Prozess              | Ersetzt den aktiven Chat für die Sitzung       |
| Typischer Zweck | Spezialisierte Teilaufgabe (z. B. Security-Scan) | Ganze Session in einer bestimmten Rolle führen |
