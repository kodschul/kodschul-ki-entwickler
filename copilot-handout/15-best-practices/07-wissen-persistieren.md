# Best Practices – Wissen persistieren

**Block:** 20 min | **Tag 4**

---

## Das Problem

Erkenntnisse aus einer Chat-Session (z. B. "diese Lösung hat beim letzten Mal nicht funktioniert", "dieses Pattern ist unser Standard") gehen verloren, sobald die Session endet – außer sie werden aktiv gesichert.

## Wo Wissen persistiert werden kann

| Ort                                        | Für welche Art von Wissen                                                                         |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `.github/copilot-instructions.md`          | Projektweite, dauerhaft gültige Konventionen (Modul 05)                                           |
| `.instructions.md` (mit `applyTo`)         | Konventionen für bestimmte Dateitypen/Bereiche (Modul 06)                                         |
| `SKILL.md`                                 | Wiederverwendbare Fähigkeiten/Workflows inkl. Beispielen (Modul 06)                               |
| `.prompt.md` / `.agent.md`                 | Wiederkehrende Aufgabenstellungen, damit sie nicht jedes Mal neu formuliert werden (Modul 07, 08) |
| ADRs / Projekt-Doku                        | Architektur-Entscheidungen, die über reinen Code-Stil hinausgehen                                 |
| Agentisches "Memory" (persistente Notizen) | Tool-/Umgebungs-Eigenheiten, wiederkehrende Fehlerquellen, Team-Präferenzen                       |

## Faustregel: Wann lohnt sich Persistieren?

```
Ist es wahrscheinlich, dass diese Erkenntnis noch einmal gebraucht wird?
  → Ja, oft/für alle relevant     → Instructions/SKILL.md (repo-weit)
  → Ja, aber nur für mich/dieses Projekt → persönliche/projektbezogene Notizen
  → Nein, einmalige Ausnahme       → nicht persistieren, Chat reicht
```

## Best Practices

- Wissen so nah wie möglich am Ort seiner Anwendung ablegen (z. B. Instructions neben dem betroffenen Code-Bereich, nicht in einer zentralen, unübersichtlichen Datei)
- Regelmäßig aufräumen: veraltete Instructions/Notizen genauso pflegen wie Code (siehe Best Practices – Team-Zusammenarbeit)
- Nicht jede Chat-Antwort ist persistierwürdig – nur wiederkehrende, verallgemeinerbare Erkenntnisse
- Persistiertes Wissen genauso reviewen wie Code, damit falsche/veraltete Annahmen nicht unbemerkt bestehen bleiben
