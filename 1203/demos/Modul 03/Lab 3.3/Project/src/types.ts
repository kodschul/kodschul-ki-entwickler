export type PaymentProvider = 'CREDIT_CARD' | 'PAYPAL' | 'BANK_TRANSFER' | 'CRYPTO';
export type PaymentStatus = 'PENDING' | 'PROCESSING' | 'COMPLETED' | 'FAILED' | 'REFUNDED';
export type CustomerTier = 'STANDARD' | 'SILVER' | 'GOLD' | 'PLATINUM';

export interface PaymentRequest {
  id: string;
  customerId: string;
  customerTier: CustomerTier;
  amount: number;
  currency: string;
  provider: PaymentProvider;
  description: string;
  items: PaymentItem[];
  couponCode?: string;
}

export interface PaymentItem {
  name: string;
  quantity: number;
  unitPrice: number;
  taxCategory: 'STANDARD' | 'REDUCED' | 'EXEMPT';
}

export interface PaymentResult {
  transactionId: string;
  status: PaymentStatus;
  processedAmount: number;
  fee: number;
  timestamp: Date;
  invoiceUrl?: string;
}

export interface Invoice {
  invoiceNumber: string;
  customerId: string;
  items: InvoiceLineItem[];
  subtotal: number;
  discount: number;
  taxAmount: number;
  total: number;
  createdAt: Date;
  dueDate: Date;
}

export interface InvoiceLineItem {
  description: string;
  quantity: number;
  unitPrice: number;
  taxRate: number;
  lineTotal: number;
}
