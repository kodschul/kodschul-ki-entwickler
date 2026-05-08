namespace UserApp.Controllers;

using Microsoft.AspNetCore.Mvc;
using UserApp.DTOs.Auth;
using UserApp.Services;

[ApiController]
[Route("api/auth")]
public sealed class auth_controller : ControllerBase
{
    private readonly Lauth_service auth_service;

    public auth_controller(Lauth_service auth_service)
    {
        this.auth_service = auth_service;
    }

    /// <summary>
    /// Registriert ein neues Benutzerkonto.
    /// </summary>
    [HttpPost("register")]
    [ProducesResponseType(typeof(register_response_dto), StatusCodes.Status201Created)]
    [ProducesResponseType(StatusCodes.Status409Conflict)]
    [ProducesResponseType(StatusCodes.Status422UnprocessableEntity)]
    public async Task<ActionResult<register_response_dto>> Async_register(
        [FromBody] register_request_dto request,
        CancellationToken cancellationToken)
    {
        try
        {
            register_response_dto response = await auth_service
                .Async_register(request, cancellationToken)
                .ConfigureAwait(false);

            return CreatedAtAction(nameof(Async_register), response);
        }
        catch (InvalidOperationException)
        {
            return Conflict(new { message = "Diese E-Mail-Adresse ist bereits registriert." });
        }
        catch (ArgumentException)
        {
            return UnprocessableEntity(new { message = "Das Passwort ist ungültig." });
        }
    }

    /// <summary>
    /// Authentifiziert einen Benutzer und liefert einfache Tokens zurück.
    /// </summary>
    [HttpPost("login")]
    [ProducesResponseType(typeof(login_response_dto), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status401Unauthorized)]
    public async Task<ActionResult<login_response_dto>> Async_login(
        [FromBody] login_request_dto request,
        CancellationToken cancellationToken)
    {
        try
        {
            login_response_dto response = await auth_service
                .Async_login(request, cancellationToken)
                .ConfigureAwait(false);

            return Ok(response);
        }
        catch (UnauthorizedAccessException)
        {
            return Unauthorized(new { message = "Ungültige E-Mail-Adresse oder Passwort." });
        }
    }
}
