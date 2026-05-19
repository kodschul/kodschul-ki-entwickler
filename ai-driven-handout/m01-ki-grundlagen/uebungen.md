# Modul 1 — Übungen

---

## Übung 1.1-A — KI, Automatisierung oder klassische Logik?

Ordnen Sie jede Aufgabe der richtigen Kategorie zu und begründen Sie kurz.  
Kategorien: **KI** · **Automatisierung** · **Klassische Softwarelogik**

| # | Aufgabe |
|---|---|
| 1 | Mehrwertsteuer auf einen Rechnungsbetrag berechnen |
| 2 | 100 realistische deutsche Kundennamen mit Adressen generieren |
| 3 | Täglich um 02:00 Uhr neue Bestellungen als CSV exportieren |
| 4 | Einen unbekannten Legacy-Code-Block auf Deutsch erklären |
| 5 | Prüfen ob eine E-Mail-Adresse das `@`-Zeichen enthält |
| 6 | Eine passende Betreffzeile für eine Support-Antwort-E-Mail vorschlagen |
| 7 | Eine Liste von Bestellungen nach Datum sortieren |
| 8 | Ein 50-seitiges Anforderungsdokument zusammenfassen |
| 9 | Nach jedem Git-Push automatisch Build, Tests und Deployment ausführen |
| 10 | Erkennen ob ein Kundenkommentar positiv, neutral oder negativ ist |

**Tabelle zum Ausfüllen:**

| # | Kategorie | Begründung |
|---|---|---|
| 1 | | |
| 2 | | |
| ... | | |

**Bonus:** Welche Aufgaben eignen sich für eine sinnvolle Kombination mehrerer Ansätze?

---

## Übung 1.1-B — Fachbegriffe zuordnen

Ordnen Sie die Beschreibungen den korrekten Begriffen zu.

**Begriffe:**
`Token` · `Halluzination` · `Temperatur` · `Context Window` · `Fine-Tuning` · `RAG` · `Prompt` · `LLM` · `Embedding` · `Completion`

| Beschreibung | Begriff |
|---|---|
| Die Eingabe, die ein Entwickler an die KI schickt | |
| Ein Modell erfindet eine nicht existierende Bibliotheksmethode | |
| Bestimmt wie kreativ oder reproduzierbar die Ausgaben sind | |
| Kleinste Verarbeitungseinheit, ca. ¾ eines Wortes | |
| Wie viel Text das Modell gleichzeitig verarbeiten und "erinnern" kann | |
| Modell wird auf unternehmenseigenen Daten nachtrainiert | |
| Modell wird mit externen Dokumenten angereichert, ohne Nachtraining | |
| Neuronales Netz mit Milliarden Parametern, auf Textmengen trainiert | |
| Die Antwort/Ausgabe des Modells | |
| Numerische Vektordarstellung von Text für semantische Ähnlichkeitssuche | |

---

## Übung 1.2-A — KI-Einsatzfelder im Entwicklungsprozess kartieren

**Szenario:** Ihr Team entwickelt ein neues internes Ticketsystem für die IT-Abteilung.

Füllen Sie die Tabelle aus. Identifizieren Sie **mindestens zwei** konkrete KI-Einsatzmöglichkeiten pro Phase und formulieren Sie jeweils einen kurzen Prompt-Ansatz.

| Phase | Konkreter KI-Einsatz | Prompt-Ansatz (Stichworte) |
|---|---|---|
| Anforderungsanalyse | | |
| Domänenmodellierung | | |
| Implementierung | | |
| Code Review | | |
| Testing | | |
| Dokumentation | | |
| Bugfixing | | |

---

## Übung 1.2-B — Extremaussagen einordnen

**Kollege A sagt:**
> „Mit KI können wir ab sofort alle Entwickler einsparen – die KI schreibt den Code!"

**Kollege B sagt:**
> „KI ist viel zu unzuverlässig für unsere Projekte. Das setzen wir bei uns nie ein."

Aufgaben:
1. Formulieren Sie **drei konkrete Argumente**, die Aussage A relativieren.
2. Formulieren Sie **drei konkrete Argumente**, die Aussage B relativieren.
3. Beschreiben Sie in 3–5 Sätzen, wie eine **realistische und produktive KI-Nutzung** im Entwicklungsalltag aussieht.

---

## Übung 1.3-A — Datenschutz-Checkliste entwickeln

**Szenario:** Ihr Unternehmen (50 Entwickler, B2B-SaaS, Deutschland) möchte GitHub Copilot und ChatGPT Plus einführen.

Erstellen Sie eine **Checkliste mit mindestens 8 Punkten**, die vor der Einführung geprüft werden müssen.

Berücksichtigen Sie:
- DSGVO-Anforderungen
- Unternehmensgeheimnisse / geistiges Eigentum
- Technische Schutzmaßnahmen
- Vertragsrechtliche Absicherung (AVV, Nutzungsbedingungen)
- Mitarbeiterschulung und -richtlinien

**Format:**
```
☐ [Punkt 1]: [Beschreibung was geprüft werden muss]
☐ [Punkt 2]: ...
```

**Bonus:** Nennen Sie drei Alternativen für Unternehmen mit besonders hohen Datenschutzanforderungen (z. B. Banken, Kliniken).

---

## Übung 1.3-B — Datenschutzkritische Prompts erkennen und verbessern

Analysieren Sie die folgenden drei Prompts. Markieren Sie problematische Stellen und schreiben Sie jeweils eine datenschutzkonforme Alternative.

**Prompt A:**
```
Hier sind unsere Kundendaten aus der Datenbank:
Name: Max Mustermann, E-Mail: max@beispiel.de, IBAN: DE89 3704 0044 0532 0130 00
Schreibe einen freundlichen Mahnungstext für diesen Kunden.
```

**Prompt B:**
```
Hier ist unser zentraler Zahlungsalgorithmus aus dem Produktivsystem:
[500 Zeilen interner Quellcode]
Erkläre wie er funktioniert und optimiere ihn.
```

**Prompt C:**
```
Ich arbeite in einer Arztpraxis. Patient Hans Müller (geb. 12.03.1965)
hat folgende Diagnosen: Diabetes Typ 2, Bluthochdruck.
Erstelle einen Arztbrief an den Kardiologen.
```

Für jeden Prompt:
1. Welche Daten sind problematisch? Warum?
2. Wie lautet die datenschutzkonforme Alternative?

---

## Übung 1.4-A — Halluzinationen aufspüren

Die folgende KI-Antwort auf die Frage *„Wie lese ich alle Bestellungen eines Kunden mit EF Core 9?"* enthält mehrere Halluzinationen. Finden und markieren Sie alle problematischen Stellen.

```csharp
var orders = await _context.Orders
    .WhereCustomer(customerId)                          // Zeile A
    .IncludeDeep(o => o.Lines.Product)                 // Zeile B
    .OrderByCreatedDescending()                         // Zeile C
    .AsCachedAsync(TimeSpan.FromMinutes(5))             // Zeile D
    .ToListAsync();

// EF Core 9 unterstützt außerdem die neue SmartBatch-Funktion,
// die Queries automatisch bündelt (verfügbar seit EF Core 9.2).  // Zeile E
```

Für jede markierte Stelle:
1. Was ist das Problem?
2. Wie lautet die korrekte EF Core 9 Syntax?

---

## Übung 1.4-B — Prompt-Qualität und Ergebnisqualität vergleichen

Testen Sie die folgenden zwei Prompts mit einer KI Ihrer Wahl und vergleichen Sie die Ausgaben systematisch.

**Prompt A — schlecht:**
```
Schreibe einen Test.
```

**Prompt B — gut:**
```
Du bist ein erfahrener C#-Entwickler mit xUnit- und FluentAssertions-Expertise.

Schreibe Unit-Tests für folgende Methode:

public void Confirm()
{
    if (Status != OrderStatus.Open)
        throw new InvalidOperationException("Nur offene Bestellungen können bestätigt werden.");
    if (!_lines.Any())
        throw new InvalidOperationException("Leere Bestellungen können nicht bestätigt werden.");
    Status = OrderStatus.Confirmed;
}

Anforderungen:
- Framework: xUnit + FluentAssertions (.NET 9)
- Testfälle: Happy Path, leere Bestellung, falscher Ausgangsstatus
- Struktur: Arrange / Act / Assert mit Kommentaren
- Methodenname: MethodName_Szenario_ErwarteteAusgabe
- Kein Mocking nötig
```

**Auswertungsmatrix:**

| Kriterium | Prompt A | Prompt B |
|---|---|---|
| Kompilierbar ohne Änderungen? | | |
| Alle 3 Testfälle abgedeckt? | | |
| Korrekte Bibliothek verwendet? | | |
| Arrange/Act/Assert sichtbar? | | |
| Methodennamen sprechend? | | |
| Nachbearbeitungszeit geschätzt | | |

**Reflexion:**
1. Welche Elemente in Prompt B haben den größten Qualitätsunterschied erzeugt?
2. Welche weiteren Verbesserungen würden Sie an Prompt B noch vornehmen?
