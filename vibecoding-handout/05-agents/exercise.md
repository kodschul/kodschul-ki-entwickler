# Exercise: Agent-Kette bauen

## Ziel

Ihr erstellt drei Agents und nutzt sie als feste Pipeline fuer Angebotsqualitaet.

## Aufgabe 1: Agenten anlegen

Pflicht:

1. `compliance-reviewer`
2. `quality-reviewer`
3. `translator`

## Aufgabe 2: Reihenfolge testen

Pipeline:

1. generate-offer
2. quality-reviewer
3. compliance-reviewer
4. translator

## Muster-Prompts

```text
Erstelle `.claude/agents/quality-reviewer.md`.
Pruefe Struktur, Klarheit, Redundanz und Nutzenargumentation.
```

```text
Erstelle `.claude/agents/compliance-reviewer.md`.
Pruefe Datenschutz, riskante Aussagen, fehlende Ausschluesse.
```

```text
Fasse die Resultate der Agenten in einer priorisierten
Umsetzungsliste fuer die naechste Angebotsversion zusammen.
```

## Abgabe

- 3 Agent-Dateien
- 1 Pipeline-Durchlauf dokumentiert
- finale Angebotsversion mit 5 wichtigsten Verbesserungen

## Done-Kriterien

- [ ] 3 Agent-Dateien vorhanden
- [ ] klarer Scope je Agent
- [ ] dokumentierter Pipeline-Run
