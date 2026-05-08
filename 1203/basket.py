class basket_item:
    def __init__(self, product_name: str, price: float, quantity: int):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return f"basket_item(product_name={self.product_name!r}, price={self.price}, quantity={self.quantity})"


class shopping_basket:
    def __init__(self):
        self.items: list[basket_item] = []

    def add_item(self, product_name: str, price: float, quantity: int = 1) -> None:
        for item in self.items:
            if item.product_name == product_name:
                item.quantity += quantity
                return
        self.items.append(basket_item(product_name, price, quantity))

    def remove_item(self, product_name: str) -> bool:
        for item in self.items:
            if item.product_name == product_name:
                self.items.remove(item)
                return True
        return False

    def update_quantity(self, product_name: str, quantity: int) -> bool:
        for item in self.items:
            if item.product_name == product_name:
                if quantity <= 0:
                    return self.remove_item(product_name)
                item.quantity = quantity
                return True
        return False

    def calculate_total(self) -> float:
        return sum(item.total_price() for item in self.items)

    def item_count(self) -> int:
        return sum(item.quantity for item in self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def clear(self) -> None:
        self.items.clear()

    def display(self) -> None:
        if self.is_empty():
            print("Basket is empty.")
            return
        print("=== Shopping Basket ===")
        for item in self.items:
            print(f"  {item.product_name} x{item.quantity} @ €{item.price:.2f} = €{item.total_price():.2f}")
        print(f"  -----------------------")
        print(f"  Total: €{self.calculate_total():.2f} ({self.item_count()} items)")


if __name__ == "__main__":
    my_basket = shopping_basket()

    my_basket.add_item("Apple", 0.50, 4)
    my_basket.add_item("Bread", 1.99)
    my_basket.add_item("Milk", 1.20, 2)

    my_basket.display()

    print("\nUpdating Milk quantity to 3...")
    my_basket.update_quantity("Milk", 3)
    my_basket.display()

    print("\nRemoving Bread...")
    my_basket.remove_item("Bread")
    my_basket.display()
