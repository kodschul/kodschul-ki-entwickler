# Best Practices – Parallele Sessions & Delegation

**Block:** 30 min | **Tag 4**

---

## Worum geht's?

Statt eine Aufgabe nach der anderen abzuarbeiten, lassen sich mehrere Aufgaben **parallel** bearbeiten – entweder von einer Person in mehreren gleichzeitigen Claude-Code-Sessions (z. B. mehrere Terminal-Tabs/Worktrees), oder indem Aufgaben gezielt an andere Personen oder an Claude Code im Web/Headless-Betrieb (Modul 14, 11) delegiert werden.

## Delegation mit Specs

Eine gute Grundlage für Delegation ist eine **Spec** statt einer mündlichen/kurzen Beschreibung (Modul 12):

```
1. Spec/Plan schreiben              → was soll gebaut werden, welche Constraints gelten
2. Spec reviewen                    → mit dem Team oder als Selbst-Check
3. Spec an Person/Session übergeben → klar abgegrenzte Aufgabe, nachvollziehbares Ziel
4. Umsetzung parallel zu anderen Aufgaben
5. Ergebnis gegen die Spec reviewen
```

Eine Spec macht die Aufgabe **selbsterklärend** – die empfangende Person (oder Claude Code) braucht keinen zusätzlichen mündlichen Kontext.

## Parallele Sessions im Alltag

| Szenario                                        | Empfehlung                                                              |
| ----------------------------------------------------- | ------------------------------------------------------------------------------ |
| Mehrere Terminal-Sessions/Worktrees gleichzeitig         | Pro Aufgabe ein eigener Branch/Worktree, um Kontext-Vermischung zu vermeiden      |
| Aufgabe headless/im Web delegieren, selbst weiterarbeiten | Klar formulierter Prompt/Spec, damit Claude Code autonom arbeiten kann (Modul 11, 14) |
| Aufgaben an Teammitglieder delegieren                    | Spec + Akzeptanzkriterien statt "mach mal iwie"                                  |
| Viele kleine parallele Änderungen                        | Kleine, unabhängige Branches/PRs statt einem großen – einfacher zu reviewen       |

## Grenzen

- Delegation funktioniert nur so gut wie die zugrunde liegende Spec – vage Aufgaben führen zu vagen Ergebnissen, egal ob an Mensch oder Agent delegiert
- Zu viele parallele Stränge ohne Review-Kapazität führen zu einem Rückstau statt zu Beschleunigung
- Mehrere parallele Claude-Code-Sessions auf demselben Arbeitsverzeichnis können sich gegenseitig überschreiben – getrennte Worktrees/Branches verwenden
