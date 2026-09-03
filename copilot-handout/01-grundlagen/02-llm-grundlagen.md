# 02 – Generative KI und LLMs in a Nutshell

**Block:** 45 min | **Tag 1**

---

## Was kann generative KI – und was wird sie nie können?

**Kann gut:**

- Muster aus großen Mengen an Trainingsdaten reproduzieren und kombinieren (Boilerplate, bekannte Algorithmen, Standard-Patterns)
- Sprache verstehen und in Code übersetzen (und umgekehrt: Code erklären)
- Variationen und Alternativen zu bestehendem Code vorschlagen

**Wird strukturell nie können (mit aktueller Architektur):**

- Objektives Verständnis / Bewusstsein über die eigene Ausgabe haben – es gibt kein "Wissen", nur Wahrscheinlichkeiten
- Garantiert korrekten Code liefern (kein Beweis, keine Ausführung im Kopf)
- Verantwortung für Entscheidungen übernehmen – das bleibt beim Menschen

---

## Wie funktionieren LLMs?

```
Text → Tokenisierung → Vektoren → Transformer-Schichten → Wahrscheinlichkeitsverteilung → nächstes Token
```

- **Tokens**: Wörter/Wortteile, keine ganzen Sätze – ein Token ≈ 4 Zeichen (Englisch), oft weniger effizient bei Deutsch
- **Context Window**: begrenzter Speicher pro Anfrage (z. B. 128k–1M Tokens je nach Modell) – alles, was Copilot "sieht", muss hineinpassen
- **Kein Gedächtnis zwischen Sessions** (außer explizit gespeichert, z. B. Custom Instructions oder Chat-Verlauf)

## Wie bekomme ich meine Dateien "hinein"?

| Mechanismus           | Wie                                               |
| --------------------- | ------------------------------------------------- |
| Automatischer Kontext | Aktive Datei, offene Tabs                         |
| Manuell               | `#file`, `#folder`, Drag & Drop                   |
| Semantische Suche     | `#codebase` – Embeddings statt Volltextsuche      |
| Persistent            | `.instructions.md` – wird immer/bei Match geladen |
| Extern                | MCP-Server (Modul 13) – Live-Daten von außen      |

---

## Wie kann KI in der Softwareentwicklung helfen?

- Wiederkehrende Aufgaben beschleunigen (CRUD, Tests, Doku)
- Als "Rubber Duck" zum Denken und Erklären nutzen
- Refactoring-Vorschläge und Alternativen liefern
- Onboarding in unbekannten Codebases erleichtern (Codebase-Fragen beantworten)

## Überblick: KI-Assistenten für Softwareentwicklung

| Kategorie                         | Beispiele                            |
| --------------------------------- | ------------------------------------ |
| IDE-integriert                    | GitHub Copilot, Cursor, JetBrains AI |
| Terminal-first                    | Claude Code, Copilot CLI, Aider      |
| Cloud/autonom                     | GitHub Copilot Coding Agent          |
| Allzweck-Chat (kein Repo-Zugriff) | ChatGPT, Claude.ai, Gemini           |
