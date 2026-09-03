# Best Practices – Parallele Sessions & Delegation

**Block:** 30 min | **Tag 4**

---

## Worum geht's?

Statt eine Aufgabe nach der anderen abzuarbeiten, lassen sich mehrere Aufgaben **parallel** bearbeiten – entweder von einer Person in mehreren gleichzeitigen Sessions, oder indem Aufgaben gezielt an andere Personen (oder an den Coding Agent, Modul 14) delegiert werden.

## Delegation mit Specs

Eine gute Grundlage für Delegation ist ein **Spec** statt einer mündlichen/kurzen Beschreibung (siehe Modul 12 – Spec-Driven Development):

```
1. Spec schreiben (Plan)        → was soll gebaut werden, welche Constraints gelten
2. Spec reviewen                → mit dem Team oder als Selbst-Check
3. Spec an Person/Agent übergeben → klar abgegrenzte Aufgabe, nachvollziehbares Ziel
4. Umsetzung parallel zu anderen Aufgaben
5. Ergebnis gegen die Spec reviewen
```

Eine Spec macht die Aufgabe **selbsterklärend** – die empfangende Person (oder der Coding Agent) braucht keinen zusätzlichen mündlichen Kontext.

## Parallele Sessions im Alltag

| Szenario                                                  | Empfehlung                                                                                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Mehrere IDE-Fenster/Worktrees gleichzeitig                | Pro Aufgabe ein eigener Branch/Worktree, um Kontext-Vermischung zu vermeiden              |
| Aufgabe an Coding Agent delegieren, selbst weiterarbeiten | Klar formulierter Issue/Spec, damit der Agent autonom arbeiten kann (Modul 14)            |
| Aufgaben an Teammitglieder delegieren                     | Spec + Akzeptanzkriterien statt "mach mal iwie"                                           |
| Viele kleine parallele Änderungen                         | Kleine, unabhängige PRs statt einem großen – einfacher zu reviewen und zu parallelisieren |

## Grenzen

- Delegation funktioniert nur so gut wie die zugrunde liegende Spec – vage Aufgaben führen zu vagen Ergebnissen, egal ob an Mensch oder Agent delegiert
- Zu viele parallele Stränge ohne Review-Kapazität führen zu einem Rückstau statt zu Beschleunigung
