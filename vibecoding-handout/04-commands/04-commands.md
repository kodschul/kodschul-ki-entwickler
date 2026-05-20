# Commands

**Block:** 15:15 - 17:00 Uhr (Tag 1)

---

## Wie funktioniert das unter der Haube?

```
User ruft /generate-offer auf
	-> Claude laedt Command-Datei aus .claude/commands/
	-> folgt den Workflow-Schritten aus der Datei
	-> nutzt Skills/Agents bei Bedarf
	-> liefert reproduzierbares Ergebnis
```

Ein Command ist ein **ausfuehrbarer Workflow als Slash-Befehl**.

**Pfad:** `.claude/commands/<name>.md`

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
