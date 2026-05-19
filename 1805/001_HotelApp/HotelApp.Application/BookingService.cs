using HotelApp.Domain;

namespace HotelApp.Application;

/// <summary>
/// Application Service — orchestriert Laden, Domänenlogik und Persistenz.
/// Geschäftsregeln liegen im Domain Layer (Booking-Methoden).
/// </summary>
public sealed class BookingService(IBookingRepository repository)
{
    // --- Queries ---

    public async Task<Booking?> func_GetByIdAsync(Guid id, CancellationToken ct = default)
        => await repository.GetByIdAsync(id, ct);

    public async Task<IReadOnlyList<Booking>> func_GetAllAsync(CancellationToken ct = default)
        => await repository.GetAllAsync(ct);

    // --- Commands ---

    public async Task func_CreateAsync(
        Guid roomId,
        Guid guestId,
        DateOnly checkInDate,
        DateOnly checkOutDate,
        decimal totalPrice,
        CancellationToken ct = default)
    {
        var booking = new Booking(Guid.NewGuid(), roomId, guestId, checkInDate, checkOutDate, totalPrice);
        await repository.AddAsync(booking, ct);
        await repository.SaveChangesAsync(ct);
    }

    public async Task func_ConfirmAsync(Guid id, CancellationToken ct = default)
    {
        // 1. Laden
        var booking = await repository.GetByIdAsync(id, ct)
            ?? throw new KeyNotFoundException($"Booking {id} not found.");

        // 2. Domänenlogik delegieren → Booking wirft bei Regelverstoß
        booking.Confirm();

        // 3. Persistieren
        await repository.SaveChangesAsync(ct);
    }

    public async Task func_CancelAsync(Guid id, CancellationToken ct = default)
    {
        var booking = await repository.GetByIdAsync(id, ct)
            ?? throw new KeyNotFoundException($"Booking {id} not found.");

        booking.Cancel(DateTimeOffset.UtcNow);

        await repository.SaveChangesAsync(ct);
    }

    public async Task func_CheckInAsync(Guid id, CancellationToken ct = default)
    {
        var booking = await repository.GetByIdAsync(id, ct)
            ?? throw new KeyNotFoundException($"Booking {id} not found.");

        booking.CheckIn();

        await repository.SaveChangesAsync(ct);
    }
}
