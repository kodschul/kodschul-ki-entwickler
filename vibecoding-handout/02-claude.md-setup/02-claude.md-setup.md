# CLAUDE.md Setup

**Block:** 10:45 - 12:15 Uhr (Tag 1) + Vertiefung 13:15 - 15:00

---

## Wie funktioniert das unter der Haube?

```
Claude startet Session
  -> liest CLAUDE.md als Kernkontext
  -> wendet Regeln auf alle Antworten an
  -> liefert konsistente Angebotsentwuerfe
```

`CLAUDE.md` ist die zentrale Steuerdatei fuer Produktziel, Stil, Regeln und Grenzen.

---

## Warum / Wann nicht?

| Warum nutzen                      | Wann nicht                                              |
| --------------------------------- | ------------------------------------------------------- |
| Einheitlicher Output im Team      | Sehr kurzer Einmaltest ohne Wiederverwendung            |
| Weniger Prompt-Wiederholung       | Wenn Regeln bewusst explorativ/offen bleiben sollen     |
| Schnellere Skalierung auf neue TN | Wenn kein gemeinsamer Qualitaetsstandard benoetigt wird |

---

## Bestandteile einer starken CLAUDE.md

1. Produktkontext

- App: Offer Studio
- Zielgruppe: Sales, Consulting, Bid-Team
- Input/Output klar benannt

2. Ausgabestandards

- Pflichtabschnitte je Angebot
- Tonalitaet und Sprache
- Qualitaetskriterien

3. Compliance

- Datenschutz
- Risikoaussagen
- Preisdarstellung

4. UI-Flow-Regeln

- Eingabe ueber OfferForm
- Ausgabe in OfferPreview
- Aktionen: Generate, Review, Translate, Export

---

## Vollstaendiges Muster

```markdown
# Projekt: Offer Studio

## Ziel

Diese Frontend-App erzeugt Angebotsentwuerfe aus strukturierten Formulardaten.

## Pflichtstruktur je Angebot

1. Executive Summary
2. Scope
3. Timeline
4. Pricing
5. Next Steps

## Ton und Sprache

- Deutsch standardmaessig
- Praezise, business-orientiert, C-Level verstaendlich
- Keine unbelegten Versprechen

## Compliance

- Keine echten personenbezogenen Daten in Samples
- Preise als Bandbreite oder Annahme kennzeichnen
- Riskante Aussagen markieren statt verschweigen

## UI-Flow

- Inputs kommen aus OfferForm
- Ergebnis erscheint in OfferPreview
- Aktionen: Generate, Review, Translate, Export
```

---

## Muster-Prompts

```text
Erstelle eine CLAUDE.md fuer Offer Studio mit Produktziel,
Pflichtstruktur, Compliance und UI-Flow-Regeln.
```

```text
Pruefe meine bestehende CLAUDE.md auf Luecken und schlage
maximal 8 konkrete Verbesserungen vor.
```

```text
Wende die CLAUDE.md auf sample-inputs/rfp-basic.md an
und zeige, ob alle Regeln eingehalten werden.
```

---

## Ergebnis

Nach dem Modul liefert Claude reproduzierbar Angebotsentwuerfe, die zur Frontend-App und zum Business-Kontext passen.
