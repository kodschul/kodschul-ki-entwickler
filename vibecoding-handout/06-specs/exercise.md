# Exercise: Spec schreiben und validieren

## Ziel

Ihr erstellt eine umsetzbare Spec fuer den Offer-Flow und validiert sie gegen reale Beispielinputs.

## Aufgabe

Erzeuge `.claude/specs/offer-flow-spec.md` mit:

- 3 User Stories
- je mindestens 3 Akzeptanzkriterien
- 2 Negativfaellen
- klaren Out-of-Scope Punkten

## Muster-Prompts

```text
Erstelle eine Spec fuer Offer Studio mit den Stories
Generate, Review, Translate und Given/When/Then Kriterien.
```

```text
Fuege pro Story einen Abschnitt "Out of Scope" hinzu,
damit in der Umsetzung kein Scope Creep entsteht.
```

```text
Validiere die Spec gegen `sample-inputs/rfp-basic.md`
und nenne Luecken in den Akzeptanzkriterien.
```

## Abgabe

- Spec-Datei
- kurze Liste mit 3 identifizierten Luecken und deren Fix

## Done-Kriterien

- [ ] Spec-Datei vorhanden
- [ ] Kriterien testbar und eindeutig
- [ ] Negativfaelle sinnvoll abgedeckt
