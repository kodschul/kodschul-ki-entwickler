namespace UserApp.Repositories;

using UserApp.Models;

public interface Luser_repository
{
    /// <summary>
    /// Findet einen Benutzer anhand der E-Mail-Adresse.
    /// </summary>
    Task<user?> Async_get_by_email(string email, CancellationToken cancellationToken = default);

    /// <summary>
    /// Speichert einen neuen Benutzer.
    /// </summary>
    Task<user> Async_add(user user, CancellationToken cancellationToken = default);
}
