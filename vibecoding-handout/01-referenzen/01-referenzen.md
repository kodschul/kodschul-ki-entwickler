# 01 - Referenzen: Claude Code fuer Frontend Offer Studio

Dauer: 09:00 - 10:30

## Ziel des Moduls

Du verstehst, wie Claude Code ein Frontend-Projekt fuer Angebotsgenerierung Schritt fuer Schritt aufbaut.

## Claude Code Referenzen (fuer TN)

- `CLAUDE.md`: Produktregeln, Tonalitaet, Angebotsstruktur
- `.claude/skills/`: wiederverwendbare Regeln
- `.claude/commands/`: Slash-Befehle fuer wiederkehrende Workflows
- `.claude/agents/`: spezialisierte Pruefer/Generatoren
- `.claude/specs/`: Anforderungen und Akzeptanzkriterien
- `.claude/hooks/`: automatische Folgeaktionen

## Beispiel-Prompts

### Prompt 1: Frontend-Grundgeruest

```text
Erstelle ein Frontend-Grundgeruest fuer "Offer Studio".
Seiten: OfferForm, OfferPreview, Settings.
Komponenten: ClientSection, ScopeSection, PricingSection, GenerateButton.
Nutze eine klare Struktur fuer src/pages, src/components und src/services.
```

### Prompt 2: Angebotsentwurf generieren

```text
Nutze die Eingaben aus dem OfferForm und erzeuge einen Angebotsentwurf im Markdown-Format.
Struktur: Executive Summary, Scope, Timeline, Pricing, Next Steps.
Sprache: Deutsch.
```

### Prompt 3: Verbesserungsrunde

```text
Ueberarbeite den Angebotsentwurf fuer C-Level Lesbarkeit.
Kuetze Saetze, mache ROI klar, behalte Fakten bei.
```

## Erwartetes Lernresultat

- TN koennen gute Prompts fuer UI + Angebotslogik schreiben
- TN verstehen, welche Datei in `.claude/` welchen Zweck hat
- TN kennen den End-to-End Flow von Formulareingabe bis Angebotsoutput

## Uebergang

Naechstes Modul: `02-claude.md-setup`.
