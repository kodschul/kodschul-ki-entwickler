# 02 – Generative KI und LLMs in a Nutshell

**Block:** 45 min | **Tag 1**

---

## Was kann generative KI – und was wird sie nie können?

**Kann gut:**

- Muster aus großen Mengen an Trainingsdaten reproduzieren und kombinieren (Boilerplate, bekannte Algorithmen, Standard-Patterns)
- Sprache verstehen und in Code übersetzen (und umgekehrt: Code erklären)
- Variationen und Alternativen zu bestehendem Code vorschlagen, mehrstufig planen und Tools orchestrieren

**Wird strukturell nie können (mit aktueller Architektur):**

- Objektives Verständnis / Bewusstsein über die eigene Ausgabe haben – es gibt kein "Wissen", nur Wahrscheinlichkeiten
- Garantiert korrekten Code liefern (kein Beweis, keine Ausführung im Kopf – auch wenn Claude Code Tests selbst ausführen kann)
- Verantwortung für Entscheidungen übernehmen – das bleibt beim Menschen

---

## Wie funktionieren LLMs?

```
Text → Tokenisierung → Vektoren → Transformer-Schichten → Wahrscheinlichkeitsverteilung → nächstes Token
```

- **Tokens**: Wörter/Wortteile, keine ganzen Sätze – ein Token ≈ 4 Zeichen (Englisch), oft weniger effizient bei Deutsch
- **Context Window**: begrenzter Speicher pro Anfrage – alles, was Claude "sieht" (Dateien, `CLAUDE.md`, Tool-Ausgaben), muss hineinpassen
- **Kein Gedächtnis zwischen Sessions**, außer explizit gespeichert (`CLAUDE.md`, persistierte Notizen, Session-Resume)

## Wie bekomme ich meine Dateien "hinein"?

| Mechanismus           | Wie                                                       |
| ---------------------- | ---------------------------------------------------------- |
| Automatischer Kontext   | `CLAUDE.md` wird bei jedem Start automatisch gelesen       |
| Manuell                 | Datei-/Pfadangabe im Prompt, `@datei` in manchen Clients   |
| Tool-basiert            | Claude nutzt `Read`/`Glob`/`Grep`, um sich Kontext selbst zu holen |
| Persistent              | `CLAUDE.md`, `SKILL.md` – wird immer/bei Bedarf geladen    |
| Extern                  | MCP-Server (Modul 13) – Live-Daten von außen               |

---

## Wie kann KI in der Softwareentwicklung helfen?

- Wiederkehrende Aufgaben beschleunigen (CRUD, Tests, Doku)
- Als "Rubber Duck" zum Denken und Erklären nutzen
- Refactoring-Vorschläge und Alternativen liefern
- Onboarding in unbekannten Codebases erleichtern (Claude durchsucht die Codebase selbst über Tools)

## Überblick: KI-Assistenten für Softwareentwicklung

| Kategorie                         | Beispiele                              |
| ---------------------------------- | ---------------------------------------- |
| Terminal-first / agentisch          | **Claude Code**, Copilot CLI, Aider     |
| IDE-integriert                      | GitHub Copilot, Cursor, JetBrains AI     |
| Cloud/autonom                       | GitHub Copilot Coding Agent, Claude Agent SDK in CI |
| Allzweck-Chat (kein Repo-Zugriff)   | ChatGPT, Claude.ai, Gemini               |
