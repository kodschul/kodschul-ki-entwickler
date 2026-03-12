export type ProductCategory = 'ELECTRONICS' | 'CLOTHING' | 'FOOD' | 'BOOKS' | 'OTHER';

export class Product {
  public id: string;
  public name: string;
  public description: string;
  public basePrice: number;
  public category: ProductCategory;
  public stockQuantity: number;
  public sku: string;
  public isActive: boolean;

  constructor(
    id: string,
    name: string,
    description: string,
    basePrice: number,
    category: ProductCategory,
    stockQuantity: number,
    sku: string
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.basePrice = basePrice;
    this.category = category;
    this.stockQuantity = stockQuantity;
    this.sku = sku;
    this.isActive = true;
  }

  isInStock(): boolean {
    return this.stockQuantity > 0;
  }

  reduceStock(quantity: number): void {
    if (quantity > this.stockQuantity) {
      throw new Error(`Nicht genügend Lagerbestand für Produkt ${this.name}`);
    }
    this.stockQuantity -= quantity;
  }

  increaseStock(quantity: number): void {
    this.stockQuantity += quantity;
  }
}
