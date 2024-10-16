from Customer import Customer
from Manager import Manager
from InvalidUserError import InvalidUserError

class Users:
    def __init__(self, initialUsers=[]):  # Initialize with list of initialUsers - contains both customer and manager
        self.users = initialUsers

    def get_users(self):  # Return list of users
        return self.users

    # Function to append a list of customers and managers
    def seed_data(self, stores):
        # Customers only require four fields defined in the user class
        self.users.append(Customer("Alice", "Johnson", "1", "1", 28))  # Includes age for legal drinking verification
        self.users.append(Customer("Bob", "Smith", "bobsmith", "vodka", 32))
        self.users.append(Customer("Cathy", "Brown", "cathyB", "champagne", 27))
        self.users.append(Customer("Daniel", "Lee", "danlee", "ginlover", 40))

        # Managers require the region, obtained from the stores parameter
        self.users.append(Manager("Michael", "Scott", "2", "2", [
            stores.get_by_region("Hurstville"),  # The Whiskey Den
            stores.get_by_region("Rockdale"),    # Vodka Vault
            stores.get_by_region("Carlton"),     # Wine Haven
            stores.get_by_region("Heathcote"),   # Barrel & Cork
            stores.get_by_region("Engadine")     # Tequila Sunrise
        ]))
        self.users.append(Manager("Jessica", "Day", "jessday", "daylight", [
            stores.get_by_region("Loftus"),      # Gin Palace
            stores.get_by_region("Sutherland"),  # Craft Brew Emporium
            stores.get_by_region("Waterfall"),   # Rum Shack
            stores.get_by_region("Mortdale")     # The Cognac Lounge
        ]))
        self.users.append(Manager("Nick", "Miller", "nickm", "grumpy", [
            stores.get_by_region("Penshurst"),   # Champagne Cellars
            stores.get_by_region("Redfern"),     # Ultimate Parts Source (modify if needed)
            stores.get_by_region("Central")      # Rapid Repair Parts (modify if needed)
        ]))
        self.users.append(Manager("Leslie", "Knope", "lesliek", "waffles", [
            stores.get_by_region("Wolli Creek"),  # DriveLine Parts Warehouse (modify if needed)
            stores.get_by_region("Sydenham")      # Essential Auto Components (modify if needed)
        ]))
        
        # Ensure the manager data is set correctly
        if len(self.users[4].__dict__) < 6:
            print("Exception occurred when attempting to seed data.\nHave you implemented the Manager constructor?")
        return self

    # Function to validate user credentials
    def validate_user(self, username, password):
        for u in self.users:
            if username == u.get_username() and password == u.get_password():
                return u
        raise InvalidUserError("Invalid username or password.")
