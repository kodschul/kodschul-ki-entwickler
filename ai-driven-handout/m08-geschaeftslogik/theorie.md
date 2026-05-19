# Modul 8 — Geschäftslogik mit KI strukturiert implementieren

---

## Lab 8.1 — Geschäftslogik aus Anforderungen ableiten

### Wo lebt Geschäftslogik?

```
Controller / Razor Views     → KEINE Geschäftslogik
Application Services         → Orchestrierung (lädt Repos, ruft Domain auf)
Domain Layer (Entitäten)     → HIER lebt Geschäftslogik
Infrastructure (EF Core)     → KEINE Geschäftslogik
```

### Regelkategorien

**Muss-Regeln** (immer gültig, Exception wenn verletzt):
> „Eine Bestellung kann nur bestätigt werden wenn sie mindestens eine Position enthält."

**Kann-Regeln** (konfigurierbar, Standardverhalten):
> „Stammkunden erhalten 10% Rabatt."

**Verbots-Regeln** (Pre-Conditions):
> „Lagerbestand darf nie negativ werden."

**KI-Prompt zur Regelextraktion:**
```
Analysiere diese Anforderung. Kategorisiere alle Geschäftsregeln:
- Muss-Regeln: [immer gültig, wirft Exception]
- Kann-Regeln: [konfigurierbar, Default-Verhalten]
- Verbots-Regeln: [Pre-Conditions, verhindert Aktion]
- Invarianten: [muss immer wahr sein]

Für jede Regel: Wo implementieren? (Entitäts-Methode / Domain Service / Application Service)

Anforderung: [Text]
```

---

## Lab 8.2 — Geschäftslogik implementieren und integrieren

### Entitätsmethode vs. Domain Service

**Entitätsmethode** (bevorzugt) – wenn nur ein Aggregate betroffen:
```csharp
public void Confirm()  // Order kennt ihre eigenen Regeln
{
    if (!_lines.Any()) throw new InvalidOperationException("Leere Bestellungen können nicht bestätigt werden.");
    if (Status != OrderStatus.Open) throw new InvalidOperationException("Nur offene Bestellungen können bestätigt werden.");
    Status = OrderStatus.Confirmed;
    _events.Add(new OrderConfirmed(Id, DateTime.UtcNow));
}
```

**Domain Service** – wenn mehrere Aggregate oder externe Informationen nötig:
```csharp
public sealed class BookingPricingService
{
    public decimal Calculate(Room room, Guest guest, DateTime checkIn, DateTime checkOut)
    {
        // Braucht Informationen aus Room UND Guest → kein einzelnes Aggregate
        var nights = (checkOut - checkIn).Days;
        var basePrice = room.PricePerNight * nights;
        var discount = guest.CompletedBookingsCount > 5 ? 0.10m : 0m;
        return basePrice * (1 - discount);
    }
}
```

### Saubere Application Service Struktur

```csharp
public async Task ConfirmOrderAsync(Guid orderId, CancellationToken ct)
{
    // 1. Laden (Infrastruktur → Application)
    var order = await _orderRepo.GetByIdAsync(orderId, ct)
        ?? throw new KeyNotFoundException($"Bestellung {orderId} nicht gefunden.");

    // 2. Domänenlogik delegieren (Application ruft Domain auf)
    order.Confirm();    // wirft InvalidOperationException wenn nicht möglich

    // 3. Persistieren (Application → Infrastruktur)
    await _orderRepo.SaveAsync(order, ct);
}
```

---

## Lab 8.3 — KI gezielt für Logikimplementierung nutzen

### KI-Stärken

- ✅ Berechnungslogik (Preise, Rabatte, Steuern, Stornierungsgebühren)
- ✅ Status-Maschinen mit Guards implementieren
- ✅ Edge Cases vorschlagen die man übersehen hätte
- ✅ Validierungslogik und Guard-Klauseln

### KI-Grenzen

- ❌ Fachdomäne kennt die KI nicht – implizite Regeln werden ignoriert
- ❌ Komplexe Multi-Aggregate-Interaktionen werden oft falsch platziert
- ❌ Zeitzonenprobleme (DateTime vs. DateTimeOffset) werden übersehen
- ❌ Race Conditions und Nebenläufigkeit werden nicht berücksichtigt

### Review-Prompt für Geschäftslogik
```
Reviewe diese Geschäftslogik gegen folgende Anforderungen:

Anforderungen: [Regeln aus Lab 8.1]
Code: [Implementierung]

Prüfe auf:
1. Alle Regeln vollständig implementiert?
2. Fehlende Edge Cases?
3. Logik in richtiger Schicht?
4. Zeitzonen korrekt (DateTimeOffset statt DateTime für Grenzwertberechnungen)?
5. Exception-Typen korrekt?
```

---

## Lab 8.4 — Fachlichkeit, Datenmodell und Logik zusammenführen

### Integrations-Checkliste

- [ ] Domain Events werden vom Application Layer dispatched
- [ ] Repository-Calls ausschließlich im Application Layer (nie in Controllern)
- [ ] Kein `DbContext` im Domain Layer
- [ ] Zusammengehörige Operationen in einer Transaktion
- [ ] Domain-Exceptions von Infrastructure-Exceptions unterschieden
- [ ] CancellationToken in allen async-Methoden
- [ ] Logging für kritische Operationen

### Transaktionen korrekt einsetzen

```csharp
public async Task ConfirmAndNotifyAsync(Guid orderId, CancellationToken ct)
{
    using var tx = await _context.Database.BeginTransactionAsync(ct);
    try
    {
        var order = await _orderRepo.GetByIdAsync(orderId, ct)
            ?? throw new KeyNotFoundException();

        order.Confirm();
        await _orderRepo.SaveAsync(order, ct);
        await _emailService.SendConfirmationAsync(order.CustomerEmail, ct);

        await tx.CommitAsync(ct);
    }
    catch
    {
        await tx.RollbackAsync(ct);
        throw;
    }
}
```
