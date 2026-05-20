# 00 - Overview: Frontend Offer App

Schulungszeit: 09:00 - 17:00 Uhr (2 Tage)

## Zielbild

Wir bauen eine Frontend-App, mit der Business-Teams Angebote erzeugen koennen.

App-Name: Offer Studio

Kernablauf in der App:

1. Angebotstyp waehlen
2. Kundendaten eingeben
3. Anforderungen/RFP einfuellen
4. "Generate" klicken
5. Claude erzeugt Angebotsentwurf
6. Review, Uebersetzung, Export

## Was Teilnehmende am Ende koennen

- Eine lauffaehige Frontend-App mit Formular, Vorschau und Export bauen
- Claude mit `CLAUDE.md`, Skills, Commands und Agents steuern
- Angebotslogik Schritt fuer Schritt erweitern (Specs, Hooks, MCP optional)
- Reale Angebots-Workflows fuer den Business-Alltag abbilden

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
