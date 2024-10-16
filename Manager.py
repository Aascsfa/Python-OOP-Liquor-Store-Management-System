from User import User

class Manager(User):
    def __init__(self, first_name, last_name, username, password, managed_stores):
        super().__init__(first_name, last_name, username, password)
        self.managed_stores = managed_stores
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.managed_stores = managed_stores

    def view_managed_stores(self):
        for store in self.managed_stores:
            print(f"- {store.get_name()}")

    def view_managed_stores_detail(self):
        for store in self.managed_stores:
            print(f"- {store.name} ({store.get_region()}), {store.address}")

    def get_stores(self):
        return self.managed_stores;

    def __str__(self):
        return f"Manager: {self.username}"
    
    
