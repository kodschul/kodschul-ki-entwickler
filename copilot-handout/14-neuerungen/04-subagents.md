# 14d – Subagents / Multi-Agent-Orchestrierung

**Seit wann:** Kein einzelnes GA-Datum – anders als die anderen drei Themen in diesem Modul ist "Subagents" (noch) kein einzelnes, offiziell benanntes GitHub-Copilot-Feature mit festem Launch-Datum, sondern ein **Architekturmuster**, das sich seit Mitte/Ende 2025 zunehmend in agentischen Coding-Tools durchsetzt (u. a. sichtbar in Erweiterungen rund um Copilot Chat sowie in vergleichbaren Tools wie Claude Code).

> Vor dem Unterrichten prüfen, ob es inzwischen ein offizielles, benanntes Copilot-Feature dazu gibt (z. B. im [GitHub Changelog](https://github.blog/changelog/?label=copilot)) – dieser Abschnitt beschreibt das Konzept, nicht ein einzelnes fixes Produkt-Feature.

---

## Was ist das Konzept?

Copilot kann Teilaufgaben an spezialisierte Subagenten delegieren (z. B. einen reinen Recherche-Agenten), die eigenständig arbeiten und nur ein Endergebnis zurückmelden.

```
Hauptagent erhält komplexe Aufgabe
  → zerlegt sie in Teilaufgaben
  → delegiert Teilaufgabe an Subagent (eigener Kontext, eigenes Tool-Set)
  → Subagent arbeitet isoliert, meldet nur das Ergebnis zurück
  → Hauptagent führt Ergebnisse zusammen
```

**Nutzen:** Große, mehrteilige Aufgaben parallelisieren, ohne den Hauptkontext zu überladen (siehe Modul 10 – Token-Management). Recherche/Exploration lässt sich so isoliert vom eigentlichen Bearbeitungs-Kontext halten.
