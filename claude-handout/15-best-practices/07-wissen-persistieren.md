# Best Practices – Wissen persistieren

**Block:** 20 min | **Tag 4**

---

## Das Problem

Erkenntnisse aus einer Session (z. B. "diese Lösung hat beim letzten Mal nicht funktioniert", "dieses Pattern ist unser Standard") gehen verloren, sobald die Session endet – außer sie werden aktiv gesichert.

## Wo Wissen persistiert werden kann

| Ort                                      | Für welche Art von Wissen                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `CLAUDE.md` (Root)                       | Projektweite, dauerhaft gültige Konventionen (Modul 03/05)                                        |
| `CLAUDE.md` (verschachtelt)              | Konventionen für bestimmte Ordner/Bereiche (Modul 06)                                             |
| `SKILL.md`                               | Wiederverwendbare Fähigkeiten/Workflows inkl. Beispielen (Modul 06)                               |
| `.claude/commands/`, `.claude/agents/`   | Wiederkehrende Aufgabenstellungen, damit sie nicht jedes Mal neu formuliert werden (Modul 07, 08) |
| ADRs / Projekt-Doku                      | Architektur-Entscheidungen, die über reinen Code-Stil hinausgehen                                 |
| Session-Resume (`--resume`/`--continue`) | Fortsetzung einer konkreten, noch offenen Aufgabe (Modul 11)                                      |

## Faustregel: Wann lohnt sich Persistieren?

```
Ist es wahrscheinlich, dass diese Erkenntnis noch einmal gebraucht wird?
  → Ja, oft/für alle relevant     → CLAUDE.md / SKILL.md (repo-weit)
  → Ja, aber nur für mich/dieses Projekt → persönliche/lokale Notizen (settings.local.json-Bereich)
  → Nein, einmalige Ausnahme       → nicht persistieren, Session reicht
```

## Best Practices

- Wissen so nah wie möglich am Ort seiner Anwendung ablegen (z. B. verschachtelte `CLAUDE.md` neben dem betroffenen Code-Bereich, nicht in einer zentralen, unübersichtlichen Datei)
- Regelmäßig aufräumen: veraltete `CLAUDE.md`/Skills genauso pflegen wie Code (siehe Best Practices – Team-Zusammenarbeit)
- Nicht jede Session-Erkenntnis ist persistierwürdig – nur wiederkehrende, verallgemeinerbare Erkenntnisse
- Persistiertes Wissen genauso reviewen wie Code, damit falsche/veraltete Annahmen nicht unbemerkt bestehen bleiben
