import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk  # To handle the logo image
from model.LiquorMemberships import LiquorMemberships

class LSLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LS - MMS")
        self.root.geometry("400x400")
        self.memberships = LiquorMemberships()  # Instance of LiquorMemberships to authenticate users

        # Header - Logo and Title
        # self.logo_img = Image.open("liquor_store_logo.png")  # Placeholder for the liquor store logo
        # self.logo_img = self.logo_img.resize((100, 100), Image.ANTIALIAS)
        # self.logo = ImageTk.PhotoImage(self.logo_img)
        # self.logo_label = tk.Label(root, image=self.logo)
        # self.logo_label.pack(pady=10)
        
        self.header_label = tk.Label(root, text="Liquor Store Membership Management System", font=("Arial", 16))
        self.header_label.pack(pady=20)

        # Login Button
        self.login_button = tk.Button(root, text="Login", command=self.open_login_window, width=15, height=2)
        self.login_button.pack(pady=20)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
        self.exit_button.pack()

    def open_login_window(self):
        # Create a new window for the login
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Login - LS - MMS")
        self.login_window.geometry("300x250")

        # Email Label and Entry
        self.email_label = tk.Label(self.login_window, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.login_window, width=30)
        self.email_entry.pack(pady=5)
      
        # Password Label and Entry
        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.login_window, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_submit_button = tk.Button(self.login_window, text="Login", command=self.authenticate_user)
        self.login_submit_button.pack(pady=10)

    def authenticate_user(self):
        # Get email and password from entries
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        # Authenticate using LiquorMemberships
        member = self.memberships.authenticate_member(email, password)

        if member:
            messagebox.showinfo("Login Successful", f"Welcome, {member.getName()}!")
            self.login_window.destroy()  # Close login window
            self.open_customer_manager_menu(member)
        else:
            messagebox.showerror("Login Failed", "Incorrect email or password. Please try again.")

    def open_customer_manager_menu(self, member):
        # Check if the member object is a manager or customer and open the appropriate menu
        self.menu_window = tk.Toplevel(self.root)
        self.menu_window.title(f"{member.getName()} - Menu")
        self.menu_window.geometry("300x300")

        if isinstance(member, LiquorMembership):
            # Assuming LiquorMembership can also mean manager for simplicity
            self.manager_menu(member)
        else:
            # Otherwise open customer menu
            self.customer_menu(member)

    def customer_menu(self, member):
        # Customer-specific menu
        tk.Label(self.menu_window, text="Customer Menu", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.menu_window, text="View My Details", width=20, command=lambda: self.view_user_details(member)).pack(pady=5)
        tk.Button(self.menu_window, text="Shop at Store", width=20, command=lambda: self.shop_at_store(member)).pack(pady=5)
        tk.Button(self.menu_window, text="Logout", width=20, command=self.menu_window.destroy).pack(pady=5)

    def manager_menu(self, member):
        # Manager-specific menu
        tk.Label(self.menu_window, text="Manager Menu", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.menu_window, text="View Store Details", width=20, command=lambda: self.view_store_details(member)).pack(pady=5)
        tk.Button(self.menu_window, text="Manage Store Products", width=20, command=lambda: self.manage_store_products(member)).pack(pady=5)
        tk.Button(self.menu_window, text="Logout", width=20, command=self.menu_window.destroy).pack(pady=5)

    def view_user_details(self, member):
        messagebox.showinfo("User Details", f"Name: {member.getName()}
Email: {member.getEmail()}")

    def shop_at_store(self, member):
        messagebox.showinfo("Shop", "Shopping functionality to be implemented.")

    def view_store_details(self, member):
        messagebox.showinfo("Store Details", f"Store: {member.getName()}
Email: {member.getEmail()}")

    def manage_store_products(self, member):
        messagebox.showinfo("Manage Products", "Manage products functionality to be implemented.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LSLoginApp(root)
    root.mainloop()