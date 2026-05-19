# Modul 9 — Softwaretests mit KI zur Qualitätsabsicherung

---

## Lab 9.1 — Teststrategie für KI-gestützte Entwicklung

### Die Testpyramide

```
         /\
        /  \       E2E-Tests (wenige, teuer, langsam)
       /────\      → Browser/API-Integration
      /      \
     /────────\    Integrationstests (mittel)
    /          \   → EF Core, HTTP, externe Services
   /────────────\
  /              \ Unit-Tests (viele, schnell, billig)
 /________________\ → Domänenlogik, Services, Validierung
```

**Faustregel:** 70% Unit · 20% Integration · 10% E2E

### Testarten im Überblick

| Testart | Was wird getestet? | Frameworks |
|---|---|---|
| Unit-Test | Einzelne Klasse/Methode, isoliert | xUnit, FluentAssertions, NSubstitute |
| Integrationstest | Mehrere Komponenten zusammen (EF Core + DB) | xUnit, EfCore.Testing / Testcontainers |
| API-Test | HTTP-Endpunkte über echten HTTP-Stack | `WebApplicationFactory<Program>` |
| E2E-Test | Vollständiger User-Workflow im Browser | Playwright, Selenium |

### KI-Unterstützung beim Testen

**Stärken:**
- Unit-Test-Gerüst aus Produktionscode generieren
- Testdaten in verschiedenen Variationen erzeugen
- Edge Cases und Grenzwerte vorschlagen
- Testbenennung und Struktur konsistent halten

**Grenzen:**
- Kennt keine impliziten Anforderungen
- Mock-Setup für komplexe Abhängigkeiten oft fehlerhaft
- Testen keinen echten fachlichen Wert ohne Domänenverständnis

---

## Lab 9.2 — Testdaten mit KI generieren

### Testdaten-Kategorien

| Typ | Beschreibung | Wann nötig |
|---|---|---|
| **Happy-Path-Daten** | Gültige Eingaben die erfolgreich verarbeitet werden sollen | Immer |
| **Boundary-Daten** | Grenzwerte (Min/Max, exakte Grenzen) | Immer |
| **Invalid-Daten** | Ungültige Eingaben die Exceptions auslösen | Immer |
| **Null/Empty-Daten** | Leere Strings, null, leere Collections | Immer |
| **Realistic-Daten** | Realistische Massendaten für Performance | Bei Last-Tests |

### Testdaten-Prompt
```
Generiere Testdaten für [KLASSE/METHODE].

Kategorien:
1. Happy Path (3 Varianten): gültige Eingaben die erfolgreich verarbeitet werden
2. Boundary (3 Varianten): Grenzwerte – genau am Limit, ein drüber, ein drunter
3. Invalid (3 Varianten): Eingaben die [EXCEPTION] werfen sollen
4. Edge Cases (2 Varianten): Sonderfälle

Format: xUnit [Theory] mit [InlineData] oder [MemberData].
.NET 9, C# 13.
```

### Realistische Massendaten
```csharp
// Bogus-Bibliothek für realistische Fake-Daten
using Bogus;

var faker = new Faker<Customer>("de")
    .RuleFor(c => c.FirstName, f => f.Name.FirstName())
    .RuleFor(c => c.LastName, f => f.Name.LastName())
    .RuleFor(c => c.Email, (f, c) => f.Internet.Email(c.FirstName, c.LastName));

var customers = faker.Generate(100);
```

---

## Lab 9.3 — Testdaten validieren und verbessern

### Plausibilitätsprüfungen für KI-generierte Daten

```
Prüfe diese Testdaten auf:
1. Fachliche Plausibilität (z. B. Check-out vor Check-in?)
2. Grenzwerte korrekt (genau an der Grenze, nicht daneben)?
3. Vollständigkeit (alle Zweige des zu testenden Codes abgedeckt?)
4. Duplikate oder redundante Fälle?
5. Fehlende kritische Szenarien (null, leer, Maximum)?

Testdaten: [InlineData-Liste einfügen]
Zu testende Methode: [Code einfügen]
```

### Coverage sicherstellen

Nach KI-Testgenerierung prüfen:
- Alle if/else-Zweige abgedeckt?
- Alle Exception-Pfade getestet?
- Switch-Expressions vollständig?
- Null-Checks abgedeckt?

```powershell
# Coverage messen
dotnet test --collect:"XPlat Code Coverage"
reportgenerator -reports:coverage.xml -targetdir:coveragereport
```

---

## Lab 9.4 — CRUD-Tests mit KI erzeugen

### Unit-Tests: Domänenlogik isoliert

```csharp
public sealed class BookingTests
{
    [Fact]
    public void Confirm_OpenBooking_ChangesStatusToConfirmed()
    {
        // Arrange
        var booking = CreatePendingBooking();

        // Act
        booking.Confirm();

        // Assert
        booking.Status.Should().Be(BookingStatus.Confirmed);
    }

    [Fact]
    public void Confirm_AlreadyConfirmed_ThrowsInvalidOperationException()
    {
        // Arrange
        var booking = CreateConfirmedBooking();

        // Act
        var act = () => booking.Confirm();

        // Assert
        act.Should().Throw<InvalidOperationException>()
           .WithMessage("*bestätigt*");
    }
}
```

### Integrationstests: EF Core mit echter Datenbank

```csharp
// Testcontainers für SQL Server
public sealed class BookingRepositoryTests(SqlServerFixture fixture) : IClassFixture<SqlServerFixture>
{
    [Fact]
    public async Task SaveAsync_NewBooking_CanBeRetrievedById()
    {
        // Arrange
        using var context = fixture.CreateDbContext();
        var repo = new EfBookingRepository(context);
        var booking = CreateTestBooking();

        // Act
        await repo.SaveAsync(booking);
        var retrieved = await repo.GetByIdAsync(booking.Id);

        // Assert
        retrieved.Should().NotBeNull();
        retrieved!.GuestId.Should().Be(booking.GuestId);
        retrieved.Status.Should().Be(BookingStatus.Pending);
    }
}
```

### KI-Prompt für CRUD-Tests
```
Du bist C#-Test-Entwickler. xUnit + FluentAssertions + NSubstitute. .NET 9.

Erstelle vollständige CRUD-Tests für [REPOSITORY/SERVICE]:

Create:  - Neues Objekt wird korrekt gespeichert
         - Pflichtfeld fehlt → Exception
Read:    - Existierendes Objekt wird gefunden
         - Nicht existierende ID → null zurück
Update:  - Vorhandenes Objekt wird aktualisiert
         - Unveränderliche Felder bleiben unverändert
Delete:  - Soft Delete setzt IsDeleted = true
         - Hard Delete entfernt den Datensatz

Kontext: [Klasse + Interface einfügen]
Naming: MethodName_Szenario_ErwarteteAusgabe.
```
