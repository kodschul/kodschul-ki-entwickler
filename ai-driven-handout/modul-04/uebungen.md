# Modul 4 — Übungen

---

## Übung 4.1-A — Agent vs. Chat: Den Unterschied erleben

**Aufgabe:** Lösen Sie dieselbe Aufgabe einmal als einstufigen Chat-Prompt und einmal als mehrstufigen Agent-Workflow. Vergleichen Sie danach die Qualität.

**Aufgabe (einstufig):**
```
Erstelle für einen Online-Shop vollständige Domänenklassen,
EF Core Konfiguration und Unit-Tests.
```

**Aufgabe (mehrstufig):**
```
Schritt 1: Welche Domänenklassen braucht ein Online-Shop (DDD-Perspektive)?
Schritt 2: [Ergebnis aus Schritt 1] → Erstelle die C#-Klassen nach DDD-Prinzipien
Schritt 3: [Klassen] → Erstelle die EF Core 9 Konfiguration
Schritt 4: [Klassen] → Erstelle xUnit + FluentAssertions Tests
```

**Vergleichsmatrix:**

| Kriterium | Einstufig | Mehrstufig |
|---|---|---|
| Vollständigkeit der Klassen | | |
| Qualität der EF Core Konfiguration | | |
| Qualität der Tests | | |
| Nachbearbeitungsaufwand | | |
| Wo lagen die Fehler? | | |

---

## Übung 4.1-B — Chancen-Risiken-Analyse

**Szenario:** Ihr Team erwägt, einen vollautomatischen KI-Agenten einzusetzen, der:
1. GitHub Issues analysiert
2. Code-Änderungen plant und beschreibt
3. Pull Requests mit Implementierung erstellt
4. CI/CD-Tests ausführt
5. Bei grünen Tests den PR automatisch merged

**Aufgaben:**
1. Bei welchen Schritten ist ein menschlicher Prüfpunkt zwingend? Begründen Sie.
2. Welche konkreten Risiken entstehen bei vollständiger Automatisierung jedes Schrittes?
3. Entwerfen Sie einen sicheren Workflow mit Human-in-the-Loop-Punkten.
4. Schreiben Sie die Prompt-Sicherheitsregeln für den Agenten (was darf er nie tun?).

---

## Übung 4.2-A — User Story in Prompt-Kette übersetzen

**User Story:**
```
Als Lagermitarbeiter möchte ich den Lagerbestand eines Produkts erhöhen,
wenn eine Lieferung eingeht, damit der aktuelle Bestand immer korrekt ist.

Akzeptanzkriterien:
- Bestand wird um die gelieferte Menge erhöht
- Menge muss positiv sein (> 0)
- Maximaler Bestand: 50.000 Einheiten
- Domain Event StockReplenished wird ausgelöst (mit ProductId, AddedQuantity, NewStock)
- Lieferant-Referenznummer wird gespeichert
```

**Aufgabe:** Zerlegen Sie die Implementierung in eine 5-stufige Prompt-Kette.

Für jeden Schritt definieren Sie:
| | Input | Prompt (Stichwort) | Erwarteter Output | Prüfpunkt |
|---|---|---|---|---|
| Schritt 1 | | | | |
| Schritt 2 | | | | |
| Schritt 3 | | | | |
| Schritt 4 | | | | |
| Schritt 5 | | | | |

---

## Übung 4.2-B — Prompt-Kette tatsächlich durchführen

**Aufgabe:** Führen Sie die Prompt-Kette aus Übung 4.2-A durch.

Starten Sie Schritt 1 mit diesem Input:
```
User Story: Als Lagermitarbeiter möchte ich den Lagerbestand erhöhen wenn eine Lieferung eingeht.

Akzeptanzkriterien:
- Menge muss positiv sein
- Maximaler Bestand 50.000
- Domain Event: StockReplenished(ProductId, AddedQuantity, NewStock, SupplierReference, OccurredAt)
- SupplierReference: string, max. 50 Zeichen
```

**Dokumentieren Sie ehrlich:**
- Welche Anpassungen mussten Sie zwischen den Schritten vornehmen?
- Wo hat die KI Fehler gemacht?
- Wie haben Sie diese erkannt und korrigiert?
- Hat sich ein Fehler aus einem frühen Schritt in späteren fortgepflanzt?

---

## Übung 4.3-A — Wiederholbaren Workflow dokumentieren

**Aufgabe:** Erstellen Sie eine **Workflow-Vorlage** als Markdown, die Ihr Team für jedes neue Feature im Online-Shop-Projekt verwenden kann.

Die Vorlage muss enthalten:
- Workflow-Name und Beschreibung
- Voraussetzungen (was muss vorher vorhanden sein?)
- Schritt-für-Schritt-Prompts mit Platzhaltern `[IN_KLAMMERN]`
- Prüfkriterien nach jedem Schritt (Checkliste)
- Abbruchbedingungen (wann besser manuell vorgehen?)
- Geschätzter Zeitaufwand (KI-Durchlauf vs. manuell)

---

## Übung 4.3-B — Human-in-the-Loop planen

**Szenario:** Sie automatisieren die Testdaten-Generierung:

Der Agent soll:
1. Datenbankschema lesen
2. Realistische Testdaten generieren (20 Kunden, 50 Produkte, 100 Bestellungen)
3. SQL INSERT-Skripte erstellen
4. Skripte gegen lokale Testdatenbank ausführen

**Aufgabe:**
1. Nach welchen Schritten MUSS ein Mensch prüfen? Begründen Sie.
2. Welche automatischen Validierungen kann der Agent selbst durchführen?
3. Wie wird ein Rollback ermöglicht wenn Schritt 4 fehlschlägt?
4. Schreiben Sie die vollständigen Sicherheitsregeln für diesen Agenten als Prompt-Präambel.

---

## Übung 4.4-A — Mini-Sprint mit KI planen

**Feature:**
> Kunden sollen ihre letzten 10 Bestellungen als Liste sehen können. Klick auf eine Bestellung öffnet die Detailansicht mit allen Positionen.

Erstellen Sie einen KI-unterstützten Ablaufplan:

| Schritt | Was wird gemacht? | KI-Tool | Prompt-Stichworte | Manueller Prüfpunkt? | Zeit KI | Zeit manuell |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| ... | | | | | | |
| **Gesamt** | | | | | | |

---

## Übung 4.4-B — Reflexion und Grenzen

**Aufgabe:** Schreiben Sie nach Abschluss der Übungen 4.2-B und 4.4-A eine strukturierte Reflexion (min. ½ Seite).

Beantworten Sie:
1. **Qualität:** Wo hat KI-Unterstützung am meisten gebracht? Wo am wenigsten?
2. **Fehlerfortpflanzung:** Gab es Fehler die sich durch mehrere Schritte zogen? Wie hätte man sie früher erkannt?
3. **Nachvollziehbarkeit:** Können Sie jeden Teil des generierten Codes einem Kollegen vollständig erklären? Wenn nicht, was fehlt?
4. **Effizienz:** War Multi-Step tatsächlich schneller als manuelle Implementierung? Ab welcher Aufgabengröße kippt das?
5. **Empfehlung:** Für welche Aufgaben-Typen empfehlen Sie Multi-Step-Prompting in Ihrem Team – für welche nicht?
