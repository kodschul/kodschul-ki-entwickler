# Exercise: Skills - Regeln fuer Claude anlegen

## Ziel

Du erstellst Skill-Dateien durch einfache Beschreibungen.
Claude schreibt den Inhalt. Du entscheidest, was du willst.

---

## Aufgabe 1: Angebotsstruktur als Skill

Schreibe diesen Prompt an Claude:

```text
Erstelle `.claude/skills/offer-structure.md`.
Dieser Skill soll sicherstellen, dass jedes Angebot genau diese
5 Abschnitte enthaelt: Zusammenfassung, Leistungsumfang, Zeitplan,
Preis, Naechste Schritte.
Pro Abschnitt maximal 8 Stichpunkte. Keine Floskeln.
Ende mit einer kurzen Qualitaets-Checkliste.
```

---

## Aufgabe 2: Sprachstil als Skill

```text
Erstelle `.claude/skills/language-style.md`.
Die Sprache soll Deutsch sein, klar und professionell.
Kurze Saetze. Verstaendlich fuer Entscheider ohne technisches Wissen.
Keine absoluten Aussagen wie 'garantiert' oder 'risikofrei'.
```

---

## Aufgabe 3: Eigenen Skill erfinden

Ueberlege: Was soll Claude in deiner App immer beachten?
Schreibe einen eigenen Skill-Prompt:

```text
Erstelle `.claude/skills/[dein-name].md` mit folgenden Regeln:
[beschreibe in eigenen Worten, was Claude immer tun soll]
```

Optionen zur Inspiration:

- Preisregeln: Preise immer als Schaetzung kennzeichnen
- Risikohinweise: Offene Punkte immer am Ende auflisten
- Zusammenfassung: Immer mit einem Ein-Satz-Fazit beginnen

---

## Aufgabe 4: Skills im Vergleich testen

Erstelle zuerst ein Angebot OHNE Skills:

```text
Schreibe ein Angebot fuer: Firma Mustermann, Projekt: CRM-Einfuehrung,
Budget: 50.000 Euro, Dauer: 3 Monate.
```

Dann erstelle ein Angebot MIT allen Skills:

```text
Wende alle Skills aus .claude/skills/ an und erstelle das
gleiche Angebot noch einmal.
```

Notiere den Unterschied:

```
Ohne Skills: ___________________________________
Mit Skills: ____________________________________
Groesster Unterschied: _________________________
```

---

## Done-Kriterien

- [ ] `offer-structure.md` Skill vorhanden
- [ ] `language-style.md` Skill vorhanden
- [ ] Eigener dritter Skill erstellt
- [ ] Vorher/Nachher Vergleich gemacht

## Naechstes Modul

`04-commands`: Kurzbefehle fuer haeufige Aktionen.
