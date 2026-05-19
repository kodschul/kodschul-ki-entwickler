# Modul 6 — Datenklassen und Datenmodell mit KI und EF Core

## Lab 6.1 — Datenklassen mit KI generieren und bewerten

### Bewertungscheckliste

| Punkt         | Prüffrage                                              |
| ------------- | ------------------------------------------------------ |
| Kapselung     | Alle Properties `private set` oder `init`?             |
| Validierung   | Konstruktor/Methoden validieren alle Eingaben?         |
| Null-Safety   | Nullable Reference Types aktiviert und korrekt?        |
| UTC-Zeiten    | `DateTime.UtcNow` statt `DateTime.Now`?                |
| EF Core       | `protected` Konstruktor für Materialisation vorhanden? |
| Domain Events | Fachliche Ereignisse als records vorhanden?            |
| Status-Guards | Methoden prüfen Status vor Ausführung?                 |
| Typen         | `decimal` für Geld, `Guid` für IDs?                    |

### Prompt-Template für Klassen

```
Du bist Senior C#-Entwickler. .NET 9, C# 13, DDD.
Erstelle [KLASSE] als [Entity / AggregateRoot / ValueObject]:
Properties: [mit Typen + nullable]
Methoden: [Signatur + Domänenregel]
Validierung: [Regeln + Exception-Typ]
Anforderungen: private setter, protected EF-Ctor, XML-Docs, Domain Events.
Nur Code. Keine Erklärungen.
```

## Lab 6.2 — Code-First-Ansatz mit EF Core 8

### DbContext Grundstruktur

```csharp
public sealed class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Customer> Customers => Set<Customer>();
    public DbSet<Order> Orders => Set<Order>();
    public DbSet<Product> Products => Set<Product>();

    protected override void OnModelCreating(ModelBuilder builder)
        => builder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly);
}
```

### Fluent API vs. Data Annotations

Fluent API hält die Domäneklassen frei von Infrastruktur-Attributen:

```csharp
// ❌ Domäne mit Infrastruktur verschmutzt
[MaxLength(100), Required]
public string Name { get; private set; }

// ✅ Konfiguration getrennt in IEntityTypeConfiguration<T>
builder.Property(e => e.Name).HasMaxLength(100).IsRequired();
```

## Lab 6.3 — Entwicklungsumgebung einrichten

### NuGet-Pakete

```xml
<PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="8.*" />
<PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="8.*">
  <PrivateAssets>all</PrivateAssets>
</PackageReference>
```

### Verbindungsstring (Development mit LocalDB)

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\MSSQLLocalDB;Database=HotelAppDb;Trusted_Connection=True;MultipleActiveResultSets=true;TrustServerCertificate=True"
  }
}
```

### Registration in Program.cs

```csharp
builder.Services.AddDbContext<AppDbContext>(options =>
        options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"))
           .EnableSensitiveDataLogging(builder.Environment.IsDevelopment())
           .EnableDetailedErrors(builder.Environment.IsDevelopment()));
```

### Praxis: So integrierst du es im Projekt (001_HotelApp)

1. Web-Projekt mit EF-Design-Paket ausstatten:

```powershell
dotnet add .\HotelApp.Web\HotelApp.Web.csproj package Microsoft.EntityFrameworkCore.Design --version 8.*
```

2. In `HotelApp.Web\appsettings.json` den ConnectionString eintragen:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\MSSQLLocalDB;Database=HotelAppDb;Trusted_Connection=True;MultipleActiveResultSets=true;TrustServerCertificate=True"
  }
}
```

3. In `HotelApp.Infrastructure` den DbContext anlegen:

```csharp
public sealed class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
}
```

4. In `HotelApp.Web\Program.cs` DbContext registrieren:

```csharp
builder.Services.AddDbContext<AppDbContext>(options =>
        options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"))
                     .EnableSensitiveDataLogging(builder.Environment.IsDevelopment())
                     .EnableDetailedErrors(builder.Environment.IsDevelopment()));
```

5. Setup prüfen:

```powershell
dotnet restore
dotnet build
```

## Lab 6.4 — Konsistentes und wartbares Datenmodell

### Basisklassen

```csharp
public abstract class Entity
{
    public Guid Id { get; protected set; } = Guid.NewGuid();
    public override bool Equals(object? obj) =>
        obj is Entity e && GetType() == e.GetType() && Id == e.Id;
    public override int GetHashCode() => Id.GetHashCode();
}

public abstract class AuditableEntity : Entity
{
    public DateTime CreatedAt { get; private set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; private set; } = DateTime.UtcNow;
    internal void Touch() => UpdatedAt = DateTime.UtcNow;
}
```

### Häufige Modellierungsfehler

| Fehler                  | Auswirkung                | Lösung                                 |
| ----------------------- | ------------------------- | -------------------------------------- |
| `double` für Geld       | Rundungsfehler            | `decimal` + `HasPrecision(18,2)`       |
| `DateTime.Now`          | Zeitzonen-Bug             | `DateTime.UtcNow` immer                |
| Enum als int            | DB unleserlich            | `HasConversion<string>()`              |
| DbContext als Singleton | Thread-Sicherheitsproblem | `AddDbContext` → Scoped                |
| Kein Index auf FK       | Langsame Joins            | `HasIndex()` oder automatisch durch EF |
