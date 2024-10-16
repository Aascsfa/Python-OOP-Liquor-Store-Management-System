class LiquorProduct:
    def __init__(self, name, price, stock, alcohol_content, available  = True):
        self.name = name
        self.price = price
        self.stock = stock
        self.alcohol_content = alcohol_content  # percentage
        self.available = available #initially , all AV = true

    def is_available(self):
        """Check if the product is available (not delisted)."""
        return self.available 

    def hasStock(self, quantity):
        return self.stock >= quantity

    def __str__(self):
        return f"{self.name} (${self.price:.2f}, {self.alcohol_content}% alcohol, {self.stock} in stock)"
    
    def restock(self, quantity):
        """Restocks the product by adding the specified quantity."""
        self.stock += quantity
        print(f"Restocked {self.name}. New stock: {self.stock}")

    def delist(self):
        """Set the product as unavailable."""
        self.available = False
        print(f"\n{self.name} has been delisted.")