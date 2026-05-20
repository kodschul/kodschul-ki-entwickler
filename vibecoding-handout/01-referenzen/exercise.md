# Exercise: Referenzen anwenden

## Ziel

Du setzt die ersten Claude-Prompts fuer die Frontend-Angebots-App um und dokumentierst den Unterschied zwischen vagen und praezisen Prompts.

## Aufgabe 1: Projektstruktur erzeugen

Muster-Prompt:

```text
Erstelle die Projektstruktur fuer eine Frontend-App "Offer Studio".
Lege an: frontend/src/pages, frontend/src/components, frontend/src/services,
CLAUDE.md, README.md, sample-inputs/rfp-basic.md und .claude Unterordner.
```

## Aufgabe 2: Basis-UI definieren

Muster-Prompt:

```text
Erzeuge eine UI-Struktur mit OfferForm, OfferPreview und GenerateButton.
Beschreibe pro Komponente Aufgabe, Input, Output und Validierung.
```

## Aufgabe 3: Prompt-Qualitaet vergleichen

Prompt A (vage):

```text
Erstelle ein Angebot.
```

Prompt B (praezise):

```text
Erstelle aus den Formfeldern Kunde, Scope, Budget, Timeline einen Angebotsentwurf
mit den Abschnitten Executive Summary, Scope, Timeline, Pricing, Next Steps.
Sprache: Deutsch, Ton: professionell.
```

## Aufgabe 4: Verbesserungsrunde

Muster-Prompt:

```text
Analysiere den Unterschied zwischen Output A und B.
Gib 5 konkrete Prompt-Verbesserungen fuer Offer Studio.
```

## Abgabe

- Vergleich A/B (kurz)
- finaler Prompt v1
- 3 wichtigste Lernpunkte

## Done-Kriterien

- [ ] Grundstruktur vorhanden
- [ ] UI-Definition vorhanden
- [ ] Promptvergleich dokumentiert

Naechstes Modul: `02-claude.md-setup`.
