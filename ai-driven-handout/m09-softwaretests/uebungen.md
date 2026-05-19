# Modul 9 — Übungen

---

## Übung 9.1-A — Teststrategie entwickeln

**Aufgabe:** Entwickeln Sie eine vollständige Teststrategie für das Hotelreservierungssystem.

Für jede Schicht definieren Sie:

| Schicht | Testart | Framework | Abdeckungsziel | Beispiel-Testfall |
|---|---|---|---|---|
| Domain (Booking, Room...) | | | | |
| Application (BookingApplicationService) | | | | |
| Infrastructure (EfBookingRepository) | | | | |
| API (BookingsController) | | | | |
| E2E (Buchungsworkflow) | | | | |

**Begründen Sie:** Warum dieser Mix? Warum nicht alles E2E?

---

## Übung 9.1-B — KI und Tests einordnen

**Aussage:** *„KI schreibt die Tests, wir müssen uns ums Testen keine Gedanken mehr machen."*

Analysieren Sie diese Aussage:
1. Was stimmt daran? (Konkrete Vorteile KI-generierter Tests)
2. Was ist gefährlich? (Konkrete Risiken und blinde Flecken)
3. Formulieren Sie eine realistischere Aussage über den Einsatz von KI beim Testen

---

## Übung 9.2-A — Testdaten mit KI generieren

**Aufgabe:** Generieren Sie Testdaten für `Booking.CalculateCancellationFee(DateTimeOffset cancellationTime)`.

1. Erstellen Sie einen Testdaten-Prompt der alle Kategorien abdeckt
2. Führen Sie den Prompt aus
3. Erzeugen Sie mindestens:
   - 3 Happy-Path-Varianten (kostenlose Stornierung)
   - 3 Boundary-Varianten (genau 48h, 24h und Grenzwerte drum herum)
   - 3 Invalid-Varianten (nach Check-in, nach Check-out)
   - 2 Edge Cases (Mitternacht, Zeitzonen)

**Format:** xUnit `[Theory]` mit `[InlineData]` oder `[MemberData]`

---

## Übung 9.2-B — Realistische Testdaten für Integrationstests

**Aufgabe:** Erstellen Sie einen `BookingTestDataBuilder` (Builder-Pattern) der realistische, konfigurierbare Testdaten erzeugt.

```csharp
// Gewünschte Verwendung:
var booking = BookingTestDataBuilder.Create()
    .WithRoom(roomId: Guid.NewGuid(), pricePerNight: 129m)
    .WithGuest(guestId: Guid.NewGuid())
    .WithDates(checkIn: DateTime.Today.AddDays(10), checkOut: DateTime.Today.AddDays(13))
    .AsConfirmed()
    .Build();
```

Nutzen Sie KI um den Builder zu generieren. Prüfen Sie:
- Sind Default-Werte sinnvoll (gültige Daten)?
- Lässt sich jede relevante Eigenschaft konfigurieren?
- Funktioniert Chaining korrekt?

---

## Übung 9.3-A — KI-Testdaten validieren

**Aufgabe:** Die folgende KI-generierte Testdatenliste enthält Probleme. Finden Sie sie.

```csharp
[Theory]
[InlineData("2025-01-15", "2025-01-14", 100.00)]  // A
[InlineData("2025-01-15", "2025-01-15", 100.00)]  // B
[InlineData("2025-01-15", "2025-01-16", 100.00)]  // C
[InlineData("2025-01-15", "2025-01-16", 0.00)]    // D
[InlineData("2025-01-15", "2025-01-16", -50.00)]  // E
[InlineData("2025-01-15", "2025-01-22", 100.00)]  // F
[InlineData("2025-01-15", "2025-01-22", 100.00)]  // G
public void CalculatePrice_ReturnsExpectedTotal(string checkIn, string checkOut, decimal pricePerNight)
```

Für jede Zeile (A–G): Ist dieser Testfall sinnvoll? Falls nicht, warum?

---

## Übung 9.3-B — Testabdeckung analysieren

**Aufgabe:** Analysieren Sie ob die folgenden Tests die Methode vollständig abdecken.

**Methode:**
```csharp
public void AddLine(Product product, int quantity)
{
    if (Status != OrderStatus.Open)
        throw new InvalidOperationException("Nur offene Bestellungen können bearbeitet werden.");
    if (quantity <= 0)
        throw new ArgumentOutOfRangeException(nameof(quantity), "Menge muss positiv sein.");
    if (!product.HasSufficientStock(quantity))
        throw new InvalidOperationException($"Unzureichender Lagerbestand für {product.Name}.");
    _lines.Add(new OrderLine(product, quantity));
}
```

**Vorhandene Tests:**
```csharp
[Fact] void AddLine_ValidProduct_AddsToLines() { ... }
[Fact] void AddLine_ZeroQuantity_ThrowsArgumentOutOfRange() { ... }
```

1. Welche Zweige sind NICHT abgedeckt?
2. Schreiben Sie die fehlenden Tests (mit KI-Unterstützung)
3. Welcher Grenzwert fehlt noch?

---

## Übung 9.4-A — CRUD-Tests für Repository

**Aufgabe:** Erstellen Sie vollständige CRUD-Tests für `EfBookingRepository`.

Erstellen Sie einen KI-Prompt der Tests für alle CRUD-Operationen generiert:
- `SaveAsync`: neue Buchung speichern, existierende aktualisieren
- `GetByIdAsync`: existierende ID, nicht existierende ID
- `GetByGuestIdAsync`: Buchungen für Gast, Buchungen paginiert, kein Ergebnis
- `SoftDeleteAsync`: IsDeleted wird gesetzt, Booking danach nicht mehr gefunden

**Setup:** Nutzen Sie entweder:
- **In-Memory:** `UseInMemoryDatabase` (schnell aber begrenzt)
- **SQLite:** `UseSqlite("Data Source=:memory:")` (näher an Produktion)
- **Testcontainers:** SQL Server Container (produktionsnah, langsamer)

---

## Übung 9.4-B — API-Tests mit WebApplicationFactory

**Aufgabe:** Erstellen Sie API-Tests für den `BookingsController`.

```csharp
public sealed class BookingsControllerTests(WebApplicationFactory<Program> factory)
    : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client = factory.CreateClient();

    [Fact]
    public async Task GetById_ExistingBooking_Returns200WithBookingDetails() { ... }

    [Fact]
    public async Task GetById_NonExistingBooking_Returns404() { ... }

    [Fact]
    public async Task CreateBooking_ValidRequest_Returns201WithId() { ... }

    [Fact]
    public async Task CreateBooking_InvalidDates_Returns400WithValidationErrors() { ... }
}
```

Nutzen Sie KI um die Testklasse vollständig zu implementieren. Prüfen Sie:
- Wird eine Testdatenbank verwendet (nicht Produktionsdatenbank)?
- Sind HTTP-Statuscodes korrekt geprüft?
- Wird der Response-Body deserialisiert und geprüft?
