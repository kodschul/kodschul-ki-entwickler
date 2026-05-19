using HotelApp.Domain;
using Microsoft.EntityFrameworkCore;

namespace HotelApp.Infrastructure;

public sealed class BookingRepository(AppDbContext db) : IBookingRepository
{
    public async Task<Booking?> GetByIdAsync(Guid id, CancellationToken ct = default)
        => await db.Bookings.FindAsync([id], ct);

    public async Task<IReadOnlyList<Booking>> GetAllAsync(CancellationToken ct = default)
        => await db.Bookings.AsNoTracking().ToListAsync(ct);

    public async Task AddAsync(Booking booking, CancellationToken ct = default)
        => await db.Bookings.AddAsync(booking, ct);

    public async Task SaveChangesAsync(CancellationToken ct = default)
        => await db.SaveChangesAsync(ct);
}
