# Agents

**Block:** 09:00 - 10:30 Uhr (Tag 2, zusammen mit Specs)

---

## Wie funktioniert das unter der Haube?

```
Claude bekommt Aufgabe
	-> waehlt passenden Agent nach Beschreibung
	-> Agent arbeitet mit eigenem Prompt und ggf. Tool-Restriktionen
	-> Agent liefert Teilresultat zuruueck
	-> Hauptflow setzt Ergebnis zusammen
```

Ein Agent ist ein **spezialisierter Subprozess** fuer klar abgegrenzte Aufgaben.

**Pfad:** `.claude/agents/<name>.md`

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
