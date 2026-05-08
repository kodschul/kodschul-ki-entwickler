namespace UserApp.DTOs.Auth;

using UserApp.Models;

public sealed class register_response_dto
{
    public Guid id { get; init; }

    public string email { get; init; } = string.Empty;

    public user_role role { get; init; }
}
