from .LiquorMemberships import LiquorMemberships

from .LiquorMembership import LiquorMembership

class LiquorStore:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.memberships = LiquorMemberships()

    def matches(self, email, password):
        return self.email == email and self.password == password

    def get_memberships(self):
        return self.memberships.get_memberships()

    def add_membership(self, membership):
        self.memberships.add_membership(membership)

    def update_membership(self, old_name, new_name, email, phone, address, ID, total_spent):
        self.memberships.update_membership(old_name, new_name, email, phone, address, ID, total_spent)

    def delete_membership(self, name):
        self.memberships.delete_membership(name)

    def get_name(self):
        return self.name

    def get_membership(self, name):
        return self.memberships.get_membership(name)
