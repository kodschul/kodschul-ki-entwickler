namespace UserApp.DTOs.Auth;

public sealed class login_response_dto
{
    public string access_token { get; init; } = string.Empty;

    public string refresh_token { get; init; } = string.Empty;
}
