namespace UserApp.Services;

using System.Security.Cryptography;
using System.Text;
using UserApp.DTOs.Auth;
using UserApp.Models;
using UserApp.Repositories;

public sealed class auth_service : Lauth_service
{
    private const int min_password_length = 8;
    private const int salt_size = 16;
    private const int hash_size = 32;
    private const int hash_iterations = 100_000;

    private readonly Luser_repository user_repository;

    public auth_service(Luser_repository user_repository)
    {
        this.user_repository = user_repository;
    }

    /// <inheritdoc />
    public async Task<register_response_dto> Async_register(
        register_request_dto request,
        CancellationToken cancellationToken = default)
    {
        if (string.IsNullOrWhiteSpace(request.password) || request.password.Length < min_password_length)
        {
            throw new ArgumentException("Password does not meet minimum length.");
        }

        user? existing_user = await user_repository
            .Async_get_by_email(request.email, cancellationToken)
            .ConfigureAwait(false);

        if (existing_user is not null)
        {
            throw new InvalidOperationException("Email is already registered.");
        }

        user user = new()
        {
            id = Guid.NewGuid(),
            first_name = request.first_name,
            last_name = request.last_name,
            email = request.email,
            password_hash = create_password_hash(request.password),
            role = user_role.user,
            active = true
        };

        user saved_user = await user_repository
            .Async_add(user, cancellationToken)
            .ConfigureAwait(false);

        return new register_response_dto
        {
            id = saved_user.id,
            email = saved_user.email,
            role = saved_user.role
        };
    }

    /// <inheritdoc />
    public async Task<login_response_dto> Async_login(
        login_request_dto request,
        CancellationToken cancellationToken = default)
    {
        user? existing_user = await user_repository
            .Async_get_by_email(request.email, cancellationToken)
            .ConfigureAwait(false);

        if (existing_user is null || !verify_password(request.password, existing_user.password_hash))
        {
            throw new UnauthorizedAccessException("Invalid credentials.");
        }

        return new login_response_dto
        {
            access_token = create_token("access", existing_user.id),
            refresh_token = create_token("refresh", existing_user.id)
        };
    }

    private static string create_password_hash(string password)
    {
        byte[] salt = RandomNumberGenerator.GetBytes(salt_size);
        byte[] hash = Rfc2898DeriveBytes.Pbkdf2(
            password,
            salt,
            hash_iterations,
            HashAlgorithmName.SHA256,
            hash_size);

        return $"{Convert.ToBase64String(salt)}.{Convert.ToBase64String(hash)}";
    }

    private static bool verify_password(string password, string stored_hash)
    {
        string[] parts = stored_hash.Split('.', 2, StringSplitOptions.TrimEntries);
        if (parts.Length != 2)
        {
            return false;
        }

        byte[] salt;
        byte[] known_hash;
        try
        {
            salt = Convert.FromBase64String(parts[0]);
            known_hash = Convert.FromBase64String(parts[1]);
        }
        catch (FormatException)
        {
            return false;
        }

        byte[] test_hash = Rfc2898DeriveBytes.Pbkdf2(
            password,
            salt,
            hash_iterations,
            HashAlgorithmName.SHA256,
            known_hash.Length);

        return CryptographicOperations.FixedTimeEquals(test_hash, known_hash);
    }

    private static string create_token(string token_type, Guid user_id)
    {
        string raw = $"{token_type}:{user_id}:{DateTimeOffset.UtcNow.ToUnixTimeSeconds()}:{Guid.NewGuid()}";
        return Convert.ToBase64String(Encoding.UTF8.GetBytes(raw));
    }
}
