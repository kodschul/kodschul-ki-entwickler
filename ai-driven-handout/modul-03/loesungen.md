# Modul 3 — Lösungen

---

## Lösung 3.1-A — Prompt-Qualität bewerten

| Prompt | Sterne | Fehlende Elemente | Erwartetes Problem |
|---|---|---|---|
| 1 | ⭐ | Alles: Rolle, Kontext, Erwartung, Format | Ausgabe: irgendein Code in irgendeiner Sprache |
| 2 | ⭐⭐ | Rolle, Framework, Eigenschaften, Format | Unvollständige Klasse, falsches Muster, unbekannte Felder |
| 3 | ⭐⭐⭐ | Methoden, Validierung, Format, Framework | Klasse vorhanden aber ohne Domänenlogik, public setter |
| 4 | ⭐⭐⭐⭐⭐ | Vollständig | Direkt nutzbare, korrekte DDD-Implementierung |

---

## Lösung 3.1-B — Fehlende Elemente ergänzen

**Prompt A — Rolle und Format ergänzt:**
```
Du bist Senior .NET 9 Entwickler mit DDD- und Clean-Architecture-Erfahrung.

Kontext: Lagerverwaltungssystem, .NET 9, Clean Architecture.
Entität: Product (Id: Guid, Name: string, Price: decimal, Stock: int)

Erstelle IProductStockService (Interface) und ProductStockService (Implementierung):
- AddStockAsync(Guid productId, int quantity, CancellationToken ct)
- ReduceStockAsync(Guid productId, int quantity, CancellationToken ct)
- GetStockLevelAsync(Guid productId, CancellationToken ct) → int

Einschränkungen: IProductRepository per DI, KeyNotFoundException wenn nicht gefunden,
InvalidOperationException wenn Bestand negativ würde.
Nur Code. XML-Docs. CancellationToken überall.
```

**Prompt B — Kontext ergänzt:**
```
Du bist erfahrener Softwarearchitekt.

Kontext:
- Projekt: Online-Shop mit Clean Architecture und DDD
- ORM: EF Core 9, SQL Server
- Entität: Product (Id: Guid, Name: string, Price: decimal, Stock: int, IsDeleted: bool)
- Muster: Repository + Unit of Work

Erstelle IProductRepository mit:
- GetByIdAsync(Guid id, CancellationToken ct) → Product?
- SearchAsync(string? term, int page, int pageSize, CancellationToken ct) → PagedResult<Product>
- SaveAsync(Product product, CancellationToken ct)
- SoftDeleteAsync(Guid id, CancellationToken ct)

XML-Docs. CancellationToken überall. Nur Interface (keine Implementierung).
```

**Prompt C — Format und Einschränkungen ergänzt:**
```
Du bist Senior .NET-Architekt mit DDD-Expertise und EF Core 9 Kenntnissen.

Analysiere dieses Datenbankmodell und identifiziere Probleme:
[Modell-Beschreibung]

Ausgabe-Format:
Für jedes Problem:
  Stelle: [Tabellenname.Spalte oder Beziehung]
  Problem: [Was ist falsch und warum?]
  Auswirkung: [Was passiert dadurch in der Anwendung?]
  Lösung: [Korrigierte EF Core Konfiguration als C#-Code]

Sortierung: Kritischste Probleme (Data Loss, Inkonsistenz) zuerst.
Abschluss: Gesamtbewertung in 2-3 Sätzen.
```

---

## Lösung 3.2-A — Few-Shot Validator (Musterlösung)

**Vollständiger Prompt:**
```
Du bist Senior C#-Entwickler mit FluentValidation-Expertise. .NET 9.

Erstelle einen Validator exakt nach diesem Muster:

// Muster (genau so soll die Ausgabe aussehen):
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

Erstelle nach exakt diesem Stil einen Validator für:

public sealed record CreateProductRequest(string Name, decimal Price, int InitialStock, string? Description);

Validierungsregeln:
- Name: Pflichtfeld, 1–200 Zeichen
- Price: Pflichtfeld, > 0, ≤ 99999.99
- InitialStock: 0–10000 (InclusiveBetween)
- Description: Optional, maximal 500 Zeichen (nur wenn nicht null prüfen)

Fehlermeldungen auf Deutsch. Nur Code. Kein Erklärungstext.
```

**Erwartetes Ergebnis:**
```csharp
public sealed class CreateProductValidator : AbstractValidator<CreateProductRequest>
{
    public CreateProductValidator()
    {
        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Name ist erforderlich.")
            .Length(1, 200).WithMessage("Name muss zwischen 1 und 200 Zeichen lang sein.");

        RuleFor(x => x.Price)
            .GreaterThan(0).WithMessage("Preis muss größer als 0 sein.")
            .LessThanOrEqualTo(99999.99m).WithMessage("Preis darf 99.999,99 nicht überschreiten.");

        RuleFor(x => x.InitialStock)
            .InclusiveBetween(0, 10000).WithMessage("Lagerbestand muss zwischen 0 und 10.000 liegen.");

        RuleFor(x => x.Description)
            .MaximumLength(500).WithMessage("Beschreibung darf maximal 500 Zeichen haben.")
            .When(x => x.Description is not null);
    }
}
```

---

## Lösung 3.3-A — Schlechte Prompts repariert

**Prompt 1 repariert:**
```
Du bist Senior ASP.NET Core 9 Entwickler.

Erstelle ProductsController (Web API, [ApiController]):
- GET /api/products → alle Produkte paginiert (Parameter: page=1, pageSize=20, search?)
- GET /api/products/{id} → einzelnes Produkt (404 wenn nicht gefunden)
- POST /api/products → neues Produkt anlegen (400 bei Validierungsfehler)
- PUT /api/products/{id} → aktualisieren
- DELETE /api/products/{id} → Soft Delete

Anforderungen: IProductService per DI injizieren, ProducesResponseType-Attribute,
ILogger<ProductsController>, CancellationToken, XML-Docs. Nur Code.
```

**Prompt 2 repariert:**
```
Dieser C#-Code enthält einen kritischen Fehler:

public decimal Calculate(int a, int b) { return a / b; }

1. Erkläre präzise welcher Fehler auftritt und bei welchen Eingaben
2. Zeige die korrekte Lösung mit Validierung (ArgumentException wenn b == 0)
3. Zeige außerdem den Integer-Division-Fehler und wie man ihn behebt
4. Schreibe xUnit + FluentAssertions Tests die beide Fehler nachweisen und den Fix bestätigen
```

**Prompt 3 repariert:**
```
Du bist .NET-Trainer. Erkläre LINQ für einen C#-Junior (1 Jahr Erfahrung).

Struktur:
1. Was ist LINQ und warum ist es nützlich? (3 Sätze)
2. Die 5 wichtigsten Operatoren mit je einem Beispiel aus einem Online-Shop-Kontext
3. Method Syntax vs. Query Syntax – wann was?
4. Häufiger Fehler: N+1 Problem mit EF Core (Beispiel + Fix)

Alle Code-Beispiele: Orders, Products, Customers (konsistentes Domänenmodell). .NET 9.
```

**Prompt 4 repariert:**
```
Du bist erfahrener C#-Entwickler. Framework: xUnit + FluentAssertions + NSubstitute. .NET 9.

Testklasse: OrderServiceTests
Zu testende Methode: OrderApplicationService.ConfirmOrderAsync(Guid orderId, CancellationToken ct)

Verhalten:
- Bestätigt eine Order (Status: Open → Confirmed) und speichert sie
- Wirft KeyNotFoundException wenn Order mit orderId nicht gefunden
- Wirft InvalidOperationException wenn Status != Open

Testfälle:
1. Happy Path: offene Order → erfolgreich bestätigt + Repository.SaveAsync aufgerufen
2. Not Found: nicht vorhandene ID → KeyNotFoundException
3. Falscher Status: bereits bestätigte Order → InvalidOperationException

Mocking: IOrderRepository mit NSubstitute mocken.
Naming: ConfirmOrderAsync_Szenario_ErwarteteAusgabe. Nur Code.
```

---

## Lösung 3.4-B — Vollständiger Level-3-Prompt (Muster)

```
Du bist Senior .NET-Entwickler mit Clean Architecture und DDD-Expertise.

[C] Kontext:
- Online-Shop, .NET 9, EF Core 9, Clean Architecture
- Pattern: Application Service (kein MediatR)
- Interfaces: IOrderRepository, ICustomerRepository, IProductRepository
- CancellationToken in allen async-Methoden

[R] Rolle: Senior .NET-Architekt der sauberen, wartbaren Code schreibt.

[E] Erstelle OrderApplicationService mit diesen drei Methoden:

1. PlaceOrderAsync(PlaceOrderCommand cmd, CancellationToken ct) → Guid
   - Customer laden (KeyNotFoundException wenn nicht gefunden)
   - Alle Produkte laden + Lagerbestand prüfen (InvalidOperationException wenn unzureichend)
   - Order mit OrderLines erstellen
   - Speichern + OrderId zurückgeben

2. ConfirmOrderAsync(Guid orderId, CancellationToken ct)
   - Order laden (KeyNotFoundException wenn nicht gefunden)
   - order.Confirm() aufrufen (wirft InvalidOperationException bei falschem Status)
   - Speichern

3. GetOrderDetailsAsync(Guid orderId, CancellationToken ct) → OrderDetailsDto?
   - Order laden, auf OrderDetailsDto mappen, null zurückgeben wenn nicht gefunden

Records:
- PlaceOrderCommand(Guid CustomerId, IReadOnlyList<OrderLineRequest> Lines)
- OrderLineRequest(Guid ProductId, int Quantity)
- OrderDetailsDto(Guid Id, string CustomerName, string Status, decimal Total, IReadOnlyList<OrderLineDto> Lines)
- OrderLineDto(string ProductName, int Quantity, decimal UnitPrice, decimal LineTotal)

[F] Format:
- Nur C#-Code. Kein Fließtext.
- ILogger<OrderApplicationService> per DI, kritische Operationen loggen
- XML-Docs für alle public Member auf Deutsch
- Records am Ende der Datei
```

**Erwartete Qualitätsunterschiede:**

| Kriterium | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Kompilierbar | Nein | Teils | Ja |
| Alle Methoden | Nein | Teils | Ja |
| CancellationToken | Nein | Teils | Ja |
| Fehlerbehandlung | Nein | Nein | Ja |
| XML-Docs | Nein | Nein | Ja |
| Nachbearbeitungszeit | 60+ min | 20–30 min | 5–10 min |
