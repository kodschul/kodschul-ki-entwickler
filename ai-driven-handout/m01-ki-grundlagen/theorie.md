# Modul 1 — Künstliche Intelligenz in der Softwareentwicklung verstehen

---

## Lab 1.1 — Grundlagen der künstlichen Intelligenz einordnen

### Was ist Künstliche Intelligenz?

Künstliche Intelligenz (KI) bezeichnet Computersysteme, die Aufgaben ausführen, für die bislang menschliche Intelligenz erforderlich war: Sprache verstehen, Muster erkennen, Entscheidungen treffen, Texte und Code erzeugen.

Moderne KI in der Softwareentwicklung basiert überwiegend auf **Large Language Models (LLMs)** – neuronale Netze, die auf riesigen Textmengen trainiert wurden und auf Basis statistischer Wahrscheinlichkeiten das jeweils nächste Token (Wortfragment) vorhersagen.

### Zentrale Begriffe

| Begriff | Bedeutung |
|---|---|
| **LLM** | Large Language Model – z. B. GPT-4o, Claude, Gemini |
| **Token** | Kleinste Verarbeitungseinheit (~¾ eines Wortes) |
| **Prompt** | Eingabe des Nutzers an das Modell |
| **Completion** | Antwort/Ausgabe des Modells |
| **Temperatur** | Parameter zwischen 0–1: niedrig = präzise, hoch = kreativ |
| **Context Window** | Maximale Textmenge die das Modell gleichzeitig "sieht" |
| **Halluzination** | Modell erfindet plausibel klingende, aber falsche Fakten |
| **Fine-Tuning** | Nachtrainieren eines Modells auf spezifischen Daten |
| **RAG** | Retrieval-Augmented Generation – KI + externe Wissensquelle |
| **Embedding** | Numerische Vektordarstellung von Text für semantische Suche |

### Abgrenzung: KI vs. Automatisierung vs. klassische Softwarelogik

```
Klassische Softwarelogik:
  if (bestellung.Betrag > 1000) { rabatt = 0.10; }
  → Explizite Regeln, deterministisch, kein Lernen

Automatisierung:
  Skript kopiert täglich Dateien von A nach B um 02:00 Uhr
  → Wiederholbare, regelbasierte Prozesse, kein Lernaspekt

Künstliche Intelligenz:
  "Analysiere diese Bestellung und erkläre warum sie auffällig ist"
  → Kontextverständnis, Generalisierung, probabilistisch
```

**Wann ist KI der richtige Ansatz?**
- Das Problem lässt sich schlecht durch explizite Regeln beschreiben
- Natürlichsprachliche Ein- oder Ausgabe ist gefragt
- Kreative oder generative Aufgaben (Code, Text, Entwürfe)
- Muster in großen Datenmengen erkennen

**Wann ist klassische Logik besser?**
- 100 % deterministisches Verhalten ist zwingend
- Regulatorisch erklärbare Entscheidungen erforderlich
- Einfache, gut definierte Regeln existieren bereits

---

## Lab 1.2 — Einsatzgebiete von KI in der Softwareentwicklung

### Typische Anwendungsfelder

#### Konzeptionsphase
- Anforderungen aus User Stories extrahieren und strukturieren
- Domänenmodelle und Entitäten vorschlagen (DDD)
- Technologieentscheidungen abwägen und dokumentieren
- Architekturentwürfe skizzieren und diskutieren

#### Implementierungsphase
- Code-Snippets und vollständige Klassen generieren
- Bestehenden Code erklären und kommentieren
- Refactoring-Vorschläge erstellen
- Reguläre Ausdrücke, SQL-Queries, LINQ-Abfragen schreiben
- Bugs identifizieren und Fixes vorschlagen

#### Testing
- Unit-Tests aus Implementierungscode ableiten
- Realistische Testdaten in verschiedenen Szenarien generieren
- Edge Cases und Grenzwerte vorschlagen
- Testabdeckung analysieren und ergänzen

#### Dokumentation
- XML-Docs, README, Changelogs erstellen
- API-Dokumentation aus Code generieren
- Technische Konzepte verständlich erklären

### Chancen und Grenzen

| Chancen | Grenzen |
|---|---|
| Enorme Beschleunigung bei Routineaufgaben | Kein echtes Domänenwissen – nur statistische Muster |
| Sofortzugriff auf bewährte Patterns | Halluzinationen bei spezifischen oder neuen Themen |
| Niedrigschwellige Einstiegshilfe | Veraltetes Wissen (Trainingsdaten-Cutoff) |
| Gute Unterstützung bei populären Technologien | Schwächen bei proprietären oder internen APIs |
| 24/7 verfügbar, keine Wartezeiten | Kein Verständnis des Gesamtkontexts ohne Prompt |

---

## Lab 1.3 — Datenschutz und rechtliche Anforderungen

### Was darf nicht in den Prompt?

Bei der Nutzung kommerzieller KI-Dienste (ChatGPT, Claude, Copilot) gelten wichtige Grenzen:

**Niemals eingeben:**
- Personenbezogene Kundendaten (Name, E-Mail, Adresse, IBAN) → DSGVO!
- Interner Quellcode mit Geschäftsgeheimnissen
- Zugangsdaten, API-Keys, Passwörter
- Vertrauliche Architekturdokumente und Betriebsdaten

**Technische Schutzmaßnahmen:**
- On-Premise-Modelle (Ollama, Azure OpenAI Private Endpoint)
- Anonymisierung vor KI-Eingabe
- Unternehmensweite KI-Policy einhalten und durchsetzen

### Rechtliche Rahmenbedingungen

**DSGVO:**
- Art. 25: Privacy by Design – KI-Einsatz datenschutzfreundlich gestalten
- Art. 22: Vollautomatische Entscheidungen mit Rechtswirkung benötigen menschliche Kontrolle
- AVV (Auftragsverarbeitungsvertrag) mit KI-Anbieter prüfen

**EU AI Act (ab 2025):**
- Risikoklassen: Minimal / Begrenzt / Hoch / Inakzeptabel
- Hochrisiko-KI (HR, Kreditvergabe, Strafverfolgung) unterliegt strengen Anforderungen
- Transparenzpflichten bei KI-generierten Inhalten

**Urheberrecht:**
- KI-generierter Code kann Muster aus Trainingsdaten enthalten
- Lizenzprüfung bei GitHub Copilot (trainiert auf öffentlichem Code)
- Urheberschaft liegt beim Autor, nicht bei der KI

---

## Lab 1.4 — Qualität und Verlässlichkeit von KI-Ergebnissen

### Wie KI-Ergebnisse entstehen

LLMs erzeugen Ausgaben durch Wahrscheinlichkeitsverteilungen über mögliche nächste Tokens. Sie „wissen" nichts im eigentlichen Sinne – sie haben statistische Muster aus Trainingsdaten gelernt.

Das bedeutet: Die Ausgabe ist immer eine **wahrscheinliche**, nicht zwingend eine **korrekte** Antwort.

### Halluzinationen erkennen

Typische Anzeichen:
- Spezifische Zahlen, Daten oder Namen ohne Quellenangabe
- Nicht existierende Bibliotheken, Methoden oder API-Endpunkte
- Widersprüche innerhalb einer Antwort
- Zu glatte Antworten auf sehr spezifische, neue Fragen

```csharp
// Halluzinations-Beispiel: Diese EF Core Methode existiert nicht!
var result = await _context.Orders
    .FilterByCustomerRegion("Bayern")   // ❌ Existiert nicht!
    .AsCachedAsync(TimeSpan.FromMinutes(5))  // ❌ Existiert nicht!
    .ToListAsync();
```

### Was die Ergebnisqualität beeinflusst

| Faktor | Auswirkung |
|---|---|
| **Kontext im Prompt** | Mehr relevanter Kontext → bessere Ausgabe |
| **Modellgröße** | Größere Modelle → besser, langsamer, teurer |
| **Temperatur** | 0.0–0.3: Code/Fakten; 0.7–1.0: Kreativität |
| **Formulierung** | Präzise Sprache → präzisere Ergebnisse |
| **Beispiele** | Few-Shot-Prompts verbessern Ausgabeformat deutlich |

### Goldene Regel

> **Jeder KI-generierte Code muss gelesen, verstanden, fachlich geprüft und getestet werden – bevor er in die Codebasis eingecheckt wird.**

KI ist ein Beschleuniger, kein Autopilot. Die Verantwortung für den Code bleibt beim Entwickler.
