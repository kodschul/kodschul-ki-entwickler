from dataclasses import dataclass, field
from typing import Optional


@dataclass
class product:
    product_id: int
    name: str
    price: float
    stock: int
    category: str

    def is_in_stock(self) -> bool:
        return self.stock > 0

    def apply_discount(self, percent: float) -> float:
        discounted_price = self.price * (1 - percent / 100)
        return round(discounted_price, 2)


@dataclass
class order_item:
    product: product
    quantity: int

    def subtotal(self) -> float:
        return round(self.product.price * self.quantity, 2)


@dataclass
class shopping_cart:
    customer_name: str
    items: list[order_item] = field(default_factory=list)

    def add_item(self, item: order_item) -> None:
        if not item.product.is_in_stock():
            print(f"'{item.product.name}' is out of stock.")
            return
        if item.quantity > item.product.stock:
            print(f"Only {item.product.stock} unit(s) of '{item.product.name}' available.")
            return
        self.items.append(item)
        item.product.stock -= item.quantity

    def remove_item(self, product_id: int) -> None:
        self.items = [i for i in self.items if i.product.product_id != product_id]

    def total_price(self) -> float:
        return round(sum(item.subtotal() for item in self.items), 2)

    def item_count(self) -> int:
        return sum(item.quantity for item in self.items)

    def display_summary(self) -> None:
        print(f"\nCart for: {self.customer_name}")
        print("-" * 40)
        for item in self.items:
            print(f"  {item.product.name} x{item.quantity}  —  ${item.subtotal():.2f}")
        print("-" * 40)
        print(f"  Total items : {self.item_count()}")
        print(f"  Total price : ${self.total_price():.2f}\n")


@dataclass
class order:
    order_id: int
    cart: shopping_cart
    status: str = "pending"

    def place_order(self) -> None:
        if not self.cart.items:
            print("Cannot place an empty order.")
            return
        self.status = "confirmed"
        print(f"Order #{self.order_id} confirmed for {self.cart.customer_name}.")

    def cancel_order(self) -> None:
        if self.status == "shipped":
            print("Cannot cancel a shipped order.")
            return
        self.status = "cancelled"
        for item in self.cart.items:
            item.product.stock += item.quantity
        print(f"Order #{self.order_id} has been cancelled.")


def find_product_by_name(catalog: list[product], name: str) -> Optional[product]:
    name_lower = name.lower()
    return next((p for p in catalog if p.name.lower() == name_lower), None)


def get_products_by_category(catalog: list[product], category: str) -> list[product]:
    return [p for p in catalog if p.category.lower() == category.lower()]


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Build a small product catalog
    catalog = [
        product(1, "Laptop",     999.99, 10, "Electronics"),
        product(2, "Headphones", 149.99, 25, "Electronics"),
        product(3, "Desk Chair", 299.99,  5, "Furniture"),
        product(4, "Notebook",     4.99, 100, "Stationery"),
        product(5, "Pen Set",      9.99,  50, "Stationery"),
    ]

    # Show electronics
    electronics = get_products_by_category(catalog, "electronics")
    print("Electronics available:")
    for p in electronics:
        print(f"  [{p.product_id}] {p.name}  —  ${p.price:.2f}  (stock: {p.stock})")

    # Customer builds a cart
    cart = shopping_cart("Alice")
    cart.add_item(order_item(catalog[0], 1))   # 1x Laptop
    cart.add_item(order_item(catalog[1], 2))   # 2x Headphones
    cart.add_item(order_item(catalog[3], 3))   # 3x Notebook
    cart.display_summary()

    # Place the order
    new_order = order(order_id=1001, cart=cart)
    new_order.place_order()

    # Show discounted price for the laptop
    laptop = find_product_by_name(catalog, "laptop")
    if laptop:
        discounted = laptop.apply_discount(10)
        print(f"\n10% off {laptop.name}: ${discounted:.2f}")

    # Cancel the order
    new_order.cancel_order()
    print(f"Stock restored — Laptop stock: {catalog[0].stock}")
