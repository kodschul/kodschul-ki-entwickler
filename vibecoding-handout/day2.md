# Tag 2 - Browser-App bauen mit Claude Code (Offer Studio)

## Ueberblick zuerst (fuer deine Validierung)

Empfohlene Reihenfolge fuer den Einstieg in Tag 2:

1. Input-Phase bis 12:15: Ueberblick, Rollenlogik, gemeinsames Demo-Beispiel
2. Transfer-Phase ab 13:15: Jede Person waehlt einen eigenen Use-Case und baut die eigene App
3. Glossar nur als Referenz bei Bedarf (nicht als langer Frontalteil)
4. Hands-on Bloecke A bis D mit klarem Wechsel von Input zu Eigenbau

Validierungscheck vor Start:

- Ist das Lernziel klar: browserbasierte Offer-Studio App mit HTML/CSS/JS?
- Ist die Rollenlogik klar: Skill vs Command vs Agent vs Spec?
- Sind die Pflichtfeatures klar: Formular, Validierung, Generierung, Export?
- Ist No-Admin/No-Download fuer alle Aufgaben eingehalten?
- Ist der Uebergang klar: bis 12:15 Input, ab 13:15 individuelle Umsetzung?

---

## Ziel von Tag 2

- Die TN bauen mit Claude Code eine browserbasierte App (HTML, CSS, JavaScript) am Beispiel Offer Studio.
- Wir arbeiten unter realistischen Rahmenbedingungen: keine Admin-Rechte, idealerweise keine Downloads.
- Ergebnis am Ende: Eine lauffaehige Frontend-App im Browser mit Formular, AI-Generierung, Review-Ansicht und Export.

## Vibe-Coding Prinzip: TN muessen API-Details nicht kennen

Wichtig fuer den Kurs:

- Die TN sollen nicht API-Architektur lernen, sondern Apps bauen.
- Technische Komplexitaet wird durch einen vorbereiteten API-Baustein gekapselt.
- Die TN arbeiten mit Copy/Paste + Prompting, nicht mit Infrastruktur-Setup.

Was der Trainer vorbereitet:

1. Einen funktionierenden Endpoint (z.B. /generate-offer).
2. Einen kurzen Snippet-Block fuer app.js (Funktion generateOfferViaApi).
3. Einen Test-Request zum schnellen Verifizieren.
4. Eine Fallback-Option (Mock), falls das Netz ausfaellt.

Was die TN wirklich tun:

1. Formular bauen.
2. Button mit einer vorhandenen Funktion verbinden.
3. Ergebnis im UI anzeigen.
4. Prompt und UI verbessern.

Merksatz fuer die Gruppe:
- "Ihr baut das Produktverhalten. Die API-Verkabelung ist ein vorbereiteter Baustein."

---

## Rahmenbedingungen (ohne Admin / ohne Download)

- Kein lokales Setup erzwingen (kein npm install, kein globales Tooling voraussetzen).
- Fokus auf Browser-Assets und einfache Projektstruktur:
  - index.html
  - styles.css
  - app.js
  - data/prompts.json (optional)
  - assets/ (optional)
- Claude Code erstellt und aendert diese Dateien direkt per Prompt.
- Ausfuehrung lokal im Browser (Datei oeffnen) oder in vorhandener Web-Vorschau.

### Real API ist Pflicht: so klappt es trotz No-Admin

- Die Browser-App ruft eine bereits bereitgestellte HTTPS-API auf (Trainer-Endpoint).
- Der Endpoint uebernimmt den Call zum AI-Provider.
- API-Keys liegen nicht im Frontend-Code.
- Jede Person nutzt nur:
  - API_BASE_URL
  - optional APP_TOKEN (kurzlebig, kursbezogen)

Warum dieses Muster:
- Kein lokaler Server notwendig.
- Kein Paket-Setup bei TN.
- Echter AI-Output statt Mock.

Empfohlener Request-Flow:

1. Browser sendet POST an den Trainer-Endpoint.
2. Endpoint validiert Input und Token.
3. Endpoint ruft AI-Provider auf.
4. Endpoint sendet strukturierten Output zurueck.

### Zero-Technical Setup (fuer TN)

Nur diese 2 Zeilen werden angepasst:

```javascript
const API_BASE_URL = "https://YOUR-TRAINER-ENDPOINT";
const APP_TOKEN = "OPTIONAL_SHORT_LIVED_TOKEN";
```

Danach gilt fuer TN:

- Kein eigenes Backend bauen.
- Keine Provider-Doku lesen.
- Keine Key-Verwaltung im Code lernen.
- Fokus nur auf UI, Prompt, User Flow und Ergebnisqualitaet.

---

## Schulungs-Demo: Skills, Commands, Agents, Specs (Offer Studio)

Demo-Use-Case in einem Satz:
- In der Schulung zeigen wir an Offer Studio, wie Skills, Commands, Agents und Specs zusammen eine AI-gestuetzte Browser-App steuern.

Wichtig:
- Dieser Abschnitt ist die gemeinsame Trainer-Demo bis 12:15.
- Ab 13:15 uebertragen die TN das Muster auf ihren eigenen Use-Case.

So zeigst du die 4 Konzepte konkret:

- Spec (Was soll gebaut werden?)
  - Definiert die fachlichen Anforderungen.
  - Beispiel: "Als Vertrieb moechte ich aus 5 Eingaben einen Entwurf in 5 Abschnitten erzeugen."

- Skill (Welche Qualitaetsregeln gelten immer?)
  - Erzwingt Stil und Struktur in jeder Ausgabe.
  - Beispiel: "Preis immer als Schaetzung markieren, keine absoluten Versprechen."

- Command (Welcher Ablauf startet auf Zuruf?)
  - Startet wiederkehrende Schritte reproduzierbar.
  - Beispiel: "/generate-offer" validiert Eingaben, baut Prompt, erzeugt Entwurf, zeigt offene Annahmen.

- Agent (Wer prueft spezialisiertes Thema?)
  - Uebernimmt fokussierte Teilpruefung.
  - Beispiel: "risk-checker" markiert riskante Formulierungen und gibt Verbesserungsvorschlaege.

Schulungs-Demo Ablauf (15 Minuten):

1. Zeige eine kurze Spec mit 2 Akzeptanzkriterien.
2. Zeige einen Skill fuer Angebotsstil.
3. Starte den Command-Flow fuer Generierung.
4. Lasse den Agenten den Entwurf pruefen.
5. Uebernehme 2-3 Empfehlungen live und zeige den verbesserten Output.

---

## Glossar fuer Tag 2

- Browser-App: Anwendung, die komplett im Browser mit HTML, CSS und JavaScript laeuft.
- UI-Komponente: Sichtbarer Baustein wie Formular, Ergebnis-Karte oder Modal.
- State: Aktueller Zustand der App (z.B. Formulardaten, generiertes Angebot, Fehler).
- Event-Handler: JavaScript-Funktion, die auf Nutzeraktionen reagiert (z.B. Button-Klick).
- Prompt-Template: Textvorlage, die aus Formulardaten den AI-Input erstellt.
- Mock-AI: Simulierter AI-Output fuer Unterricht ohne externe API.
- Validation: Pruefung, ob Eingaben vollstaendig und plausibel sind.
- Fallback: Verhalten, wenn AI/API nicht verfuegbar ist.
- Export: Ausgabe als kopierbarer Text oder Download-Datei.
- Offer Studio: Unser durchgehendes Lernbeispiel fuer AI-gestuetzte Angebotserstellung.
- Akzeptanzkriterium: Messbare Bedingung, wann etwas als fertig gilt.
- Risikohinweis: Stelle im Angebot, die fachlich oder rechtlich praezisiert werden sollte.
- Annahme: Explizite Unterstellung, weil Information fehlt (muss sichtbar gemacht werden).

---

## Zusammenfassung: Wichtige Claude-Code Prompts fuer HTML, CSS, JavaScript

Hinweis: Die TN koennen diese Prompt-Bausteine direkt in Claude Code verwenden.

- Projektgrundlage erstellen
  - "Erstelle eine einfache Browser-App fuer Offer Studio mit index.html, styles.css und app.js. Nutze nur Vanilla JavaScript."

- UI aufbauen
  - "Baue ein Formular mit den Feldern Kundenname, Firma, Projektbeschreibung, Budget und Lieferzeit. Fuege einen Button Angebot erstellen hinzu."

- Logik verbinden
  - "Verbinde das Formular mit JavaScript. Bei Klick soll aus den Eingaben ein strukturierter Angebotsentwurf erzeugt und im Ergebnisbereich angezeigt werden."

- Validierung einfuegen
  - "Pruefe Pflichtfelder. Zeige klare Fehlermeldungen direkt unter den betroffenen Feldern."

- AI-Simulation integrieren
  - "Erzeuge eine Funktion simulateAIOffer(input), die einen realistischen Angebotsentwurf als Textblock zurueckgibt."

- Real API integrieren
  - "Ersetze die Simulation durch fetch auf ${API_BASE_URL}/generate-offer (POST JSON). Zeige Loading, Error-Handling und Retry-Button."

- Export ergaenzen
  - "Fuege einen Export-Button hinzu. Exportiere das Ergebnis als Textdatei und biete alternativ Copy-to-Clipboard an."

- Styling verbessern
  - "Gestalte die App modern, responsiv und klar lesbar. Nutze CSS-Variablen, Kartenlayout und mobile Breakpoints."

- Debug prompten
  - "Analysiere den Fehler im aktuellen JavaScript, erklaere kurz die Ursache und liefere nur die noetige minimale Korrektur."

### Minimalbeispiel fuer echten API-Call (Frontend)

```javascript
const API_BASE_URL = window.API_BASE_URL || "https://YOUR-TRAINER-ENDPOINT";
const APP_TOKEN = window.APP_TOKEN || "";

async function generateOfferViaApi(input) {
  const response = await fetch(`${API_BASE_URL}/generate-offer`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...(APP_TOKEN ? { "Authorization": `Bearer ${APP_TOKEN}` } : {})
    },
    body: JSON.stringify({ input })
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`API error ${response.status}: ${errText}`);
  }

  const data = await response.json();
  return data.offer;
}
```

Erwartetes Antwortformat des Endpoints:

```json
{
  "offer": {
    "summary": "...",
    "scope": ["..."],
    "timeline": ["..."],
    "price": ["..."],
    "nextSteps": ["..."],
    "assumptions": ["..."]
  }
}
```

---

## Day-2 Hands-on: Offer Studio als Browser-App bauen

### Block A (09:00 - 10:30): UI und Grundstruktur bauen

Ziel:
- Die TN haben eine laufende HTML/CSS/JS App-Struktur und ein funktionierendes Formular.

Format:
- Input und Live-Demo (Trainer fuehrt, TN folgen)

Hands-on Schritte:
1. Dateien anlegen lassen: index.html, styles.css, app.js.
2. Formular und Ergebnisbereich in HTML erzeugen.
3. Basislayout und responsive Verhalten in CSS umsetzen.
4. Event-Handling in JavaScript verdrahten.

Beispielprompt:
"Erstelle eine browserbasierte Offer-Studio App mit index.html, styles.css, app.js.
Formularfelder: Kundenname, Firma, Projektbeschreibung, Budget, Lieferzeit.
Nach Klick auf Angebot erstellen soll ein Ergebnis-Panel sichtbar werden."

---

### Block B (10:45 - 12:15): AI-Generierung und Validierung

Ziel:
- Durchgaengiger Ablauf im Browser: Eingabe -> Validierung -> Entwurf.

Format:
- Input und Guided Practice (Trainer gibt Schritte, TN setzen direkt um)

Hands-on Schritte:
1. Pflichtfeld-Validierung umsetzen (inkl. nutzerfreundlicher Fehlermeldungen).
2. Prompt-Template aus Formulardaten bauen.
3. Echten API-Call an den Trainer-Endpoint integrieren.
4. Ergebnis als strukturierte Abschnitte anzeigen (Zusammenfassung, Leistungsumfang, Zeitplan, Preis, Naechste Schritte).

Done-Kriterium:
- Ein vollstaendiger Angebotsentwurf wird per realem API-Call im Browser erzeugt.

Zwischenfazit um 12:15:
- Alle haben den gemeinsamen Kern-Flow einmal gesehen und umgesetzt.
- Danach ist das Muster klar genug fuer eigene App-Ideen.

---

### Block C (13:15 - 15:00): Eigener Use-Case und individueller App-Bau

Ziel:
- Jede Person uebertraegt das Muster auf den eigenen Use-Case und baut die eigene App-Version.

Format:
- Eigenbau-Phase mit Coaching (Trainer als Sparringspartner)

Hands-on Schritte:
1. Jede Person formuliert den eigenen Use-Case in 2-3 Saetzen.
2. App-Grundstruktur fuer den eigenen Use-Case anpassen (Felder, Labels, Ergebnisformat).
3. Eigene Generierungslogik mit Prompt-Template und realem API-Call umsetzen.
4. Einen ersten End-to-End Lauf mit Testdaten durchfuehren.

Wichtig unter No-Admin-Bedingung:
- Keine Abhaengigkeiten voraussetzen. Alles laeuft mit HTML, CSS, JS im Browser.

---

### Block D (15:15 - 17:00): Finalisierung, Test und Demo

Ziel:
- Jede Person liefert eine vorzeigbare eigene Web-App inklusive kurzer Demo-Story.

Format:
- Eigenbau finalisieren, danach Kurz-Demos

Hands-on Schritte:
1. Finale Features fuer den eigenen Use-Case abschliessen (mind. Validierung + Generierung + Ergebnisdarstellung).
2. Kurzer Frontend-Test: Pflichtfelder, Fehlerfaelle, Ergebnisanzeige, optional Export.
3. 2-Minuten Demo vorbereiten: Problem -> Eingabe -> Generierung -> Ergebnis.

Erwartetes Endergebnis:
- Reproduzierbare Browser-App pro Person, die ohne lokale Admin-Rechte durchfuehrbar ist.

---

## Konkrete Prompt-Vorlagen fuer den Tag

- "Erzeuge in index.html ein barrierearmes Formular und einen Ergebnisbereich fuer Offer Studio."
- "Schreibe in app.js eine Funktion buildPrompt(input), die aus Formulardaten einen klaren AI-Prompt erstellt."
- "Implementiere generateOfferViaApi(input) mit fetch, Error-Handling und Mapping auf 5 Ergebnisabschnitte."
- "Zeige Validierungsfehler neben den Eingabefeldern und deaktiviere den Button bis alle Pflichtfelder gueltig sind."
- "Ergaenze einen Export-Button fuer TXT und einen Copy-Button fuer die Zwischenablage."
- "Optimiere styles.css fuer mobile Nutzung ab 390px und fuer Desktop ab 1024px."

---

## Minimum Scope fuer Day 2

- Muss:
  - Bis 12:15 gemeinsamer Kern-Flow in Offer Studio verstanden und umgesetzt
  - Ab 13:15 eigene Browser-App mit HTML, CSS, JavaScript gebaut
  - Eigene App mit Formular, Validierung und realem API-Call laeuft
- Soll:
  - Ergebnisdarstellung und optionaler Export in der eigenen App
  - Responsives, sauberes UI
- Kann:
  - Retry-Strategie, Caching oder Fallback auf Mock erweitern
