# Specs

**Block:** 09:00 - 10:30 Uhr (Tag 2)

---

## Was ist eine Spec?

Eine Spec ist eine **verstaendliche Beschreibung**, was deine App koennen soll.
Kein Fachvokabular. Keine Diagramme. Nur Geschichten aus der Nutzerperspektive.

Format: "Als [Person] moechte ich [Ziel], damit [Grund]."

```
Du beschreibst, was Nutzer mit der App machen sollen
  -> Claude versteht die genaue Anforderung
  -> Umsetzung folgt der Beschreibung
  -> Keine Missverstaendnisse zwischen dir und Claude
  -> Ergebnis entspricht dem, was du wirklich wolltest
```

**Pfad:** `.claude/specs/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                           | Wann nicht                                   |
| -------------------------------------- | -------------------------------------------- |
| Claude weiss genau, was du meinst      | Sehr kleine Demo ohne Teamabstimmung         |
| Missverstaendnisse vermeiden           | Wenn die App noch im Experimentier-Modus ist |
| Gute Grundlage fuer Qualitaetspruefung | Einmalige Ideensammlung ohne Umsetzung       |

---

## Aufbau einer Spec - ohne Fachkenntnisse

Ein Spec-Dokument hat:

**1. User Stories** - Geschichten aus Nutzerperspektive:

```
Als Vertriebsmitarbeiter moechte ich schnell ein Angebot erstellen,
damit ich dem Kunden sofort antworten kann.
```

**2. Akzeptanzkriterien** - Wann ist es fertig?

```
- Wenn ich auf "Angebot erstellen" klicke und alle Felder ausgefuellt sind,
  erhalte ich einen fertigen Entwurf.
- Wenn ein Pflichtfeld leer ist, sehe ich eine verstaendliche Fehlermeldung.
```

**3. Was nicht dazugehoert** - Grenzen setzen:

```
Nicht Teil dieser Version: Automatisches Versenden per E-Mail.
```

---

## Vollstaendiges Beispiel

**`.claude/specs/offer-flow-spec.md`**

```markdown
# Spec: Offer Studio - Was die App koennen soll

## Geschichte 1: Angebot erstellen

Als Vertriebsmitarbeiter moechte ich aus meinen Eingaben einen
Angebotsentwurf erstellen, damit ich schnell eine erste Version habe.

### Wann ist es fertig?

- Wenn ich alle Felder ausgefuellt und auf "Angebot erstellen" geklickt habe,
  erhalte ich einen vollstaendigen Entwurf mit 5 Abschnitten.
- Wenn das Budget-Feld leer ist, erscheint die Meldung
  "Bitte gib ein Budget an".

### Was gehoert nicht dazu?

- Automatisches Versenden des Angebots per E-Mail.

## Geschichte 2: Angebot pruefen lassen

Als Reviewer moechte ich potenzielle Probleme im Entwurf sehen,
damit ich ihn sicher freigeben kann.

### Wann ist es fertig?

- Nach dem Review sehe ich eine Liste konkreter Verbesserungen.
- Riskante Aussagen sind direkt im Text markiert.

## Geschichte 3: Angebot uebersetzen

Als Vertriebsmitarbeiter moechte ich eine englische Version,
damit internationale Kunden das Angebot lesen koennen.

### Wann ist es fertig?

- Ein Klick auf "Englisch" erzeugt die uebersetzte Version.
- Struktur und Abschnitte bleiben erhalten.
```

---

## So laesst du Claude die Spec schreiben

```text
Erstelle `.claude/specs/offer-flow-spec.md` fuer Offer Studio.
Schreibe 3 User Stories: Angebot erstellen, Angebot pruefen, Angebot uebersetzen.
Jede Story braucht: Nutzerperspektive, Akzeptanzkriterien (mindestens 2),
einen Negativfall und was nicht Teil dieser Version ist.
```

---

## Muster-Prompts

```text
Schreibe eine Spec fuer meine App in verstaendlicher Sprache.
Keine technischen Begriffe. Drei User Stories. Klare Kriterien.
```

```text
Pruefe meine Spec auf Widersprueche und Unklarheiten.
Nenne maximal 5 Stellen, die zu Missverstaendnissen fuehren koennten.
```

```text
Fuege in jede User Story einen 'Out of Scope' Abschnitt ein,
damit klar ist, was NICHT gebaut werden soll.
```

---

## Ergebnis

Du hast eine klare Beschreibung, was deine App kann - und was nicht.
Claude baut genau das, was du beschrieben hast.

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
