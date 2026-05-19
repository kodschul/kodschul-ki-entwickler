using HotelApp.Domain;
using Microsoft.EntityFrameworkCore;

namespace HotelApp.Infrastructure;

public sealed class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Booking> Bookings => Set<Booking>();

    protected override void OnModelCreating(ModelBuilder builder)
    {
        base.OnModelCreating(builder);

        builder.Entity<Booking>(e =>
        {
            e.HasKey(b => b.Id);

            e.Property(b => b.Status)
             .HasConversion<string>()
             .HasMaxLength(20)
             .HasDefaultValue(BookingStatus.Requested);

            e.Property(b => b.TotalPrice)
             .HasPrecision(18, 2);

            e.Property(b => b.CancellationFee)
             .HasPrecision(18, 2);

            e.HasIndex(b => b.RoomId);
            e.HasIndex(b => b.GuestId);

            // Seed-Daten mit fixen GUIDs für Idempotenz
            e.HasData(
                new
                {
                    Id              = Guid.Parse("aaaaaaaa-0000-0000-0000-000000000001"),
                    RoomId          = Guid.Parse("bbbbbbbb-0000-0000-0000-000000000001"),
                    GuestId         = Guid.Parse("cccccccc-0000-0000-0000-000000000001"),
                    CheckInDate     = new DateOnly(2026, 6, 1),
                    CheckOutDate    = new DateOnly(2026, 6, 5),
                    Status          = BookingStatus.Confirmed,
                    TotalPrice      = 516.00m,
                    CancellationFee = (decimal?)null
                },
                new
                {
                    Id              = Guid.Parse("aaaaaaaa-0000-0000-0000-000000000002"),
                    RoomId          = Guid.Parse("bbbbbbbb-0000-0000-0000-000000000002"),
                    GuestId         = Guid.Parse("cccccccc-0000-0000-0000-000000000002"),
                    CheckInDate     = new DateOnly(2026, 7, 10),
                    CheckOutDate    = new DateOnly(2026, 7, 14),
                    Status          = BookingStatus.Requested,
                    TotalPrice      = 356.00m,
                    CancellationFee = (decimal?)null
                },
                new
                {
                    Id              = Guid.Parse("aaaaaaaa-0000-0000-0000-000000000003"),
                    RoomId          = Guid.Parse("bbbbbbbb-0000-0000-0000-000000000001"),
                    GuestId         = Guid.Parse("cccccccc-0000-0000-0000-000000000003"),
                    CheckInDate     = new DateOnly(2026, 5, 1),
                    CheckOutDate    = new DateOnly(2026, 5, 3),
                    Status          = BookingStatus.Cancelled,
                    TotalPrice      = 258.00m,
                    CancellationFee = 50.00m
                }
            );
        });
    }
}
