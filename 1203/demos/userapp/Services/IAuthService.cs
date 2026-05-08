namespace UserApp.Services;

using UserApp.DTOs.Auth;

public interface Lauth_service
{
    /// <summary>
    /// Registriert einen neuen Benutzer.
    /// </summary>
    Task<register_response_dto> Async_register(
        register_request_dto request,
        CancellationToken cancellationToken = default);

    /// <summary>
    /// Authentifiziert einen Benutzer per E-Mail und Passwort.
    /// </summary>
    Task<login_response_dto> Async_login(
        login_request_dto request,
        CancellationToken cancellationToken = default);
}
