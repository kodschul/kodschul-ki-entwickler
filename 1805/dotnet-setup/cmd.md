dotnet new sln -n HotelApp

# --- 001_HotelApp Setup ---

# Arbeitsverzeichnis: 1805/001_HotelApp

# Migration erstellen (leere AppDbContext)

dotnet ef migrations add InitialCreate --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Datenbank aktualisieren

dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Migrationseintrag manuell löschen (nach manueller Bearbeitung der Up()-Methode)

Invoke-Sqlcmd -ServerInstance ".\SQLEXPRESS" -Database "HotelSampleDB" -Query "DELETE FROM [__EFMigrationsHistory]"

# Datenbank neu befüllen (mit korrekter Up()-Methode für Bookings-Tabelle)

dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Seed-Migration erstellen (nach DbSet<Booking> + HasData in AppDbContext)

dotnet ef migrations add SeedBookings --project HotelApp.Infrastructure --startup-project HotelApp.Web

# Datenbank aktualisieren

dotnet ef migrations remove --project HotelApp.Infrastructure --startup-project HotelApp.Web --force

dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web

# HotelApp — AI Prompts zum Reproduzieren

## Modul 6 — Domain Model & EF Core Setup

```prompt
Wir bauen eine .NET 8 Clean Architecture Solution namens HotelApp
mit den Projekten: HotelApp.Domain, HotelApp.Application,
HotelApp.Infrastructure, HotelApp.Web (Blazor), HotelApp.Tests.

Erstelle die Booking-Klasse als Aggregate Root im Domain Layer mit:
- Properties: Id, RoomId, GuestId, CheckInDate, CheckOutDate,
  Status (enum: Requested, Confirmed, CheckedIn, CheckedOut, Cancelled),
  TotalPrice, CancellationFee (nullable)
- Methoden: Confirm(), Cancel(DateTimeOffset), CheckIn()
- Validierung im Konstruktor (Guards)
- Private Setter (Encapsulation)
```

## Modul 7 — Migration & Seed-Daten

```prompt
Konfiguriere den AppDbContext mit DbSet<Booking> und OnModelCreating:
- Status als nvarchar(20) mit HasConversion<string>
- TotalPrice und CancellationFee mit HasPrecision(18,2)
- Indizes auf RoomId und GuestId
- HasData mit 3 Seed-Eintraegen (Confirmed, Requested, Cancelled)
  mit fixen GUIDs fuer Idempotenz.

Erstelle dann mit EF Core eine Migration InitialCreate und wende
sie auf SQL Server Express an:
  dotnet ef migrations add InitialCreate --project HotelApp.Infrastructure --startup-project HotelApp.Web
  dotnet ef database update --project HotelApp.Infrastructure --startup-project HotelApp.Web
```

## Modul 8 — Geschaeftslogik

```prompt
Integriere die Clean Architecture Geschaeftslogik-Schicht fuer Booking:

1. IBookingRepository Interface im Domain Layer
   (GetByIdAsync, GetAllAsync, AddAsync, SaveChangesAsync)

2. BookingService im Application Layer (Orchestrierung nach dem Muster:
   Laden -> Domaenenlogik delegieren -> Persistieren)
   Methoden: func_CreateAsync, func_ConfirmAsync, func_CancelAsync, func_CheckInAsync

3. BookingRepository im Infrastructure Layer als EF Core Implementierung

4. Registriere IBookingRepository und BookingService als Scoped Services
   in Program.cs
```

## Modul 9 - Softwaretests

```prompt
Erstelle Unit-Tests fuer das HotelApp-Projekt mit xUnit, FluentAssertions und Moq.

1. BookingTests.cs - Domain Unit Tests fuer die Booking-Klasse:
   - Konstruktor Happy Path (Status = Requested, Properties korrekt)
   - Konstruktor Guards (EmptyRoomId, EmptyGuestId, CheckOut <= CheckIn, negativer Preis)
   - Confirm() Happy Path und alle ungueltigen Status (Theory/InlineData)
   - Cancel() Happy Path fuer Requested (kein Fee) und Confirmed spaet (Fee > 0)
   - Cancel() Guards fuer CheckedIn, CheckedOut, Cancelled

2. BookingServiceTests.cs - Application Service Tests mit gemocktem IBookingRepository:
   - func_CreateAsync: prueft AddAsync + SaveChangesAsync mit korrekten Werten
   - func_ConfirmAsync: confirmt Booking und ruft SaveChangesAsync auf
   - func_ConfirmAsync: BookingNotFound wirft KeyNotFoundException
   - func_CancelAsync: cancelt Booking und speichert
   - func_CheckInAsync: checked-in wenn Confirmed und CheckInDate = heute
   - func_GetByIdAsync: gibt Booking zurueck oder null

Konventionen: camelCase, func_-Praefix, Private Setter per Reflection fuer Test-Setup.
```

# Befehl zum Ausfuehren der Tests:

dotnet test

## Modul 10 - Frontend + Backend API

```prompt
Integriere fuer das finale Modul m10 eine komplette Booking-Webflaeche mit API:

Backend (Minimal API in Program.cs):
- GET /api/bookings
- GET /api/bookings/{id}
- POST /api/bookings
- POST /api/bookings/{id}/confirm
- POST /api/bookings/{id}/cancel
- POST /api/bookings/{id}/checkin
- Validiere Input (Guid nicht leer, CheckOut > CheckIn, Preis >= 0)
- Mapping auf BookingService und passende HTTP-Responses (404/400/204/201)

Frontend (Blazor):
- Neue Seite Components/Pages/Bookings.razor
- Liste aller Bookings aus /api/bookings
- Formular zum Anlegen einer Booking
- Buttons fuer Confirm/Cancel/Check-In je Zeile
- Fehler als Meldung anzeigen und nach Aktionen Reload ausfuehren
- Navigationseintrag in NavMenu.razor ergaenzen
```

# m10 ausgefuehrte Kommandos:

dotnet build HotelApp.sln
dotnet build "c:\Users\User\Documents\kodschul\kodschul-ki-entwickler\1805\001_HotelApp\HotelApp.sln"
dotnet run --project "c:\Users\User\Documents\kodschul\kodschul-ki-entwickler\1805\001_HotelApp\HotelApp.Web\HotelApp.Web.csproj"
