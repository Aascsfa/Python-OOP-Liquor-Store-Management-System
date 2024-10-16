from User import User

class Customer(User):
    def __init__(self, first_name, last_name, username, password, age):
        super().__init__(first_name, last_name, username, password)
        self.age = age

    def is_legal_age(self):
        return self.age >= 21  # Assuming 21 is the legal drinking age

    def __str__(self):
        return f"Customer: {self.username}, Age: {self.age}"
