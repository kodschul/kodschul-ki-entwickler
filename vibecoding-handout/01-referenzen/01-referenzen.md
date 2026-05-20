# Referenzen

**Block:** 09:00 - 10:30 Uhr

---

## Wie funktioniert das unter der Haube?

```
TN formuliert Business-Ziel
	-> Claude erzeugt Projektstruktur
	-> Kontextdateien lenken das Verhalten
	-> UI + Angebotslogik wachsen iterativ
```

In diesem Modul setzen wir das Fundament fuer alle spaeteren Module.

---

## Zentrale Referenzen fuer TN

- `CLAUDE.md`: Produktregeln und Tonalitaet
- `.claude/skills/`: Wiederverwendbare Regeln
- `.claude/commands/`: Slash-Workflows
- `.claude/agents/`: Spezialrollen fuer Pruefung/Transformation
- `.claude/specs/`: Anforderungen und Akzeptanzkriterien
- `.claude/hooks/`: Automatische Folgeaktionen

---

## Warum / Wann nicht?

| Warum nutzen                             | Wann nicht                                   |
| ---------------------------------------- | -------------------------------------------- |
| Klarer Einstieg ohne Chaos               | Wenn nur eine Einmal-Demo geplant ist        |
| Gemeinsames Begriffsverstaendnis im Kurs | Wenn keine Teamarbeit stattfindet            |
| Grundlage fuer spaetere Module           | Wenn Scope des Workshops stark reduziert ist |

---

## Muster-Prompts

```text
Erstelle ein Frontend-Grundgeruest fuer "Offer Studio".
Seiten: OfferForm, OfferPreview, Settings.
Komponenten: ClientSection, ScopeSection, PricingSection, GenerateButton.
```

```text
Nutze die Eingaben aus dem OfferForm und erzeuge einen Angebotsentwurf.
Struktur: Executive Summary, Scope, Timeline, Pricing, Next Steps.
```

```text
Erklaere die Rolle von CLAUDE.md, Skills, Commands, Agents, Specs und Hooks
anhand eines einzigen Generate-Workflows.
```

---

## Mini-Referenz: Dateibaum

```text
offer-studio/
	CLAUDE.md
	.claude/
		skills/
		commands/
		agents/
		specs/
		hooks/
	frontend/
		src/
			pages/
			components/
			services/
```

---

## Ergebnis

TN verstehen den Gesamtzusammenhang und koennen die Module 02-08 zielgerichtet umsetzen.

Naechstes Modul: `02-claude.md-setup`.
