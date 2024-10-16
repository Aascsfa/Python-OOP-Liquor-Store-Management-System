from LiquorProducts import LiquorProducts
from Liquor_Product import LiquorProduct

class LiquorStore:
    def __init__(self, name, region, address, products):
        self.name = name
        self.region = region
        self.address = address
        self.products = LiquorProducts(products)
        self.profit = 0

    def get_name(self):
        return self.name
    
    def get_region(self):
        return self.region

    def get_products(self):
        return self.products.get_products_list()

    def __str__(self):
        return f"{self.name} Liquor Store ({self.region})"
