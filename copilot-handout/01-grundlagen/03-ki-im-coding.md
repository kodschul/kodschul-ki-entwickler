# 03 – Generative KI im Coding

**Block:** 45 min | **Tag 1**

---

## Code mit KI-Assistenten planen, schreiben und dokumentieren

```
Planen (Chat, Ask-Modus)  →  Schreiben (Agent-Modus / Inline)  →  Dokumentieren (/doc, Kommentare)
```

- **Planen:** Vor dem ersten Prompt kurz die Aufgabe in 2–3 Sätzen beschreiben lassen (Plan-Mode / Ask-Modus) – verhindert, dass die KI in die falsche Richtung baut.
- **Schreiben:** Kleine, überprüfbare Schritte statt "baue die ganze App" – gilt für Inline Completions genauso wie für den Agent-Modus.
- **Dokumentieren:** `/doc` (Modul 04) für Docstrings/JSDoc, aber: KI-generierte Doku immer gegenlesen, sie beschreibt oft nur _was_ der Code tut, nicht _warum_.

---

## Generative KI zur Codeanalyse verwenden

- Unbekannten Code erklären lassen (`/explain`, Modul 04)
- Architektur-Fragen an `#codebase` stellen ("Wo wird X validiert?")
- Sicherheits- und Qualitätsprobleme aufspüren lassen (Prompt: "Finde Code-Smells in dieser Datei")

> Wichtig: KI-Analyse ersetzt keine echten Tools (Linter, SAST-Scanner) – sie ergänzt sie, mit dem Vorteil natürlicher Sprache.

## Refactoring mit KI-Unterstützung

- Selektion markieren → Chat: "Extrahiere diese Logik in eine eigene Funktion"
- Große Refactorings in Teilschritte zerlegen (Datei für Datei), sonst verliert das Modell den Überblick
- Nach jedem Schritt Tests laufen lassen – Refactoring ohne Testnetz ist ein Risiko, KI hin oder her

## Software-Testing mit KI

- Testfälle generieren lassen (`/tests`, Modul 04), aber Edge Cases selbst ergänzen
- KI eignet sich gut für Testdaten-Generierung (Fixtures, Mocks)
- Coverage-Lücken durch KI identifizieren lassen ("Welche Zweige in dieser Funktion sind ungetestet?")

---

## Faustregel für dieses Modul

Je kleiner der Auftrag, desto zuverlässiger das Ergebnis. Plane groß, promptet klein.
