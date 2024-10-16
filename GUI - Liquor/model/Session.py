from model.LiquorStores import LiquorStores

class Session:
    def __init__(self):
        self.stores = LiquorStores()

    def use(self):
        self.help_menu()
        choice = input("Command (L/X): ").upper()
        while choice != 'X':
            if choice == 'L':
                self.login()
            else:
                self.help_menu()
            choice = input("Command (L/X): ").upper()

        print("\nSession Terminated!")

    def login(self):
        store = self.stores.authenticate_store(input("Email: "), input("Password: "))
        if store:
            store.use()
        else:
            print("Incorrect store details!")

    def help_menu(self):
        print("Liquor Store Membership System:")
        print("L- Login")
        print("X- Exit")
