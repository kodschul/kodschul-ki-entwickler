using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace HotelApp.Infrastructure.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Bookings",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uniqueidentifier", nullable: false),
                    RoomId = table.Column<Guid>(type: "uniqueidentifier", nullable: false),
                    GuestId = table.Column<Guid>(type: "uniqueidentifier", nullable: false),
                    CheckInDate = table.Column<DateOnly>(type: "date", nullable: false),
                    CheckOutDate = table.Column<DateOnly>(type: "date", nullable: false),
                    Status = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: false, defaultValue: "Requested"),
                    TotalPrice = table.Column<decimal>(type: "decimal(18,2)", precision: 18, scale: 2, nullable: false),
                    CancellationFee = table.Column<decimal>(type: "decimal(18,2)", precision: 18, scale: 2, nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Bookings", x => x.Id);
                });

            migrationBuilder.InsertData(
                table: "Bookings",
                columns: new[] { "Id", "CancellationFee", "CheckInDate", "CheckOutDate", "GuestId", "RoomId", "Status", "TotalPrice" },
                values: new object[] { new Guid("aaaaaaaa-0000-0000-0000-000000000001"), null, new DateOnly(2026, 6, 1), new DateOnly(2026, 6, 5), new Guid("cccccccc-0000-0000-0000-000000000001"), new Guid("bbbbbbbb-0000-0000-0000-000000000001"), "Confirmed", 516.00m });

            migrationBuilder.InsertData(
                table: "Bookings",
                columns: new[] { "Id", "CancellationFee", "CheckInDate", "CheckOutDate", "GuestId", "RoomId", "TotalPrice" },
                values: new object[] { new Guid("aaaaaaaa-0000-0000-0000-000000000002"), null, new DateOnly(2026, 7, 10), new DateOnly(2026, 7, 14), new Guid("cccccccc-0000-0000-0000-000000000002"), new Guid("bbbbbbbb-0000-0000-0000-000000000002"), 356.00m });

            migrationBuilder.InsertData(
                table: "Bookings",
                columns: new[] { "Id", "CancellationFee", "CheckInDate", "CheckOutDate", "GuestId", "RoomId", "Status", "TotalPrice" },
                values: new object[] { new Guid("aaaaaaaa-0000-0000-0000-000000000003"), 50.00m, new DateOnly(2026, 5, 1), new DateOnly(2026, 5, 3), new Guid("cccccccc-0000-0000-0000-000000000003"), new Guid("bbbbbbbb-0000-0000-0000-000000000001"), "Cancelled", 258.00m });

            migrationBuilder.CreateIndex(
                name: "IX_Bookings_GuestId",
                table: "Bookings",
                column: "GuestId");

            migrationBuilder.CreateIndex(
                name: "IX_Bookings_RoomId",
                table: "Bookings",
                column: "RoomId");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Bookings");
        }
    }
}
