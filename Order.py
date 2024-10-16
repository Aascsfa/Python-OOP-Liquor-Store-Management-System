class Order:
    def __init__(self, liquor_product, quantity):
        self.liquor_product = liquor_product
        self.quantity = quantity

    def __str__(self):
        return f"Order of {self.quantity} x {self.liquor_product}"
