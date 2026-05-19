# Kursübersicht — Tag 3

---

## Tag 1 & 2 — Grundlagen → Copilot Deep Dive

**KI & Prompting**
- Was ist KI — Einsatzgebiete in der Softwareentwicklung, Datenschutz, rechtliche Anforderungen
- KI-Anbieter im Vergleich: ChatGPT, Claude, Copilot, Gemini, Le Chat, Perplexity, Phind, Codeium
- Schwerpunkte der Anbieter: Coding vs. Text vs. Bild
- Prompt Engineering: Strukturen, Techniken, Best Practices, Beispiele & Übungen
- AI-Agenten & Multi-Step-Prompting — Konzept, Unterschied zu einfachem Chat

**Inline Completions**
- Ghosttext, Tab-Akzeptanz, Partial Completions
- Mehrere Vorschläge anzeigen, navigieren, ablehnen
- Wann Copilot etwas vorschlägt — und wann nicht

**Chat & Kontext**
- Kontext-Variablen: `#file`, `#selection`, `#codebase`, `@workspace`
- Integrierte Commands: `/explain`, `/fix`, `/tests`, `/doc`
- Token-Management — was Copilot sieht, was nicht, wie Kontext sparen

**Konfiguration**
- VS Code Settings, Trust, Modellauswahl
- `copilot-instructions.md` — globale Projektregeln, immer geladen
- `*.instructions.md` mit `applyTo` — scoped auf Dateityp/Ordner

**Skills & Custom Agents**
- `*.prompt.md` — wiederverwendbare Prompts, Aufruf per `/name`
- `*.agent.md` — eigener System-Prompt, Tool-Whitelist, autonomer Ablauf
- Multi-Agent — Agents die andere Agents aufrufen

**Spec-Driven Development**
- Spec schreiben → Copilot generiert Code + Tests daraus
- Anforderung als Quelle der Wahrheit — nicht Kommentare im Code

**Copilot CLI**
- `gh copilot suggest` — Terminal-Befehle per KI
- `gh copilot explain` — unbekannte Commands erklären lassen

> Ohne Instructions → generischer Code | Mit Instructions → **dein** Code

---

## Tag 3 — was wir heute bauen

**Hotel Reservierungssystem** — vollständiger .NET Stack, AI-driven von Anfang bis Ende

| Zeit | Block | Was entsteht |
|---|---|---|
| 09:00–10:30 | m05 + m06 | Domänenmodell → C# Entitäten + EF Core Config |
| 10:45–12:15 | m07 + m08 | Migration → DB → Geschäftslogik in C# |
| 13:00–15:00 | m09 + m10 | xUnit Tests → ASP.NET Controller + DTOs |
| 15:15–16:30 | MCP + Transfer | Copilot spricht direkt mit DB & GitHub |

---

---

## Was du heute mitnimmst

- Anforderungstext → vollständiges Domänenmodell → **1 Prompt**
- Domänenmodell → alle C# Klassen → **1 Agent**
- Migration generieren + reviewen → **1 Skill**
- Geschäftsregeln aus Fließtext → direkt C# → **1 Agent**
- Produktionscode → vollständige xUnit Testsuite → **1 Prompt**
- Application Service → Controller + DTOs + Swagger → **1 Agent**
- MCP: Copilot stellt DB-Queries, liest Issues, keine Copy-Paste mehr

---

## Projektstruktur

```
HotelReservierung/
├── Domain/                  ← m05 + m06
├── Infrastructure/Migrations/  ← m07
├── Application/             ← m08
├── Api/Controllers/ + DTOs/ ← m10
├── HotelReservierung.Tests/ ← m09
└── .github/
    ├── instructions/        ← Konventionen pro Schicht
    ├── prompts/             ← Skills: /domain-model /generate-entity ...
    └── agents/              ← Workflows: ddd-analyst, test-generator ...
```

→ Alle fertigen Dateien: `agentic-lab.md` in jedem Modul

---

## Projektstruktur heute

```
HotelReservierung/
├── Domain/                  ← Entitäten, Value Objects, Domain Events   (m05+m06)
├── Infrastructure/
│   ├── Configurations/      ← EF Core Konfigurationen                   (m06)
│   └── Migrations/          ← Datenbankmigrationen                      (m07)
├── Application/             ← Application Services, Geschäftslogik      (m08)
├── Api/
│   ├── Controllers/         ← REST API Endpunkte                        (m10)
│   └── DTOs/                ← Request/Response Records                  (m10)
├── HotelReservierung.Tests/ ← xUnit Tests                               (m09)
└── .github/
    ├── copilot-instructions.md
    ├── instructions/        ← Scoped Instructions pro Schicht
    ├── prompts/             ← Wiederverwendbare Prompt-Dateien
    └── agents/              ← Custom Agents für Workflows
```

---

## Handout-Struktur

Jedes Modul (m05–m10) enthält vier Dateien:

| Datei | Inhalt |
|---|---|
| `theorie.md` | Konzepte, Patterns, Referenz |
| `uebungen.md` | Weiterführende Aufgaben |
| `lab.md` | Demo-Prompt + Deine Aufgabe + Musterlösung |
| `agentic-lab.md` | Fertige Instructions, Skills & Agents zum Kopieren |
