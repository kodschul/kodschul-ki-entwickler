// BUG: Diese Datei enthält einen Logikfehler bei der Datumsberechnung.
// isExpired() liefert falsche Ergebnisse – abgelaufene Artikel werden als gültig
// angezeigt und gültige Artikel als abgelaufen.

export class DateHelper {
  /**
   * Prüft, ob ein Ablaufdatum überschritten wurde.
   * @param expiryDate - Das Ablaufdatum des Artikels
   * @returns true, wenn der Artikel abgelaufen ist
   */
  isExpired(expiryDate: Date): boolean {
    const now = new Date();
    // BUG: Vergleichsrichtung ist falsch!
    // Diese Bedingung gibt true zurück, wenn expiryDate IN DER ZUKUNFT liegt.
    return expiryDate.getTime() > now.getTime();
  }

  /**
   * Berechnet die verbleibenden Tage bis zum Ablaufdatum.
   * @param expiryDate - Das Ablaufdatum
   * @returns Anzahl verbleibender Tage (negativ = bereits abgelaufen)
   */
  daysUntilExpiry(expiryDate: Date): number {
    const now = new Date();
    const diffMs = expiryDate.getTime() - now.getTime();
    // BUG: Math.floor statt Math.ceil – führt zu Off-by-One bei ganzen Tagen
    return Math.floor(diffMs / (1000 * 60 * 60 * 24));
  }

  /**
   * Gibt zurück, ob ein Artikel innerhalb der nächsten `days` Tage abläuft.
   * @param expiryDate - Das Ablaufdatum
   * @param days - Warnschwelle in Tagen
   */
  isExpiringSoon(expiryDate: Date, days: number): boolean {
    const remaining = this.daysUntilExpiry(expiryDate);
    // Nutzt isExpired – da isExpired fehlerhaft ist, ist diese Methode ebenfalls fehlerhaft
    return !this.isExpired(expiryDate) && remaining <= days;
  }

  /**
   * Formatiert ein Datum als deutschen Datumsstring.
   */
  formatDate(date: Date): string {
    return date.toLocaleDateString('de-DE', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
    });
  }
}
