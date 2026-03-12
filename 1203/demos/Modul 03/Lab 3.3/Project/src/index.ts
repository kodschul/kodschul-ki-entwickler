import { PaymentProcessor } from './PaymentProcessor';
import { PaymentRequest } from './types';

const processor = new PaymentProcessor();

// Demo-Zahlung
const req: PaymentRequest = {
  id: 'PAY-001',
  customerId: 'CUST-42',
  customerTier: 'GOLD',
  amount: 299.90,
  currency: 'EUR',
  provider: 'CREDIT_CARD',
  description: 'Software-Lizenz Jahresabo',
  couponCode: 'SAVE10',
  items: [
    { name: 'Pro-Lizenz', quantity: 1, unitPrice: 249.00, taxCategory: 'STANDARD' },
    { name: 'Support-Paket', quantity: 1, unitPrice: 50.90, taxCategory: 'STANDARD' },
  ],
};

const { result, invoice } = processor.processAndGenerateInvoice(req);
console.log('\n--- Zahlungsergebnis ---');
console.log(`Transaction ID: ${result.transactionId}`);
console.log(`Status: ${result.status}`);
console.log(`Betrag: ${result.processedAmount.toFixed(2)} EUR`);
console.log(`Gebühr: ${result.fee.toFixed(2)} EUR`);
console.log('\n--- Rechnung ---');
console.log(`Rechnungsnummer: ${invoice.invoiceNumber}`);
console.log(`Zwischensumme: ${invoice.subtotal.toFixed(2)} EUR`);
console.log(`Rabatt: -${invoice.discount.toFixed(2)} EUR`);
console.log(`MwSt.: ${invoice.taxAmount.toFixed(2)} EUR`);
console.log(`Gesamt: ${invoice.total.toFixed(2)} EUR`);
console.log(`Fällig am: ${invoice.dueDate.toLocaleDateString('de-DE')}`);
