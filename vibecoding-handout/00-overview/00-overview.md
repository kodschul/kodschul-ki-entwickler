# 00 - Overview: App bauen ohne Coding

Schulungszeit: 09:00 - 17:00 Uhr (2 Tage)

## Was ist Vibecoding?

> "Vibecoding" bedeutet: Du beschreibst, was du willst - Claude baut es.
> Kein Code schreiben. Kein Code lesen. Nur natuerliche Sprache.

Du bist der **Produktverantwortliche** - du kennst das Problem und die Loesung.
Claude ist dein **Entwickler** - er kennt die Technik.

---

## Das gemeinsame Beispiel: Offer Studio

Wir bauen zusammen eine App, mit der jeder Angebote erstellen kann.

App-Name: **Offer Studio**

Kernablauf:

1. Angebotstyp und Kundendaten eingeben
2. Anforderungen in eigenen Worten beschreiben
3. "Generate" klicken
4. Claude erzeugt einen fertigen Angebotsentwurf
5. Angebot pruefen, uebersetzen, exportieren

Du kannst jederzeit deine eigene App-Idee parallel einbringen.

---

## Dein Werkzeug: Claude Code

Claude Code ist eine KI, die direkt in deiner Entwicklungsumgebung laeuft.
Du chattest mit ihr wie mit einem Kollegen:

- "Erstelle eine Seite mit einem Formular fuer Kundendaten."
- "Fuge einen Button hinzu, der das Formular abschickt."
- "Aendere die Farbe des Buttons auf Blau."
- "Mache die App auf dem Handy nutzbar."

Claude antwortet mit Code - und setzt ihn direkt um.
Du siehst das Ergebnis sofort.

---

## Was Teilnehmende am Ende koennen

- Eine echte, lauffaehige App bauen - ohne Code zu schreiben
- Claude mit klaren Beschreibungen steuern
- Claude beibringen, wie deine App "denken" soll (CLAUDE.md)
- Wiederverwendbare Regeln und Kurzbefehle anlegen
- Qualitaetspruefung und Automatisierung einrichten
- Echte Daten einbinden (optional)

---

## Agenda mit Pausen

### Tag 1

- 09:00 - 10:30: Intro + Live-Demo: Erste App in 30 Minuten
- 10:30 - 10:45: Pause
- 10:45 - 12:15: CLAUDE.md - der Masterplan fuer deine App
- 12:15 - 13:15: Pause
- 13:15 - 15:00: Hands-on: Formular + erste Funktion live bauen
- 15:00 - 15:15: Pause
- 15:15 - 17:00: Skills + Commands: Claude mit Regeln und Shortcuts steuern

### Tag 2

- 09:00 - 10:30: Agents und Specs: Qualitaet ohne Expertenwissen
- 10:30 - 10:45: Pause
- 10:45 - 12:15: Hands-on: Review-Flow + Uebersetzung + Export
- 12:15 - 13:15: Pause
- 13:15 - 15:00: Hooks, MCP (optional) - Automatisierung und echte Daten
- 15:00 - 15:15: Pause
- 15:15 - 17:00: Finalisierung, Demo, Feedback

---

## Das Geheimnis guter Vibecoding-Prompts

| Statt...                   | Besser...                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------ |
| "Mach eine App"            | "Baue eine App mit einem Formular fuer Name, Firma und Projektbeschreibung."         |
| "Etwas stimmt nicht"       | "Der Generate-Button tut nichts, wenn das Budget-Feld leer ist. Zeige eine Meldung." |
| "Aendere das Design"       | "Mache den Hintergrund weiss und den Button dunkelblau, Schriftgroesse 16px."        |
| "Fuge eine Funktion hinzu" | "Wenn ich auf Export klicke, soll die App eine PDF-Datei herunterladen."             |

**Regel:** Je konkreter deine Beschreibung, desto besser das Ergebnis.

---

## Wachsende App - Schritt fuer Schritt

### Tag 1 Vormittag

- Erste Seite mit Claude beschreiben
- Formular fuer Angebotsdaten
- Generate-Button + Ergebnis anzeigen

### Tag 1 Nachmittag

- CLAUDE.md: App-Regeln hinterlegen
- Skills: Angebotsstruktur festlegen
- Commands: Kurzbefehle einrichten

### Tag 2 Vormittag

- Agents: Prueflogik einbauen
- Specs: Anforderungen als Geschichten
- Review und Uebersetzen

### Tag 2 Nachmittag

- Hooks: Automatische Folgeaktionen
- MCP: Echte Daten einbinden (optional)
- Finaler End-to-End Flow

---

## Ziel-Codebase (Endstand - Claude schreibt das alles)

```
offer-studio/
  CLAUDE.md          <- deine App-Regeln in Textform
  README.md
  .claude/
    skills/
      offer-structure.md
      language-style.md
    commands/
      generate-offer.md
      review-offer.md
    agents/
      quality-reviewer.md
      translator.md
    specs/
      offer-flow-spec.md
    hooks/
      auto-version.md
  frontend/
    src/
      pages/
      components/
```

Du erstellst keine dieser Dateien selbst - du beschreibst Claude, was sie enthalten sollen.

## Agenda mit Pausen

### Tag 1

- 09:00 - 10:30: Intro, App-Ziel, Demo, Prompt-Basics
- 10:30 - 10:45: Pause
- 10:45 - 12:15: Referenzen, Projektstruktur, `CLAUDE.md`
- 12:15 - 13:15: Pause
- 13:15 - 15:00: Hands-on Frontend Grundgeruest + Angebotsformular
- 15:00 - 15:15: Pause
- 15:15 - 17:00: Hands-on Skills + Commands + erster App-Flow

### Tag 2

- 09:00 - 10:30: Agents, Specs, Qualitaetsregeln
- 10:30 - 10:45: Pause
- 10:45 - 12:15: Hands-on Review-Flow + Uebersetzung + Export
- 12:15 - 13:15: Pause
- 13:15 - 15:00: Hooks, MCP (optional), Integrations-Demo
- 15:00 - 15:15: Pause
- 15:15 - 17:00: Finalisierung, Demo, Feedback

## Wachsende Anforderungen (Step by Step)

### Phase 1 (Tag 1 Mittag)

- Angebot erfassen (Kunde, Scope, Budget, Timeline)
- Entwurf mit Claude erzeugen

### Phase 2 (Tag 1 Nachmittag)

- Offer-Struktur als Skill hinterlegen
- `/generate-offer` Command nutzen
- Ersten Quality-Agent integrieren

### Phase 3 (Tag 2 Vormittag)

- Review-Logik und Akzeptanzkriterien als Spec
- Uebersetzung DE/EN
- Export-Formate (Markdown/PDF-ready)

### Phase 4 (Tag 2 Nachmittag)

- Optional: externe Daten (MCP)
- Finaler End-to-End Flow in der UI

## Ziel-Codebase (Endstand)

```
offer-studio/
  CLAUDE.md
  README.md
  sample-inputs/
    rfp-basic.md
    rfp-extended.md
  .claude/
    skills/
      offer-structure.md
      pricing-rules.md
    commands/
      generate-offer.md
      review-offer.md
    agents/
      compliance-reviewer.md
      translator.md
      quality-reviewer.md
    specs/
      offer-flow-spec.md
    hooks/
      notify-review.md
  frontend/
    src/
      pages/
      components/
      services/
  outputs/
    offer-client-xyz.md
```

## Modulfolge

- 01-referenzen
- 02-claude.md-setup
- 03-skills
- 04-commands
- 05-agents
- 06-specs
- 07-hooks
- 08-mcp

Jedes Modul hat:

- eine Moduldatei mit Thema, Referenzen, Sample Prompts
- eine `exercise.md` mit klaren Aufgaben fuer TN
