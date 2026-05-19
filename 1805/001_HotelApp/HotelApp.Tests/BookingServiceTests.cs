using FluentAssertions;
using HotelApp.Application;
using HotelApp.Domain;
using Moq;

namespace HotelApp.Tests;

public class BookingServiceTests
{
    private readonly Mock<IBookingRepository> _repoMock = new();
    private readonly BookingService _sut;

    public BookingServiceTests()
    {
        _sut = new BookingService(_repoMock.Object);
    }

    // --- func_CreateAsync ---

    [Fact]
    public async Task func_CreateAsync_ValidData_AddsAndSaves()
    {
        var roomId = Guid.NewGuid();
        var guestId = Guid.NewGuid();
        var checkIn = DateOnly.FromDateTime(DateTime.Today.AddDays(1));
        var checkOut = checkIn.AddDays(3);

        await _sut.func_CreateAsync(roomId, guestId, checkIn, checkOut, 300m);

        _repoMock.Verify(r => r.AddAsync(It.Is<Booking>(b =>
            b.RoomId == roomId &&
            b.GuestId == guestId &&
            b.TotalPrice == 300m &&
            b.Status == BookingStatus.Requested
        ), default), Times.Once);

        _repoMock.Verify(r => r.SaveChangesAsync(default), Times.Once);
    }

    // --- func_ConfirmAsync ---

    [Fact]
    public async Task func_ConfirmAsync_ExistingBooking_ConfirmsAndSaves()
    {
        var booking = func_CreateRequestedBooking();
        _repoMock.Setup(r => r.GetByIdAsync(booking.Id, default))
                 .ReturnsAsync(booking);

        await _sut.func_ConfirmAsync(booking.Id);

        booking.Status.Should().Be(BookingStatus.Confirmed);
        _repoMock.Verify(r => r.SaveChangesAsync(default), Times.Once);
    }

    [Fact]
    public async Task func_ConfirmAsync_BookingNotFound_ThrowsKeyNotFoundException()
    {
        var missingId = Guid.NewGuid();
        _repoMock.Setup(r => r.GetByIdAsync(missingId, default))
                 .ReturnsAsync((Booking?)null);

        var act = async () => await _sut.func_ConfirmAsync(missingId);

        await act.Should().ThrowAsync<KeyNotFoundException>();
        _repoMock.Verify(r => r.SaveChangesAsync(default), Times.Never);
    }

    // --- func_CancelAsync ---

    [Fact]
    public async Task func_CancelAsync_ExistingBooking_CancelsAndSaves()
    {
        var booking = func_CreateRequestedBooking();
        _repoMock.Setup(r => r.GetByIdAsync(booking.Id, default))
                 .ReturnsAsync(booking);

        await _sut.func_CancelAsync(booking.Id);

        booking.Status.Should().Be(BookingStatus.Cancelled);
        _repoMock.Verify(r => r.SaveChangesAsync(default), Times.Once);
    }

    [Fact]
    public async Task func_CancelAsync_BookingNotFound_ThrowsKeyNotFoundException()
    {
        var missingId = Guid.NewGuid();
        _repoMock.Setup(r => r.GetByIdAsync(missingId, default))
                 .ReturnsAsync((Booking?)null);

        var act = async () => await _sut.func_CancelAsync(missingId);

        await act.Should().ThrowAsync<KeyNotFoundException>();
    }

    // --- func_CheckInAsync ---

    [Fact]
    public async Task func_CheckInAsync_ConfirmedBookingToday_ChecksInAndSaves()
    {
        var today = DateOnly.FromDateTime(DateTime.Today);
        var booking = new Booking(
            Guid.NewGuid(), Guid.NewGuid(), Guid.NewGuid(),
            today, today.AddDays(2), 200m);
        booking.Confirm();

        _repoMock.Setup(r => r.GetByIdAsync(booking.Id, default))
                 .ReturnsAsync(booking);

        await _sut.func_CheckInAsync(booking.Id);

        booking.Status.Should().Be(BookingStatus.CheckedIn);
        _repoMock.Verify(r => r.SaveChangesAsync(default), Times.Once);
    }

    [Fact]
    public async Task func_CheckInAsync_BookingNotFound_ThrowsKeyNotFoundException()
    {
        var missingId = Guid.NewGuid();
        _repoMock.Setup(r => r.GetByIdAsync(missingId, default))
                 .ReturnsAsync((Booking?)null);

        var act = async () => await _sut.func_CheckInAsync(missingId);

        await act.Should().ThrowAsync<KeyNotFoundException>();
    }

    // --- func_GetByIdAsync ---

    [Fact]
    public async Task func_GetByIdAsync_ExistingId_ReturnsBooking()
    {
        var booking = func_CreateRequestedBooking();
        _repoMock.Setup(r => r.GetByIdAsync(booking.Id, default))
                 .ReturnsAsync(booking);

        var result = await _sut.func_GetByIdAsync(booking.Id);

        result.Should().Be(booking);
    }

    [Fact]
    public async Task func_GetByIdAsync_MissingId_ReturnsNull()
    {
        _repoMock.Setup(r => r.GetByIdAsync(It.IsAny<Guid>(), default))
                 .ReturnsAsync((Booking?)null);

        var result = await _sut.func_GetByIdAsync(Guid.NewGuid());

        result.Should().BeNull();
    }

    // --- Helper ---

    private static Booking func_CreateRequestedBooking()
    {
        var checkIn = DateOnly.FromDateTime(DateTime.Today.AddDays(1));
        return new Booking(Guid.NewGuid(), Guid.NewGuid(), Guid.NewGuid(),
            checkIn, checkIn.AddDays(2), 200m);
    }
}
