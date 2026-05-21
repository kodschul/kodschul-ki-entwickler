# Skills

**Block:** 15:15 - 17:00 Uhr (Tag 1)

---

## Was ist ein Skill?

Ein Skill ist eine **Textdatei mit Regeln** - du beschreibst darin, wie Claude
bei einer bestimmten Aufgabe vorgehen soll.

Beispiel: Du moechtest, dass jedes Angebot immer gleich aufgebaut ist.
Statt es jedes Mal neu zu erklaeren, schreibst du es einmal in einen Skill.
Claude folgt diesen Regeln automatisch.

```
Du stellst eine Anfrage an Claude
  -> Claude prueft: Gibt es einen passenden Skill?
  -> Skill-Regeln werden automatisch angewendet
  -> Ergebnis folgt immer deinen Vorgaben
  -> Kein Erinnern, kein Wiederholen
```

**Pfad:** `.claude/skills/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                                  | Wann nicht                                             |
| --------------------------------------------- | ------------------------------------------------------ |
| Gleiches Format bei jeder Antwort             | Einmalige Sonderaufgabe ohne Wiederholung              |
| Kein Erklaeren bei jeder neuen Frage          | Wenn du noch experimentierst, welche Regeln du willst  |
| Neue Teammitglieder bekommen sofort Qualitaet | Wenn ein Command mit festem Ablauf schon alles abdeckt |

---

## Skill vs Command vs Agent - der Unterschied

|               | Skill                         | Command                | Agent                            |
| ------------- | ----------------------------- | ---------------------- | -------------------------------- |
| Was es ist    | Regeln und Stil               | Fertiger Ablauf        | Spezialisierter Helfer           |
| Wann es wirkt | Automatisch im Hintergrund    | Du tippst einen Befehl | Du bittest Claude um Hilfe       |
| Beispiel      | "Angebote immer 5 Abschnitte" | "/angebot-erstellen"   | "Pruefe das Angebot auf Risiken" |

---

## So schreibst du einen Skill - kein Code noetig

Du beschreibst einfach, was du willst. Claude legt die Datei an.

**Beispiel: Angebotsstruktur**

```text
Erstelle die Datei `.claude/skills/offer-structure.md`.
Dieser Skill soll sicherstellen, dass jedes Angebot
genau diese 5 Abschnitte enthaelt:
1. Zusammenfassung
2. Leistungsumfang
3. Zeitplan
4. Preis
5. Naechste Schritte
Pro Abschnitt maximal 8 Stichpunkte.
Keine unbelegten Versprechen.
```

Claude schreibt die Datei. Du pruefst sie durch und sagst, was noch fehlt.

---

## Vollstaendige Beispiel-Dateien

**`.claude/skills/offer-structure.md`**

```markdown
# Skill: Angebotsstruktur

Jedes Angebot muss genau diese 5 Abschnitte enthalten:

1. Zusammenfassung - Was bieten wir an?
2. Leistungsumfang - Was genau machen wir?
3. Zeitplan - Wann liefern wir was?
4. Preis - Was kostet es?
5. Naechste Schritte - Was passiert jetzt?

## Regeln

- Maximal 8 Stichpunkte pro Abschnitt
- Keine Marketing-Phrasen ohne Inhalt
- Zahlen nur nennen, wenn sie aus dem Input stammen
- Zeitplan immer mit Phasen (z.B. Analyse, Umsetzung, Einfuehrung)

## Qualitaetscheck

- Sind alle 5 Abschnitte vorhanden?
- Ist der Mehrwert fuer den Kunden klar?
- Kann ein Entscheider es in 5 Minuten lesen?
```

**`.claude/skills/language-style.md`**

```markdown
# Skill: Sprache und Stil

## Wie soll die App schreiben?

- Sprache: Deutsch (Geschaftsstil)
- Ton: klar, loesungsorientiert, ruhig
- Saetze: eher kurz

## Was vermeiden?

- Technische Details, die der Kunde nicht braucht
- Unklare Begriffe ohne Erklaerung
- Absolute Aussagen wie "garantiert" oder "risikofrei"
```

---

## Muster-Prompts

```text
Erstelle `.claude/skills/offer-structure.md`.
Jedes Angebot soll immer die Abschnitte Zusammenfassung, Leistungsumfang,
Zeitplan, Preis und Naechste Schritte enthalten.
Maximal 8 Stichpunkte pro Abschnitt, kein Fachjargon.
```

```text
Erstelle `.claude/skills/language-style.md`.
Sprache: Deutsch, Ton: professionell aber verstaendlich,
kurze Saetze, kein Marketing-Sprech ohne Substanz.
```

```text
Wende alle Skills auf dieses Angebot an und zeige mir
vorher und nachher, was sich veraendert hat.
```

---

## Ergebnis

Nach diesem Modul hat Claude feste Regeln - und haelt sie automatisch ein.
Du musst es nie wieder erklaeren.

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
