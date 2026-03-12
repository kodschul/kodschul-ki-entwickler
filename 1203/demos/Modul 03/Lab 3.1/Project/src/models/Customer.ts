export class Customer {
  public id: string;
  public firstName: string;
  public lastName: string;
  public email: string;
  public phone?: string;
  public address?: CustomerAddress;
  public createdAt: Date;
  public loyaltyPoints: number;

  constructor(id: string, firstName: string, lastName: string, email: string) {
    this.id = id;
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
    this.createdAt = new Date();
    this.loyaltyPoints = 0;
  }

  get fullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }

  addLoyaltyPoints(points: number): void {
    this.loyaltyPoints += points;
  }

  redeemLoyaltyPoints(points: number): boolean {
    if (points > this.loyaltyPoints) {
      return false;
    }
    this.loyaltyPoints -= points;
    return true;
  }
}

export interface CustomerAddress {
  street: string;
  city: string;
  postalCode: string;
  country: string;
}
