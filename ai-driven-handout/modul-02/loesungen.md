# Modul 2 — Lösungen

---

## Lösung 2.1-A — Anbieter-Steckbriefe (Muster)

```
Anbieter:         Anthropic (Claude)
Hauptmodell:      Claude Sonnet 4.5 / Claude Opus 4 (2025)
Kontextfenster:   200.000 Token
Serverstandort:   USA (AWS) / EU über AWS Frankfurt optional
DSGVO-konform:    Bedingt – AVV verfügbar, aber US-Server
Preismodell:      Free (claude.ai), Pro 20$/Monat, API pay-per-token
Stärke:           Größtes Kontextfenster, hervorragend bei langen Codebasen
                  und Anforderungsanalysen, weniger Halluzinationen
Schwäche:         Kein natives Web-Browsing ohne Tool-Integration
Ideal für:        Lange Code-Reviews, Architektur-Diskussionen,
                  Anforderungsdokumente analysieren, Dokumentation erstellen
```

```
Anbieter:         Mistral AI (Le Chat)
Hauptmodell:      Mistral Large 2 / Mistral Small
Kontextfenster:   128.000 Token
Serverstandort:   EU (Frankreich) ✓
DSGVO-konform:    Ja – EU-Unternehmen, EU-Server, DSGVO-nativ
Preismodell:      Free Tier (Le Chat), API pay-per-token, Open-Source-Modelle kostenlos
Stärke:           EU-Datenschutz ohne Kompromisse, Open-Source-Modelle
                  für On-Premise-Betrieb, gute Coding-Qualität
Schwäche:         Kleinerer Ökosystem als OpenAI/Anthropic, weniger Tools
Ideal für:        DSGVO-kritische Projekte, Banken/Versicherungen,
                  On-Premise-Deployments, EU-Behörden
```

---

## Lösung 2.1-B — Krankenhaus-Szenario

**Sofort ausgeschlossene Dienste:**
- ChatGPT (Standard): US-Server, kein ausreichender AVV für Gesundheitsdaten
- Perplexity: Keine AVV, Cloud-basiert, kein medizinischer Datenschutz
- Standard-Copilot (Free/Individual): Fließt in Training, kein AVV

**Grundsätzlich geeignet:**
- **Azure OpenAI Service (EU-Region):** Daten bleiben in EU, kein Training, AVV mit Microsoft
- **GitHub Copilot Enterprise:** DSGVO-konform, kein Training auf Unternehmens-Code, AVV möglich
- **On-Premise (Ollama + Llama 3):** Kein Datenaustausch, volle Kontrolle, keine externen Server

**Zwingend erforderlich:**
1. AVV nach DSGVO Art. 28 mit jedem KI-Anbieter
2. Nachweis EU-Serverstandort (oder SCCs für US-Anbieter)
3. Garantie: Keine Nutzung der Daten für Modell-Training
4. Sicherheitsaudit des Anbieters (ISO 27001, SOC 2)
5. Verbot der Eingabe echter Patientendaten – nur pseudonymisiert

**Datenschutzkonforme Architektur:**
```
Entwickler-PC (intern, klinikinternes Netz)
    │
    ├── GitHub Copilot Enterprise → Code-Completion (nur Code-Dateien, keine Patientendaten)
    │
    └── Internes KI-Gateway (eigener Server)
            │ Logging + Prompt-Filter
            ├── Azure OpenAI (EU-Region) → für Chat/Analyse
            │   (Anonymisierte/pseudonymisierte Eingaben only)
            └── Ollama/Llama 3 (On-Premise) → für sensible Domänenfragen
```

---

## Lösung 2.2-A — Kopf-an-Kopf (Erwartete Ergebnisse)

**Die drei Ansätze, die beide nennen sollten:**

1. **In-Process Events mit MediatR** (INotification)
   - Einfach, kein externer Broker, ideal als Startpunkt
   - Kein persistentes Messaging, kein Failover

2. **Message Queue (RabbitMQ + MassTransit oder Azure Service Bus)**
   - Persistent, entkoppelt, skalierbar
   - Mehr Infrastruktur, höhere Komplexität

3. **Outbox Pattern** (EF Core + Background Service)
   - Atomare Persistenz von Event + Datenbankoperation
   - Komplexer zu implementieren, aber sehr zuverlässig

**Typische Unterschiede Claude vs. ChatGPT:**

| Kriterium | Claude | ChatGPT |
|---|---|---|
| Erklärungen | Ausführlicher, didaktischer | Kompakter, direkter |
| Empfehlung | Nuancierter, mit Caveats | Eindeutiger, klarer |
| Code-Stil | Meist modernes C# | Gut, teils ältere Patterns |
| Länge | Tendenziell länger | Kürzer und prägnanter |

**Empfehlung für 5-10 Entwickler-Team:**
MediatR für In-Process als Einstieg, Migration zu MassTransit + RabbitMQ wenn Skalierung oder Microservices nötig.

---

## Lösung 2.4-B — Repository-Interface (Musterlösung)

```csharp
namespace Shop.Domain.Interfaces;

/// <summary>Repository für Bestellungen.</summary>
public interface IOrderRepository
{
    /// <summary>Lädt eine Bestellung anhand ihrer ID.</summary>
    Task<Order?> GetByIdAsync(Guid id, CancellationToken ct = default);

    /// <summary>Lädt alle Bestellungen eines Kunden paginiert.</summary>
    Task<PagedResult<Order>> GetByCustomerIdAsync(
        Guid customerId, int page, int pageSize, CancellationToken ct = default);

    /// <summary>Lädt alle offenen und bestätigten Bestellungen.</summary>
    Task<IReadOnlyList<Order>> GetPendingOrdersAsync(CancellationToken ct = default);

    /// <summary>Speichert eine neue oder aktualisiert eine bestehende Bestellung.</summary>
    Task SaveAsync(Order order, CancellationToken ct = default);

    /// <summary>Markiert eine Bestellung als gelöscht (Soft Delete).</summary>
    Task SoftDeleteAsync(Guid id, CancellationToken ct = default);
}
```

```csharp
namespace Shop.Infrastructure.Persistence.Repositories;

public sealed class EfOrderRepository(ShopDbContext context) : IOrderRepository
{
    public async Task<Order?> GetByIdAsync(Guid id, CancellationToken ct = default)
        => await context.Orders
            .Include(o => o.Lines).ThenInclude(l => l.Product)
            .FirstOrDefaultAsync(o => o.Id == id && !o.IsDeleted, ct);

    public async Task<PagedResult<Order>> GetByCustomerIdAsync(
        Guid customerId, int page, int pageSize, CancellationToken ct = default)
    {
        var query = context.Orders
            .Where(o => o.CustomerId == customerId && !o.IsDeleted)
            .OrderByDescending(o => o.CreatedAt);

        var total = await query.CountAsync(ct);
        var items = await query
            .Skip((page - 1) * pageSize).Take(pageSize)
            .Include(o => o.Lines)
            .ToListAsync(ct);

        return new PagedResult<Order>(items, total, page, pageSize);
    }

    public async Task<IReadOnlyList<Order>> GetPendingOrdersAsync(CancellationToken ct = default)
        => await context.Orders
            .Where(o => (o.Status == OrderStatus.Open || o.Status == OrderStatus.Confirmed)
                        && !o.IsDeleted)
            .OrderBy(o => o.CreatedAt)
            .ToListAsync(ct);

    public async Task SaveAsync(Order order, CancellationToken ct = default)
    {
        var exists = await context.Orders.AnyAsync(o => o.Id == order.Id, ct);
        if (exists) context.Orders.Update(order);
        else context.Orders.Add(order);
        await context.SaveChangesAsync(ct);
    }

    public async Task SoftDeleteAsync(Guid id, CancellationToken ct = default)
        => await context.Orders
            .Where(o => o.Id == id)
            .ExecuteUpdateAsync(s => s
                .SetProperty(o => o.IsDeleted, true)
                .SetProperty(o => o.DeletedAt, DateTime.UtcNow), ct);
}
```

**Qualitätsprüfung:**
- ✅ Alle 5 Methoden vorhanden
- ✅ CancellationToken überall
- ✅ Soft Delete mit `ExecuteUpdateAsync` (EF Core 7+, kein Laden nötig)
- ✅ Nullable korrekt (`Order?`, `IReadOnlyList`)
- ✅ Global Filter oder explizites `&& !o.IsDeleted`
