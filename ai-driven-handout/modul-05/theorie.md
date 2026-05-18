# Modul 5 — Fachliche Modellierung mit Domain Driven Design

---

## Lab 5.1 — DDD für KI-gestützte Entwicklung einordnen

### Die drei Kernideen

**Ubiquitous Language** — Eine gemeinsame Fachsprache die Domänenexperten und Entwickler verwenden. Begriffe aus Gesprächen erscheinen 1:1 im Code:

```
Gespräch:  „Eine Buchung kann storniert werden, bis 48 Stunden vor Check-in."
Code:      booking.Cancel(cancellationTime);  // nicht: booking.Delete() oder booking.SetInactive()
```

**Bounded Context** — Große Systeme in fachliche Grenzen aufteilen. „Kunde" bedeutet im Vertriebskontext etwas anderes als im Versandkontext.

**Domain Model** — Strukturiertes Abbild der Fachlichkeit: Entitäten, Value Objects, Aggregate, Domain Events.

### KI im DDD-Prozess

```
Anforderungstext (natürliche Sprache)
         │
         ▼  KI analysiert
Kandidaten für Entitäten / Value Objects / Events
         │
         ▼  Mensch prüft fachlich
Validiertes Domänenmodell
         │
         ▼  KI generiert
C#-Klassen-Gerüst
         │
         ▼  Mensch ergänzt Domänenlogik
Fertige Implementierung
```

**KI-Stärken in der Modellierung:** Entitäten aus Fließtext identifizieren, Ubiquitous Language vorschlagen, Klassengerüste generieren.

**KI-Schwächen:** Versteht implizite Fachregeln nicht, ohne expliziten Kontext modelliert sie generisch.

---

## Lab 5.2 — Fachliche Anforderungen in Domänenmodelle überführen

### DDD-Bausteine in C#

**Entity** — Eindeutige Identität, Lebenszyklus:
```csharp
public class Order : Entity   // gleiche Id = gleiche Bestellung, egal ob Status sich ändert
```

**Value Object** — Keine Identität, unveränderlich, Gleichheit über Inhalt:
```csharp
public sealed record Email(string Value)   // zwei Emails mit gleichem Value sind gleich
{
    public Email(string value) : this(value)
    {
        if (!value.Contains('@')) throw new ArgumentException("Ungültige E-Mail.");
    }
}
```

**Aggregate Root** — Einstiegspunkt, kontrolliert Konsistenz aller Kinder:
```csharp
public class Order : Entity
{
    private readonly List<OrderLine> _lines = [];
    public IReadOnlyCollection<OrderLine> Lines => _lines.AsReadOnly();
    // OrderLine nur über Order zugänglich – nie direkt!
}
```

**Domain Event** — Was fachlich Wichtiges passiert ist (Vergangenheitsform!):
```csharp
public record OrderConfirmed(Guid OrderId, DateTime OccurredAt) : IDomainEvent;
```

### Entscheidung: Entity oder Value Object?

**Entity wenn:** eigene Identität, Lebenszyklus, Mutabilität (Fahrer, Bestellung, Produkt)

**Value Object wenn:** Gleichheit über Inhalt, unveränderlich, keine eigene Identität (Adresse, Geldbetrag, E-Mail, GPS-Koordinate)

---

## Lab 5.3 — Klassendiagramme mit draw.io

### UML-Beziehungen

| Notation | Typ | Beispiel |
|---|---|---|
| `──────◆` | Komposition (stark, Lifecycle-Abhängigkeit) | Order „besitzt" OrderLine |
| `──────◇` | Aggregation (schwach, keine Lifecycle-Abhängigkeit) | Order referenziert Product |
| `──────>` | Assoziation mit Navigationsrichtung | Order → Customer (via Id) |
| `- - - ->` | Abhängigkeit / Nutzung | Service → Repository Interface |

### draw.io Workflow

1. Neue Datei anlegen → UML-Bibliothek aktivieren
2. Klassen-Shapes (dreigeteilt: Name / Properties / Methoden)
3. Beziehungen mit korrekter Notation verbinden
4. Als `.drawio.xml` im Repository speichern (textbasiert, diff-fähig)
5. Export als PNG/SVG für Dokumentation

**KI-Prompt für draw.io XML-Export:**
```
Erstelle ein valides draw.io XML-Klassendiagramm für:
- Order (Aggregate Root): Id, CustomerId, Status (Enum), Lines, CreatedAt
- OrderLine (Entity): Id, ProductId, Quantity, UnitPrice, LineTotal
- Customer (Aggregate Root): Id, FirstName, LastName, Email (Value Object)
- Product (Aggregate Root): Id, Name, Price, Stock

Zeige Beziehungen mit Kardinalitäten (1, 0..*, 1..*).
Valides draw.io XML ausgeben – direkt importierbar.
```

---

## Lab 5.4 — Fachmodell und technisches Modell abstimmen

### Die drei Ebenen

| Ebene | Inhalt | Abhängigkeiten |
|---|---|---|
| Domain Layer | Entities, Value Objects, Domain Events, Interfaces | Keine |
| Application Layer | Commands, Queries, DTOs, Application Services | → Domain |
| Infrastructure Layer | EF Core, Repositories, external APIs | → Application, → Domain |

### Typische Spannungen

| Fachmodell-Wunsch | Technisches Modell-Bedarf | Lösung |
|---|---|---|
| private setter | EF Core braucht Zugriff | `protected` Konstruktor + Reflection |
| Value Object als Record | EF Core Owned Type | `.OwnsOne()` in Konfiguration |
| Enum in Domäne | Lesbare DB-Spalte | `.HasConversion<string>()` |
| Keine Navigation zurück | EF Core Queries brauchen sie | Bidirektionale Navigation, aber privat |

### Häufige KI-Fehler bei DDD-Klassen

```csharp
// KI generiert oft so – und das ist falsch:
public class Order
{
    public int Id { get; set; }                        // ❌ int statt Guid
    public string Status { get; set; } = "Open";       // ❌ string statt Enum
    public List<OrderLine> Lines { get; set; } = [];   // ❌ public List + public setter
    public Order() { }                                 // ❌ public Ctor (EF Core braucht protected)

    public void SetStatus(string status) { Status = status; } // ❌ generischer Setter
}
```

```csharp
// So sollte es aussehen:
public class Order : Entity
{
    public Guid CustomerId { get; private set; }
    public OrderStatus Status { get; private set; }
    private readonly List<OrderLine> _lines = [];
    public IReadOnlyCollection<OrderLine> Lines => _lines.AsReadOnly();

    protected Order() { }  // EF Core

    public void Confirm() { /* Domänenlogik mit Status-Guard */ }
}
```
