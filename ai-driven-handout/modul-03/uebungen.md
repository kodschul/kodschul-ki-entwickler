# Modul 3 — Übungen

---

## Übung 3.1-A — Prompt-Qualität bewerten

Bewerten Sie die folgenden Prompts auf einer Skala von 1–5 Sterne. Identifizieren Sie jeweils welche CREF-Elemente fehlen und warum die Ausgabe problematisch wäre.

**Prompt 1:**
```
Hilf mir mit C#.
```

**Prompt 2:**
```
Schreibe eine Klasse für Bestellungen.
```

**Prompt 3:**
```
Du bist C#-Entwickler. Schreibe eine Order-Klasse mit Id, CustomerId, Status und Lines.
```

**Prompt 4:**
```
Du bist Senior .NET 9 Entwickler mit DDD-Erfahrung.
Erstelle Order als Aggregate Root:
- Id: Guid (private set)
- CustomerId: Guid (private set)
- Status: OrderStatus Enum (Open/Confirmed/Shipped/Completed, private set)
- Lines: IReadOnlyCollection<OrderLine> (readonly backing field)
- Methode Confirm(): Status-Übergang Open→Confirmed, Exception wenn keine Lines
- Methode AddLine(Product product, int quantity): nur wenn Status Open, Mengen-Validierung
.NET 9, private setter überall, XML-Docs, nur Code.
```

**Bewertungsvorlage:**

| Prompt | Sterne (1–5) | Fehlende CREF-Elemente | Erwartetes Problem |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

---

## Übung 3.1-B — CREF-Elemente ergänzen

Ergänzen Sie die jeweils fehlenden Elemente in diesen unvollständigen Prompts:

**Prompt A (Rolle fehlt):**
```
Wir entwickeln eine Lagerverwaltung in .NET 9.
Erstelle einen ProductService mit Methoden für Bestandsverwaltung.
Nur Code.
```
→ Welche Rolle soll die KI haben? Formulieren Sie den vollständigen Prompt.

**Prompt B (Kontext fehlt):**
```
Du bist erfahrener Softwarearchitekt.
Erstelle ein Interface IProductRepository.
```
→ Welcher Kontext fehlt? Ergänzen Sie ihn so, dass die Ausgabe direkt nutzbar ist.

**Prompt C (Format und Einschränkungen fehlen):**
```
Du bist Senior .NET-Entwickler in einem DDD-Projekt mit EF Core 9.
Analysiere dieses Datenbankmodell und identifiziere Probleme.
[Modell-Beschreibung]
```
→ Wie soll die Ausgabe strukturiert sein? Was sind die Einschränkungen?

---

## Übung 3.2-A — Few-Shot Prompt für FluentValidation

Schreiben Sie einen Few-Shot-Prompt, der eine KI dazu bringt, FluentValidation-Klassen in einem konsistenten Stil zu generieren.

**Muster-Validator (zeigen Sie das der KI):**
```csharp
public sealed class CreateCustomerValidator : AbstractValidator<CreateCustomerRequest>
{
    public CreateCustomerValidator()
    {
        RuleFor(x => x.FirstName)
            .NotEmpty().WithMessage("Vorname ist erforderlich.")
            .MaximumLength(100).WithMessage("Vorname darf maximal 100 Zeichen haben.");

        RuleFor(x => x.Email)
            .NotEmpty().WithMessage("E-Mail ist erforderlich.")
            .EmailAddress().WithMessage("Ungültige E-Mail-Adresse.");
    }
}
```

**Ziel-Request-Klasse:**
```csharp
public sealed record CreateProductRequest(
    string Name,
    decimal Price,
    int InitialStock,
    string? Description);
```

**Validierungsregeln:**
- Name: Pflichtfeld, 1–200 Zeichen
- Price: Pflichtfeld, größer 0, maximal 99.999,99
- InitialStock: Pflichtfeld, 0 bis 10.000
- Description: Optional, maximal 500 Zeichen

Schreiben Sie den vollständigen Few-Shot-Prompt und führen Sie ihn aus.

---

## Übung 3.2-B — Chain-of-Thought für Architekturentscheidungen

**Szenario:** Sie müssen entscheiden: **CQRS mit MediatR** oder **einfaches Service-Layer-Pattern** für eine neue .NET 9 Anwendung.

Formulieren Sie einen Chain-of-Thought-Prompt, der die KI zwingt, in dieser Reihenfolge zu denken:
1. Projektkontext einordnen
2. Vor- und Nachteile gegenüberstellen
3. Entscheidungskriterien gewichten (mit Bewertung 1–5)
4. Erst am Ende eine begründete Empfehlung geben

Kontext für Ihren Prompt: 4 Entwickler, mittelkomplexe Business-Logik, kein Event Sourcing, MVP in 3 Monaten gewünscht.

---

## Übung 3.3-A — Schlechte Prompts reparieren

Verbessern Sie folgende Prompts so, dass sie direkt nutzbare, hochwertige .NET 9 / C# Ausgaben erzeugen:

**Schlechter Prompt 1:**
```
Schreibe einen Controller.
```

**Schlechter Prompt 2:**
```
Mein Code hat einen Fehler:
public decimal Calculate(int a, int b) { return a / b; }
```

**Schlechter Prompt 3:**
```
Erkläre mir LINQ.
```

**Schlechter Prompt 4:**
```
Schreibe Tests für meine App. Die App hat Produkte und Bestellungen.
```

Für jeden Prompt: Benennen Sie das Problem, dann schreiben Sie die verbesserte Version.

---

## Übung 3.3-B — Persönliche Prompt-Bibliothek aufbauen

Schreiben Sie für **fünf** der folgenden Aufgaben einen vollständigen, wiederverwendbaren Prompt mit `[PLATZHALTERN]`:

1. Neue DDD-Entität generieren
2. Repository-Interface + EF Core 9 Implementierung
3. Unit-Tests für eine einzelne Methode
4. Code-Review einer Klasse
5. Exception + StackTrace analysieren und fixen
6. LINQ-Abfrage auf Performance optimieren
7. Async-Code auf Deadlock-Risiken prüfen
8. README.md für ein Modul schreiben

**Format pro Prompt:**
```markdown
## [Name der Aufgabe]

**Wann einsetzen:** [Kurzbeschreibung]

**Prompt:**
[Vollständiger Prompt mit [PLATZHALTERN]]

**Anleitung:** [Was muss in die Platzhalter?]
```

---

## Übung 3.4-A — Iterativer Verfeinerungsprozess

Entwickeln Sie in **vier Iterationen** eine vollständige `Product`-Klasse für das Online-Shop-Projekt.

**Iteration 1 — Grundstruktur:**
Starten Sie mit einem simplen Prompt. Dokumentieren Sie was generiert wurde.

**Iteration 2 — Domänenlogik ergänzen:**
Auf Basis des Ergebnisses: Methoden für Lagerbestandsverwaltung, Preisvalidierung, Domänenregeln hinzufügen.

**Iteration 3 — EF Core fit machen:**
Auf Basis des Ergebnisses: EF Core 9 Kompatibilität sicherstellen (protected Ctor, Owned Types, etc.)

**Iteration 4 — Tests generieren:**
Auf Basis der fertigen Klasse: xUnit + FluentAssertions Tests für alle Methoden.

**Dokumentieren Sie pro Iteration:**
- Ihren vollständigen Prompt
- Was die KI gut gemacht hat
- Was Sie manuell korrigieren mussten
- Was Sie beim nächsten Mal anders formulieren würden

---

## Übung 3.4-B — Prompt-Qualitätsnachweis

Beweisen Sie empirisch den Qualitätsunterschied zwischen drei Prompt-Stufen für denselben Use Case.

**Level 1 — Minimal:**
```
Schreibe einen OrderService in C#.
```

**Level 2 — Mittel:**
```
Schreibe einen C# OrderService mit Methoden für Bestellungen.
Nutze .NET 9 und EF Core 9.
```

**Level 3 — Vollständig (selbst formulieren nach CREF):**
Schreiben Sie einen vollständigen CREF-Prompt für einen `OrderApplicationService` mit:
- `PlaceOrderAsync(PlaceOrderCommand cmd, CancellationToken ct)`: Neue Bestellung aufgeben
- `ConfirmOrderAsync(Guid orderId, CancellationToken ct)`: Bestellung bestätigen
- `GetOrderDetailsAsync(Guid orderId, CancellationToken ct)`: Details laden → `OrderDetailsDto?`

**Auswertungsmatrix:**

| Kriterium | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Kompilierbar ohne Änderungen? | | | |
| Alle 3 Methoden vorhanden? | | | |
| CancellationToken in allen async? | | | |
| Fehlerbehandlung (KeyNotFoundException etc.)? | | | |
| XML-Dokumentation? | | | |
| Geschätzte Nachbearbeitungszeit (min) | | | |
