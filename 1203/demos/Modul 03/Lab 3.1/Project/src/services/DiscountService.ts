export interface Discount {
  code: string;
  percentage: number;
  minOrderValue: number;
  validUntil: Date;
  isActive: boolean;
}

export class DiscountService {
  private discounts: Map<string, Discount> = new Map([
    ['SAVE10', { code: 'SAVE10', percentage: 10, minOrderValue: 50, validUntil: new Date('2027-12-31'), isActive: true }],
    ['SAVE20', { code: 'SAVE20', percentage: 20, minOrderValue: 100, validUntil: new Date('2027-12-31'), isActive: true }],
    ['EXPIRED', { code: 'EXPIRED', percentage: 15, minOrderValue: 0, validUntil: new Date('2020-01-01'), isActive: false }],
  ]);

  getDiscount(code: string | undefined): Discount | null {
    if (!code) return null;
    const discount = this.discounts.get(code.toUpperCase());
    if (!discount || !discount.isActive) return null;
    if (discount.validUntil < new Date()) return null;
    return discount;
  }

  // TODO: Implementiere applyDiscount(subtotal: number, code: string): number
  // Wendet den Rabatt auf den Subtotal an, wenn:
  // - Der Rabattcode gültig ist
  // - Der Bestellwert >= minOrderValue ist
  // Gibt den reduzierten Preis zurück (oder den Originalpreis, wenn kein Rabatt gilt)
  applyDiscount(subtotal: number, code?: string): number {
    // TODO
    return subtotal;
  }
}
