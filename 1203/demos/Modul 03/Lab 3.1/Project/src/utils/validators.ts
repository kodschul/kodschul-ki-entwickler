import { Customer } from '../models/Customer';

// TODO: Alle Validierungsfunktionen müssen hier implementiert werden.
// Nutze den KI-Assistenten, um die Funktionen basierend auf den JSDoc-Beschreibungen zu generieren.

/**
 * Prüft, ob eine E-Mail-Adresse gültig ist.
 * Eine gültige E-Mail enthält ein @-Zeichen, einen lokalen Teil und eine Domain mit TLD.
 * @param email - Die zu prüfende E-Mail-Adresse
 * @returns true, wenn die E-Mail gültig ist
 */
export function isValidEmail(email: string): boolean {
  // TODO
  return false;
}

/**
 * Prüft, ob eine Bestell-ID das korrekte Format hat.
 * Gültiges Format: ORD-XXXXXX (ORD- gefolgt von genau 6 Ziffern)
 * Beispiele: ORD-001234, ORD-999999
 * @param id - Die zu prüfende Bestell-ID
 * @returns true, wenn das Format korrekt ist
 */
export function isValidOrderId(id: string): boolean {
  // TODO
  return false;
}

/**
 * Prüft, ob eine Produktmenge gültig ist.
 * Gültig bedeutet: positiv, ganzzahlig, maximal 9999
 * @param quantity - Die zu prüfende Menge
 * @returns true, wenn die Menge gültig ist
 */
export function isValidProductQuantity(quantity: number): boolean {
  // TODO
  return false;
}

/**
 * Prüft, ob ein Kundenobjekt die minimum erforderlichen Felder enthält.
 * firstName, lastName und email müssen vorhanden und nicht leer sein.
 * Die E-Mail muss außerdem das gültige Format haben (nutze isValidEmail).
 * @param customer - Das zu prüfende Kundenobjekt
 * @returns true, wenn der Kunde valide ist
 */
export function isValidCustomer(customer: Customer): boolean {
  // TODO
  return false;
}
