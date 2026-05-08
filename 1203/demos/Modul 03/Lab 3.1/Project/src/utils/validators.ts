import { Customer } from "../models/Customer";

// TODO: Alle Validierungsfunktionen müssen hier implementiert werden.
// Nutze den KI-Assistenten, um die Funktionen basierend auf den JSDoc-Beschreibungen zu generieren.

/**
 * Prüft, ob eine E-Mail-Adresse gültig ist.
 * Eine gültige E-Mail enthält ein @-Zeichen, einen lokalen Teil und eine Domain mit TLD.
 * @param email - Die zu prüfende E-Mail-Adresse
 * @returns true, wenn die E-Mail gültig ist
 */
export function is_Email(email: string): boolean {
  if (!email.includes("@")) {
    return false;
  }

  if (email.startsWith("@") || email.endsWith("@")) {
    return false;
  }

  if (!email.includes(".")) {
    return false;
  }
  const domainPart = email.split("@")[1];
  if (!domainPart.includes(".")) {
    return false;
  }
  const tld = domainPart.split(".").pop();
  if (tld.length < 2) {
    return false;
  }

  return true;
}

/**
 * Prüft, ob eine Bestell-ID das korrekte Format hat.
 * Gültiges Format: ORD-XXXXXX (ORD- gefolgt von genau 6 Ziffern)
 * Beispiele: ORD-001234, ORD-999999
 * @param id - Die zu prüfende Bestell-ID
 * @returns true, wenn das Format korrekt ist
 */
export function is_OrderId(id: string): boolean {
  const orderIdPattern = /^ORD-\d{6}$/;
  return orderIdPattern.test(id);
}

/**
 * Prüft, ob eine Produktmenge gültig ist.
 * Gültig bedeutet: positiv, ganzzahlig, maximal 9999
 * @param quantity - Die zu prüfende Menge
 * @returns true, wenn die Menge gültig ist
 */
export function is_ProductQuantity(quantity: number): boolean {
  return Number.isInteger(quantity) && quantity > 0 && quantity <= 9999;
}

/**
 * Prüft, ob ein Kundenobjekt die minimum erforderlichen Felder enthält.
 * firstName, lastName und email müssen vorhanden und nicht leer sein.
 * Die E-Mail muss außerdem das gültige Format haben (nutze is_Email).
 * @param customer - Das zu prüfende Kundenobjekt
 * @returns true, wenn der Kunde valide ist
 */
export function is_OkCustomer(customer: Customer): boolean {
  if (!customer.firstName || !customer.lastName || !customer.email) {
    return false;
  }
  return is_Email(customer.email);
}
