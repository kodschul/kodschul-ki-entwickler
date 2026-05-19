using FluentAssertions;
using HotelApp.Domain;

namespace HotelApp.Tests;

public class BookingTests
{
    // --- Happy Path: Konstruktor ---

    [Fact]
    public void func_Constructor_ValidArguments_CreatesRequestedBooking()
    {
        var roomId = Guid.NewGuid();
        var guestId = Guid.NewGuid();
        var checkIn = DateOnly.FromDateTime(DateTime.Today.AddDays(1));
        var checkOut = checkIn.AddDays(3);

        var booking = new Booking(Guid.NewGuid(), roomId, guestId, checkIn, checkOut, 300m);

        booking.RoomId.Should().Be(roomId);
        booking.GuestId.Should().Be(guestId);
        booking.CheckInDate.Should().Be(checkIn);
        booking.CheckOutDate.Should().Be(checkOut);
        booking.TotalPrice.Should().Be(300m);
        booking.Status.Should().Be(BookingStatus.Requested);
        booking.CancellationFee.Should().BeNull();
    }

    [Fact]
    public void func_Constructor_EmptyId_GeneratesNewId()
    {
        var booking = func_CreateValidBooking(id: Guid.Empty);
        booking.Id.Should().NotBe(Guid.Empty);
    }

    // --- Guard: Konstruktor ---

    [Fact]
    public void func_Constructor_EmptyRoomId_Throws()
    {
        var act = () => func_CreateValidBooking(roomId: Guid.Empty);
        act.Should().Throw<ArgumentException>().WithParameterName("roomId");
    }

    [Fact]
    public void func_Constructor_EmptyGuestId_Throws()
    {
        var act = () => func_CreateValidBooking(guestId: Guid.Empty);
        act.Should().Throw<ArgumentException>().WithParameterName("guestId");
    }

    [Fact]
    public void func_Constructor_CheckOutBeforeCheckIn_Throws()
    {
        var checkIn = new DateOnly(2026, 6, 10);
        var checkOut = new DateOnly(2026, 6, 5);

        var act = () => func_CreateValidBooking(checkIn: checkIn, checkOut: checkOut);
        act.Should().Throw<ArgumentException>().WithParameterName("checkOutDate");
    }

    [Fact]
    public void func_Constructor_CheckOutEqualsCheckIn_Throws()
    {
        var date = new DateOnly(2026, 6, 10);
        var act = () => func_CreateValidBooking(checkIn: date, checkOut: date);
        act.Should().Throw<ArgumentException>().WithParameterName("checkOutDate");
    }

    [Fact]
    public void func_Constructor_NegativeTotalPrice_Throws()
    {
        var act = () => func_CreateValidBooking(totalPrice: -1m);
        act.Should().Throw<ArgumentOutOfRangeException>().WithParameterName("totalPrice");
    }

    // --- Confirm ---

    [Fact]
    public void func_Confirm_WhenRequested_SetsStatusConfirmed()
    {
        var booking = func_CreateValidBooking();
        booking.Confirm();
        booking.Status.Should().Be(BookingStatus.Confirmed);
    }

    [Theory]
    [InlineData(BookingStatus.Confirmed)]
    [InlineData(BookingStatus.CheckedIn)]
    [InlineData(BookingStatus.CheckedOut)]
    [InlineData(BookingStatus.Cancelled)]
    public void func_Confirm_WhenNotRequested_Throws(BookingStatus initialStatus)
    {
        var booking = func_CreateBookingWithStatus(initialStatus);
        var act = () => booking.Confirm();
        act.Should().Throw<InvalidOperationException>();
    }

    // --- Cancel ---

    [Fact]
    public void func_Cancel_WhenRequested_SetsCancelledWithNoFee()
    {
        var booking = func_CreateValidBooking();
        booking.Cancel(DateTimeOffset.UtcNow);

        booking.Status.Should().Be(BookingStatus.Cancelled);
        booking.CancellationFee.Should().Be(0m); // Requested => no fee
    }

    [Fact]
    public void func_Cancel_WhenConfirmedLate_SetsFeeAndCancelled()
    {
        var booking = func_CreateValidBooking(
            checkIn: DateOnly.FromDateTime(DateTime.Today.AddDays(1)));
        booking.Confirm();

        // Cancelling after check-in time has passed (simulate late cancel)
        var cancellationTime = DateTimeOffset.UtcNow.AddDays(2); // past check-in
        booking.Cancel(cancellationTime);

        booking.Status.Should().Be(BookingStatus.Cancelled);
        booking.CancellationFee.Should().BeGreaterThan(0m);
    }

    [Theory]
    [InlineData(BookingStatus.CheckedIn)]
    [InlineData(BookingStatus.CheckedOut)]
    [InlineData(BookingStatus.Cancelled)]
    public void func_Cancel_WhenNotCancellable_Throws(BookingStatus initialStatus)
    {
        var booking = func_CreateBookingWithStatus(initialStatus);
        var act = () => booking.Cancel(DateTimeOffset.UtcNow);
        act.Should().Throw<InvalidOperationException>();
    }

    // --- Helpers ---

    private static Booking func_CreateValidBooking(
        Guid? id = null,
        Guid? roomId = null,
        Guid? guestId = null,
        DateOnly? checkIn = null,
        DateOnly? checkOut = null,
        decimal totalPrice = 200m)
    {
        var checkInDate = checkIn ?? DateOnly.FromDateTime(DateTime.Today.AddDays(1));
        var checkOutDate = checkOut ?? checkInDate.AddDays(2);

        return new Booking(
            id ?? Guid.NewGuid(),
            roomId ?? Guid.NewGuid(),
            guestId ?? Guid.NewGuid(),
            checkInDate,
            checkOutDate,
            totalPrice);
    }

    private static Booking func_CreateBookingWithStatus(BookingStatus status)
    {
        // Uses reflection to bypass constructor guards for test setup
        var booking = func_CreateValidBooking();
        var statusProp = typeof(Booking).GetProperty(nameof(Booking.Status))!;
        statusProp.SetValue(booking, status);
        return booking;
    }
}
