# CLAUDE.md Setup

**Block:** 10:45 - 12:15 Uhr (Tag 1)

---

## Was ist CLAUDE.md?

CLAUDE.md ist dein **Brief an Claude** - du erklaerst darin, was deine App ist,
wer sie nutzt, wie sie klingen soll und was sie koennen muss.

Jedes Mal wenn Claude mit deiner App arbeitet, liest er zuerst diesen Brief.
So musst du nie wieder erklaeren, worum es geht.

```
Du startest eine neue Sitzung mit Claude
  -> Claude liest CLAUDE.md
  -> Claude kennt deine App sofort
  -> Alle Antworten passen zu deiner App
  -> Du musst nichts wiederholen
```

---

## Warum / Wann nicht?

| Warum nutzen                               | Wann nicht                                          |
| ------------------------------------------ | --------------------------------------------------- |
| Claude kennt deine App in jeder Sitzung    | Einmalige kurze Demo ohne Wiederholung              |
| Gleiches Ergebnis fuer alle Teammitglieder | Wenn du absichtlich verschiedene Stile ausprobierst |
| Kein stetiges Wiederholen von Regeln       | Wenn die App noch komplett im Fluss ist             |

---

## Was gehoert in eine gute CLAUDE.md?

### 1. Was ist deine App?

- Name und Zweck
- Wer benutzt sie?
- Was ist das wichtigste, was sie tut?

### 2. Wie soll sie sich anfuehlen?

- Sprache (Deutsch? Englisch?)
- Ton (formell? locker? technisch?)
- Stil der Texte, die sie erzeugt

### 3. Was sind die Regeln?

- Was darf die App auf keinen Fall machen?
- Was muss immer vorhanden sein?
- Grenzen und Ausnahmen

### 4. Wie sieht der Ablauf aus?

- Schritt 1: Nutzer macht ...
- Schritt 2: App zeigt ...
- Schritt 3: Nutzer kann ...

---

## Vollstaendiges Beispiel

```markdown
# Offer Studio - Beschreibung fuer Claude

## Was ist diese App?

Offer Studio hilft Vertriebsmitarbeitern dabei, schnell professionelle
Angebote zu erstellen. Der Nutzer gibt Kundendaten und Projektinfos ein,
klickt auf "Angebot erstellen" und erhaelt sofort einen fertigen Entwurf.

## Wer nutzt die App?

Vertriebsmitarbeiter, Berater und Bid-Manager. Kein technisches Vorwissen.

## Wie soll die App klingen?

- Sprache: Deutsch (Standard), Englisch auf Wunsch
- Ton: professionell, klar, fuer Entscheider verstaendlich
- Keine Floskeln, keine Versprechen ohne Grundlage

## Was muss ein Angebot immer enthalten?

1. Zusammenfassung (was bieten wir an?)
2. Leistungsumfang (was genau machen wir?)
3. Zeitplan (wann wird was geliefert?)
4. Preis (was kostet es?)
5. Naechste Schritte (was passiert jetzt?)

## Was darf nie passieren?

- Preise als Festpreise nennen, wenn sie Schaetzungen sind
- Echte Kundendaten in Beispielen verwenden
- Riskante Formulierungen ohne Hinweis uebernehmen

## Ablauf in der App

1. Nutzer fuellt Formular aus (Kunde, Scope, Budget, Timeline)
2. Klick auf "Angebot erstellen"
3. App zeigt Entwurf
4. Nutzer kann pruefen, uebersetzen oder exportieren
```

---

## So laesst du Claude die CLAUDE.md schreiben

```text
Ich baue eine App namens "Offer Studio".
Sie hilft Vertriebsmitarbeitern, Angebote zu erstellen.
Nutzer geben Kundendaten und Projektinfos ein und bekommen
einen fertigen Angebotsentwurf.
Erstelle mir eine CLAUDE.md fuer diese App.
Sie soll enthalten: App-Beschreibung, Zielgruppe, Tonalitaet,
Pflichtstruktur pro Angebot, Regeln und App-Ablauf.
```

---

## Muster-Prompts

```text
Pruefe meine CLAUDE.md auf Luecken.
Was fehlt, damit Claude meine App wirklich gut versteht?
Nenne maximal 5 konkrete Verbesserungen.
```

```text
Ich habe eine neue Idee: Nutzer sollen Angebote in Englisch
exportieren koennen. Aktualisiere die CLAUDE.md entsprechend.
```

```text
Simuliere, dass du (Claude) die CLAUDE.md gelesen hast und
erzeuge einen Angebotsentwurf fuer einen fiktiven Kunden.
```

---

## Ergebnis

Du hast eine CLAUDE.md, die Claude in jeder Sitzung sofort versteht.
Klare Regeln, konsistente Ergebnisse - ohne eine Zeile Code.

---

## Warum / Wann nicht?

| Warum nutzen                      | Wann nicht                                              |
| --------------------------------- | ------------------------------------------------------- |
| Einheitlicher Output im Team      | Sehr kurzer Einmaltest ohne Wiederverwendung            |
| Weniger Prompt-Wiederholung       | Wenn Regeln bewusst explorativ/offen bleiben sollen     |
| Schnellere Skalierung auf neue TN | Wenn kein gemeinsamer Qualitaetsstandard benoetigt wird |

---

## Bestandteile einer starken CLAUDE.md

1. Produktkontext

- App: Offer Studio
- Zielgruppe: Sales, Consulting, Bid-Team
- Input/Output klar benannt

2. Ausgabestandards

- Pflichtabschnitte je Angebot
- Tonalitaet und Sprache
- Qualitaetskriterien

3. Compliance

- Datenschutz
- Risikoaussagen
- Preisdarstellung

4. UI-Flow-Regeln

- Eingabe ueber OfferForm
- Ausgabe in OfferPreview
- Aktionen: Generate, Review, Translate, Export

---

## Vollstaendiges Muster

```markdown
# Projekt: Offer Studio

## Ziel

Diese Frontend-App erzeugt Angebotsentwuerfe aus strukturierten Formulardaten.

## Pflichtstruktur je Angebot

1. Executive Summary
2. Scope
3. Timeline
4. Pricing
5. Next Steps

## Ton und Sprache

- Deutsch standardmaessig
- Praezise, business-orientiert, C-Level verstaendlich
- Keine unbelegten Versprechen

## Compliance

- Keine echten personenbezogenen Daten in Samples
- Preise als Bandbreite oder Annahme kennzeichnen
- Riskante Aussagen markieren statt verschweigen

## UI-Flow

- Inputs kommen aus OfferForm
- Ergebnis erscheint in OfferPreview
- Aktionen: Generate, Review, Translate, Export
```

---

## Muster-Prompts

```text
Erstelle eine CLAUDE.md fuer Offer Studio mit Produktziel,
Pflichtstruktur, Compliance und UI-Flow-Regeln.
```

```text
Pruefe meine bestehende CLAUDE.md auf Luecken und schlage
maximal 8 konkrete Verbesserungen vor.
```

```text
Wende die CLAUDE.md auf sample-inputs/rfp-basic.md an
und zeige, ob alle Regeln eingehalten werden.
```

---

## Ergebnis

Nach dem Modul liefert Claude reproduzierbar Angebotsentwuerfe, die zur Frontend-App und zum Business-Kontext passen.
