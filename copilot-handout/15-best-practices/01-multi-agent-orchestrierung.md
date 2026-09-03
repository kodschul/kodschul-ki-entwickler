# Best Practices – Multi-Agent-Orchestrierung

**Block:** 30 min | **Tag 4**

---

## Worum geht's?

Statt eine einzelne, lange Chat-Session immer weiter zu befüllen, werden Aufgaben gezielt an mehrere spezialisierte Agenten verteilt – jeder mit eigenem Kontext, eigenem Tool-Set und einer klar abgegrenzten Verantwortung. Das Konzept selbst wurde in Modul 14 (Subagents) eingeführt; hier geht es um die **praktische Anwendung im Alltag**.

## Typisches Muster

```
Hauptagent (Orchestrator)
  ├── Recherche-Agent      → durchsucht Codebase, fasst Ergebnis zusammen
  ├── Implementierungs-Agent → schreibt Code basierend auf Recherche
  └── Test-/Review-Agent    → prüft das Ergebnis, meldet Findings
```

Der Orchestrator sieht nur die **Endergebnisse** der Subagenten, nicht deren kompletten Arbeitsweg – das hält den eigenen Kontext klein (siehe Modul 10 – Token-Management).

## Best Practices

| Empfehlung                                                                 | Warum                                                                   |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Aufgaben klar abgrenzen, bevor delegiert wird                              | Vage Aufgaben führen zu vagen, schwer verwertbaren Ergebnissen          |
| Read-only-Agenten für Recherche/Analyse nutzen                             | Verhindert versehentliche Änderungen durch einen "nur lesenden" Schritt |
| Ergebnisse von Subagenten immer gegenlesen                                 | Subagenten können sich gegenseitig widersprechende Annahmen treffen     |
| Nicht mehr Subagenten parallel starten, als man reviewen kann              | Parallelität hilft nur, wenn die Ergebnisse auch geprüft werden         |
| Orchestrator-Prompt explizit sagen lassen, was NICHT delegiert werden soll | Verhindert unnötige Verzweigung bei trivialen Aufgaben                  |

## Wann lohnt sich Multi-Agent-Orchestrierung?

- Große, klar in Teilaufgaben zerlegbare Features
- Recherche-lastige Aufgaben (z. B. "wo im Code wird X verwendet?"), die den Hauptkontext sonst aufblähen würden
- Nicht sinnvoll bei kleinen, einfachen Änderungen – der Overhead durch Koordination übersteigt dann den Nutzen
