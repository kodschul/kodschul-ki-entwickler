# Modul 1 — Lösungen

---

## Lösung 1.1-A — KI, Automatisierung oder klassische Logik?

| # | Kategorie | Begründung |
|---|---|---|
| 1 | Klassische Softwarelogik | Deterministisch, explizite Formel (Betrag × 0,19), kein Lernaspekt |
| 2 | KI | Kreative Generierung, Sprachverständnis, realistische Variationen |
| 3 | Automatisierung | Geplanter Prozess, regelbasiert, keine Intelligenz nötig |
| 4 | KI | Sprachverstehen, Kontextinterpretation, natürlichsprachliche Ausgabe |
| 5 | Klassische Softwarelogik | Einfache String-Prüfung: `email.Contains('@')` |
| 6 | KI | Kreative Textgenerierung, Kontextverständnis, keine feste Regel |
| 7 | Klassische Softwarelogik | Deterministischer Sortieralgorithmus, `OrderBy(o => o.Date)` |
| 8 | KI | Natürlichsprachliches Verstehen, Zusammenfassung und Priorisierung |
| 9 | Automatisierung | Regelbasierter CI/CD-Workflow, deterministisch |
| 10 | KI | Mustererkennung im Text, Sentiment-Analyse, Sprachverständnis |

**Sinnvolle Kombinationen:**
- Aufgabe 6: Automatisierung (Trigger bei neuem Support-Ticket) + KI (Betreff generieren)
- Aufgabe 10: KI (Sentiment-Score ermitteln) + Klassische Logik (Schwellenwert → Eskalation)
- Aufgabe 3: Automatisierung (Zeitplan) + KI (Berichtstext generieren)

---

## Lösung 1.1-B — Fachbegriffe

| Beschreibung | Begriff |
|---|---|
| Die Eingabe, die ein Entwickler an die KI schickt | `Prompt` |
| Ein Modell erfindet eine nicht existierende Bibliotheksmethode | `Halluzination` |
| Bestimmt wie kreativ oder reproduzierbar die Ausgaben sind | `Temperatur` |
| Kleinste Verarbeitungseinheit, ca. ¾ eines Wortes | `Token` |
| Wie viel Text das Modell gleichzeitig verarbeiten und "erinnern" kann | `Context Window` |
| Modell wird auf unternehmenseigenen Daten nachtrainiert | `Fine-Tuning` |
| Modell wird mit externen Dokumenten angereichert, ohne Nachtraining | `RAG` |
| Neuronales Netz mit Milliarden Parametern, auf Textmengen trainiert | `LLM` |
| Die Antwort/Ausgabe des Modells | `Completion` |
| Numerische Vektordarstellung von Text für semantische Ähnlichkeitssuche | `Embedding` |

---

## Lösung 1.2-A — KI-Einsatzfelder

| Phase | KI-Einsatz | Prompt-Ansatz |
|---|---|---|
| Anforderungsanalyse | User Stories extrahieren; Akzeptanzkriterien formulieren | „Extrahiere aus diesem Text User Stories im Format: Als [Rolle] möchte ich [Funktion] damit [Nutzen]" |
| Domänenmodellierung | Entitäten und Beziehungen vorschlagen; Ubiquitous Language entwickeln | „Identifiziere Entitäten, Value Objects und Domänenereignisse nach DDD aus dieser Anforderung" |
| Implementierung | Klassen generieren; LINQ-Abfragen schreiben; Boilerplate erzeugen | „Erstelle eine C#-Klasse Ticket als DDD-Entität mit folgenden Properties und Methoden..." |
| Code Review | Potenzielle Bugs aufzeigen; Best Practices prüfen | „Reviewe diesen Code auf DDD-Verletzungen, EF Core Anti-Patterns und .NET 9 Verbesserungen" |
| Testing | Unit-Tests ableiten; Grenzwerte vorschlagen; Testdaten generieren | „Erstelle xUnit-Tests für alle öffentlichen Methoden dieser Klasse mit FluentAssertions" |
| Dokumentation | XML-Docs generieren; README schreiben | „Generiere vollständige XML-Dokumentation für alle public Member dieser Klasse auf Deutsch" |
| Bugfixing | Exception-Ursache erklären; Fix vorschlagen; Ursachenanalyse | „Erkläre diese Exception mit Stack Trace, benenne die Ursache und schlage einen Fix vor" |

---

## Lösung 1.2-B — Extremaussagen einordnen

**Argumente gegen Aussage A (KI ersetzt alle Entwickler):**
1. KI hat kein Verständnis für Unternehmenskontext, Domänenwissen und Projekthistorie – sie braucht erfahrene Entwickler als „Steuerer"
2. Generierten Code zu lesen, zu prüfen und zu verantworten erfordert volle Entwickler-Expertise
3. Architekturentscheidungen, Design-Trade-offs und Systemintegration sind genuine Denkleistungen, die aktuelle KI nicht eigenständig trägt
4. Debugging in komplexen, verteilten Systemen übersteigt die Fähigkeiten heutiger KI erheblich

**Argumente gegen Aussage B (KI zu unzuverlässig):**
1. KI beschleunigt Routineaufgaben wie Boilerplate, Tests und Dokumentation erheblich und messbar
2. Mit präzisen Prompts und konsequenter Validierung sind KI-Ausgaben regelmäßig direkt nutzbar
3. Wettbewerbsnachteile drohen, wenn Konkurrenten KI produktiv einsetzen und das eigene Team nicht
4. Die Qualität verbessert sich mit wachsender Erfahrung im Prompting und steigt mit den Modellen

**Realistische und produktive KI-Nutzung:**
KI ist ein Werkzeug zur Geschwindigkeitssteigerung bei klar definierten Teilaufgaben – nicht ein Ersatz für Entwicklungsexpertise. Entwickler setzen KI gezielt für Boilerplate-Code, Testgenerierung und Dokumentation ein, prüfen jede Ausgabe kritisch und behalten die architektonische und fachliche Gesamtverantwortung. Die Rolle des Entwicklers verändert sich vom „Code-Schreiber" zum „Code-Reviewer und KI-Steuerer". Teams, die früh lernen KI richtig einzusetzen, gewinnen erheblich an Liefergeschwindigkeit.

---

## Lösung 1.3-A — Datenschutz-Checkliste

```
☐ AVV abschließen: Auftragsverarbeitungsvertrag mit KI-Anbieter prüfen und unterzeichnen (DSGVO Art. 28)
☐ Datenklassifizierung: Klare Policy welche Datenklassen in KI eingegeben werden dürfen
☐ Kein personenbezogene Daten: Policy gegen Eingabe von Kunden-, Mitarbeiterdaten, IBANs
☐ Kein proprietärer Code: Interne Geschäftslogik und IP nicht an externe Dienste senden
☐ Technische Maßnahmen: Enterprise-Modus konfigurieren (kein Training auf Firmendaten)
☐ Mitarbeiterschulung: Alle Nutzer schulen und Nutzungsvereinbarung unterzeichnen lassen
☐ Audit-Trail: Protokollieren wer KI-Tools wann für welche Aufgaben nutzt
☐ Regelmäßige Überprüfung: Policy mindestens jährlich und bei Anbieteränderungen aktualisieren
☐ Incident-Prozess: Was passiert wenn versehentlich sensible Daten eingegeben wurden?
```

**Alternativen mit hohen Datenschutzanforderungen:**
1. **Azure OpenAI Service** (EU-Region): Daten verlassen nicht das EU-Rechenzentrum, kein Training
2. **On-Premise mit Ollama + Llama 3 / Mistral**: Daten verlassen das Unternehmens-Netzwerk nie
3. **GitHub Copilot Enterprise**: DSGVO-konform, kein Training auf Unternehmens-Code

---

## Lösung 1.3-B — Datenschutzkritische Prompts

**Prompt A:**
Problematisch: Vollständiger Name, E-Mail und IBAN sind personenbezogene Daten (DSGVO-Verstoß).

Alternative:
```
Schreibe einen freundlichen Mahnungstext für einen Kunden mit offener Rechnung.
Platzhalter: {{KUNDENNAME}}, {{RECHNUNGSNUMMER}}, {{BETRAG}}, {{FAELLIGKEITSDATUM}}
Ton: höflich aber bestimmt. Sprache: Deutsch. Länge: max. 3 Absätze.
```

**Prompt B:**
Problematisch: Proprietärer Quellcode ist Geschäftsgeheimnis und geistiges Eigentum.

Alternative:
```
Ich habe einen Zahlungsalgorithmus mit dieser abstrakten Struktur:
- Eingabe: Betrag (decimal), Währung (string), Zeitstempel (DateTime)
- Verarbeitung: Validierung → Rundung → Währungskonvertierung → Logging
- Ausgabe: Transaktions-Objekt mit Status

Welche Best Practices und Optimierungsansätze empfiehlst du für solche Algorithmen in .NET 9?
```

**Prompt C:**
Problematisch: Patientenname, Geburtsdatum und Diagnosen sind nach DSGVO Art. 9 besonders schützenswerte Gesundheitsdaten.

Alternative:
```
Erstelle eine Vorlage für einen Arztbrief an einen Kardiologen:
Abschnitte: Anamnese, Diagnosen (ICD-10 Platzhalter: {{ICD_CODE}}), Therapieempfehlung, Verlauf.
Verwende Platzhalter für alle patientenbezogenen Informationen: {{PATIENT}}, {{GEBURTSDATUM}}.
```

---

## Lösung 1.4-A — Halluzinationen aufspüren

| Stelle | Problem | Korrekte EF Core 9 Syntax |
|---|---|---|
| A: `.WhereCustomer(customerId)` | Methode existiert nicht | `.Where(o => o.CustomerId == customerId)` |
| B: `.IncludeDeep(o => o.Lines.Product)` | Methode existiert nicht | `.Include(o => o.Lines).ThenInclude(l => l.Product)` |
| C: `.OrderByCreatedDescending()` | Methode existiert nicht | `.OrderByDescending(o => o.CreatedAt)` |
| D: `.AsCachedAsync(...)` | Existiert nicht in EF Core | Separates Caching mit `IMemoryCache` implementieren |
| E: SmartBatch / Version 9.2 | Funktion und Version existieren nicht | EF Core 9 hat keine SmartBatch-Funktion (Stand 2025) |

**Korrekte Abfrage:**
```csharp
var orders = await _context.Orders
    .Where(o => o.CustomerId == customerId)
    .Include(o => o.Lines)
        .ThenInclude(l => l.Product)
    .OrderByDescending(o => o.CreatedAt)
    .ToListAsync(ct);
```

---

## Lösung 1.4-B — Prompt-Qualität vergleichen

| Kriterium | Prompt A | Prompt B |
|---|---|---|
| Kompilierbar ohne Änderungen? | Selten | Meist ja |
| Alle 3 Testfälle abgedeckt? | Nein (oft nur Happy Path) | Ja |
| Korrekte Bibliothek verwendet? | Zufällig (NUnit, MSTest, xUnit gemischt) | Ja (xUnit + FluentAssertions) |
| Arrange/Act/Assert sichtbar? | Nein | Ja |
| Methodennamen sprechend? | Nein (test1, TestMethod) | Ja |
| Nachbearbeitungszeit | 45–60 min | 5–10 min |

**Einflussreichste Elemente in Prompt B:**
1. **Expliziter Testcode** im Prompt: KI kennt die genaue Methode und Domänenlogik
2. **Framework-Angabe**: Verhindert falsches Testing-Framework
3. **Explizite Testfälle**: Verhindert, dass nur der Happy Path getestet wird
4. **Format-Vorgabe** (Arrange/Act/Assert): Einheitliche, lesbare Struktur

**Weitere Verbesserungen für Prompt B:**
- Testklassen-Name vorgeben
- Naming-Convention präzisieren (`MethodName_Szenario_ErwarteteAusgabe`)
- Angabe ob Mocks/Stubs benötigt werden (hier: nein)
- Gewünschte FluentAssertions-Methoden nennen (`.Should().Throw<>()`)
