// TODO: Dieser Service muss vollständig implementiert werden.
//
// Anforderungen:
// - Methode: calculateUnitPrice(product: Product, quantity: number): number
//     Berechnet den Preis pro Einheit basierend auf der Menge:
//     - Standard: basePrice
//     - Ab 10 Stück: 5% Rabatt auf den Stückpreis
//     - Ab 50 Stück: 10% Rabatt auf den Stückpreis
//
// - Methode: applyTax(price: number, taxRate: number): number
//     Wendet eine Steuerrate auf einen Preis an (z.B. 0.19 für 19% MwSt.)
//     Gibt den Bruttopreis zurück.
//
// - Methode: formatPrice(amount: number, currency: string): string
//     Formatiert einen Preis als lesbaren String.
//     Beispiel: formatPrice(29.9, 'EUR') => "29,90 €"
//     Nutze die Intl.NumberFormat API.
//
// Importiere Product aus '../models/Product' und implementiere die Klasse PricingService.

import { Product } from '../models/Product';

// TODO: Implementiere PricingService hier
