# Best Practices – Kostenoptimierung mit KI

**Block:** 30 min | **Tag 4**

---

## Warum Kosten aktiv steuern?

Copilot-Nutzung wird meist über **Premium Requests** und/oder Modellwahl abgerechnet. Ohne bewusste Steuerung wachsen die Kosten proportional zur Kontextgröße und zur Anzahl unnötiger Anfragen.

## Kostenhebel

| Hebel                           | Wirkung                                                                                                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Modellwahl passend zur Aufgabe  | Kleinere/günstigere Modelle für einfache Aufgaben (Autocomplete, Standard-Refactoring), teurere Reasoning-Modelle nur für komplexe Planungs-/Debugging-Aufgaben |
| Kontext gezielt einbringen      | `#file`/`#codebase` statt "ganzes Repo" durchsuchen lassen (siehe Modul 10)                                                                                     |
| Kurze, fokussierte Sessions     | Ein Chat pro Aufgabe statt einer endlos wachsenden Session                                                                                                      |
| Caching/Wiederverwendung        | Wiederkehrende Prompts als `.prompt.md` ablegen statt jedes Mal neu zu formulieren (Modul 07)                                                                   |
| Automatisierung nur wo sinnvoll | Nicht jede CI-Prüfung braucht einen KI-Aufruf – klassische Linter/Tests sind oft günstiger und schneller                                                        |

## Im Team/Unternehmen

- **Budgets und Policies** zentral verwalten (Modell-Zugriff, Nutzungsgrenzen pro Team/Rolle)
- **Nutzungsmetriken** regelmäßig auswerten (z. B. über Copilot-Metrics-API/Dashboards), um Ausreißer zu erkennen
- ROI nicht nur an "verbrauchten Requests" messen, sondern an eingesparter Entwicklerzeit – dafür braucht es eine bewusste Erfolgsmessung, nicht nur Kostenkontrolle

## Faustregel

> Je präziser der Prompt und je kleiner der notwendige Kontext, desto günstiger und schneller die Antwort. Kostenoptimierung beginnt also meist schon bei guter Prompt- und Kontext-Hygiene (Modul 03, Modul 10) – nicht erst bei der Modellwahl.
