# Commands

**Block:** 15:15 - 17:00 Uhr (Tag 1)

---

## Was ist ein Command?

Ein Command ist ein **Kurzbefehl**, den du einmal definierst und dann immer wieder nutzt.
Statt jedesmal einen langen Prompt zu schreiben, tippst du einfach `/angebot-erstellen`.
Claude weiss dann genau, was zu tun ist.

```
Du tippst /angebot-erstellen
  -> Claude laedt den Command aus .claude/commands/
  -> Folgt den Schritten, die du einmal beschrieben hast
  -> Nutzt passende Skills automatisch
  -> Liefert immer das gleiche Ergebnisformat
```

**Pfad:** `.claude/commands/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                             | Wann nicht                                          |
| ---------------------------------------- | --------------------------------------------------- |
| Haeufige Aktionen mit einem Wort starten | Einmalige Ad-hoc Anfrage                            |
| Gleiches Ergebnis fuer jeden im Team     | Wenn der Ablauf noch nicht klar ist                 |
| Kein langes Erklaeren jedes Mal          | Wenn eine einfache Stilregel als Skill schon reicht |

---

## Wie beschreibst du einen Command?

Du erklaerst Claude in Textform:

- Was gibt der Nutzer ein?
- Was soll Claude Schritt fuer Schritt tun?
- Was soll am Ende herauskommen?

Kein Code noetig - nur eine klare Beschreibung.

---

## Vollstaendige Beispiele

**`.claude/commands/generate-offer.md`**

```markdown
# Command: /generate-offer

Eingabe des Nutzers:

- Kundenname
- Firmenbeschreibung
- Was soll gemacht werden?
- Budget (ungefaehr)
- Zeitraum

Was Claude tun soll:

1. Pruefen: Sind alle Pflichtfelder vorhanden? Wenn nicht: kurze Fehlermeldung.
2. Die Angebotsstruktur aus den Skills nutzen.
3. Den Sprachstil aus den Skills einhalten.
4. Einen vollstaendigen Angebotsentwurf erstellen.
5. Am Ende: Liste offener Fragen und Annahmen ausgeben.

Ergebnis:

- Fertiger Angebotsentwurf (alle 5 Abschnitte)
- Liste offener Annahmen
```

**`.claude/commands/review-offer.md`**

```markdown
# Command: /review-offer

Eingabe:

- Ein vorhandener Angebotsentwurf

Was Claude tun soll:

1. Pruefen: Sind alle 5 Abschnitte vorhanden?
2. Unklare oder riskante Aussagen markieren.
3. Maximal 10 konkrete Verbesserungsvorschlaege nennen.
4. Priorisierte To-do Liste erstellen.

Ergebnis:

- Review-Bericht mit Prioritaeten
```

---

## So laesst du Claude den Command anlegen

```text
Erstelle `.claude/commands/generate-offer.md`.
Wenn ich /generate-offer schreibe, soll Claude:
1. Die Eingabefelder (Kunde, Scope, Budget, Zeitraum) pruefen.
2. Einen vollstaendigen Angebotsentwurf mit 5 Abschnitten erstellen.
3. Am Ende offene Annahmen auflisten.
Nutze dabei die vorhandenen Skills.
```

---

## Muster-Prompts

```text
Erstelle `.claude/commands/generate-offer.md`.
Der Befehl soll Pflichtfelder pruefen, dann einen Entwurf erstellen
und am Ende eine Liste offener Fragen ausgeben.
```

```text
Erstelle `.claude/commands/review-offer.md`.
Der Befehl soll Vollstaendigkeit pruefen, Risiken markieren
und maximal 10 priorisierte Verbesserungen nennen.
```

```text
Fuehre /generate-offer und danach /review-offer auf dem gleichen Angebot aus.
Zeige mir, was sich durch den Review verbessert hat.
```

---

## Ergebnis

Du kannst jetzt mit einem Wort komplexe Ablaeufe starten.
Das Ergebnis ist immer gleich - egal wer es aufruft.

---

## Warum / Wann nicht?

| Warum nutzen                                | Wann nicht                                          |
| ------------------------------------------- | --------------------------------------------------- |
| Wiederkehrender Ablauf mit festen Schritten | Einmalige Ad-hoc Anfrage                            |
| Gleiches Ergebnisformat fuer alle TN        | Wenn der Ablauf noch vollkommen offen ist           |
| Gute Uebergabe im Team                      | Wenn nur eine kleine Stilregel fehlt (Skill reicht) |

---

## Aufbau - Vollstaendiges Beispiel

**`.claude/commands/generate-offer.md`**

```markdown
# Command: /generate-offer

Input:

- Kunde
- Scope
- Budget
- Timeline

Workflow:

1. Validiere, ob alle Pflichtfelder vorhanden sind.
2. Nutze Skill "offer-structure" fuer die Gliederung.
3. Nutze Skill "language-style" fuer den Ton.
4. Erzeuge Angebotsentwurf in Markdown.
5. Gib am Ende eine kurze Liste offener Annahmen aus.

Output:

- Vollstaendiger Angebotsentwurf
- Offene Fragen/Annahmen
```

**`.claude/commands/review-offer.md`**

```markdown
# Command: /review-offer

Input:

- Vorhandener Angebotsentwurf

Workflow:

1. Pruefe Vollstaendigkeit der 5 Pflichtabschnitte.
2. Markiere unklare Aussagen.
3. Nenne maximal 10 konkrete Verbesserungen.
4. Erstelle eine priorisierte To-do Liste.

Output:

- Review-Report mit Prioritaeten
```

---

## Muster-Prompts

```text
Erstelle `.claude/commands/generate-offer.md` fuer unser Offer Studio.
Der Command soll Pflichtfelder validieren und danach einen Entwurf erzeugen.
```

```text
Erstelle `.claude/commands/review-offer.md` mit einer priorisierten Review-Ausgabe.
```

```text
Teste den Flow: zuerst /generate-offer, danach /review-offer,
und gib die Unterschiede im Ergebnis aus.
```

---

## Ergebnis

Die Frontend-App bekommt stabile, teamweit wiederholbare Angebots-Workflows.
