import { InventoryItem } from './InventoryManager';

export class ReportGenerator {
  // BUG: Diese Methode stürzt ab, wenn ein InventoryItem kein 'value'-Feld hat.
  // Das Interface InventoryItem hat kein 'value'-Feld – es wird hier aber erwartet.
  // Außerdem fehlt eine Null-Prüfung.
  private formatLine(item: InventoryItem & { value?: number }): string {
    const valueStr = item.value.toFixed(2); // CRASH: item.value kann undefined sein
    return `| ${item.productId.padEnd(12)} | ${item.productName.padEnd(30)} | ${String(item.currentStock).padStart(8)} | ${item.unit.padEnd(6)} | ${valueStr.padStart(12)} |`;
  }

  generateStockReport(items: InventoryItem[]): string {
    const header = '='.repeat(80);
    const title = 'LAGERBERICHT - ' + new Date().toLocaleDateString('de-DE');
    const columnHeader = '| Produkt-ID   | Produktname                    | Bestand | Einh.  | Wert (EUR)   |';
    const separator = '-'.repeat(80);

    const lines = items.map((item) => this.formatLine(item));

    // BUG: Hier wird versucht, auf items[0].value zuzugreifen ohne zu prüfen,
    // dass items nicht leer ist und value definiert ist.
    const totalValue = items.reduce((sum, item: any) => sum + (item.value || 0), 0);
    const totalLine = `Gesamtwert: ${totalValue.toFixed(2)} EUR`;

    return [header, title, header, columnHeader, separator, ...lines, separator, totalLine, header].join('\n');
  }

  generateMovementSummary(movements: any[]): string {
    if (!movements || movements.length === 0) {
      return 'Keine Lagerbewegungen im ausgewählten Zeitraum.';
    }

    // BUG: Diese Methode iteriert über movements, aber ruft .productName direkt auf –
    // movements haben productId, nicht productName. Kein Absturz, aber falsche Ausgabe.
    return movements
      .map((m) => `${m.timestamp} | ${m.type} | ${m.productName ?? m.productId} | ${m.quantity}`)
      .join('\n');
  }
}
