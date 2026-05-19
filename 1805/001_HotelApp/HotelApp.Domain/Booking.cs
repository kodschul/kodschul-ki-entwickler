namespace HotelApp.Domain;

public enum BookingStatus
{
    Requested = 0,
    Confirmed = 1,
    CheckedIn = 2,
    CheckedOut = 3,
    Cancelled = 4
}

public class Booking
{
    protected Booking()
    {
    }

    public Booking(
        Guid id,
        Guid roomId,
        Guid guestId,
        DateOnly checkInDate,
        DateOnly checkOutDate,
        decimal totalPrice)
    {
        if (roomId == Guid.Empty)
        {
            throw new ArgumentException("RoomId must not be empty.", nameof(roomId));
        }

        if (guestId == Guid.Empty)
        {
            throw new ArgumentException("GuestId must not be empty.", nameof(guestId));
        }

        if (checkOutDate <= checkInDate)
        {
            throw new ArgumentException("Check-out must be after check-in.", nameof(checkOutDate));
        }

        if (totalPrice < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(totalPrice), "TotalPrice must be >= 0.");
        }

        Id = id == Guid.Empty ? Guid.NewGuid() : id;
        RoomId = roomId;
        GuestId = guestId;
        CheckInDate = checkInDate;
        CheckOutDate = checkOutDate;
        Status = BookingStatus.Requested;
        TotalPrice = totalPrice;
        CancellationFee = null;
    }

    public Guid Id { get; private set; }

    public Guid RoomId { get; private set; }

    public Guid GuestId { get; private set; }

    public DateOnly CheckInDate { get; private set; }

    public DateOnly CheckOutDate { get; private set; }

    public BookingStatus Status { get; private set; }

    public decimal TotalPrice { get; private set; }

    public decimal? CancellationFee { get; private set; }

    public void Confirm()
    {
        if (Status != BookingStatus.Requested)
        {
            throw new InvalidOperationException("Only requested bookings can be confirmed.");
        }

        Status = BookingStatus.Confirmed;
    }

    public void Cancel(DateTimeOffset cancellationTime)
    {
        if (Status is BookingStatus.CheckedIn or BookingStatus.CheckedOut or BookingStatus.Cancelled)
        {
            throw new InvalidOperationException("Booking cannot be cancelled in current status.");
        }

        CancellationFee = CalculateCancellationFee(cancellationTime);
        Status = BookingStatus.Cancelled;
    }

    public void CheckIn()
    {
        if (Status != BookingStatus.Confirmed)
        {
            throw new InvalidOperationException("Only confirmed bookings can be checked in.");
        }

        var today = DateOnly.FromDateTime(DateTime.Now);
        if (today != CheckInDate)
        {
            throw new InvalidOperationException("Check-in is only allowed on check-in date.");
        }

        Status = BookingStatus.CheckedIn;
    }

    private decimal CalculateCancellationFee(DateTimeOffset cancellationTime)
    {
        if (Status != BookingStatus.Confirmed)
        {
            return 0m;
        }

        var checkInDateTime = CheckInDate.ToDateTime(TimeOnly.MinValue);
        var checkInOffset = new DateTimeOffset(checkInDateTime, cancellationTime.Offset);
        var hoursUntilCheckIn = (checkInOffset - cancellationTime).TotalHours;

        if (hoursUntilCheckIn < 0)
        {
            return TotalPrice;
        }

        if (hoursUntilCheckIn <= 24)
        {
            return Math.Round(TotalPrice * 0.5m, 2, MidpointRounding.AwayFromZero);
        }

        return Math.Round(TotalPrice * 0.1m, 2, MidpointRounding.AwayFromZero);
    }
}
