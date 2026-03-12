# Lab 3.2 – Debugging und Code-Analyse mit KI

## Szenario

Du übernimmst ein **Lagerbestandssystem** (Inventory System) von einem Kollegen,
der das Unternehmen kurzfristig verlassen hat. Das System wird seit kurzem
produktiv eingesetzt, aber die Nutzer melden seltsame Fehler:

- Lagerbestände werden falsch berechnet
- Beim Export von Berichten kommt es zu einem Absturz
- Beim Import von Produkten werden einige Einträge still verworfen
- Eine Datumsberechnung liefert falsche Ergebnisse

Du hast bereits einige Log-Ausgaben und Stack-Traces gesammelt (siehe `logs/`).
Deine Aufgabe ist es, die Fehler zu analysieren, die Ursachen zu finden und die
Bugs zu beheben – mithilfe des KI-Assistenten.

---

## Projekt-Überblick

Ein Lagerbestandssystem in TypeScript. Es verwaltet Produkte, Lagerbewegungen
(Stock Movements) und erstellt Reports.

```
Project/
├── src/
│   ├── InventoryManager.ts   ← Haupt-Logik, enthält mehrere Bugs
│   ├── ReportGenerator.ts    ← Absturz beim Exportieren
│   ├── ProductImporter.ts    ← Stille Datenverluste
│   └── DateHelper.ts         ← Falsche Datumsberechnungen
├── logs/
│   ├── error.log             ← echte Fehlerlogs mit Stack-Traces
│   └── import.log            ← Log des letzten Imports
├── data/
│   └── sample-import.csv     ← Beispiel-Import-Datei
├── package.json
└── tsconfig.json
```

---

## Lernziele

- Stack-Traces lesen und interpretieren
- Logische Fehler in Code erkennen
- KI zur Fehleranalyse einsetzen
- Root-Cause-Analyse durchführen
- Bugs systematisch beheben und testen

---

## Fehlerübersicht

### Fehler 1 – Falscher Lagerbestand (InventoryManager)

**Symptom:** Der angezeigte Lagerbestand eines Artikels ist nach mehreren
Buchungen negativ, obwohl Unterschreitung des Mindestbestands verhindert werden soll.

**Relevante Datei:** `src/InventoryManager.ts`

---

### Fehler 2 – Absturz beim Report-Export (ReportGenerator)

**Symptom:** `TypeError: Cannot read properties of undefined (reading 'toFixed')`

Aus `logs/error.log`:
```
[2026-03-10 09:14:32] ERROR ReportGenerator crashed
TypeError: Cannot read properties of undefined (reading 'toFixed')
    at ReportGenerator.formatLine (src/ReportGenerator.ts:47)
    at ReportGenerator.generateStockReport (src/ReportGenerator.ts:31)
    at InventoryManager.exportReport (src/InventoryManager.ts:89)
```

**Relevante Datei:** `src/ReportGenerator.ts`

---

### Fehler 3 – Stille Datenverluste beim Import (ProductImporter)

**Symptom:** Beim Import einer CSV-Datei mit 50 Produkten erscheinen nur 43
im System. Keine Fehlermeldung.

Aus `logs/import.log`:
```
[2026-03-10 08:00:01] Import gestartet: sample-import.csv (50 Einträge)
[2026-03-10 08:00:01] Verarbeite Zeile 1: OK
[2026-03-10 08:00:01] Verarbeite Zeile 2: OK
...
[2026-03-10 08:00:02] Verarbeite Zeile 50: OK
[2026-03-10 08:00:02] Import abgeschlossen: 43 Produkte importiert
```

**Relevante Datei:** `src/ProductImporter.ts`

---

### Fehler 4 – Falsche Datumsberechnung (DateHelper)

**Symptom:** „Artikel abgelaufen"-Warnungen erscheinen für Artikel, die noch
30 Tage gültig sind. Artikel, die wirklich abgelaufen sind, werden nicht
angezeigt.

**Relevante Datei:** `src/DateHelper.ts`

---

## Aufgaben

### Aufgabe 1 – Stack-Trace analysieren (10 Min.)

Öffne `logs/error.log`. Nutze den **KI-Chat**, um:

1. Den Stack-Trace zu erklären: Was ist schiefgelaufen? In welcher Datei und Zeile?
2. Was könnte die Ursache sein?
3. Welche Codevariable ist wahrscheinlich `undefined`?

> **Tipp:** Kopiere den Stack-Trace in den KI-Chat und frage:  
> *„Analysiere diesen Stack-Trace und erkläre, was schiefgelaufen ist."*

---

### Aufgabe 2 – Bug in `InventoryManager.ts` finden und beheben (15 Min.)

Öffne `src/InventoryManager.ts`. Suche die Methode `bookStockOut`.

1. Nutze KI, um den Code zu analysieren: *„Gibt es einen Logikfehler in dieser Methode?"*
2. Identifiziere den Bug: Warum kann der Bestand negativ werden?
3. Behebe den Fehler.

> **Tipp:** Achte besonders auf Vergleichsoperatoren und die Reihenfolge von
> Operationen. Frage die KI: *„Vergleiche diese Bedingung mit der Anforderung
> und prüfe, ob sie korrekt ist."*

---

### Aufgabe 3 – `ReportGenerator.ts` debuggen (15 Min.)

Öffne `src/ReportGenerator.ts`. Der Absturz kommt aus `formatLine`.

1. Finde heraus, warum `toFixed` auf `undefined` aufgerufen wird.
2. Welche Daten werden erwartet, welche werden tatsächlich geliefert?
3. Behebe den Fehler mit einer sicheren Null-Prüfung.

> **Tipp:** Frage die KI: *„Warum könnte dieser Wert undefined sein?
> Wie kann ich die Methode absturzsicher machen?"*

---

### Aufgabe 4 – Stille Fehler in `ProductImporter.ts` aufdecken (15 Min.)

Öffne `src/ProductImporter.ts`. Warum werden 7 von 50 Produkten verworfen?

1. Untersuche die `parseRow`-Methode.
2. Frage die KI, welche Eingaben zum Verwerfen führen.
3. Korrigiere die Validierungslogik, sodass gültige Produkte nicht verworfen werden.
4. Füge eine Warnung hinzu, damit verworfene Zeilen im Log erscheinen.

> **Tipp:** Nutze `data/sample-import.csv` und frage die KI:  
> *„Analysiere diese Validierungslogik. Welche gültigen Zeilen könnten fälschlicherweise abgelehnt werden?"*

---

### Aufgabe 5 – `DateHelper.ts` korrigieren (10 Min.)

Öffne `src/DateHelper.ts`. Die Methode `isExpired` liefert falsche Ergebnisse.

1. Frage die KI: *„Gibt es einen Off-by-One-Fehler oder einen Vorzeichenfehler in dieser Datumsmethode?"*
2. Schreibe 3 Testfälle (manuell oder mit KI), die das falsche und das korrekte Verhalten zeigen.
3. Behebe den Bug.

---

## Erwartetes Ergebnis

- ✅ Alle 4 Bugs identifiziert und behoben
- ✅ Kein negativer Lagerbestand mehr möglich
- ✅ ReportGenerator stürzt nicht mehr ab
- ✅ Alle 50 CSV-Zeilen werden korrekt importiert (oder klar protokolliert)
- ✅ Datumsvergleiche liefern korrekte Ergebnisse
- ✅ Fehlerhafte Stellen sind im Code kommentiert erklärt

---

## Hinweise zum KI-Einsatz

| Aufgabe                        | Empfohlener Modus  | Beispiel-Prompt                                                          |
|--------------------------------|--------------------|--------------------------------------------------------------------------|
| Stack-Trace verstehen          | Chat / Ask         | „Erkläre diesen Stack-Trace Zeile für Zeile"                             |
| Logikfehler finden             | Ask mit Code       | „Gibt es einen Logikfehler in dieser Methode? Erkläre deine Antwort"     |
| Null-Safety hinzufügen         | Edit / Inline      | „Mache diese Funktion sicher gegen undefined-Werte"                      |
| Validierung prüfen             | Ask mit Beispiel   | „Welche dieser Eingaben würden die Validierung fälschlicherweise ablehnen?" |
| Datumsfehler debuggen          | Ask                | „Gibt es einen Off-by-One oder Vorzeichenfehler in dieser Funktion?"     |
