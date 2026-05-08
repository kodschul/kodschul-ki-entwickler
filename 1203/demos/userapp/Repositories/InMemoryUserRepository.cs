namespace UserApp.Repositories;

using System.Collections.Concurrent;
using UserApp.Models;

public sealed class in_memory_user_repository : Luser_repository
{
    private readonly ConcurrentDictionary<string, user> users_by_email =
        new(StringComparer.OrdinalIgnoreCase);

    /// <inheritdoc />
    public Task<user?> Async_get_by_email(string email, CancellationToken cancellationToken = default)
    {
        users_by_email.TryGetValue(email, out user? user);
        return Task.FromResult(user);
    }

    /// <inheritdoc />
    public Task<user> Async_add(user user, CancellationToken cancellationToken = default)
    {
        users_by_email[user.email] = user;
        return Task.FromResult(user);
    }
}
