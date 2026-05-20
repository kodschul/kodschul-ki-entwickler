# Specs

**Block:** 09:00 - 10:30 Uhr (Tag 2)

---

## Wie funktioniert das unter der Haube?

```
Produktziel wird in Stories zerlegt
	-> jede Story bekommt Akzeptanzkriterien
	-> Kriterien steuern Implementierung und Review
	-> weniger Missverstaendnisse im Team
```

Specs sind die **verbindliche Uebersetzung von Idee zu umsetzbaren Anforderungen**.

**Pfad:** `.claude/specs/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                          | Wann nicht                             |
| ------------------------------------- | -------------------------------------- |
| Klare Anforderungen fuer alle TN      | Sehr kleine Demo ohne Teamabstimmung   |
| Messbare Akzeptanz statt Bauchgefuehl | Wenn Scope noch komplett unklar ist    |
| Gute Basis fuer Review und Test       | Einmalige Ideensammlung ohne Umsetzung |

---

## Aufbau - Vollstaendiges Beispiel

**`.claude/specs/offer-flow-spec.md`**

```markdown
# Spec: Offer Studio Flow

## User Story 1

Als Sales-Mitarbeiter moechte ich aus Formulardaten einen Angebotsentwurf erzeugen,
damit ich schneller eine belastbare Erstversion habe.

### Akzeptanzkriterien

- Given gueltige Eingabedaten, when ich auf Generate klicke,
  then erhalte ich alle 5 Pflichtabschnitte.
- Given fehlendes Budget, when Generate ausgefuehrt wird,
  then wird eine klare Fehlermeldung gezeigt.

## User Story 2

Als Reviewer moechte ich Risiken und Unklarheiten markiert sehen,
damit ich den Entwurf sicher freigeben kann.

## User Story 3

Als Bid-Team moechte ich eine EN-Version,
damit internationale Stakeholder direkt lesen koennen.
```

---

## Muster-Prompts

```text
Erstelle `.claude/specs/offer-flow-spec.md` mit 3 User Stories,
Given/When/Then-Kriterien und 2 Negativfaellen.
```

```text
Ergaenze fuer jede Story einen "Out of Scope" Abschnitt,
damit der Umfang klar begrenzt ist.
```

```text
Pruefe die Spec auf widerspruechliche Anforderungen und schlage
konkrete Korrekturen vor.
```

---

## Ergebnis

Entwicklung, Review und Demo laufen auf der gleichen Erwartungsbasis.
