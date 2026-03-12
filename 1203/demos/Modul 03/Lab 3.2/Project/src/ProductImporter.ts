// BUG: Diese Datei enthält mehrere Validierungsprobleme, die zu stillem
// Datenverlust führen. 7 von 50 CSV-Zeilen werden verworfen ohne Fehlermeldung.

export interface RawProductRow {
  id: string;
  name: string;
  stock: string;
  minStock: string;
  maxStock: string;
  unit: string;
}

export interface ParsedProduct {
  productId: string;
  productName: string;
  currentStock: number;
  minimumStock: number;
  maximumStock: number;
  unit: string;
}

export class ProductImporter {
  private importedCount = 0;
  private skippedCount = 0;

  parseCSV(csvContent: string): ParsedProduct[] {
    const lines = csvContent.split('\n');
    const results: ParsedProduct[] = [];

    // Erste Zeile ist Header – überspringen
    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim();
      if (!line) continue;

      const parts = line.split(',');
      const row: RawProductRow = {
        id: parts[0],
        name: parts[1],
        stock: parts[2],
        minStock: parts[3],
        maxStock: parts[4],
        unit: parts[5],
      };

      const parsed = this.parseRow(row, i + 1);
      if (parsed) {
        results.push(parsed);
        this.importedCount++;
      } else {
        // BUG: Verworfen, aber kein Log-Eintrag! Student soll Logging hinzufügen.
        this.skippedCount++;
      }
    }

    console.log(`Import abgeschlossen: ${this.importedCount} Produkte importiert`);
    return results;
  }

  private parseRow(row: RawProductRow, lineNumber: number): ParsedProduct | null {
    // BUG 1: .trim() fehlt beim ID-Check – IDs mit Leerzeichen werden verworfen
    if (!row.id || row.id === '') {
      return null;
    }

    if (!row.name || row.name.trim() === '') {
      return null;
    }

    const stock = parseInt(row.stock);
    const minStock = parseInt(row.minStock);
    const maxStock = parseInt(row.maxStock);

    // BUG 2: isNaN-Check ist falsch herum – er verwirft gültige Zahlen (0 ist falsy)
    // parseInt('0') = 0, aber !0 === true → wird als ungültig gewertet
    if (!stock || !minStock || !maxStock) {
      return null;
    }

    // BUG 3: Validierung auf maxStock > minStock fehlt – keine Prüfung auf Konsistenz
    // Wird zwar importiert, kann aber später einen Logikfehler verursachen

    const unit = row.unit ? row.unit.trim() : '';
    // BUG 4: Wenn unit fehlt oder leer ist, wird die Zeile NICHT verworfen –
    // aber unit ist ein Pflichtfeld laut Spec. Hier fehlt die Validierung.

    return {
      productId: row.id.trim(),
      productName: row.name.trim(),
      currentStock: stock,
      minimumStock: minStock,
      maximumStock: maxStock,
      unit: unit || 'STK', // Stille Korrektur – sollte ein Fehler sein
    };
  }

  getImportStats(): { imported: number; skipped: number } {
    return { imported: this.importedCount, skipped: this.skippedCount };
  }
}
