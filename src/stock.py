class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Stock:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def decrease_product(self, product_name, amount):
        for item in self.items:
            if item.name == product_name:
                item.amount -= amount
                return

        raise ValueError(f"Produkten '{product_name}' finns inte i lagret")