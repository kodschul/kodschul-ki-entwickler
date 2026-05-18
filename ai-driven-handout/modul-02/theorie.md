# Modul 2 — KI-Anbieter und Werkzeuge gezielt auswählen

---

## Lab 2.1 — Den Markt relevanter KI-Anbieter überblicken

### Marktüberblick (Stand 2025)

**General-Purpose-Chatbots mit Coding-Fähigkeiten**
| Anbieter | Modell | Besonderheit |
|---|---|---|
| OpenAI | GPT-4o, o3, o4-mini | Größte Nutzerbasis, o-Serie für Reasoning |
| Anthropic | Claude Sonnet/Opus | 200K Kontext, stark bei langen Texten |
| Google | Gemini 1.5/2.0 Pro | 1M-Token-Fenster, Google-Workspace-Integration |
| Meta | Llama 3.x | Open Source, lokal betreibbar |
| Mistral | Mistral Large 2 | EU-Unternehmen, DSGVO-freundlich |

**IDE-integrierte Coding-Assistenten**
| Tool | Integration | Besonderheit |
|---|---|---|
| GitHub Copilot | VS Code, Visual Studio, JetBrains | Marktführer, Enterprise-Option |
| Cursor | Eigener Editor (VS Code Fork) | KI-nativ, Agent-Modus |
| Windsurf (Codeium) | VS Code, JetBrains | Kostenfreier Tier, lokal möglich |
| JetBrains AI | Rider, IntelliJ | Tief in JetBrains-IDEs integriert |
| Continue.dev | VS Code, JetBrains | Open Source, lokale Modelle |

**Spezialisierte Werkzeuge**
- **Perplexity AI**: Suchbasiert, zeigt immer Quellen, ideal für Recherche
- **Phind**: Entwickler-Suchmaschine mit Code-Generierung
- **Le Chat**: Mistral-basierter Chat, EU-Datenschutz
- **v0 by Vercel**: UI-Komponentengenerierung (React, Tailwind)

### Auswahlkriterien

| Kriterium | Fragen |
|---|---|
| **Datenschutz** | DSGVO-konform? EU-Server? AVV verfügbar? |
| **Aktualität** | Trainingsdaten-Cutoff? Websuche verfügbar? |
| **Kontextfenster** | Wie viel Code/Dokument passt rein? |
| **Modellqualität** | Benchmarks (HumanEval, SWE-Bench)? |
| **Integration** | API, IDE-Plugin, CI/CD? |
| **Kosten** | Pro Seat, pro Token, Free Tier? |

---

## Lab 2.2 — ChatGPT, Claude, Copilot und Gemini im Vergleich

### ChatGPT (OpenAI)
- **Stärken:** Größte Nutzerbasis, o3 für komplexes Reasoning, Code Interpreter, breite Tool-Integration
- **Schwächen:** US-Server, bei hohem Volumen teuer, Datenschutz kritisch
- **Ideal für:** Allgemeine Coding-Aufgaben, Datenanalyse, algorithmische Probleme

### Claude (Anthropic)
- **Stärken:** 200K Token Kontextfenster, exzellent bei langen Dokumenten und Code-Reviews, weniger Halluzinationen
- **Schwächen:** Kein natives Browsing ohne Tools, US-Server
- **Ideal für:** Lange Codebasen analysieren, Architekturberatung, Dokumentation

### GitHub Copilot
- **Stärken:** Direkt in IDE integriert (kein Kontextwechsel), Inline-Completion, kennt geöffnete Dateien
- **Schwächen:** Nur für Coding, Qualität abhängig vom geöffneten Kontext
- **Ideal für:** Tägliche Entwicklungsarbeit, Autovervollständigung, Test-Generierung im Kontext

### Google Gemini
- **Stärken:** Bis zu 1 Mio. Token Fenster, Google Workspace Integration, Vertex AI
- **Schwächen:** Code-Qualität teils hinter GPT-4o/Claude, Google-Ökosystem nötig
- **Ideal für:** Google Cloud Projekte, Analyse sehr langer Dokumente

---

## Lab 2.3 — Le Chat, Perplexity, Phind und Codeium

### Le Chat (Mistral)
- Europäisches Unternehmen (Paris) → DSGVO-nativ
- Mistral Large 2: starke Coding-Qualität
- Open-Source-Modelle (Mistral 7B, Mixtral) lokal betreibbar
- **Einsatz:** Datenschutzsensible EU-Projekte, On-Premise-Alternativen

### Perplexity AI
- Kombiniert Web-Suche + KI → **immer aktuelle Quellen**
- Zeigt Quellen zu jeder Aussage → nachvollziehbar
- **Einsatz:** Library-Recherche, NuGet-Pakete, aktuelle Framework-Versionen, Changelog-Fragen

### Phind
- Speziell für Entwickler: Websuche + Code-Generierung kombiniert
- Versteht technische Fragen besser als Generalsuchmaschinen
- **Einsatz:** Technische Fehlersuche, How-to-Fragen, Bibliotheks-Dokumentation

### Codeium / Windsurf
- Kostenfreier Copilot-Konkurrent
- Windsurf: KI-nativer Editor, Cascade-Agent-Modus
- Unterstützt 70+ Sprachen
- **Einsatz:** Copilot-Alternative ohne Kosten, Einstieg in KI-Coding

---

## Lab 2.4 — Anbieter nach Schwerpunkt auswählen

### Entscheidungsmatrix

| Aufgabe | Empfehlung 1 | Empfehlung 2 | Grund |
|---|---|---|---|
| Tägliche Code-Completion | GitHub Copilot | Cursor/Codeium | IDE-Integration, Kontext-aware |
| Architektur-Diskussion | Claude | ChatGPT o3 | Großes Fenster, Reasoning |
| Library-Recherche | Perplexity | Phind | Websuche, Quellen |
| EU-Datenschutz | Le Chat | Azure OpenAI | EU-Server |
| Algorithmen/Mathe | ChatGPT o3 | Claude | Reasoning-Stärke |
| UI-Prototyp | v0 by Vercel | ChatGPT Canvas | Spezialisiert |
| Lange Dokumente | Claude | Gemini 1.5 | Kontextfenster |

### Typischer Multi-Tool-Workflow

```
Anforderungsanalyse   →  Claude (lange Dokumente, Strukturierung)
Architekturentwurf    →  Claude / ChatGPT o3 (Reasoning)
Tägliche Entwicklung  →  GitHub Copilot (IDE-integriert)
Library-Recherche     →  Perplexity (aktuell + Quellen)
Code-Review           →  Claude (großer Kontext)
Dokumentation         →  Claude (Schreibqualität)
```
