from LiquorStores import LiquorStores
from Users import Users
from InvalidUserError import InvalidUserError
from Customer import Customer
from Manager import Manager
from Cart import Cart
from Liquor_Product import LiquorProduct


class Organisation:
    def __init__(self, stores, users):
        self.stores = stores
        self.users = users

    def login(self):
        print("Welcome to the Liquor Store Management System.")
        
        while True:
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            try:
                user = self.users.validate_user(username, password)
                print(f"Login successful.")
                
                # Check if the user is a Customer or a Manager and display the appropriate menu
                if isinstance(user, Customer):
                    self.customer_menu(user)  # Direct the customer to the customer menu
                elif isinstance(user, Manager):
                    self.manager_menu(user)  # Direct the manager to the manager menu
                return  # Exit the login process once a user has logged in and accessed their menu
            except InvalidUserError as e:
                print("{e.message}. Please try again.")
                
            retry = input("Press y to try again or any letter to log out: ").strip().lower()
            if retry != 'y':
                print("Goodbye!")
                return None

    def customer_menu(self, customer): # customer = user
        cart =  None
        liquor_store_selected = None

        while True:
            print(f"\nWelcome to the customer menu, {customer.first_name}.")
            print("1. View my details")
            print("2. Shop at a store")
            print("3. View my order history")
            print("4. Logout")

            choice = input("Please enter a choice: ").strip()

            if choice == "1":
                self.view_user_details(customer)
            elif choice == "2":
                # Select liquor store and get cart
                liquor_store_selected, cart = self.get_store_cart(customer)
    
                self.view_shop(customer, liquor_store_selected, cart)
            elif choice == "3":
                self.view_purchase_history(customer)
            elif choice == "4":
                print("Thanks for using the Liquor Store Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def view_user_details(self, user):
        print(f"\nUser Details\nFirst Name: {user.get_first_name()}\nLast Name: {user.get_last_name()}")


    def view_purchase_history():
        pass

    def get_store_cart(self, customer):
        while True:  # Loop until a valid supplier is chosen

            """Allows customer to select a store and returns the selected store and a new cart."""
            print("\nAvailable Liquor Stores:")
            for count, store in enumerate(self.stores.stores): #get the store, then list of store
                print(f"{count+1}. {store}")

            choice = input("Select the store number to shop at: ").strip()

            try:
                # if the value is not int -> Value Error
                choice_number = int(choice)
                if 1 <= choice_number <= len(self.stores.stores):
                    selected_store = self.stores.stores[choice_number - 1]
                    print(f"You selected {selected_store.name}.")

                    # Create a new cart associated with the selected store and customer
                    cart = Cart(selected_store, customer)
                    return selected_store, cart
                else:
                    print("-------------------------------------")
                    print("Invalid selection. Returning to menu.")
                    print("-------------------------------------")
                    return None, None
            except ValueError:
                print("----------------------------------------------------")
                print(f"\nInvalid input. Please enter a valid number from 1 to {len(self.stores.stores)} \n Enter 4 to log out")
                print("----------------------------------------------------")

                return None, None
    def view_shop(self, customer, liquor_store_selected, cart):
        
        """Displays a menu to view shop details, view products, or place an order."""
        while True:
            print(f"\n--- Welcome to {liquor_store_selected.name} ---")
            print("1. View Shop Details")
            print("2. View Products")
            print("3. Place Order")
            print("4. Go Back to Customer Menu")
            choice = input("Please enter a choice: ").strip()

            if choice == "1":
                self.view_shop_details(liquor_store_selected)
            elif choice == "2":
                self.view_products(liquor_store_selected, cart)
            elif choice == "3":
                self.place_order(cart)
            elif choice == "4":
                print(f"Thanks for shopping at {liquor_store_selected.get_name()}") 
                print("Returning to the customer menu...")
                return  # Go back to customer menu
            else:
                print("----------------------------------------------------")
                print("Invalid choice. Please try again or press X to exit.")
                print("----------------------------------------------------")

    def view_shop_details(self, liquor_store_selected):
        """Displays the details of the selected liquor store."""
        print(f"\n--- Shop Details for {liquor_store_selected.name} ---")
        print(f"Location: {liquor_store_selected.address}")
        print(f"Region: {liquor_store_selected.region}")


    def __init__(self, stores, users):
        self.stores = stores
        self.users = users

    def login(self):
        print("\nWelcome to the Liquor Store Management System.")
        
        while True:
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            try:
                user = self.users.validate_user(username, password)
                print(f"Login successful. Welcome, {user.get_first_name()}!")
                
                if isinstance(user, Customer):
                    self.customer_menu(user)
                elif isinstance(user, Manager):
                    self.manager_menu(user)
                return
            except InvalidUserError:
                print("Invalid username or password. Please try again.")
                
            retry = input("Do you want to try again? (y/n): ").strip().lower()
            if retry != 'y':
                print("Goodbye!")
                return None

    def customer_menu(self, customer):
        cart = None
        liquor_store_selected = None

        while True:
            print(f"\nWelcome to the customer menu, {customer.first_name}.")
            print("1. View my details")
            print("2. Shop at a store")
            print("3. View my order history")
            print("4. View my cart")
            print("5. Logout")
            choice = input("Please enter a choice: ").strip()

            if choice == "1":
                self.view_user_details(customer)
            elif choice == "2":
                liquor_store_selected, cart = self.get_store_cart(customer)
                if liquor_store_selected and cart:
                    self.view_shop(customer, liquor_store_selected, cart)
            elif choice == "3":
                self.view_purchase_history(customer)
            elif choice == "4":
                if cart:
                    self.view_cart(cart)
                else:
                    print("Your cart is empty.")
            elif choice == "5":
                print("\nThanks for using the Liquor Store Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_store_cart(self, customer):
        print("\nAvailable Liquor Stores:")
        for i, store in enumerate(self.stores.stores):
            print(f"{i+1}. {store}")

        choice = input("Select the store number to shop at: ").strip()

        try:
            choice_number = int(choice)
            if 1 <= choice_number <= len(self.stores.stores):
                selected_store = self.stores.stores[choice_number - 1]
                print(f"You selected {selected_store.name}.")
                cart = Cart(selected_store, customer)
                return selected_store, cart
            else:
                print("Invalid selection. Returning to menu.")
                return None, None
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None, None

    def view_shop(self, customer, liquor_store_selected, cart):
        """Displays a menu to view shop details, view products, or place an order."""
        while True:
            print(f"\n--- Welcome to {liquor_store_selected.name} ---")
            print("1. View Shop Details")
            print("2. View Products")
            print("3. Place Order")
            print("4. Go Back to Customer Menu")
            choice = input("Please enter a choice: ").strip()

            if choice == "1":
                self.view_shop_details(liquor_store_selected)
            elif choice == "2":
                self.view_products(liquor_store_selected)
            elif choice == "3":
                self.place_order(customer, cart, liquor_store_selected)
            elif choice == "4":
                print("Returning to the customer menu...")
                return  # Go back to customer menu
            else:
                print("Invalid choice. Please try again.")

    def view_shop_details(self, liquor_store_selected):
        """Displays the details of the selected liquor store."""
        print(f"\n--- Shop Details for {liquor_store_selected.name} ---")
        print(f"Location: {liquor_store_selected.address}")
        print(f"Region: {liquor_store_selected.region}")

    def view_products(self, liquor_store_selected):
        """Displays the available products in the selected liquor store without adding to cart."""
        print(f"\n--- Products Available at {liquor_store_selected.name} ---")
        products = liquor_store_selected.get_products()

        # Display products with their name, price, and available stock
        for i, product in enumerate(products):
            print(f"{i+1}: {product.name} - Price: ${product.price:.2f} (Stock: {product.stock})")
    def place_order(self, customer, cart, liquor_store_selected):
        """Handles the cart management and checkout process with options for adding, removing, viewing, and canceling."""
        while True:
            print(f"\n--- Welcome {customer.get_first_name()} to the Order Menu ---")
            print("1. Add Product to Cart")
            print("2. Remove Product from Cart")
            print("3. View Cart")
            print("4. Cancel Order and Go Back")
            print("5. Check Out")
            print("6. Clear Cart")

            choice = input("Please enter a choice: ").strip()
            
            if choice == "1":
                self.add_product_to_cart(cart, liquor_store_selected)
            elif choice == "2":
                self.remove_product_from_cart(cart, liquor_store_selected)
            elif choice == "3":
                self.view_cart(cart)
            elif choice == "4":
                print("Order canceled. Returning to the shop menu...")
                return  # Exit to the shop menu
            elif choice == "5":
                print("\nProceeding to checkout...")  # Placeholder for checkout functionality
                self.check_out(cart, customer)  # Calling a new check_out function (placeholder)
            elif choice == "6":
                self.clear_cart(cart)
            else:
                print("Invalid choice. Please try again.")

    def add_product_to_cart(self, cart,liquor_store_selected):
        """Allows the user to add products to the cart from the selected liquor store."""
        # Get the products from the selected liquor store
        products = liquor_store_selected.get_products()  

        while True:
            print(f"\n--- Products Available at {liquor_store_selected.name} ---")
            # List the products available in the selected store
            for i, product in enumerate(products):
                print(f"{i+1}: {product.name} at ${product.price:.2f} ({product.stock} in stock)")
            try:
                # User selects a product by its number
                choice = input("Enter the index of the product to add to your cart: ").strip()
                product_choice = int(choice) - 1  # Adjust for zero-based index

                if 0 <= product_choice < len(products):
                    selected_product = products[product_choice]
                    
                    # Ask the user for the quantity to add to the cart
                    quantity = int(input(f"Enter the quantity of {selected_product.name} to add to the cart: ").strip())
                    
                    if selected_product.hasStock(quantity):
                        # Add product to the cart and reduce the stock in the store
                        cart.add_to_cart(selected_product, quantity)
                        selected_product.stock -= quantity
                        print(f"Added {quantity} x {selected_product.name} to the cart.")
                        break  # Successfully added, exit loop
                    else:
                        print("\n------------------------------------------------------")
                        print(f"Not enough stock. Only {selected_product.stock} left.")
                        print("------------------------------------------------------")
                else:
                    print("\n-------------------------------------------------------------------------")
                    print(f"Invalid selection. Please choose a number between 1 and {len(products)}.")
                    print("-------------------------------------------------------------------------")
            except ValueError:
                print("\n-----------------------------------------")
                print("Invalid input. Please enter a valid number.")
                print("-------------------------------------------")

    def remove_product_from_cart(self, cart, liquor_store_selected):
        """Allows the user to remove products from the cart."""
        if not cart.items:
            print("Your cart is empty. There is nothing to remove.")
            return

        print("\n--- Products in Your Cart ---")
        # Display the products in the cart with their index
        for i, (product, quantity) in enumerate(cart.items):  # Unpack tuple (product, quantity)
            print(f"{i+1}: {product.name} - Quantity: {quantity}")

        while True:
            try:
                choice = input("Enter the index of the product to remove from your cart: ").strip()
                product_index = int(choice) - 1  # Adjust for zero-based index
                cart.remove_from_cart(product_index)  # Call the method in the Cart class
                break  # Successfully removed, exit loop
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def view_cart(self, cart):
        """Displays the contents of the customer's cart."""
        cart.view_cart()

    def check_out(self, cart, customer):
        """Placeholder for the checkout process."""
        cart.checkout()

    def clear_cart(self, cart):
        """Clears all items from the cart."""
        cart.clear_all_items()  # Calling the method in the Cart class
        print("All items have been removed from your cart.")

    def manager_menu(self, manager):
        """Displays the manager menu and allows the manager to perform various tasks."""
        while True:
            print(f"\n--- Welcome to the Manager Menu, {manager.get_first_name()} ---")
            print("1. View My Details")
            print("2. List All Your Stores")
            print("3. Manage a Particular Store")
            print("4. Logout")

            choice = input("Please enter a choice: ").strip()

            if choice == "1":
                self.view_manager_details(manager)
            elif choice == "2":
                self.list_stores_managed(manager)
            elif choice == "3":
                self.manage_store(manager)
            elif choice == "4":
                print("Logging out...")
                return  # Exit the manager menu and return to the main menu
            
            else:
                print("\n-------------------------------------------------------")
                print("Invalid choice. Please try again or press 4 to log out.")
                print("-------------------------------------------------------")


    def view_manager_details(self, manager):
        """Displays the manager's details."""
        print(f"\nManager name: {manager.get_first_name()} {manager.get_last_name()}, manager for:")
        print(manager.view_managed_stores())

    def list_stores_managed(self, manager):
        """Lists all stores managed by the manager."""
        print("\nAll stores you manage:")
        print(manager.view_managed_stores_detail())
        
    def manage_store(self, manager):
        """Allows the manager to manage a particular store."""
        stores = manager.get_stores()
        manager_cart = None

        # List the stores and ask the manager to select one
        print("\nWhich store would you like to manage?")
        for i, store in enumerate(stores):
            print(f"{i+1}. {store.name} ({store.get_region()})")
        
        choice = input("Enter the number of the store you want to manage: ").strip()

        try:
            store_choice = int(choice) - 1
            if 0 <= store_choice < len(stores):
                chosen_store = stores[store_choice]
                self.manage_store_options(chosen_store,manager_cart,manager)  # Call a method to manage the store
            else:
                print("\n-------------------------------------------------------")
                print("Invalid selection. Please choose a valid store number.")
                print("-------------------------------------------------------")
        except ValueError:
            print("\n-------------------------------------------------------")
            print("Invalid input. Please enter a valid number.")
            print("-------------------------------------------------------")

    def manage_store_options(self, store, manager_cart, manager):
        """Displays options for managing a selected store with 9 tasks."""
        manager_cart = Cart(store, manager) #user here is manager

        while True:
            print(f"\nManaging {store.name} in {store.get_region()}:")
            print("1. View Store Details")
            print("2. View Store Products")
            print("3. View Available Products in Store")
            print("4. Add Product to Store")
            print("5. Remove Product from Store")
            print("6. Restock Product")
            print("7. Delist Product (Set Stock to Unavailable)")
            print("8. View Store Profit")
            print("9. Order from Store")
            print("10. Checkout")
            print("X. Return to Manager Menu")

            choice = input("Please enter a choice: ").strip().upper()

            if choice == "1":
                self.view_store_details(store)
            elif choice == "2":
                self.view_store_products(store)
            elif choice == "3":
                self.view_available_products_in_store(store)
            elif choice == "4":
                self.add_product_to_store(store)
            elif choice == "5":
                self.remove_product_from_store(store)
            elif choice == "6":
                self.restock_product(store)
            elif choice == "7":
                self.delist_product(store)
            elif choice == "8":
                self.view_store_profit(store)
            elif choice == "9":
                self.order_from_store(store,manager_cart)
            elif choice == "10":
                self.checkout_manager(manager_cart)
            elif choice == "X":
                print(f"\nReturning to the main menu from {store.name}...")
                break  # Exit and return to the manager's main menu
            else:
                print("\n-----------------------------------------------------")
                print("Invalid choice. Please try again.")
                print("-------------------------------------------------------")

    def view_store_details(self, store):
        """Displays details about the store."""
        print(f"\nStore Name: {store.name}")
        print(f"Region: {store.get_region()}")
        print(f"Address: {store.address}")

    def view_store_products(self, store):
        """Displays all products available in the store."""
        products = store.get_products()
        print(f"\n--- Products in {store.name} ---")
        for product in products:
            print(f"- {product}")

    def view_available_products_in_store(self, store):
        """Displays only the products that are marked as available."""
        products = store.get_products()

        print(f"\n--- Available Products in {store.name} ---")    
        for product in products:
            if product.is_available():
                print(product)

    def add_product_to_store(self, store):
        """Allows the manager to add a new product to the store."""
        name = input("Enter the name of the new product: ").strip()
        price = float(input("Enter the price of the product: ").strip())
        stock = int(input("Enter the stock quantity: ").strip())
        alcohol_content = int(input("Enter the alcohol content of the product (in %): ").strip())

        new_product = LiquorProduct(name, price, stock, alcohol_content)
        store.get_products().append(new_product)
        print(f"{name} has been added to {store.name} with {stock} units in stock.")

    def remove_product_from_store(self, store):
        """Allows the manager to remove a product from the store."""
        products = store.get_products()
        while True: 
            # List products in the store
            print(f"\n--- Products in {store.name} ---")
            for i, product in enumerate(products):
                print(f"{i+1}. {product.name} - {product.stock} in stock")

            choice = input("Enter the index of the product to remove: ").strip()
            try:
                product_choice = int(choice) - 1
                if 0 <= product_choice < len(products):
                    removed_product = products.pop(product_choice)
                    print(f"{removed_product.name} has been removed from {store.name}.")
                elif product_choice == -1:
                    print("")
                    return
                else:
                    print("\n----------------------------------------------------------------------")
                    print("Invalid selection. Please choose a valid product index or 0 to return.")
                    print("----------------------------------------------------------------------")

            except ValueError:
                print("\n----------------------------------------------------------")
                print("Invalid input. Please enter a valid number or 0 to return.")
                print("----------------------------------------------------------")

    def restock_product(self, store):
        """Restocks a product in the store."""
        products = store.get_products()

        while True:
            print(f"\n--- Products in {store.name} ---")
            for i, product in enumerate(products):
                print(f"{i+1}. {product.name} - {product.stock} in stock")

            choice = input("Enter the index of the product to restock (or 0 to return): ").strip()
            try:
                product_choice = int(choice) - 1
                if 0 <= product_choice < len(products):
                    restock_amount = int(input(f"Enter the quantity to add for {products[product_choice].name}: ").strip())
                    products[product_choice].restock(restock_amount)  # Use the restock method from LiquorProduct
                elif product_choice == -1: 
                    print("Returning to the previous menu...")
                    return  # Exit the loop and return to the previous menu
                else:
                    print("\n----------------------------------------------------------------------")
                    print("Invalid selection. Please choose a valid product index or 0 to return.")
                    print("----------------------------------------------------------------------")
            except ValueError:
                print("\n----------------------------------------------------------")
                print("Invalid input. Please enter a valid number or 0 to return.")
                print("----------------------------------------------------------")

    def delist_product(self, store):
        """Allows the manager to delist a product, setting it to unavailable."""
        products = store.get_products()

        while True:
            print(f"\n--- Products in {store.name} ---")
            for i, product in enumerate(products):
                print(f"{i+1}. {product.name} - {product.stock} in stock")

            choice = input("Enter the index of the product to delist (or 0 to return): ").strip()
            try:
                product_choice = int(choice) - 1
                if 0 <= product_choice < len(products):
                    products[product_choice].delist()  # Mark product as unavailable using the delist method
                elif product_choice == -1:
                    print("Returning to the previous menu...")
                    return  # Exit the loop and return to the previous menu
                else:
                    print("\n----------------------------------------------------------------------")
                    print("Invalid selection. Please choose a valid product index or 0 to return.")
                    print("----------------------------------------------------------------------")
            except ValueError:
                print("\n----------------------------------------------------------")
                print("Invalid input. Please enter a valid number or 0 to return.")
                print("----------------------------------------------------------")

    def view_store_profit(self, store):
        """Displays the total profit of the store."""
        
        while True:
            print(f"\n--- Total Profit for {store.name} ---")
            print(f"Total profit: ${store.profit:.2f}")
            
            choice = input("Press 0 to return to the previous menu: ").strip()
            
            if choice == "0":
                print("Returning to the previous menu...")
                return  # Exit to the previous menu
            else:
                print("\n--------------------------------------------------------")
                print("Invalid input. Please enter 0 to return.")
                print("----------------------------------------------------------")

    def order_from_store(self, store, manager_cart):
        """Allows the manager to place an internal order from the store for free, reducing stock without affecting profit."""
        products = store.get_products()

        while True:
            print(f"\n--- Products in {store.name} ---")
            for i, product in enumerate(products):
                print(f"{i+1}. {product.name} - ${product.price:.2f}, Stock: {product.stock}")

            choice = input("Enter the index of the product you want to order (or 0 to return): ").strip()
            try:
                product_choice = int(choice) - 1
                if 0 <= product_choice < len(products):
                    order_quantity = int(input(f"Enter the quantity to order for {products[product_choice].name}: ").strip())
                    
                    if products[product_choice].hasStock(order_quantity):  # Check if enough stock is available
                        # Deduct the stock but don't increase the profit (since it's free for the manager)
                        products[product_choice].stock -= order_quantity
                        manager_cart.add_to_cart(products[product_choice], order_quantity)

                        print(f"\n{order_quantity} units of {products[product_choice].name} added to cart. Stock is now {products[product_choice].stock}.")
                        break
                    else:
                        print("\n----------------------------------------------------------------------")
                        print(f"Not enough stock. Only {products[product_choice].stock} available.")
                        print("----------------------------------------------------------------------")
                elif product_choice == -1:
                    print("Returning to the previous menu...")
                    return  # Exit to the previous menu
                else:
                    print("\n----------------------------------------------------------------------")
                    print("Invalid selection. Please choose a valid product index or 0 to return.")
                    print("----------------------------------------------------------------------")
            except ValueError:
                print("\n----------------------------------------------------------")
                print("Invalid input. Please enter a valid number or 0 to return.")
                print("----------------------------------------------------------")



if __name__ == "__main__":
    stores = LiquorStores().seed_data()
    users = Users().seed_data(stores)
    
    org = Organisation(stores, users)
    org.login()  # No need to check instances outside of login function now
