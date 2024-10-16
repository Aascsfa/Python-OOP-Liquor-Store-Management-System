from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.purchases = []

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def add_purchase(self, cart):
        self.purchases.append(cart)

    @abstractmethod
    def __str__(self):
        pass
