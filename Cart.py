from Order import Order

class Cart:
    def __init__(self, store, user):
        self.store = store
        self.user = user
        self.items = []  # list of (liquor, quantity) tuples

    def add_to_cart(self, liquor_id, quantity):
        self.items.append((liquor_id, quantity))

    def view_cart(self):
        """Displays the contents of the cart and the total cost."""
        if not self.items:
            print("\nYour cart is empty.")
        else:
            print("\n--- Your Cart ---")
            total_cost = 0
            for i, (product, quantity) in enumerate(self.items):  # Unpack tuple (product, quantity)
                item_cost = product.price * quantity
                total_cost += item_cost
                print(f"{i+1}. {product.name}: {quantity} @ ${product.price:.2f} each = ${item_cost:.2f}")
            print(f"\nTotal Cost: ${total_cost:.2f}")


    def remove_from_cart(self, product_index):
        """Removes a product from the cart by index."""
        if 0 <= product_index < len(self.items):
            removed_item = self.items.pop(product_index)  # Remove the item using pop
            print(f"Removed {removed_item[0].name} from the cart.")  # Access product name via tuple indexing
        else:
            print(f"Invalid selection. Please choose a number between 1 and {len(self.items)}.")

    def clear_all_items(self):
        """Clears all items from the cart."""
        self.items.clear()  # Clear the entire cart list

    def checkout(self):
        """Handles the checkout process, calculates total, and clears the cart."""
        if not self.items:  # Check if the cart is empty
            print("Your cart is empty. Please add items before checking out.")
            return
        
        # Calculate the total cost of the items in the cart
        total = sum(liquor.price * quantity for liquor, quantity in self.items)
        print(f"\nCheckout complete. Total cost: ${total:.2f}")
        print("Secured Checkout... \nPowered by PayPal...")

        # Clear the cart after checkout
        self.items.clear()

    def man_checkout(self):
        """Process the checkout for the manager."""
        if not self.items:
            print("Your cart is empty.")
            return

        print(f"\n--- Checkout for Manager ---")
        print(f"Total items in cart: {len(self.items)}")

        # Just confirm the order and reduce stock without impacting profit
        for liquor, quantity in self.items:
            liquor.stock -= quantity  # Deduct the stock as ordered
            print(f"{quantity} x {liquor.name} checked out. Stock remaining: {liquor.stock}")
        total = sum(liquor.price * quantity for liquor, quantity in self.items)

        # After checkout, clear the cart
        self.items.clear()
        # print("\nCheckout complete. The store's stock has been updated accordingly.")
        print(f"The total price should be ${total}, but you get the order for free as manager")


    def __str__(self):
        return f"Cart for {self.user.get_username()} with {len(self.items)} items."
