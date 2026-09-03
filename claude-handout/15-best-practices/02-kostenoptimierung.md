# Best Practices – Kostenoptimierung mit KI

**Block:** 30 min | **Tag 4**

---

## Warum Kosten aktiv steuern?

Claude Code wird über API-Nutzung (Tokens) bzw. den jeweiligen Abo-/Nutzungsplan abgerechnet. Ohne bewusste Steuerung wachsen die Kosten proportional zur Kontextgröße und zur Anzahl unnötiger Anfragen.

## Kostenhebel

| Hebel                          | Wirkung                                                                |
| --------------------------------- | --------------------------------------------------------------------------- |
| Modellwahl passend zur Aufgabe      | Schnellere/günstigere Modelle für einfache Aufgaben, leistungsfähigere nur für komplexe Planung/Debugging (Modul 05) |
| Kontext gezielt einbringen          | Gezielt nach Dateien/Funktionen fragen statt "durchsuche alles" (Modul 10)   |
| Kurze, fokussierte Sessions         | `/clear` bei Themenwechsel statt einer endlos wachsenden Session (Modul 04, 10) |
| Wiederverwendung                    | Wiederkehrende Prompts als Custom Command ablegen statt jedes Mal neu zu formulieren (Modul 07) |
| `/cost` regelmäßig prüfen           | Sofortiges Feedback zum Tokenverbrauch der aktuellen Session (Modul 04)       |
| Automatisierung nur wo sinnvoll     | Nicht jede CI-Prüfung braucht einen Claude-Aufruf – klassische Linter/Tests sind oft günstiger und schneller |

## Im Team/Unternehmen

- **Budgets und Policies** zentral verwalten (Modell-Zugriff, Nutzungsgrenzen pro Team/Rolle)
- **Nutzungsmetriken** regelmäßig auswerten, um Ausreißer zu erkennen
- ROI nicht nur an "verbrauchten Tokens" messen, sondern an eingesparter Entwicklerzeit

## Faustregel

> Je präziser der Prompt und je kleiner der notwendige Kontext, desto günstiger und schneller die Antwort. Kostenoptimierung beginnt also meist schon bei guter Prompt- und Kontext-Hygiene (Modul 03, Modul 10) – nicht erst bei der Modellwahl.
