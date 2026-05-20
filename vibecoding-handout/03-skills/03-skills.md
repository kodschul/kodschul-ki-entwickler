# Skills

**Block:** 15:15 - 17:00 Uhr (Tag 1, zusammen mit Commands)

---

## Wie funktioniert das unter der Haube?

```
User beschreibt Aufgabe
	-> Claude prueft vorhandene Skills in .claude/skills/
	-> passende Skill-Regeln werden auf die Ausgabe angewendet
	-> Ergebnis bleibt konsistent, auch bei unterschiedlichen Inputs
```

Ein Skill ist eine **wiederverwendbare Regeldatei** fuer Stil, Struktur oder Qualitaetskriterien.

**Pfad:** `.claude/skills/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                                     | Wann nicht                                                     |
| ------------------------------------------------ | -------------------------------------------------------------- |
| Einheitliche Angebotsstruktur fuer alle TN       | Einmalige Sonderaufgabe ohne Wiederholung                      |
| Weniger Nacharbeit bei Form, Ton und Reihenfolge | Wenn Regeln noch unklar sind und erst exploriert werden sollen |
| Schnellere Einarbeitung neuer Teammitglieder     | Wenn ein Command mit fixem Workflow schon alles abdeckt        |

---

## Vergleich: Skill vs Command vs Agent

|            | Skill                        | Command                      | Agent                                 |
| ---------- | ---------------------------- | ---------------------------- | ------------------------------------- |
| Hauptzweck | Regeln                       | Workflow                     | Spezialisierte Teilaufgabe            |
| Aufruf     | implizit durch Kontext       | aktiv via `/name`            | aktiv per Beschreibung                |
| Output     | beeinflusst Format/Qualitaet | liefert Ergebnis eines Flows | liefert Analyse/Pruefung/Teilresultat |

---

## Aufbau - Vollstaendiges Beispiel

**`.claude/skills/offer-structure.md`**

```markdown
# Skill: Offer Structure

Nutze fuer jeden Angebotsentwurf exakt diese Struktur:

1. Executive Summary
2. Scope
3. Timeline
4. Pricing
5. Next Steps

## Regeln

- Maximal 8 Bullet Points pro Abschnitt
- Keine Marketing-Floskeln ohne Substanz
- Zahlen nur nennen, wenn Quelle im Input vorhanden ist
- Jede Timeline mit klaren Phasen (z.B. Analyse, Umsetzung, Rollout)

## Qualitaetscheck

- Sind alle 5 Abschnitte vorhanden?
- Ist der Nutzen fuer den Kunden klar benannt?
- Ist der Text fuer C-Level in < 5 Minuten lesbar?
```

**`.claude/skills/language-style.md`**

```markdown
# Skill: Language Style

## Zielstil

- Sprache: Deutsch (Business)
- Ton: praezise, loesungsorientiert, ruhig
- Satzlaenge: eher kurz

## Vermeiden

- zu technische Tiefen ohne Mehrwert
- unklare Begriffe wie "state-of-the-art" ohne Beleg
- absolute Aussagen wie "garantiert" oder "risikofrei"
```

---

## Muster-Prompts

```text
Erstelle `.claude/skills/offer-structure.md` fuer unsere Offer-App.
Die Struktur muss immer Executive Summary, Scope, Timeline, Pricing, Next Steps enthalten.
```

```text
Erstelle `.claude/skills/pricing-rules.md` mit Regeln fuer Preisbausteine,
Annahmen, Ausschluesse und transparente Berechnungslogik.
```

```text
Wende `offer-structure` und `language-style` auf den bestehenden Entwurf an
und zeige vorher/nachher Unterschiede.
```

---

## Ergebnis

Die App erzeugt konsistente Angebote ueber alle Teams hinweg, statt pro Person stark zu variieren.
