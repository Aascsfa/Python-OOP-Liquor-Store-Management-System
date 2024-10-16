#  from .LiquorMembership import LiquorMembership
from model.LiquorMembership import LiquorMembership

class LiquorMemberships:
    def __init__(self):
        self.memberships = []
        # Example members
        self.memberships.append(LiquorMembership("Alice Smith", "alice@liquor.com", "12345678", "123 Main St", "ID001", 1200.0))
        self.memberships.append(LiquorMembership("Bob Johnson", "bob@liquor.com", "87654321", "456 Another St", "ID002", 5500.0))
        self.memberships.append(LiquorMembership("a", "a", "a", "456 a St", "ID003", 554.0))

    def add_membership(self, membership):
        self.memberships.append(membership.copy())

    def update_membership(self, oldname, newname, email, phone, address, ID, total_spent):
        for membership in self.memberships:
            if membership.matches(oldname):
                membership.update_membership(newname, email, phone, address, ID, total_spent)

    def delete_membership(self, name):
        self.memberships = [m for m in self.memberships if not m.matches(name)]

    def get_membership(self, name):
        for membership in self.memberships:
            if membership.matches(name):
                return membership.copy()
        return None

    def get_memberships(self):
        return [m.copy() for m in self.memberships]
