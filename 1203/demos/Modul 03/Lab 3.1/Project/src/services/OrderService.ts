import { Order, OrderItem, OrderStatus } from '../models/Order';
import { DiscountService } from './DiscountService';

export class OrderService {
  private orders: Map<string, Order> = new Map();
  private discountService: DiscountService;
  private orderCounter: number = 1000;

  constructor(discountService: DiscountService) {
    this.discountService = discountService;
  }

  createOrder(customerId: string): Order {
    const id = `ORD-${++this.orderCounter}`;
    const order = new Order(id, customerId);
    this.orders.set(id, order);
    console.log(`Bestellung ${id} für Kunde ${customerId} erstellt.`);
    return order;
  }

  getOrderById(orderId: string): Order | undefined {
    return this.orders.get(orderId);
  }

  addItemToOrder(orderId: string, item: OrderItem): void {
    const order = this.orders.get(orderId);
    if (!order) {
      throw new Error(`Bestellung ${orderId} nicht gefunden`);
    }
    if (order.status !== 'PENDING') {
      throw new Error(`Artikel können nur zu Bestellungen mit Status PENDING hinzugefügt werden`);
    }
    order.addItem(item);
  }

  confirmOrder(orderId: string): void {
    const order = this.orders.get(orderId);
    if (!order) {
      throw new Error(`Bestellung ${orderId} nicht gefunden`);
    }
    if (order.items.length === 0) {
      throw new Error(`Leere Bestellungen können nicht bestätigt werden`);
    }
    order.status = 'CONFIRMED';
    order.updatedAt = new Date();
  }

  // TODO: Implementiere diese Methode.
  // Sie soll den Gesamtpreis der Bestellung berechnen.
  // Berücksichtige dabei:
  // - Die Summe aller OrderItems (quantity * unitPrice)
  // - Einen optionalen Rabatt über discountService.getDiscount(order.discountCode)
  // - Gibt 0 zurück, wenn die Bestellung nicht gefunden wird
  calculateOrderTotal(orderId: string): number {
    // TODO
    return 0;
  }

  // TODO: Implementiere diese Methode.
  // Regeln:
  // - Status muss PENDING oder CONFIRMED sein (nicht SHIPPED, DELIVERED oder CANCELLED)
  // - Setze den Status auf 'CANCELLED'
  // - Wirft einen Fehler, wenn die Bestellung nicht existiert
  // - Wirft einen Fehler, wenn die Bestellung nicht mehr stornierbar ist
  cancelOrder(orderId: string): void {
    // TODO
  }

  // TODO: Implementiere diese Methode.
  // Gibt alle Bestellungen zurück, die einem bestimmten Kunden gehören.
  // Gibt ein leeres Array zurück, wenn keine gefunden wurden.
  getOrdersByCustomer(customerId: string): Order[] {
    // TODO
    return [];
  }

  getAllOrders(): Order[] {
    return Array.from(this.orders.values());
  }

  updateOrderStatus(orderId: string, status: OrderStatus): void {
    const order = this.orders.get(orderId);
    if (!order) {
      throw new Error(`Bestellung ${orderId} nicht gefunden`);
    }
    order.status = status;
    order.updatedAt = new Date();
  }
}
