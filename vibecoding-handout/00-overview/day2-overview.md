# Day 2 - Overview: Browser-App mit Claude Code bauen

Schulungszeit: 09:00 - 17:00 Uhr

## Ziel von Tag 2

Am Ende von Tag 2 hat jede Person eine eigene browserbasierte App (HTML, CSS, JavaScript), die ohne Admin-Rechte laeuft und einen echten AI-Flow nutzt:

1. Eingabe im Formular
2. Validierung im Frontend
3. Generierung ueber Trainer-API
4. Strukturierte Ausgabe im UI
5. Optionaler Export (TXT + Copy)

Merksatz fuer Tag 2:
"Ihr baut das Produktverhalten. Die API-Verkabelung ist ein vorbereiteter Baustein."

---

## Rahmenbedingungen

- Kein npm install als Voraussetzung
- Kein lokales Backend pro TN
- Kein API-Key im Frontend-Code
- Browser only: index.html, styles.css, app.js
- Real API statt Mock (Mock nur als Fallback)

Empfohlene Konfiguration in app.js:

```javascript
const API_BASE_URL = window.API_BASE_URL || "https://YOUR-TRAINER-ENDPOINT";
const APP_TOKEN = window.APP_TOKEN || "";
```

---

## Was wir an Tag 2 machen

### Block A (09:00 - 10:30): UI und Grundstruktur

- Offer-Studio App-Struktur erstellen
- Formularfelder aufbauen
- Ergebnisbereich und Kartenlayout einrichten
- Event-Handling verbinden

Ergebnis:
- Laufende Browser-App mit sichtbarem Kern-Flow

### Block B (10:45 - 12:15): Validierung und AI-Generierung

- Pflichtfelder und Fehlermeldungen implementieren
- Prompt-Template aus Eingaben bauen
- POST auf /generate-offer integrieren
- Loading, Error-State und Retry einbauen
- Ausgabe in Abschnitte mappen

Ergebnis:
- End-to-End Flow: Eingabe -> API -> strukturierter Angebotsentwurf

### Block C (13:15 - 15:00): Eigener Use-Case

- Eigene App-Idee in 2-3 Saetzen definieren
- Formular und Felder an Use-Case anpassen
- Prompt-Template und API-Call auf Use-Case uebertragen
- Ersten produktnahen Durchlauf testen

Ergebnis:
- Individuelle App-Version pro Person

### Block D (15:15 - 17:00): Finalisierung und Demo

- Pflichtfeatures abschliessen
- Fehlerfaelle testen
- Optional Export hinzufuegen
- 2-Minuten Demo vorbereiten

Ergebnis:
- Vorzeigbare Browser-App pro Person

---

## Rollenlogik passend zum Tag-2-Ziel

### Spec: Was soll gebaut werden?

Zweck:
- Definiert fachliche Anforderungen und Akzeptanzkriterien fuer die Browser-App.

Tag-2 Fokus:
- Formular + Validierung + Generierung + strukturierte Ausgabe + optional Export.

Beispiel:
- "Als Vertrieb moechte ich aus 5 Eingaben einen belastbaren Angebotsentwurf in 5 Abschnitten erzeugen."

### Skill: Welche Regeln gelten immer?

Zweck:
- Haltet Ausgaben stilistisch und fachlich konsistent.

Tag-2 Fokus:
- Klarer Angebotsstil, transparente Annahmen, keine absoluten Versprechen.

Beispiel:
- "Preis immer als Schaetzung markieren und offene Risiken benennen."

### Command: Welcher Ablauf startet auf Zuruf?

Zweck:
- Wiederholbare Schritte als kurz ausfuehrbarer Workflow.

Tag-2 Fokus:
- Validieren -> Prompt bauen -> API aufrufen -> Ergebnis rendern.

Beispiel:
- "/generate-offer" startet den kompletten Generierungsflow.

### Agent: Wer prueft spezialisiert?

Zweck:
- Uebernimmt fokussierte Qualitaetspruefungen.

Tag-2 Fokus:
- Review auf Risiken, Widersprueche, unklare Aussagen und fehlende Annahmen.

Beispiel:
- "risk-checker" markiert kritische Formulierungen und liefert konkrete Verbesserungsvorschlaege.

---

## Zielstruktur fuer Day 2

```text
offer-studio/
  index.html
  styles.css
  app.js
  data/
    prompts.json                (optional)
  outputs/
    sample-past-offer.md        (Lernbeispiel)
  .claude/
    skills/
      offer-style.md
      pricing-guardrails.md
    commands/
      generate-offer.md
      export-offer.md
    agents/
      risk-checker.md
      tone-checker.md
    specs/
      browser-offer-flow.md
      acceptance-day2.md
```

---

## Pflichtfeatures (Minimum Scope)

- Muss:
  - Formular mit den Kernfeldern
  - Frontend-Validierung mit klaren Fehlermeldungen
  - Real API-Call an Trainer-Endpoint
  - Strukturierte Ergebnisdarstellung
- Soll:
  - Retry bei Fehlern
  - Export als TXT und Copy-to-Clipboard
  - Responsives Layout
- Kann:
  - Mock-Fallback
  - Caching letzter erfolgreicher Antworten
  - Review-Agent als zusaetzlicher Schritt

---

## Ergebnis am Tagesende

Jede Person zeigt eine eigene lauffaehige Browser-App mit:

1. Problemkontext
2. Eingabeformular
3. AI-Generierung
4. Ergebnisqualitaet
5. kurzer Demo-Story
