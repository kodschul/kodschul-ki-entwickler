/**
 * Gibt die Differenz in ganzen Tagen zwischen zwei Daten zurück.
 * Positive Werte = date2 liegt nach date1.
 */
export function daysBetween(date1: Date, date2: Date): number {
  const msPerDay = 1000 * 60 * 60 * 24;
  const diff = date2.getTime() - date1.getTime();
  return Math.floor(diff / msPerDay);
}

/**
 * Gibt zurück, ob ein Datum in der Vergangenheit liegt (vor dem aktuellen Zeitpunkt).
 */
export function isPast(date: Date): boolean {
  return date.getTime() < Date.now();
}

/**
 * Gibt zurück, ob ein Datum in der Zukunft liegt.
 */
export function isFuture(date: Date): boolean {
  return date.getTime() > Date.now();
}

/**
 * Addiert eine Anzahl von Tagen zu einem Datum und gibt das neue Datum zurück.
 * Das ursprüngliche Datum wird nicht verändert.
 */
export function addDays(date: Date, days: number): Date {
  const result = new Date(date);
  result.setDate(result.getDate() + days);
  return result;
}

/**
 * Formatiert ein Datum als deutschen Datumsstring (TT.MM.JJJJ).
 */
export function formatDateDE(date: Date): string {
  return date.toLocaleDateString('de-DE', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
}

/**
 * Gibt zurück, ob zwei Datumsangaben am selben Kalendertag liegen,
 * unabhängig von der Uhrzeit.
 */
export function isSameDay(date1: Date, date2: Date): boolean {
  return (
    date1.getFullYear() === date2.getFullYear() &&
    date1.getMonth() === date2.getMonth() &&
    date1.getDate() === date2.getDate()
  );
}

/**
 * Gibt den Beginn des Tages (00:00:00.000) für ein Datum zurück.
 */
export function startOfDay(date: Date): Date {
  const result = new Date(date);
  result.setHours(0, 0, 0, 0);
  return result;
}

/**
 * Gibt das Ende des Tages (23:59:59.999) für ein Datum zurück.
 */
export function endOfDay(date: Date): Date {
  const result = new Date(date);
  result.setHours(23, 59, 59, 999);
  return result;
}

/**
 * Prüft, ob ein Jahr ein Schaltjahr ist.
 */
export function isLeapYear(year: number): boolean {
  return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}
