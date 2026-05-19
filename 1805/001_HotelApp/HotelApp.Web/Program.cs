using HotelApp.Application;
using HotelApp.Domain;
using HotelApp.Infrastructure;
using HotelApp.Web.Components;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"))
           .EnableSensitiveDataLogging(builder.Environment.IsDevelopment())
           .EnableDetailedErrors(builder.Environment.IsDevelopment()));
builder.Services.AddHttpClient();

// Repository + Application Service (Clean Architecture)
builder.Services.AddScoped<IBookingRepository, BookingRepository>();
builder.Services.AddScoped<BookingService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

var bookingApi = app.MapGroup("/api/bookings").WithTags("Bookings");

bookingApi.MapGet("/", async (BookingService bookingService, CancellationToken ct) =>
{
    var bookings = await bookingService.func_GetAllAsync(ct);

    var response = bookings.Select(b => new BookingListItemDto(
        b.Id,
        b.RoomId,
        b.GuestId,
        b.CheckInDate,
        b.CheckOutDate,
        b.Status.ToString(),
        b.TotalPrice,
        b.CancellationFee));

    return Results.Ok(response);
});

bookingApi.MapGet("/{id:guid}", async (Guid id, BookingService bookingService, CancellationToken ct) =>
{
    var booking = await bookingService.func_GetByIdAsync(id, ct);
    if (booking is null)
    {
        return Results.NotFound();
    }

    return Results.Ok(new BookingListItemDto(
        booking.Id,
        booking.RoomId,
        booking.GuestId,
        booking.CheckInDate,
        booking.CheckOutDate,
        booking.Status.ToString(),
        booking.TotalPrice,
        booking.CancellationFee));
});

bookingApi.MapPost("/", async ([FromBody] CreateBookingRequest request, BookingService bookingService, CancellationToken ct) =>
{
    if (request.RoomId == Guid.Empty || request.GuestId == Guid.Empty)
    {
        return Results.BadRequest("RoomId and GuestId are required.");
    }

    if (request.CheckOutDate <= request.CheckInDate)
    {
        return Results.BadRequest("CheckOutDate must be after CheckInDate.");
    }

    if (request.TotalPrice < 0)
    {
        return Results.BadRequest("TotalPrice must be >= 0.");
    }

    await bookingService.func_CreateAsync(
        request.RoomId,
        request.GuestId,
        request.CheckInDate,
        request.CheckOutDate,
        request.TotalPrice,
        ct);

    return Results.Created("/api/bookings", null);
});

bookingApi.MapPost("/{id:guid}/confirm", async (Guid id, BookingService bookingService, CancellationToken ct) =>
{
    try
    {
        await bookingService.func_ConfirmAsync(id, ct);
        return Results.NoContent();
    }
    catch (KeyNotFoundException ex)
    {
        return Results.NotFound(ex.Message);
    }
    catch (InvalidOperationException ex)
    {
        return Results.BadRequest(ex.Message);
    }
});

bookingApi.MapPost("/{id:guid}/cancel", async (Guid id, BookingService bookingService, CancellationToken ct) =>
{
    try
    {
        await bookingService.func_CancelAsync(id, ct);
        return Results.NoContent();
    }
    catch (KeyNotFoundException ex)
    {
        return Results.NotFound(ex.Message);
    }
    catch (InvalidOperationException ex)
    {
        return Results.BadRequest(ex.Message);
    }
});

bookingApi.MapPost("/{id:guid}/checkin", async (Guid id, BookingService bookingService, CancellationToken ct) =>
{
    try
    {
        await bookingService.func_CheckInAsync(id, ct);
        return Results.NoContent();
    }
    catch (KeyNotFoundException ex)
    {
        return Results.NotFound(ex.Message);
    }
    catch (InvalidOperationException ex)
    {
        return Results.BadRequest(ex.Message);
    }
});

app.Run();

public sealed record BookingListItemDto(
    Guid Id,
    Guid RoomId,
    Guid GuestId,
    DateOnly CheckInDate,
    DateOnly CheckOutDate,
    string Status,
    decimal TotalPrice,
    decimal? CancellationFee);

public sealed record CreateBookingRequest(
    Guid RoomId,
    Guid GuestId,
    DateOnly CheckInDate,
    DateOnly CheckOutDate,
    decimal TotalPrice);
