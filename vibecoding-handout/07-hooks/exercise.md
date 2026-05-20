# Exercise: Hooks implementieren

## Ziel

Ihr automatisiert den Uebergang von "Generated" zu "Review" inklusive Versionierung.

## Aufgabe 1

Erstelle:

- `.claude/hooks/notify-review.md`
- `.claude/hooks/auto-version.md`

## Aufgabe 2

Simuliere den Ablauf fuer einen Testfall:

1. Angebot erzeugen
2. Hook notify-review triggert
3. Review abschliessen
4. Hook auto-version triggert

## Muster-Prompts

```text
Erstelle einen Hook fuer Event `offer.generated`, der
Status auf `in review` setzt und einen Review-Task erzeugt.
```

```text
Erstelle einen Hook fuer Event `offer.review.completed`, der
die Angebotsversion erhoeht und ein Change-Log schreibt.
```

```text
Simuliere beide Hooks mit Testdaten und gib die Zustandsaenderungen aus.
```

## Done-Kriterien

- [ ] 2 Hook-Dateien vorhanden
- [ ] Trigger und Aktionen dokumentiert
- [ ] Testsimulation nachvollziehbar
