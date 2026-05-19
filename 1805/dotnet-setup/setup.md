# m05-m10 Project Setup (Windows 11, Beginner Friendly, 100% .NET)

This guide shows you step by step how to build and run a complete project for modules m05 to m10:

- m05: Domain-Driven Design
- m06: Data classes and data model
- m07: Database migrations
- m08: Business logic
- m09: Automated tests
- m10: Web frontend

Goal at the end:

- One running .NET application
- SQL database connected and migrated
- Tests running
- Frontend running (in .NET with Blazor)

## 0) What you will build

You will build a small task/project app with this structure:

- `HotelApp.Domain` (entities, value objects, domain rules)
- `HotelApp.Application` (use cases, services, interfaces)
- `HotelApp.Infrastructure` (EF Core, database, repositories)
- `HotelApp.Web` (ASP.NET Core + Blazor frontend)
- `HotelApp.Tests` (xUnit tests)

This structure maps directly to m05-m10.

## 1) Install everything on a blank Windows 11

Open **PowerShell as Administrator** and run:

```powershell
winget install Microsoft.DotNet.SDK.8
winget install Microsoft.VisualStudioCode
winget install Git.Git
```

Install SQL Server Express and LocalDB (for easy local database use):

```powershell
winget install Microsoft.SQLServer.2022.Express


winget install Microsoft.SQLServer.2022.Express --override "/Action=Install /SkipSameLanguageCheck /IAcceptSQLServerLicenseTerms /Features=SQLEngine,LocalDB /InstanceName=SQLEXPRESS /SQLSYSADMINACCOUNTS='BUILTIN\ADMINISTRATORS' /TCPENABLED=1 /NPENABLED=1"
```

https://learn.microsoft.com/en-us/ssms/install/install?redirectedfrom=MSDN

Close and reopen PowerShell.

Verify installation:

```powershell
dotnet --version
git --version
code --version
```

If these commands print versions, you are ready.

## 2) Install VS Code extensions

Open VS Code and install:

- C# Dev Kit (Microsoft)
- C# (Microsoft)
- NuGet Gallery (optional but helpful)

## 3) Create project folder and solution

In PowerShell:

```powershell
mkdir C:\dev\hotel-app
cd C:\dev\hotel-app

dotnet new sln -n HotelApp
```

Create projects:

```powershell
dotnet new classlib -n HotelApp.Domain
dotnet new classlib -n HotelApp.Application
dotnet new classlib -n HotelApp.Infrastructure
dotnet new blazor -n HotelApp.Web
dotnet new xunit -n HotelApp.Tests
```

Add projects to solution:

```powershell
dotnet sln add .\HotelApp.Domain\HotelApp.Domain.csproj
dotnet sln add .\HotelApp.Application\HotelApp.Application.csproj
dotnet sln add .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj
dotnet sln add .\HotelApp.Web\HotelApp.Web.csproj
dotnet sln add .\HotelApp.Tests\HotelApp.Tests.csproj
```

## 4) Add project references (Clean Architecture flow)

Run:

```powershell
dotnet add .\HotelApp.Application\HotelApp.Application.csproj reference .\HotelApp.Domain\HotelApp.Domain.csproj
dotnet add .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj reference .\HotelApp.Application\HotelApp.Application.csproj
dotnet add .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj reference .\HotelApp.Domain\HotelApp.Domain.csproj
dotnet add .\HotelApp.Web\HotelApp.Web.csproj reference .\HotelApp.Application\HotelApp.Application.csproj
dotnet add .\HotelApp.Web\HotelApp.Web.csproj reference .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj
dotnet add .\HotelApp.Tests\HotelApp.Tests.csproj reference .\HotelApp.Domain\HotelApp.Domain.csproj
dotnet add .\HotelApp.Tests\HotelApp.Tests.csproj reference .\HotelApp.Application\HotelApp.Application.csproj
dotnet add .\HotelApp.Tests\HotelApp.Tests.csproj reference .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj
```

## 5) Install NuGet packages

### Infrastructure packages (EF Core + SQL Server)

```powershell
dotnet add .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj package Microsoft.EntityFrameworkCore
dotnet add .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj package Microsoft.EntityFrameworkCore.SqlServer
dotnet add .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj package Microsoft.EntityFrameworkCore.Design
```

### Web package (EF Core tooling from startup project)

```powershell
dotnet add .\HotelApp.Web\HotelApp.Web.csproj package Microsoft.EntityFrameworkCore.Design
```

### Test packages

```powershell
dotnet add .\HotelApp.Tests\HotelApp.Tests.csproj package FluentAssertions
dotnet add .\HotelApp.Tests\HotelApp.Tests.csproj package Moq
```

## 6) Install EF Core CLI tool

```powershell
dotnet tool install --global dotnet-ef
dotnet ef --version
```

If the second command fails, restart terminal and try again.

## 7) Build once to verify setup

```powershell
dotnet restore
dotnet build
```

Expected result: `Build succeeded.`

## 8) Implement m05 (Domain-Driven Design)

In `HotelApp.Domain`, create:

- Entities (for example `Project`, `TaskItem`)
- Value Objects (for example `TaskTitle`)
- Domain rules (for example status transitions)

Rules:

- Domain layer has no database code
- Domain layer has no UI code
- Keep invariants in constructors/methods

## 9) Implement m06 (Data model)

In `HotelApp.Infrastructure`:

- Create `AppDbContext : DbContext`
- Add `DbSet<Project>` and `DbSet<TaskItem>`
- Add EF Core configurations with `IEntityTypeConfiguration<T>`

In `HotelApp.Application`:

- Define repository interfaces (for example `IProjectRepository`)
- Define use case services

In `HotelApp.Infrastructure`:

- Implement repository interfaces using EF Core

## 10) Implement m07 (Migrations + database)

Use SQL Server LocalDB connection string in `HotelApp.Web\appsettings.json`:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\MSSQLLocalDB;Database=HotelAppDb;Trusted_Connection=True;MultipleActiveResultSets=true;TrustServerCertificate=True"
  }
}
```

Create first migration:

```powershell
dotnet ef migrations add InitialCreate --project .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj --startup-project .\HotelApp.Web\HotelApp.Web.csproj
```

Apply migration to create database:

```powershell
dotnet ef database update --project .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj --startup-project .\HotelApp.Web\HotelApp.Web.csproj
```

If successful, your database is ready.

## 11) Implement m08 (Business logic)

Put business rules in `HotelApp.Application` service classes, for example:

- Create project
- Add task to project
- Complete task with validation rules

Use dependency injection in `HotelApp.Web\Program.cs`:

- Register `DbContext`
- Register repositories
- Register application services

## 12) Implement m09 (Tests)

### Run all tests

```powershell
dotnet test
```

### Recommended test split

- Domain unit tests: entity/value object behavior
- Application unit tests: use case logic with mocks
- Infrastructure integration tests: EF Core repository behavior

Start with simple red-green-refactor cycles:

1. Write one failing test.
2. Implement minimal code.
3. Run tests again.
4. Refactor safely.

## 13) Implement m10 (Frontend in .NET with Blazor)

In `HotelApp.Web`:

- Create pages/components for project list and task management
- Call application services via dependency injection
- Show validation and error messages in UI

Run frontend and backend together (same ASP.NET app):

```powershell
dotnet run --project .\HotelApp.Web\HotelApp.Web.csproj
```

Open browser:

- `https://localhost:xxxx` (shown in terminal)

Now you have a full .NET web app with DB and tests.

## 14) Daily workflow commands

From solution root:

```powershell
dotnet build
dotnet test
dotnet run --project .\HotelApp.Web\HotelApp.Web.csproj
```

When model changes:

```powershell
dotnet ef migrations add YourMigrationName --project .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj --startup-project .\HotelApp.Web\HotelApp.Web.csproj
dotnet ef database update --project .\HotelApp.Infrastructure\HotelApp.Infrastructure.csproj --startup-project .\HotelApp.Web\HotelApp.Web.csproj
```

## 15) Troubleshooting (first-time beginner issues)

### `dotnet` not found

- Restart terminal/PC after SDK install.
- Check SDK with `dotnet --list-sdks`.

### `dotnet ef` not found

- Run `dotnet tool install --global dotnet-ef`.
- Restart terminal.

### Migration fails with startup project error

- Always pass both flags:
  - `--project` = Infrastructure
  - `--startup-project` = Web

### SQL Server connection error

- Verify SQL Server Express/LocalDB is installed.
- Use the exact LocalDB connection string from this guide.

### HTTPS certificate warning

Run:

```powershell
dotnet dev-certs https --trust
```

## 16) Definition of done for m05-m10

You are done when all points are true:

- Solution builds with `dotnet build`
- Tests pass with `dotnet test`
- Migrations run successfully
- Database exists and stores data
- Web UI loads and can create/update data
- Architecture layers are separated (Domain/Application/Infrastructure/Web)

## 17) Optional next improvements

- Add authentication and authorization (ASP.NET Identity)
- Add API endpoints (Minimal API or Controllers)
- Add CI pipeline (GitHub Actions)
- Add code quality tools (`dotnet format`, analyzers)

If you want, the next step can be a fully prepared folder/file template for this architecture so you can copy it and start implementing immediately.
