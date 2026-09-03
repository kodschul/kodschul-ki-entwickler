# Intro – Arten von KI-Integrationen

**Block:** 30 min | **Tag 1**

---

## Warum dieser Einstieg?

Bevor es an die konkreten Claude-Code-Features geht, brauchen wir ein gemeinsames Vokabular: Nicht jede "KI im Terminal/Editor" funktioniert gleich. Die Unterscheidung hilft später zu verstehen, warum z. B. der REPL-Modus anders reagiert als Custom Agents oder Headless-Automation.

---

## Die vier Integrationsarten

| Art                            | Beispiel                                   | Charakteristik                                                 |
| ------------------------------ | ------------------------------------------ | -------------------------------------------------------------- |
| **Autocomplete / Ghost Text**  | IDE-Erweiterungen (z. B. Copilot)          | Reaktiv, kein Dialog, greift lokalen Kontext auf               |
| **Chat-Assistent**             | Claude.ai, Claude Code im "Ask"-Stil       | Dialogbasiert, beantwortet, ändert nichts selbst               |
| **Agentisch (im Terminal)**    | **Claude Code (interaktiver Modus)**       | Plant, nutzt Tools, editiert Dateien autonom in Loop           |
| **Agentisch (headless/cloud)** | Claude Code `--print`/CI, Claude Agent SDK | Läuft losgelöst vom Terminal, arbeitet Aufgaben zu Ergebnis ab |

```
Autocomplete  →  Chat  →  Agent (Terminal)  →  Agent (headless/CI)
   reaktiv        Dialog     Tool-Loop           vollautonom
   kein Ziel      1 Antwort  mehrere Schritte     eigenes Ergebnis/PR
```

---

## Rule-based vs. LLM-based

- **Regelbasiert** (klassische Linter, Snippets): deterministisch, 100 % nachvollziehbar, aber unflexibel.
- **LLM-basiert** (Claude & Co.): probabilistisch, flexibel, aber nicht deterministisch – gleiche Eingabe kann leicht unterschiedliche Ausgabe liefern.

> Merksatz: Je autonomer die Integration, desto wichtiger werden Leitplanken (`CLAUDE.md`, Permissions, Reviews) – Thema der kommenden Module.

---

## Claude Code – Besonderheit gegenüber IDE-Tools

Claude Code ist **primär ein Terminal-Tool**, kein Autocomplete-Plugin. Es gibt keinen Ghost-Text wie bei Inline-Completions – stattdessen arbeitet Claude Code direkt agentisch: Es liest Dateien, plant Schritte, führt Befehle aus und schreibt Code, während du zusiehst und eingreifen kannst.

| Tool                        | Haupt-Integrationsart                   |
| --------------------------- | --------------------------------------- |
| **Claude Code (CLI)**       | Agent (Terminal) + headless/CI          |
| Claude Code IDE-Erweiterung | Agent, eingebettet in VS Code/JetBrains |
| GitHub Copilot (Inline)     | Autocomplete                            |
| Claude.ai / ChatGPT (Web)   | Chat (kein Datei-Zugriff)               |

---

## Was aus diesem Modul mitzunehmen ist

- Vier Integrationsarten unterscheiden zu können, hilft, Erwartungen an ein Feature realistisch einzuordnen.
- Claude Code ist von Anfang an **agentisch und terminal-first** – das prägt den gesamten restlichen Kurs.
- Der Kurs bewegt sich von "einfacher Prompt" (Modul 02) zu "vollautonome Automation" (Modul 14).
