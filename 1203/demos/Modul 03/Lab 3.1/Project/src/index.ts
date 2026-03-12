import { Order } from './models/Order';
import { Product } from './models/Product';
import { Customer } from './models/Customer';
import { OrderService } from './services/OrderService';
import { DiscountService } from './services/DiscountService';

// Beispiel-Einstiegspunkt – zeigt die Nutzung des Systems
const discountService = new DiscountService();
const orderService = new OrderService(discountService);

// Beispielkunde anlegen
const customer = new Customer('CUST-001', 'Maria', 'Müller', 'maria.mueller@example.com');
customer.address = {
  street: 'Hauptstraße 42',
  city: 'Berlin',
  postalCode: '10115',
  country: 'DE',
};

// Beispielprodukte
const laptop = new Product('PROD-001', 'Laptop Pro 15', 'Leistungsstarker Entwicklerlaptop', 1299.99, 'ELECTRONICS', 50, 'LP-PRO-15');
const mouse = new Product('PROD-002', 'Ergonomische Maus', 'Kabellose Maus mit Präzisionsscroll', 49.99, 'ELECTRONICS', 200, 'MOUSE-ERG-01');

// Bestellung erstellen
const order = orderService.createOrder(customer.id);
order.discountCode = 'SAVE10';

orderService.addItemToOrder(order.id, {
  productId: laptop.id,
  productName: laptop.name,
  quantity: 1,
  unitPrice: laptop.basePrice,
});

orderService.addItemToOrder(order.id, {
  productId: mouse.id,
  productName: mouse.name,
  quantity: 2,
  unitPrice: mouse.basePrice,
});

orderService.confirmOrder(order.id);

// Gesamtpreis berechnen (TODO in OrderService)
const total = orderService.calculateOrderTotal(order.id);
console.log(`Bestellsumme für ${order.id}: ${total} EUR`);

// Alle Bestellungen des Kunden abrufen (TODO in OrderService)
const customerOrders = orderService.getOrdersByCustomer(customer.id);
console.log(`Bestellungen von ${customer.fullName}: ${customerOrders.length}`);

console.log('System gestartet – bereit für weitere Bestellungen.');
