# Modul 3 — Prompt Engineering für die Softwareentwicklung

---

## Lab 3.1 — Einführung in modernes Prompting

### Die Kernidee

Die Qualität der KI-Ausgabe hängt direkt von der Qualität der Eingabe ab. Prompt Engineering ist die Disziplin, Eingaben so zu gestalten, dass reproduzierbar hochwertige Ergebnisse entstehen.

**Prompt-Qualitätsspektrum:**
```
"Schreibe Code"                          → 1 Stern: unbrauchbar
"Schreibe eine C#-Klasse für Orders"     → 3 Sterne: zu vage
"Du bist Senior .NET 9 Entwickler...
 Erstelle Order als Aggregate Root mit
 privaten Settern, Validierung, Domain
 Events. Nur Code. XML-Docs."            → 5 Sterne: direkt nutzbar
```

### Die CREF-Formel

| Buchstabe | Element | Zweck |
|---|---|---|
| **C** | **C**ontext | Projektumgebung, Technologie-Stack |
| **R** | **R**ole | Wer soll die KI sein? |
| **E** | **E**xpectation | Was genau soll entstehen? |
| **F** | **F**ormat | Wie soll die Ausgabe aussehen? |

**Beispiel vollständiger Prompt:**
```
[R] Du bist Senior .NET 9 Entwickler mit Clean Architecture Erfahrung.

[C] Online-Shop-Projekt: ASP.NET Core 9, EF Core 9, DDD, Clean Architecture.
    Domäne: Order (Aggregate Root), OrderLine (Entity), Product (Entity).

[E] Erstelle IOrderRepository (Interface) und EfOrderRepository (EF Core 9 Implementierung).
    Methoden: GetByIdAsync, GetByCustomerIdAsync (paginiert), SaveAsync, SoftDeleteAsync.

[F] Nur C#-Code. Zuerst Interface, dann Implementierung.
    XML-Dokumentation. CancellationToken überall. Keine Erklärungen.
```

---

## Lab 3.2 — Effektive Prompt-Strukturen entwickeln

### Few-Shot Prompting

Beispiele im Prompt verbessern Format und Stil der Ausgabe drastisch:

```
Erstelle Domain Events nach diesem Muster:

// Beispiel (genau so soll die Ausgabe aussehen):
public record OrderConfirmed(Guid OrderId, DateTime OccurredAt) : IDomainEvent;
public record OrderShipped(Guid OrderId, string TrackingNumber, DateTime OccurredAt) : IDomainEvent;

Erstelle nach exakt demselben Muster Events für:
- CustomerRegistered (mit FirstName, LastName, Email)
- ProductAddedToStock (mit ProductId, AddedQuantity, NewTotalStock)
- OrderCancelled (mit OrderId, Reason)
```

### Chain-of-Thought Prompting

Für komplexe Probleme: Explizit zum strukturierten Denken auffordern **bevor** die Antwort kommt:

```
Analysiere dieses Performance-Problem in exakt dieser Reihenfolge:

Schritt 1 - Mögliche Ursachen: Liste alle plausiblen Ursachen auf
Schritt 2 - Gewichtung: Sortiere nach Wahrscheinlichkeit (begründet)
Schritt 3 - Diagnose: Wie prüft man die wahrscheinlichste Ursache?
Schritt 4 - Erst jetzt: Vorgeschlagene Lösung

Problem: Die API-Antwortzeit steigt linear mit wachsender Datenbankgröße.
Kontext: .NET 9 API, EF Core 9, SQL Server, 500k Datensätze in Orders-Tabelle.
```

### System-Prompts und Persona

Für wiederholte Aufgaben: Persona am Anfang einer Session setzen:

```
Du bist ab jetzt ein erfahrener C#/.NET-Code-Reviewer mit DDD-Fokus.
Du reviewst jeden Code auf:
1. DDD-Verletzungen (öffentliche Setter, fehlende Validierung, Logik außerhalb der Entität)
2. EF Core Anti-Patterns (N+1, falscher Lifecycle, kein AsNoTracking bei readonly)
3. .NET 9 Verbesserungspotenzial (neuere APIs, C# 13 Features)

Format: Problem → Warum schlecht → Korrigierte Version
```

---

## Lab 3.3 — Best Practices für klare Prompts

### Goldene Regeln

**1. Positiv statt negativ formulieren**
```
❌ "Schreibe keinen zu komplexen Code"
✅ "Schreibe einfachen Code: max. 20 Zeilen pro Methode, sprechende Variablennamen"
```

**2. Frameworks und Versionen immer explizit nennen**
```
❌ "Nutze das aktuelle Framework"
✅ "Nutze .NET 9, EF Core 9, xUnit 2.9, FluentAssertions 6.12, NSubstitute 5"
```

**3. Ausgabeformat präzise steuern**
```
"Ausgabe: NUR C#-Code-Blöcke. Kein Erklärungstext. Keine Markdown-Überschriften.
 XML-Dokumentation auf Deutsch. Kommentare inline in englischer Sprache."
```

**4. Einschränkungen explizit benennen**
```
"Einschränkungen:
 - Keine statischen Methoden außer Factory-Methoden
 - Kein direkter DbContext im Application Layer
 - Alle Exceptions müssen spezifische Typen haben (keine Exception-Basis)"
```

### Typische Prompt-Fehler

| Fehler | Beispiel | Problem |
|---|---|---|
| Zu vage | „Verbessere meinen Code" | KI weiß nicht was „besser" bedeutet |
| Widersprüchlich | „Kurz aber vollständig und ausführlich" | Unmöglich zu optimieren |
| Kein Kontext | „Fix den Bug" (ohne Code) | KI kann nicht helfen |
| Alles auf einmal | 10 verschiedene Anforderungen in einem Prompt | Qualität leidet bei jeder |
| Keine Formatangabe | „Schreibe Tests" | Welches Framework? Welche Struktur? |

---

## Lab 3.4 — Prompting-Templates für den Entwickleralltag

### Template: Neue Klasse generieren
```
Du bist Senior C#-Entwickler. .NET 9, C# 13.
Erstelle [KLASSE] als [Entity / ValueObject / AggregateRoot / DomainService]:
Properties: [mit Typen und Nullable-Markierung]
Methoden: [mit Signaturen und Domänenregeln]
Validierung: [konkrete Regeln + Exception-Typ]
Anforderungen: private setter, protected EF-Ctor, XML-Docs, Domain Events falls sinnvoll.
Nur Code. Keine Erklärungen.
```

### Template: Unit-Tests generieren
```
Framework: xUnit + FluentAssertions + NSubstitute. .NET 9.
Erstelle Tests für: [KLASSE.METHODE]

Testfälle:
- Happy Path: [was soll erfolgreich durchlaufen]
- Fehlerfall 1: [was soll welche Exception werfen]
- Fehlerfall 2: [weiterer Fehlerfall]
- Grenzwert: [edge case]

Struktur: Arrange / Act / Assert (Kommentare).
Naming: MethodName_Szenario_ErwarteteAusgabe.
Nur Code. Testklasse heißt [KLASSE]Tests.
```

### Template: Code reviewen
```
Reviewe diesen C#-Code auf:
1. DDD-Verletzungen (öffentliche Setter, Validierung fehlt, Logik fehl am Platz)
2. EF Core 9 Anti-Patterns
3. .NET 9 Verbesserungspotenzial (C# 13, neue APIs)
4. Sicherheitsprobleme

Format pro Problem: Stelle benennen → Problem erklären → korrigierte Version zeigen
Sortierung: kritischste Probleme zuerst.

[CODE HIER]
```

### Template: Exception debuggen
```
Ich erhalte folgende Exception in .NET 9 / EF Core 9:
[EXCEPTION + STACKTRACE]

Kontext: [Was wurde gerade ausgeführt?]
Code: [Betroffener Code-Ausschnitt]

Analysiere in dieser Reihenfolge:
1. Ursache (präzise benennen)
2. Warum tritt das auf?
3. Fix (korrigierter Code)
4. Wie verhindert man das in Zukunft?
```
