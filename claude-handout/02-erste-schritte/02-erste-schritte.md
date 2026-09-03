# 02 – Erste Schritte mit Claude Code

**Block:** 90 min | **Tag 2**

---

## Was ist Claude Code?

Claude Code ist Anthropics **agentisches Coding-Tool** – anders als IDE-Plugins läuft es primär im **Terminal** (zusätzlich als IDE-Erweiterung für VS Code/JetBrains verfügbar). Es liest Dateien, plant Schritte, führt Shell-Befehle aus und schreibt Code – in einer durchgehenden Tool-Loop, die du live mitverfolgst.

```
claude              → interaktiver REPL-Modus (Standard)
claude "Frage..."   → Ein-Schritt-Aufruf, danach REPL
claude --print "..." → nur Antwort ausgeben, kein UI (Modul 11)
```

---

## Installation

```bash
npm install -g @anthropic-ai/claude-code
claude                      # startet den interaktiven Modus im aktuellen Ordner
```

Beim ersten Start: Login über den Browser (Anthropic-Account oder API-Key), danach merkt sich Claude Code die Anmeldung.

---

## Der REPL – interaktiver Modus

```
> Erkläre mir, was app.py tut
```

- Claude antwortet im Terminal, kann dabei automatisch Dateien lesen (`Read`, `Glob`, `Grep`)
- Bei Datei-Änderungen zeigt Claude einen **Diff** und fragt (je nach Permissions) nach Bestätigung
- **ESC** unterbricht die aktuelle Aktion, **Strg+C** beendet die Session

## Wichtige Tastenkürzel & Verhalten

| Aktion                                | Wie                                                      |
| ------------------------------------- | -------------------------------------------------------- |
| Mehrzeiliger Prompt                   | `\` am Zeilenende oder Shift+Enter (client-abhängig)     |
| Letzten Prompt wiederholen/bearbeiten | Pfeiltaste hoch                                          |
| Aktuelle Aktion abbrechen             | `ESC`                                                    |
| Bild einfügen (Screenshot)            | Einfügen per Zwischenablage (in unterstützten Terminals) |
| Datei-/Ordner-Zugriff erweitern       | `/add-dir <pfad>`                                        |

---

## Ghost Text? Nicht bei Claude Code.

Anders als Autocomplete-Tools zeigt Claude Code **keinen Inline-Ghost-Text** während des Tippens. Stattdessen: Du beschreibst eine Aufgabe, Claude arbeitet sie eigenständig ab (liest, plant, ändert, testet) und zeigt dir das Ergebnis als Diff. Das ist der zentrale Unterschied zu Modul 02 im Copilot-Kurs – Claude Code ist von Grund auf **agentisch**, nicht reaktiv.

---

## Erste sinnvolle Prompts

```
Was macht dieses Projekt? Gib mir einen kurzen Überblick.
```

```
Führe die Tests aus und fasse das Ergebnis zusammen.
```

```
Füge eine Route /health hinzu, die {"status": "ok"} als JSON zurückgibt.
```

> Je konkreter die Aufgabe, desto zuverlässiger das Ergebnis (siehe Modul 03 – Grundlagen: KI im Coding).
