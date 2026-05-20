# 02 - CLAUDE.md Setup fuer Offer Studio

Dauer: 10:45 - 12:15 (Tag 1) und Vertiefung 13:15 - 15:00

## Ziel

Wir definieren den zentralen Projektkontext fuer die Frontend-App, damit Claude konsistente Angebote erzeugt.

## Inhalt einer guten CLAUDE.md

1. Produktkontext

- App: Offer Studio
- Ziel: Angebotsentwuerfe aus Formulardaten erzeugen
- Zielgruppe: Sales, Consulting, Bid-Team

2. Ausgabestandards

- Pflichtabschnitte: Executive Summary, Scope, Timeline, Pricing, Next Steps
- Sprache: Deutsch primar, Englisch optional
- Ton: professionell, praezise, C-Level verstaendlich

3. Compliance

- Keine sensiblen Kundendaten in Beispielen
- DSGVO-konforme Formulierungen
- Keine verbindlichen Rechtsaussagen

4. Frontend-Produktregeln

- Inputs kommen aus OfferForm
- Ausgabe erscheint in OfferPreview
- Buttons: Generate, Review, Translate, Export

## Sample Prompt

```text
Erstelle eine CLAUDE.md fuer das Projekt Offer Studio.
Beruecksichtige GFT-Tonalitaet, Angebotsstruktur, Compliance und UI-Flow.
```

## Beispielauszug

```markdown
# Projekt: Offer Studio

## Ziel

Diese App erzeugt Angebotsentwuerfe aus Frontend-Formulardaten.

## Pflichtstruktur je Angebot

1. Executive Summary
2. Scope
3. Timeline
4. Pricing
5. Next Steps

## Ton und Sprache

- Deutsch standardmaessig
- Klar, praezise, business-orientiert
- Keine unbelegten Versprechen

## Compliance

- Keine echten personenbezogenen Daten in Samples
- Preise als Bereich, nicht als harte Zusage
```

## Ergebnis

Nach dem Modul ist die `CLAUDE.md` so klar, dass Claude reproduzierbar Angebotsentwuerfe fuer die Frontend-App liefert.
