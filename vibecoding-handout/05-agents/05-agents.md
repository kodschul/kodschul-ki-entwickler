# Agents

**Block:** 09:00 - 10:30 Uhr (Tag 2)

---

## Was ist ein Agent?

Ein Agent ist ein **spezialisierter Helfer** fuer eine bestimmte Aufgabe.
Waehrend ein Command einen Ablauf startet, uebernimmt ein Agent eine ganz
konkrete Teilaufgabe - zum Beispiel: Qualitaetspruefung, Uebersetzung oder Risikoanalyse.

Du beschreibst einmal, was dieser Helfer tun soll.
Claude aktiviert ihn automatisch, wenn er gebraucht wird.

```
Claude arbeitet an deiner App
  -> Erkennt, dass eine Teilaufgabe spezielles Wissen braucht
  -> Aktiviert den passenden Agent
  -> Agent prueft, analysiert oder transformiert
  -> Ergebnis fliesst zurueck in den Hauptablauf
```

**Pfad:** `.claude/agents/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                                            | Wann nicht                           |
| ------------------------------------------------------- | ------------------------------------ |
| Komplexe Aufgaben mit einem Helfer sauber trennen       | Sehr einfacher Einzelschritt reicht  |
| Verschiedene Rollen simulieren (Pruefung, Uebersetzung) | Wenn ein Command schon alles abdeckt |
| Bessere Qualitaet durch fokussierte Analyse             | Zu viele Agents ohne klare Grenzen   |

---

## Agent vs Skill vs Command

|            | Skill                 | Command             | Agent                         |
| ---------- | --------------------- | ------------------- | ----------------------------- |
| Was es ist | Regeln im Hintergrund | Ablauf per Befehl   | Spezialisierter Helfer        |
| Du machst  | Nichts extra          | Tippst einen Befehl | Bittest Claude um die Aufgabe |
| Beispiel   | Stil und Format       | Angebot erstellen   | Angebot auf Risiken pruefen   |

---

## So beschreibst du einen Agent - kein Code noetig

Du erklaerst Claude:

- Welche Rolle hat dieser Helfer?
- Auf was soll er besonders achten?
- Wie soll seine Ausgabe aussehen?

```text
Erstelle `.claude/agents/quality-reviewer.md`.
Dieser Helfer soll Angebotsentwuerfe auf Qualitaet pruefen.
Er soll checken: Ist alles klar formuliert? Ist der Nutzen
fuer den Kunden sichtbar? Kann ein Entscheider es in 5 Minuten lesen?
Ergebnis: Liste mit maximal 10 konkreten Verbesserungen, priorisiert.
```

Claude schreibt die Agent-Datei. Du pruefst und ergaenzt.

---

## Vollstaendige Beispiele

**`.claude/agents/quality-reviewer.md`**

```markdown
---
name: quality-reviewer
description: Prueft Angebote auf Verstaendlichkeit, Struktur und Ueberzeugungskraft.
tools:
  - Read
---

# Quality Reviewer

Pruefe den Angebotsentwurf auf:

- Sind alle 5 Abschnitte vorhanden und vollstaendig?
- Ist der Nutzen fuer den Kunden klar sichtbar?
- Gibt es doppelte oder unklare Aussagen?
- Kann ein Entscheider es in 5 Minuten lesen?

Ausgabe: Top 10 Verbesserungen, priorisiert nach Wichtigkeit.
```

**`.claude/agents/translator.md`**

```markdown
---
name: translator
description: Uebersetzt Angebote von Deutsch nach Englisch.
tools:
  - Read
---

# Translator

Uebersetze den Angebotsentwurf von Deutsch nach Englisch.
Behalte die Struktur bei.
Passe idiomatische Ausdruecke an britisches Business-Englisch an.
```

**`.claude/agents/risk-checker.md`**

```markdown
---
name: risk-checker
description: Prueft Angebote auf riskante Aussagen und fehlende Einschraenkungen.
tools:
  - Read
---

# Risk Checker

Pruefe den Angebotsentwurf auf:

- Riskante oder rechtlich problematische Formulierungen
- Fehlende Annahmen oder Ausschluesse
- Preise, die nicht als Schaetzungen gekennzeichnet sind

Ausgabe als Tabelle: | Stelle | Risiko | Empfehlung |
```

---

## Muster-Prompts

```text
Erstelle `.claude/agents/quality-reviewer.md`.
Dieser Helfer prueft Angebote auf Klarheit, Vollstaendigkeit
und Verstaendlichkeit. Ausgabe: Top 10 priorisierte Verbesserungen.
```

```text
Erstelle `.claude/agents/translator.md` fuer Deutsch -> Englisch.
Struktur beibehalten, Business-Englisch, keine wortwoertliche Uebersetzung.
```

```text
Lass zuerst quality-reviewer, dann risk-checker ueber das Angebot laufen.
Fasse beide Ergebnisse in einer gemeinsamen To-do Liste zusammen.
```

---

## Ergebnis

Deine App hat jetzt spezialisierte Helfer fuer Qualitaet, Uebersetzung und Risiken.
Du aktivierst sie mit einem Satz - kein technisches Wissen noetig.

---

## Warum / Wann nicht?

| Warum nutzen                                                          | Wann nicht                                   |
| --------------------------------------------------------------------- | -------------------------------------------- |
| Komplexe Teilaufgaben sauber trennen                                  | Sehr einfacher Einzelschritt                 |
| Unterschiedliche Rollen simulieren (Compliance, Quality, Translation) | Wenn ein Command ohne Spezialisierung reicht |
| Bessere Qualitaet durch fokussierte Pruefung                          | Zu viele Agents ohne klare Grenzen           |

---

## Vergleich: Skill vs Command vs Agent

|                   | Skill           | Command                | Agent                           |
| ----------------- | --------------- | ---------------------- | ------------------------------- |
| Fokus             | Regeln          | Ablauf                 | Spezialisierte Aufgabe          |
| Typischer Einsatz | Format und Stil | Ausfuehrbarer Workflow | Review, Bewertung, Uebersetzung |
| Granularitaet     | breit           | mittel                 | eng und fokussiert              |

---

## Aufbau - Vollstaendiges Beispiel

**`.claude/agents/compliance-reviewer.md`**

```markdown
---
name: compliance-reviewer
description: Prueft Angebotsentwuerfe auf Compliance-Risiken und riskante Aussagen.
tools:
	- Read
---

# Compliance Reviewer

Pruefe den Angebotsentwurf auf:

- Datenschutzrisiken
- unklare oder rechtlich riskante Formulierungen
- fehlende Annahmen / Ausschluesse

Ausgabeformat:
| Thema | Risiko | Schwere | Empfehlung |
```

**`.claude/agents/quality-reviewer.md`**

```markdown
---
name: quality-reviewer
description: Verbessert Lesbarkeit, Struktur und Ueberzeugungskraft fuer C-Level.
tools:
	- Read
---

# Quality Reviewer

Lieferung:

- Top 10 Verbesserungen
- priorisierte Reihenfolge
- kurze begruendete Hinweise
```

---

## Muster-Prompts

```text
Erstelle `.claude/agents/compliance-reviewer.md` fuer Offer Studio.
Nutze eine tabellarische Risikoausgabe.
```

```text
Erstelle `.claude/agents/translator.md` fuer DE->EN Uebersetzung
mit Erhalt der Angebotsstruktur.
```

```text
Lass erst quality-reviewer, dann compliance-reviewer laufen
und kombiniere beide Ergebnisse in einer finalen To-do Liste.
```

---

## Ergebnis

Angebote werden deutlich robuster: fachlich klar, compliance-sicher und besser lesbar.
