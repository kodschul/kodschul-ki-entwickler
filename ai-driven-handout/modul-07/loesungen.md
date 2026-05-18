# Modul 7 — Lösungen

---

## Lösung 7.4-A — Breaking Change Migrationspfad

**Risiko bei naivem Rename:**
EF Core generiert für eine Eigenschaft die umbenannt wird: `DROP COLUMN GuestName` + `ADD COLUMN CustomerId` → alle vorhandenen Daten in `GuestName` werden gelöscht.

**Sicherer 3-stufiger Migrationspfad:**

```csharp
// Migration 1: Neue Spalte nullable hinzufügen
public partial class AddCustomerIdNullable : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.AddColumn<Guid>("CustomerId", "Bookings", nullable: true);
    }
}

// Migration 2: Daten migrieren (Data Migration)
public partial class MigrateGuestNameToCustomerId : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        // Kunden anlegen für bestehende GuestNames und CustomerId setzen
        // (vereinfacht – in der Praxis komplexer)
        migrationBuilder.Sql(@"
            INSERT INTO Customers (Id, FullName, CreatedAt)
            SELECT NEWID(), GuestName, GETUTCDATE()
            FROM Bookings
            WHERE CustomerId IS NULL AND GuestName IS NOT NULL;

            UPDATE b SET b.CustomerId = c.Id
            FROM Bookings b
            INNER JOIN Customers c ON c.FullName = b.GuestName
            WHERE b.CustomerId IS NULL;
        ");
    }
}

// Migration 3: GuestName entfernen, CustomerId auf required setzen
public partial class FinalizeCustomerIdMigration : Migration
{
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.AlterColumn<Guid>("CustomerId", "Bookings", nullable: false);
        migrationBuilder.DropColumn("GuestName", "Bookings");
        migrationBuilder.CreateIndex("IX_Bookings_CustomerId", "Bookings", "CustomerId");
        migrationBuilder.AddForeignKey("FK_Bookings_Customers_CustomerId",
            "Bookings", "CustomerId", "Customers", "Id",
            onDelete: ReferentialAction.Restrict);
    }
}
```

---

## Lösung 7.4-B — Migrations-Analyse

| # | Stelle | Problem | Korrektur |
|---|---|---|---|
| 1 | `int Id` | int statt Guid, Identity-Spalte | `Guid` + `ValueGeneratedNever()` |
| 2 | `GuestName` nullable | Gastname als nullable String, kein FK | Besser: `GuestId` als FK auf `Customers` |
| 3 | `double Price` | Rundungsfehler bei Geldbeträgen | `decimal(10,2)` via `type: "decimal(10,2)"` |
| 4 | `int Status` | Enum als Zahl → unleserlich in DB | `nvarchar(30)` für String-Konvertierung |
| 5 | `int RoomId` | int statt Guid (inkonsistent) | `Guid RoomId` |
| 6 | Kein Primary Key definiert | Keine `PrimaryKey`-Constraint | `table.PrimaryKey("PK_Bookings", x => x.Id)` |
| 7 | Kein FK-Constraint für RoomId | Referentielle Integrität fehlt | `table.ForeignKey(...)` auf Rooms.Id |
| 8 | Kein Index auf RoomId | Langsame Abfragen aller Buchungen für ein Zimmer | `migrationBuilder.CreateIndex("IX_Bookings_RoomId", ...)` |

**Korrigierte Migration:**
```csharp
migrationBuilder.CreateTable(
    name: "Bookings",
    columns: table => new
    {
        Id = table.Column<Guid>(nullable: false),
        GuestId = table.Column<Guid>(nullable: false),
        CheckInDate = table.Column<DateTime>(nullable: false),
        CheckOutDate = table.Column<DateTime>(nullable: false),
        TotalPrice = table.Column<decimal>(type: "decimal(10,2)", nullable: false),
        CancellationFee = table.Column<decimal>(type: "decimal(10,2)", nullable: true),
        Status = table.Column<string>(maxLength: 30, nullable: false, defaultValue: "Pending"),
        RoomId = table.Column<Guid>(nullable: false),
        CreatedAt = table.Column<DateTime>(nullable: false, defaultValueSql: "GETUTCDATE()"),
        UpdatedAt = table.Column<DateTime>(nullable: false, defaultValueSql: "GETUTCDATE()")
    },
    constraints: table =>
    {
        table.PrimaryKey("PK_Bookings", x => x.Id);
        table.ForeignKey("FK_Bookings_Rooms_RoomId", x => x.RoomId, "Rooms", "Id",
            onDelete: ReferentialAction.Restrict);
        table.ForeignKey("FK_Bookings_Guests_GuestId", x => x.GuestId, "Guests", "Id",
            onDelete: ReferentialAction.Restrict);
    });

migrationBuilder.CreateIndex("IX_Bookings_RoomId", "Bookings", "RoomId");
migrationBuilder.CreateIndex("IX_Bookings_GuestId", "Bookings", "GuestId");
```
