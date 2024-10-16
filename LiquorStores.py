from Liquor_Product import LiquorProduct
from LiquorStore import LiquorStore
from LiquorProducts import LiquorProducts  

class LiquorStores:
    def __init__(self, stores=[]):
        self.stores = stores

    def __str__(self):
        return f"LiquorStores: {len(self.stores)} stores available."

    def get_by_region(self, region):
        for store in self.stores:
            if store.get_region() == region:
                return store
        return None

    def seed_data(self):
        # Define seed data for liquor products
        seeded_liquors = [
            LiquorProduct("Whiskey", 50.00, 100, 40),  # Name, Price, Stock, Alcohol content %
            LiquorProduct("Vodka", 30.00, 80, 40),
            LiquorProduct("Wine", 20.00, 50, 12),
            LiquorProduct("Beer", 10.00, 200, 5),
            LiquorProduct("Rum", 35.00, 60, 35),
            LiquorProduct("Tequila", 45.00, 70, 40),
            LiquorProduct("Gin", 40.00, 90, 37),
            LiquorProduct("Brandy", 55.00, 45, 38),
            LiquorProduct("Cognac", 100.00, 20, 40),
            LiquorProduct("Champagne", 75.00, 30, 12),
            LiquorProduct("Cider", 8.00, 150, 6),
            LiquorProduct("Port", 25.00, 40, 20)
        ]

        # Create liquor stores with specific products and new names
        self.stores.append(LiquorStore("The Whiskey Den", "Hurstville", "12 Oak Street", [seeded_liquors[0], seeded_liquors[2], seeded_liquors[4], seeded_liquors[6]]))
        self.stores.append(LiquorStore("Vodka Vault", "Rockdale", "46 Iceberg Lane", [seeded_liquors[1], seeded_liquors[3], seeded_liquors[5], seeded_liquors[7]]))
        self.stores.append(LiquorStore("Wine Haven", "Carlton", "22 Vineyard Blvd", [seeded_liquors[0], seeded_liquors[8], seeded_liquors[9], seeded_liquors[6]]))
        self.stores.append(LiquorStore("Barrel & Cork", "Heathcote", "89 Barrel Road", [seeded_liquors[3], seeded_liquors[4], seeded_liquors[10], seeded_liquors[2]]))
        self.stores.append(LiquorStore("Tequila Sunrise", "Engadine", "9 Fiesta Avenue", [seeded_liquors[5], seeded_liquors[6], seeded_liquors[11], seeded_liquors[7]]))
        self.stores.append(LiquorStore("Gin Palace", "Loftus", "43 Botanical Crescent", [seeded_liquors[8], seeded_liquors[0], seeded_liquors[9], seeded_liquors[1]]))
        self.stores.append(LiquorStore("Craft Brew Emporium", "Sutherland", "75 Hops Street", [seeded_liquors[2], seeded_liquors[3], seeded_liquors[10], seeded_liquors[11]]))
        self.stores.append(LiquorStore("Rum Shack", "Waterfall", "62 Pirate's Bay", [seeded_liquors[4], seeded_liquors[5], seeded_liquors[6], seeded_liquors[7]]))
        self.stores.append(LiquorStore("The Cognac Lounge", "Mortdale", "91 Prestige Avenue", [seeded_liquors[0], seeded_liquors[9], seeded_liquors[2], seeded_liquors[8]]))
        self.stores.append(LiquorStore("Champagne Cellars", "Penshurst", "10 Bubbly Road", [seeded_liquors[1], seeded_liquors[3], seeded_liquors[4], seeded_liquors[10]]))

        return self
