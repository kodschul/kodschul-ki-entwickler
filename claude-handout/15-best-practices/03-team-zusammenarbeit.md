# Best Practices – Besser im Team arbeiten mit KI

**Block:** 20 min | **Tag 4**

---

## Das Problem ohne Konventionen

Wenn jede:r im Team Claude Code anders konfiguriert (eigene `CLAUDE.md`, eigene Commands, eigener Stil), entsteht Code, der sich liest, als käme er von unterschiedlichen Personen – und Wissen bleibt in einzelnen Köpfen statt im Repository.

## Prinzipien für Teams

| Prinzip                                    | Umsetzung                                                                     |
| ---------------------------------------------- | ---------------------------------------------------------------------------------- |
| Konventionen liegen im Repo, nicht im Kopf       | `CLAUDE.md`, `.claude/skills/`, `.claude/settings.json` einchecken (Modul 03, 05, 06) |
| Ein gemeinsames Vokabular für Commands/Agents    | Wiederkehrende Aufgaben als geteilte `.claude/commands/`/`.claude/agents/` ablegen (Modul 07, 08) |
| Review-Verantwortung bleibt beim Menschen         | Agenten/Automation ergänzen, ersetzen aber nicht den fachlichen Review              |
| Wissen aus Sessions sichern, nicht nur im Kopf behalten | Ergebnisse/Entscheidungen in `CLAUDE.md`, Skills oder Doku überführen (siehe Best Practices – Wissen persistieren) |
| Onboarding beschleunigen                          | Neue Teammitglieder starten mit `/init` bzw. lesen zuerst die bestehende `CLAUDE.md` |

## Typische Stolperfallen

- Jede:r schreibt eigene, leicht unterschiedliche `CLAUDE.md`-Dateien → inkonsistenter Code-Stil trotz KI-Unterstützung
- Claude-Ergebnisse werden ungeprüft gemerged → Verantwortung verschiebt sich unbemerkt von Mensch zu KI
- Kein Review-Prozess für `CLAUDE.md`/Skills/Agents selbst → veraltete/falsche Vorgaben bleiben unbemerkt bestehen
- `settings.local.json` (persönlich) und `settings.json` (Team) werden verwechselt → persönliche Ausnahmen landen versehentlich im Team-Standard

## Empfehlung

> `CLAUDE.md`, Commands, Agents und Skills wie Produktionscode behandeln: Code-Review, Versionierung, klare Owner. Änderungen daran betreffen alle im Team gleichzeitig.
