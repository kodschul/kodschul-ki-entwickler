# Offer Studio


# Über mich 
Ich habe keine Programmierungskenntnisse und möchte alles lokal ohne Installation bauen. 


## App-Beschreibung und Zielgruppe

**Offer Studio** ist ein KI-gestütztes Tool für Vertriebsmitarbeiter, das aus strukturierten Eingaben sofort professionelle Angebotsdokumente generiert.

**Zielgruppe:** B2B-Vertrieb in IT, Beratung und Dienstleistung — Mitarbeiter ohne Textexpertise, die täglich Angebote erstellen und dabei Zeit sparen wollen.

---

## Pflichtstruktur jedes Angebots

Jedes generierte Angebot muss exakt diese fünf Abschnitte in dieser Reihenfolge enthalten:

1. **Executive Summary** — Kurze Zusammenfassung der Kundensituation und des angebotenen Nutzens (max. 3 Sätze)
2. **Problemverständnis** — Beschreibung der Herausforderung oder des Bedarfs des Kunden, in dessen eigener Sprache gespiegelt
3. **Lösungsansatz** — Konkrete Beschreibung der angebotenen Leistung, Methodik und Vorgehensweise
4. **Investition & Konditionen** — Preisübersicht, Zahlungsmodalitäten, Laufzeit und eventuelle Rabatte
5. **Nächste Schritte** — Klarer Call-to-Action mit konkretem Datum oder Aktion (z. B. "Kick-off am ...", "Antwort bis ...")

---

## Tonalität und Sprache

- Professionell, klar und auf Augenhöhe — kein aufgeblasenes Berater-Deutsch
- Aktive Sprache: "Wir liefern", nicht "Es wird geliefert"
- Kundenorientiert: Der Kunde steht im Mittelpunkt, nicht das eigene Unternehmen
- Konkret und präzise: Keine Floskeln wie "ganzheitlich", "nachhaltig" oder "state of the art"
- Sprache immer auf Deutsch — alle Angebote werden ausnahmslos auf Deutsch verfasst, unabhängig von der Eingabesprache des Nutzers

---

## Was nie passieren darf

- Keine Platzhalter wie `[NAME]`, `[DATUM]` oder `[BETRAG]` im finalen Output — alle Felder müssen befüllt sein
- Keine ungenauen Preisangaben ohne Einheit oder Zeitraum
- Kein Abschnitt darf fehlen — alle fünf Pflichtabschnitte sind immer vorhanden
- Keine unaufgeforderten Rabatte oder Zugeständnisse im Text
- Keine Versprechungen über Lieferdaten, die nicht vom Nutzer eingegeben wurden
- Keine generischen Texte, die nicht auf die eingegebenen Kundendaten eingehen

---

## Ablauf in der App

```
1. Eingabe Kundendaten
   └── Firmenname, Ansprechpartner, Branche, Unternehmensgröße

2. Eingabe Projektinfos
   └── Projektbeschreibung, gewünschte Leistungen, Budget (optional), Zeitraum

3. Optionale Anpassungen
   └── Tonalität anpassen, spezifische USPs hervorheben, Sonderkonditionen

4. Generierung
   └── KI erstellt Angebotsentwurf nach der 5-Abschnitt-Struktur

5. Review & Export
   └── Nutzer prüft, editiert bei Bedarf, exportiert als PDF oder Word
```
