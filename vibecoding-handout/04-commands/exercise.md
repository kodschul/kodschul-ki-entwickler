# Exercise: Commands - Kurzbefehle anlegen

## Ziel

Du erstellst zwei Commands durch einfache Beschreibungen.
Danach kannst du mit einem kurzen Wort komplette Ablaeufe starten.

---

## Aufgabe 1: Generate-Command anlegen

Schreibe:

```text
Erstelle `.claude/commands/generate-offer.md`.
Wenn ich /generate-offer aufrufe, soll Claude:
- Pruefen ob Kundenname, Scope, Budget und Zeitraum angegeben sind.
- Falls etwas fehlt: kurze freundliche Fehlermeldung.
- Falls alles da: vollstaendigen Angebotsentwurf erstellen.
- Angebotsstruktur aus den Skills verwenden.
- Am Ende: offene Annahmen in einer kurzen Liste ausgeben.
```

---

## Aufgabe 2: Review-Command anlegen

```text
Erstelle `.claude/commands/review-offer.md`.
Wenn ich /review-offer aufrufe, soll Claude:
- Den vorhandenen Angebotsentwurf auf Vollstaendigkeit pruefen.
- Unklare oder riskante Aussagen direkt im Text markieren.
- Maximal 10 konkrete Verbesserungsvorschlaege nennen.
- Eine priorisierte To-do Liste ausgeben.
```

---

## Aufgabe 3: Eigenen Command erfinden

Ueberlege: Welche Aktion moechtest du mit einem Wort starten?

```text
Erstelle `.claude/commands/[dein-name].md`.
Wenn ich /[dein-name] aufrufe, soll Claude:
[beschreibe in eigenen Worten, was passieren soll]
```

Beispiele zur Inspiration:

- `/uebersetzung`: Angebot auf Englisch uebersetzen
- `/zusammenfassung`: Ein-Satz-Zusammenfassung erstellen
- `/risikocheck`: Riskante Stellen im Angebot markieren

---

## Aufgabe 4: End-to-End Test

Fuehre beide Commands nacheinander aus:

```text
Fuehre /generate-offer aus fuer: Kunde Mustermann GmbH,
Projekt: neue Website, Budget: ca. 15.000 Euro, Zeitraum: 2 Monate.
```

Dann:

```text
Fuehre /review-offer auf dem gerade erstellten Angebot aus.
```

Notiere was sich verbessert hat:

```
Vorher: _______________________________________
Nachher: ______________________________________
```

---

## Done-Kriterien

- [ ] `generate-offer.md` Command vorhanden
- [ ] `review-offer.md` Command vorhanden
- [ ] Eigener Command erstellt
- [ ] End-to-End Test durchgefuehrt

## Naechstes Modul

`05-agents`: Spezialisierte Helfer fuer Pruefung und Qualitaet.
