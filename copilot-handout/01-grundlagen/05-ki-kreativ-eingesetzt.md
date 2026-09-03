# 05 – Generative KI kreativ eingesetzt

**Block:** 45 min | **Tag 1**

---

## GitHub Copilot von bestehendem Code lernen lassen

- Copilot liest automatisch offene Dateien, Projektstruktur und `.github/copilot-instructions.md` – kein Training nötig, nur guter Kontext
- Konsistenter bestehender Code = bessere Vorschläge (Copilot spiegelt Stil und Patterns aus der Umgebung)
- Schlecht strukturierter Altcode "vererbt" sich in die Vorschläge – aufräumen lohnt sich doppelt

## Mit Skills die Fähigkeiten der KI erweitern

- **Instructions** (`.instructions.md`, Modul 06) für Regeln
- **Agent Skills** (`SKILL.md`, Modul 14/06) für ganze Fähigkeitspakete inkl. Beispiel-Workflows
- **MCP-Server** (Modul 13) für externe Werkzeuge und Live-Daten

## Verschiedene KI-Modelle verwenden

- Modellauswahl im Chat-Eingabefeld (Model Picker): unterschiedliche Modelle für unterschiedliche Aufgaben (schnell/günstig vs. tiefes Reasoning)
- Für einfache Aufgaben (Umbenennungen, kleine Fixes): schnelle Modelle
- Für Architektur-Entscheidungen, komplexe Refactorings: Reasoning-Modelle mit mehr Bedenkzeit
- Modellwahl beeinflusst auch Token-Verbrauch (siehe Modul 10)

## Blick in die Zukunft: Der KI-gesteuerte Softwareprozess

```
Heute:        Entwickler prompted → Copilot schlägt vor → Entwickler prüft
Im Wandel:    Entwickler beschreibt Ziel → Agent plant + baut → Entwickler reviewt PR
Perspektive:  Issue entsteht → Coding Agent löst autonom → Team reviewt nur noch
```

- Der Trend geht von "KI schlägt vor" zu "KI erledigt, Mensch reviewt" (siehe Copilot Coding Agent, Modul 14)
- Reviewen wird zur Kernkompetenz – nicht mehr nur Schreiben
