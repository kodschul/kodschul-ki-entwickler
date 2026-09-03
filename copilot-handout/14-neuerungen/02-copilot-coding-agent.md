# 14b – GitHub Copilot Coding Agent

**Seit wann:** Public Preview seit Mai 2025 (angekündigt auf Microsoft Build 2025 / im selben VS-Code-1.101-Release integriert), seither schrittweise ausgebaut (u. a. Zuweisung direkt aus der GitHub-Pull-Requests-Erweiterung in VS Code).

> Datum gegen den [GitHub Changelog](https://github.blog/changelog/) prüfen – der Funktionsumfang wird laufend erweitert.

---

## Was ist neu?

Die cloud-seitige, vollautonome Variante von Copilot: Ein GitHub Issue wird dem Coding Agent zugewiesen, der eigenständig einen Branch erstellt, Code schreibt, testet und einen Pull Request eröffnet – ganz ohne offene IDE. Reviewt wird wie bei jedem anderen PR.

```
Issue wird dem Coding Agent zugewiesen
  → Agent erstellt Branch, arbeitet in einer Sandbox-Umgebung
  → committet schrittweise, kommentiert Fortschritt im PR
  → eröffnet Pull Request, sobald fertig
  → Team reviewt wie einen menschlichen Beitrag
```

**Einrichtung:** Issue oder PR über "Assign to Copilot" zuweisen (GitHub.com oder direkt aus der GitHub-Pull-Requests-Erweiterung in VS Code).

**Abgrenzung zum lokalen Agent-Modus (Modul 08):**

| Lokaler Agent-Modus                  | Coding Agent (cloud)                         |
| ------------------------------------ | -------------------------------------------- |
| Läuft in der geöffneten IDE-Session  | Läuft unabhängig, auch bei geschlossener IDE |
| Sofortiges Feedback im Editor        | Ergebnis erscheint als fertiger PR           |
| Für iteratives, begleitetes Arbeiten | Für klar abgegrenzte, delegierbare Aufgaben  |
