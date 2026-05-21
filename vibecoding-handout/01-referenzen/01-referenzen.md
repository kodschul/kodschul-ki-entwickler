# Referenzen

**Block:** 09:00 - 10:30 Uhr

---

## Wie funktioniert Vibecoding?

```
Du beschreibst dein Ziel in natuerlicher Sprache
  -> Claude versteht den Kontext
  -> Claude schreibt den Code selbst
  -> Du siehst das Ergebnis und gibst Feedback
  -> Claude verbessert
  -> Fertige, funktionierende App
```

Du brauchst nie zu wissen, wie der Code aussieht.
Du musst nur wissen, was du willst.

---

## Die Werkzeuge - was ist was?

| Werkzeug            | Was du darin beschreibst                         | Wer es "liest"     |
| ------------------- | ------------------------------------------------ | ------------------ |
| `CLAUDE.md`         | Was deine App ist und wie sie wirkt              | Claude immer       |
| `.claude/skills/`   | Wiederkehrende Regeln fuer Ausgaben              | Claude bei Bedarf  |
| `.claude/commands/` | Ablaeufe, die du mit einem Wort starten willst   | Du via `/befehl`   |
| `.claude/agents/`   | Spezialisierte Aufgaben (Pruefung, Uebersetzung) | Claude als Helfer  |
| `.claude/specs/`    | Was die App koennen soll (Anforderungen)         | Claude und du      |
| `.claude/hooks/`    | Automatische Folgeaktionen                       | Claude automatisch |

Alle diese Dateien sind **normale Textdateien** - kein Code.
Du beschreibst darin in Saetzen, was du willst.

---

## Warum brauche ich das alles?

Ohne Kontext-Dateien:

- Claude vergisst von Sitzung zu Sitzung
- Jedes neue Gespraech beginnt von vorn
- Ergebnisse sind inkonsistent

Mit Kontext-Dateien:

- Claude kennt deine App immer
- Regeln werden automatisch eingehalten
- Das ganze Team bekommt gleiche Ergebnisse

---

## Warum / Wann nicht?

| Warum nutzen                          | Wann nicht                                      |
| ------------------------------------- | ----------------------------------------------- |
| Konsistente App ueber viele Sitzungen | Wenn du nur einmal etwas ausprobieren willst    |
| Kein Erklaeren fuer jede neue Frage   | Wenn die App nur wenige Minuten existiert       |
| Gemeinsame Regeln fuer Teams          | Wenn du allein eine schnelle Einmal-Demo machst |

---

## Muster-Prompts

```text
Erstelle eine Projektstruktur fuer eine App namens "Offer Studio".
Lege folgende Ordner an: frontend/src/pages, frontend/src/components,
sowie .claude mit den Unterordnern skills, commands, agents, specs, hooks.
Erstelle auch eine leere CLAUDE.md und eine README.md.
```

```text
Erklaere mir in einfachen Worten, was CLAUDE.md, Skills, Commands,
Agents, Specs und Hooks sind - ohne Fachbegriffe aus der Programmierung.
```

```text
Was muss ich Claude sagen, damit er versteht, dass er eine App
zur Angebotserstellung bauen soll? Hilf mir, die perfekte Beschreibung
zu formulieren.
```

---

## Mini-Referenz: Dateibaum

```text
offer-studio/
  CLAUDE.md                <- Herzstuck: App-Beschreibung und Regeln
  .claude/
    skills/                <- Regeln fuer Stil und Struktur
    commands/              <- Kurzbefehle fuer haeufige Aktionen
    agents/                <- Spezialisierte Helfer
    specs/                 <- Anforderungen in Textform
    hooks/                 <- Automatische Folgeaktionen
  frontend/
    src/
      pages/
      components/
      services/
```

Claude legt alle diese Ordner und Dateien fuer dich an - du musst nur fragen.

---

## Ergebnis

TN verstehen den Gesamtzusammenhang und koennen die Module 02-08 zielgerichtet umsetzen.

Naechstes Modul: `02-claude.md-setup`.
