namespace UserApp.Models;

public sealed class user
{
    public Guid id { get; init; }

    public string first_name { get; set; } = string.Empty;

    public string last_name { get; set; } = string.Empty;

    public string email { get; set; } = string.Empty;

    public string password_hash { get; set; } = string.Empty;

    public user_role role { get; set; } = user_role.user;

    public bool active { get; set; } = true;

    public DateTimeOffset created_at { get; init; } = DateTimeOffset.UtcNow;
}
