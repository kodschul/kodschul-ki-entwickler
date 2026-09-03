# Best Practices – Besser im Team arbeiten mit KI

**Block:** 20 min | **Tag 4**

---

## Das Problem ohne Konventionen

Wenn jede:r im Team Copilot anders konfiguriert (eigene Instructions, eigene Prompts, eigener Stil), entsteht Code, der sich liest, als käme er von unterschiedlichen Personen – und Wissen bleibt in einzelnen Köpfen statt im Repository.

## Prinzipien für Teams

| Prinzip                                              | Umsetzung                                                                                                         |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Konventionen liegen im Repo, nicht im Kopf           | `.github/copilot-instructions.md`, `.instructions.md`, `SKILL.md` einchecken (Modul 05, 06)                       |
| Ein gemeinsames Vokabular für Prompts                | Wiederkehrende Aufgaben als geteilte `.prompt.md`/`.agent.md` ablegen (Modul 07, 08)                              |
| Review-Verantwortung bleibt beim Menschen            | Copilot Code Review ergänzt, ersetzt aber nicht den fachlichen Review (Modul 14)                                  |
| Wissen aus Chats sichern, nicht nur im Kopf behalten | Ergebnisse/Entscheidungen in Doku, ADRs oder Instructions überführen (siehe Best Practices – Wissen persistieren) |
| Onboarding beschleunigen                             | Neue Teammitglieder lesen zuerst die Instructions/Skills statt Copilot "blind" zu nutzen                          |

## Typische Stolperfallen

- Jede:r schreibt eigene, leicht unterschiedliche Instructions → Inkonsistenter Code-Stil trotz KI-Unterstützung
- Copilot-Ergebnisse werden ungeprüft gemerged → Verantwortung verschiebt sich unbemerkt von Mensch zu KI
- Kein Review-Prozess für die Instructions selbst → veraltete/falsche Vorgaben bleiben unbemerkt bestehen

## Empfehlung

> Instructions, Prompts und Agents wie Produktionscode behandeln: Code-Review, Versionierung, klare Owner. Änderungen daran betreffen alle im Team gleichzeitig.
