export interface StockMovement {
  id: string;
  productId: string;
  type: 'IN' | 'OUT' | 'ADJUSTMENT';
  quantity: number;
  timestamp: Date;
  reason: string;
}

export interface InventoryItem {
  productId: string;
  productName: string;
  currentStock: number;
  minimumStock: number;
  maximumStock: number;
  unit: string;
}

export class InventoryManager {
  private inventory: Map<string, InventoryItem> = new Map();
  private movements: StockMovement[] = [];
  private movementCounter = 0;

  addProduct(item: InventoryItem): void {
    if (this.inventory.has(item.productId)) {
      throw new Error(`Produkt ${item.productId} existiert bereits`);
    }
    this.inventory.set(item.productId, { ...item });
    console.log(`Produkt ${item.productName} zum Lager hinzugefügt`);
  }

  getProduct(productId: string): InventoryItem | undefined {
    return this.inventory.get(productId);
  }

  // BUG: Es gibt einen Logikfehler in dieser Methode.
  // Die Prüfung auf Mindestbestand funktioniert nicht korrekt.
  // Unter bestimmten Umständen kann der Bestand trotzdem unter das Minimum fallen.
  bookStockOut(productId: string, quantity: number, reason: string): StockMovement {
    const item = this.inventory.get(productId);
    if (!item) {
      throw new Error(`Produkt ${productId} nicht gefunden`);
    }

    // BUG: Diese Bedingung ist falsch – sie prüft nach der Buchung, nicht vorher
    const newStock = item.currentStock - quantity;
    item.currentStock = newStock; // Bestand wird ZUERST reduziert...

    if (item.currentStock < item.minimumStock) { // ...dann erst geprüft
      console.warn(`Warnung: Mindestbestand unterschritten für ${item.productName}`);
    }

    const movement: StockMovement = {
      id: `MOV-${++this.movementCounter}`,
      productId,
      type: 'OUT',
      quantity,
      timestamp: new Date(),
      reason,
    };
    this.movements.push(movement);
    return movement;
  }

  bookStockIn(productId: string, quantity: number, reason: string): StockMovement {
    const item = this.inventory.get(productId);
    if (!item) {
      throw new Error(`Produkt ${productId} nicht gefunden`);
    }

    if (item.currentStock + quantity > item.maximumStock) {
      throw new Error(`Maximaler Lagerbestand würde überschritten`);
    }

    item.currentStock += quantity;

    const movement: StockMovement = {
      id: `MOV-${++this.movementCounter}`,
      productId,
      type: 'IN',
      quantity,
      timestamp: new Date(),
      reason,
    };
    this.movements.push(movement);
    return movement;
  }

  getLowStockItems(): InventoryItem[] {
    return Array.from(this.inventory.values()).filter(
      (item) => item.currentStock <= item.minimumStock
    );
  }

  getMovementHistory(productId: string): StockMovement[] {
    return this.movements.filter((m) => m.productId === productId);
  }

  exportReport(): string {
    const { ReportGenerator } = require('./ReportGenerator');
    const generator = new ReportGenerator();
    return generator.generateStockReport(Array.from(this.inventory.values()));
  }
}
