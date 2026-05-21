# Exercise: Agents - Spezialisierte Helfer anlegen

## Ziel

Du erstellst Agents durch einfache Beschreibungen.
Claude schreibt den Inhalt. Du kombinierst die Helfer zu einer Qualitaets-Pipeline.

---

## Aufgabe 1: Quality Reviewer anlegen

```text
Erstelle `.claude/agents/quality-reviewer.md`.
Dieser Helfer soll Angebotsentwuerfe auf folgende Punkte pruefen:
- Sind alle 5 Abschnitte vorhanden?
- Ist der Nutzen fuer den Kunden klar?
- Gibt es unklare oder doppelte Aussagen?
- Ist der Text in 5 Minuten lesbar?
Ausgabe: maximal 10 priorisierte Verbesserungsvorschlaege.
```

---

## Aufgabe 2: Risk Checker anlegen

```text
Erstelle `.claude/agents/risk-checker.md`.
Dieser Helfer prueft Angebotsentwuerfe auf:
- Riskante oder problematische Formulierungen
- Preise, die nicht als Schaetzungen erkennbar sind
- Fehlende Einschraenkungen oder Annahmen
Ausgabe als Tabelle: Stelle, Risiko, Empfehlung.
```

---

## Aufgabe 3: Translator anlegen

```text
Erstelle `.claude/agents/translator.md`.
Dieser Helfer uebersetzt Angebote von Deutsch nach Englisch.
Struktur beibehalten. Business-Englisch. Keine wortwoertliche Uebersetzung.
```

---

## Aufgabe 4: Agents in der Praxis

Erstelle ein Angebot und fuehre danach die Agents nacheinander aus:

```text
Erstelle ein Angebot fuer: Kunde: Mustermann GmbH,
Projekt: Online-Shop-Relaunch, Budget: 30.000 Euro, Zeitraum: 4 Monate.
```

Dann:

```text
Lass quality-reviewer und risk-checker ueber das Angebot laufen.
Fasse alle Hinweise in einer gemeinsamen To-do Liste zusammen.
```

Notiere:

```
Quality Reviewer fand: _________________________________
Risk Checker fand: _____________________________________
Groeßte Verbesserung: __________________________________
```

---

## Done-Kriterien

- [ ] `quality-reviewer.md` Agent vorhanden
- [ ] `risk-checker.md` Agent vorhanden
- [ ] `translator.md` Agent vorhanden
- [ ] Agents auf einem Angebot getestet

## Naechstes Modul

`06-specs`: Anforderungen in verstaendlichen Geschichten beschreiben.
