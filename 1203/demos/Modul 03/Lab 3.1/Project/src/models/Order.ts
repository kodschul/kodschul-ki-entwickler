export type OrderStatus = 'PENDING' | 'CONFIRMED' | 'SHIPPED' | 'DELIVERED' | 'CANCELLED';

export interface OrderItem {
  productId: string;
  productName: string;
  quantity: number;
  unitPrice: number;
}

// TODO: Diese Klasse ist unvollständig. Es fehlen:
// - Eine Methode addItem(item: OrderItem): void
// - Eine Methode removeItem(productId: string): void
// - Eine Methode getTotalItemCount(): number
// - Ein Getter für den Gesamtpreis (ohne Rabatte)
// Implementiere diese Methoden mithilfe des KI-Assistenten.
export class Order {
  public id: string;
  public customerId: string;
  public items: OrderItem[];
  public status: OrderStatus;
  public createdAt: Date;
  public updatedAt: Date;
  public discountCode?: string;

  constructor(id: string, customerId: string) {
    this.id = id;
    this.customerId = customerId;
    this.items = [];
    this.status = 'PENDING';
    this.createdAt = new Date();
    this.updatedAt = new Date();
  }

  // TODO: Implementiere addItem
  addItem(item: OrderItem): void {
    // ...
  }

  // TODO: Implementiere removeItem
  removeItem(productId: string): void {
    // ...
  }

  // TODO: Implementiere getTotalItemCount
  getTotalItemCount(): number {
    return 0; // Platzhalter
  }

  // TODO: Implementiere subtotal getter
  get subtotal(): number {
    return 0; // Platzhalter
  }
}
