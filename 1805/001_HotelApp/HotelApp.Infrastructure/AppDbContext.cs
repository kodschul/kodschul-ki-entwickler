using Microsoft.EntityFrameworkCore;

namespace HotelApp.Infrastructure;

public sealed class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
}
