namespace UserApp.DTOs.Auth;

public sealed class login_request_dto
{
    public string email { get; init; } = string.Empty;

    public string password { get; init; } = string.Empty;
}
