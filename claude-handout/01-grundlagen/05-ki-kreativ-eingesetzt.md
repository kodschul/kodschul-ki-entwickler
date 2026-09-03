# 05 – Generative KI kreativ eingesetzt

**Block:** 45 min | **Tag 1**

---

## Claude Code von bestehendem Code lernen lassen

- Claude liest Dateien, Projektstruktur und `CLAUDE.md` selbst über seine Tools – kein Training nötig, nur guter Kontext
- Konsistenter bestehender Code = bessere Vorschläge (Claude spiegelt Stil und Patterns aus der Umgebung)
- Schlecht strukturierter Altcode "vererbt" sich in die Vorschläge – aufräumen lohnt sich doppelt

## Mit Skills die Fähigkeiten der KI erweitern

- **`CLAUDE.md`** (Modul 05/06) für projektweite Regeln
- **Agent Skills** (`SKILL.md`, Modul 06) für ganze Fähigkeitspakete inkl. Beispiel-Workflows – dieses Konzept stammt ursprünglich aus Claude Code
- **MCP-Server** (Modul 13) für externe Werkzeuge und Live-Daten

## Verschiedene KI-Modelle verwenden

- Modellauswahl über `settings.json` (`model`) oder Slash-Command (z. B. `/model`): unterschiedliche Modelle für unterschiedliche Aufgaben (schnell/günstig vs. tiefes Reasoning)
- Für einfache Aufgaben (Umbenennungen, kleine Fixes): schnellere/günstigere Modelle (z. B. Haiku)
- Für Architektur-Entscheidungen, komplexe Refactorings: leistungsfähigere Modelle mit mehr Reasoning (z. B. Opus)
- Modellwahl beeinflusst auch Token-Verbrauch/Kosten (siehe Modul 10 und Modul 15 – Best Practices)

## Blick in die Zukunft: Der KI-gesteuerte Softwareprozess

```
Heute:        Entwickler prompted → Claude schlägt vor/handelt → Entwickler prüft
Im Wandel:    Entwickler beschreibt Ziel → Agent plant + baut (Spec-Kit) → Entwickler reviewt
Perspektive:  Aufgabe wird delegiert → Agent/Subagent löst autonom → Team reviewt nur noch
```

- Der Trend geht von "KI schlägt vor" zu "KI erledigt, Mensch reviewt" (siehe Modul 14 – Neuerungen)
- Reviewen wird zur Kernkompetenz – nicht mehr nur Schreiben
