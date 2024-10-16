from .LiquorStore import LiquorStore
from .LiquorMemberships import LiquorMemberships

class LiquorStores:
    def __init__(self):
        self.stores = []
        # Adding sample stores
        self.stores.append(LiquorStore("Bourbon Street", "bourbon@store.com", "password123"))
        self.stores.append(LiquorStore("Whiskey Town", "whiskey@store.com", "whiskeyrocks"))

    def authenticate_store(self, email, password):
        for store in self.stores:
            if store.matches(email, password):
                return store
        return None
