# 03 – Generative KI im Coding

**Block:** 45 min | **Tag 1**

---

## Code mit KI-Assistenten planen, schreiben und dokumentieren

```
Planen (kurzer Prompt/Plan-Skizze)  →  Schreiben (Claude Code Agent-Loop)  →  Dokumentieren (Prompt/Custom Command)
```

- **Planen:** Vor dem ersten Prompt kurz die Aufgabe in 2–3 Sätzen beschreiben lassen, oder direkt mit Spec-Driven Development arbeiten (Modul 12) – verhindert, dass Claude in die falsche Richtung baut.
- **Schreiben:** Kleine, überprüfbare Schritte statt "baue die ganze App" – Claude Code arbeitet in einer Tool-Loop (lesen → ändern → testen → nächster Schritt), je kleiner der Schritt, desto zuverlässiger.
- **Dokumentieren:** Per Prompt oder eigenem Custom Command (Modul 07) für Docstrings/README, aber: KI-generierte Doku immer gegenlesen, sie beschreibt oft nur _was_ der Code tut, nicht _warum_.

---

## Generative KI zur Codeanalyse verwenden

- Unbekannten Code erklären lassen ("Erkläre mir, wie `app.py` funktioniert")
- Architektur-Fragen stellen ("Wo wird X validiert?") – Claude durchsucht die Codebase selbst mit `Grep`/`Glob`
- Sicherheits- und Qualitätsprobleme aufspüren lassen (z. B. über einen `security-reviewer`-Agent, Modul 08)

> Wichtig: KI-Analyse ersetzt keine echten Tools (Linter, SAST-Scanner) – sie ergänzt sie, mit dem Vorteil natürlicher Sprache.

## Refactoring mit KI-Unterstützung

- Konkrete Stelle benennen → "Extrahiere diese Logik in eine eigene Funktion"
- Große Refactorings in Teilschritte zerlegen (Datei für Datei), sonst verliert das Modell den Überblick
- Nach jedem Schritt Tests laufen lassen – idealerweise automatisch per Hook (Modul 09), Refactoring ohne Testnetz ist ein Risiko, KI hin oder her

## Software-Testing mit KI

- Testfälle generieren lassen (z. B. über einen `test-writer`-Agent, Modul 08), aber Edge Cases selbst ergänzen
- KI eignet sich gut für Testdaten-Generierung (Fixtures, Mocks)
- Coverage-Lücken durch KI identifizieren lassen ("Welche Zweige in dieser Funktion sind ungetestet?")

---

## Faustregel für dieses Modul

Je kleiner der Auftrag, desto zuverlässiger das Ergebnis. Plane groß, promptet klein.
