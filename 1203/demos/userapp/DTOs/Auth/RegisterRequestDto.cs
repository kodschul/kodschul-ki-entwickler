namespace UserApp.DTOs.Auth;

public sealed class register_request_dto
{
    public string first_name { get; init; } = string.Empty;

    public string last_name { get; init; } = string.Empty;

    public string email { get; init; } = string.Empty;

    public string password { get; init; } = string.Empty;
}
