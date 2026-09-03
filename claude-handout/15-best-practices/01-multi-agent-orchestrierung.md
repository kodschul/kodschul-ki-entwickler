# Best Practices – Multi-Agent-Orchestrierung

**Block:** 30 min | **Tag 4**

---

## Worum geht's?

Statt eine einzelne, lange Session immer weiter zu befüllen, werden Aufgaben gezielt an mehrere spezialisierte Subagenten (Modul 08) verteilt – jeder mit eigenem Kontext, eigenem Tool-Set und einer klar abgegrenzten Verantwortung.

## Typisches Muster

```
Hauptsession (Orchestrator)
  ├── Recherche-Agent (nur Read)     → durchsucht Codebase, fasst Ergebnis zusammen
  ├── Implementierungs-Agent         → schreibt Code basierend auf Recherche
  └── Test-/Review-Agent (Read)      → prüft das Ergebnis, meldet Findings
```

Die Hauptsession sieht nur die **Endergebnisse** der Subagenten, nicht deren kompletten Arbeitsweg – das hält den eigenen Kontext klein (Modul 10).

## Best Practices

| Empfehlung                                              | Warum                                                             |
| ----------------------------------------------------------- | --------------------------------------------------------------------- |
| Aufgaben klar abgrenzen, bevor an einen Agent delegiert wird   | Vage Aufgaben führen zu vagen, schwer verwertbaren Ergebnissen          |
| Read-only-Agenten für Recherche/Analyse nutzen (`tools: [Read]`) | Verhindert versehentliche Änderungen durch einen "nur lesenden" Schritt |
| Ergebnisse von Agenten immer gegenlesen                        | Agenten können sich gegenseitig widersprechende Annahmen treffen        |
| Nicht mehr Agenten parallel starten, als man reviewen kann      | Parallelität hilft nur, wenn die Ergebnisse auch geprüft werden          |
| In `CLAUDE.md`/Agent-Definition explizit sagen, was NICHT delegiert werden soll | Verhindert unnötige Verzweigung bei trivialen Aufgaben |

## Wann lohnt sich Multi-Agent-Orchestrierung?

- Große, klar in Teilaufgaben zerlegbare Features
- Recherche-lastige Aufgaben (z. B. "wo im Code wird X verwendet?"), die den Hauptkontext sonst aufblähen würden
- Nicht sinnvoll bei kleinen, einfachen Änderungen – der Koordinationsaufwand übersteigt dann den Nutzen
