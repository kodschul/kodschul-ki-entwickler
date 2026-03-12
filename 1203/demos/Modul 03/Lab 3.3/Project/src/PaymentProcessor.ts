import {
  PaymentRequest,
  PaymentResult,
  PaymentStatus,
  Invoice,
  InvoiceLineItem,
  PaymentItem,
} from './types';

// CODE SMELL: God Class – diese Klasse macht alles:
// Validierung, Zahlungsverarbeitung (alle Provider), Rabatte, Rechnungen, Logging
// Sie hat über 20 Methoden und kennt alle Geschäftsregeln
export class PaymentProcessor {
  private transactions: Map<string, PaymentResult> = new Map();
  private invoices: Map<string, Invoice> = new Map();
  private ic = 1000; // CODE SMELL: kryptischer Name (invoice counter)

  // CODE SMELL: Methode macht Validierung, Rabatt, Provider-Routing UND Logging
  processPayment(req: PaymentRequest): PaymentResult {
    // Validierung
    if (!req.id || !req.customerId) {
      throw new Error('Ungültige Anfrage');
    }
    if (req.amount <= 0) {
      throw new Error('Betrag muss positiv sein');
    }
    if (req.amount > 50000) { // MAGIC NUMBER
      throw new Error('Betrag überschreitet Maximum');
    }

    let amt = req.amount; // CODE SMELL: kryptischer Name

    // CODE SMELL: Duplikate Rabattlogik – fast identisch zu calculateDiscountForInvoice
    let d = 0; // CODE SMELL: kryptischer Name
    if (req.customerTier === 'SILVER') {
      d = amt * 0.05; // MAGIC NUMBER
    } else if (req.customerTier === 'GOLD') {
      d = amt * 0.10; // MAGIC NUMBER
    } else if (req.customerTier === 'PLATINUM') {
      d = amt * 0.15; // MAGIC NUMBER
    }

    if (req.couponCode === 'SAVE10') {
      d += amt * 0.10; // MAGIC NUMBER
    } else if (req.couponCode === 'SAVE20') {
      d += amt * 0.20; // MAGIC NUMBER
    } else if (req.couponCode === 'FREESHIP') {
      d += 4.99; // MAGIC NUMBER
    }

    amt = amt - d;

    // CODE SMELL: Switch-Statement das OCP verletzt – neuer Provider = Änderung hier
    let fee = 0;
    let txId = '';
    let status: PaymentStatus = 'COMPLETED';

    switch (req.provider) {
      case 'CREDIT_CARD':
        // Kreditkarte: 1.5% + 0.30 EUR
        fee = amt * 0.015 + 0.30; // MAGIC NUMBERS
        txId = `CC-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        console.log(`[CC] Verarbeite Kreditkartenzahlung: ${amt} EUR, Fee: ${fee}`);
        // Simuliere externe API
        if (amt > 1000) { // MAGIC NUMBER
          console.log('[CC] Zusätzliche 3D-Secure Prüfung erforderlich');
        }
        status = 'COMPLETED';
        break;

      case 'PAYPAL':
        // PayPal: 2.9% + 0.35 EUR
        fee = amt * 0.029 + 0.35; // MAGIC NUMBERS
        txId = `PP-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        console.log(`[PP] Verarbeite PayPal-Zahlung: ${amt} EUR, Fee: ${fee}`);
        if (req.currency !== 'EUR' && req.currency !== 'USD') { // Hardcoded
          console.warn('[PP] Währung könnte Probleme machen');
        }
        status = 'COMPLETED';
        break;

      case 'BANK_TRANSFER':
        // Überweisung: flache 1.00 EUR Gebühr
        fee = 1.00; // MAGIC NUMBER
        txId = `BT-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        console.log(`[BT] Verarbeite Banküberweisung: ${amt} EUR`);
        status = 'PENDING'; // Überweisung braucht Zeit
        break;

      case 'CRYPTO':
        // Krypto: 0.5% Gebühr
        fee = amt * 0.005; // MAGIC NUMBER
        txId = `CR-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        console.log(`[CR] Verarbeite Krypto-Zahlung: ${amt} EUR`);
        if (amt < 10) { // MAGIC NUMBER
          throw new Error('Krypto-Mindestzahlung: 10 EUR');
        }
        status = 'PROCESSING';
        break;

      default:
        throw new Error(`Unbekannter Provider: ${req.provider}`);
    }

    const result: PaymentResult = {
      transactionId: txId,
      status,
      processedAmount: amt,
      fee,
      timestamp: new Date(),
    };

    this.transactions.set(txId, result);
    console.log(`Zahlung abgeschlossen: ${txId}, Status: ${status}`);
    return result;
  }

  // CODE SMELL: Diese Methode ist 65 Zeilen lang und macht Rabatt, Tax, Invoice
  // Formatierung und Validierung in einem Block
  processAndGenerateInvoice(req: PaymentRequest): { result: PaymentResult; invoice: Invoice } {
    // Validierung (DUPLIKAT aus processPayment)
    if (!req.id || !req.customerId) {
      throw new Error('Ungültige Anfrage');
    }
    if (req.amount <= 0) {
      throw new Error('Betrag muss positiv sein');
    }

    // Zahlungsverarbeitung
    const result = this.processPayment(req);

    // Rechnungsposition aufbauen
    const lineItems: InvoiceLineItem[] = req.items.map((item: PaymentItem) => {
      // CODE SMELL: Tax-Logik ist hier inline – Magic Numbers für Steuersätze
      let tr = 0; // kryptisch: tax rate
      if (item.taxCategory === 'STANDARD') {
        tr = 0.19; // MAGIC NUMBER: 19% MwSt.
      } else if (item.taxCategory === 'REDUCED') {
        tr = 0.07; // MAGIC NUMBER: 7% MwSt.
      } else {
        tr = 0; // befreit
      }
      const lt = item.quantity * item.unitPrice * (1 + tr); // kryptisch: line total
      return {
        description: item.name,
        quantity: item.quantity,
        unitPrice: item.unitPrice,
        taxRate: tr,
        lineTotal: lt,
      };
    });

    // Summen berechnen
    const sub = lineItems.reduce((s, li) => s + li.quantity * li.unitPrice, 0); // kryptisch: subtotal
    const tax = lineItems.reduce((s, li) => s + li.quantity * li.unitPrice * li.taxRate, 0);

    // Rabatt berechnen (CODE SMELL: fast identisch zu processPayment)
    let disc = 0;
    if (req.customerTier === 'SILVER') {
      disc = sub * 0.05; // MAGIC NUMBER
    } else if (req.customerTier === 'GOLD') {
      disc = sub * 0.10; // MAGIC NUMBER
    } else if (req.customerTier === 'PLATINUM') {
      disc = sub * 0.15; // MAGIC NUMBER
    }
    if (req.couponCode === 'SAVE10') {
      disc += sub * 0.10; // MAGIC NUMBER – DUPLIKAT
    } else if (req.couponCode === 'SAVE20') {
      disc += sub * 0.20; // MAGIC NUMBER – DUPLIKAT
    } else if (req.couponCode === 'FREESHIP') {
      disc += 4.99; // MAGIC NUMBER – DUPLIKAT
    }

    // Rechnungsnummer generieren
    const invNum = `INV-${new Date().getFullYear()}-${String(++this.ic).padStart(6, '0')}`;

    // Fälligkeitsdatum: 14 Tage (MAGIC NUMBER)
    const due = new Date();
    due.setDate(due.getDate() + 14); // MAGIC NUMBER

    const invoice: Invoice = {
      invoiceNumber: invNum,
      customerId: req.customerId,
      items: lineItems,
      subtotal: sub,
      discount: disc,
      taxAmount: tax,
      total: sub - disc + tax,
      createdAt: new Date(),
      dueDate: due,
    };

    this.invoices.set(invNum, invoice);
    console.log(`Rechnung erstellt: ${invNum}, Gesamt: ${invoice.total.toFixed(2)} EUR`);

    return { result, invoice };
  }

  getTransaction(txId: string): PaymentResult | undefined {
    return this.transactions.get(txId);
  }

  getInvoice(invoiceNumber: string): Invoice | undefined {
    return this.invoices.get(invoiceNumber);
  }

  // CODE SMELL: Diese Validierungsmethode existiert, wird aber in processPayment
  // nicht genutzt – stattdessen ist Validierungslogik inline dupliziert
  validateRequest(req: PaymentRequest): string[] {
    const errors: string[] = [];
    if (!req.id) errors.push('ID fehlt');
    if (!req.customerId) errors.push('Kunden-ID fehlt');
    if (!req.amount || req.amount <= 0) errors.push('Ungültiger Betrag');
    if (req.amount > 50000) errors.push('Betrag zu hoch'); // MAGIC NUMBER
    if (!req.provider) errors.push('Provider fehlt');
    if (!req.currency) errors.push('Währung fehlt');
    return errors;
  }

  refundPayment(txId: string): PaymentResult {
    const tx = this.transactions.get(txId);
    if (!tx) {
      throw new Error(`Transaktion ${txId} nicht gefunden`);
    }
    if (tx.status === 'REFUNDED') {
      throw new Error('Bereits erstattet');
    }
    if (tx.status !== 'COMPLETED') {
      throw new Error('Nur abgeschlossene Zahlungen können erstattet werden');
    }
    tx.status = 'REFUNDED';
    console.log(`Erstattung für ${txId}: ${tx.processedAmount} EUR`);
    return tx;
  }
}
