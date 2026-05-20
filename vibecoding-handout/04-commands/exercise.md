# Exercise: Commands implementieren und testen

## Ziel

Ihr baut zwei produktive Slash-Commands und testet den End-to-End Ablauf.

## Aufgabe 1

Implementiere:

- `.claude/commands/generate-offer.md`
- `.claude/commands/review-offer.md`

## Aufgabe 2

Fuehre beide Commands auf dem gleichen Input aus und dokumentiere:

- erste Entwurfsversion
- Review-Befunde
- ueberarbeitete Version

## Muster-Prompts

```text
Erstelle `.claude/commands/generate-offer.md` mit Inputvalidierung,
Skill-Nutzung und standardisierter Ausgabe.
```

```text
Erstelle `.claude/commands/review-offer.md` mit Pruefung auf
Vollstaendigkeit, Nachvollziehbarkeit, Risikoformulierung.
```

```text
Teste beide Commands in Reihenfolge und gib eine kurze Auswertung,
welche Verbesserungen der Review-Command erzeugt hat.
```

## Done-Kriterien

- [ ] Beide Command-Dateien vorhanden
- [ ] Inputs/Outputs pro Command klar dokumentiert
- [ ] End-to-End Test dokumentiert
