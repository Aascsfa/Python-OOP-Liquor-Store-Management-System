from .LiquorMemberships import LiquorMemberships

class LiquorMembership:
    def __init__(self, name, email, phone, address, ID, total_spent):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.ID = ID
        self.total_spent = float(total_spent)
        self.membership_type = self.set_membership_type(self.total_spent)
        self.stores = LiquorMemberships() 

    def set_membership_type(self, total_spent):
        if total_spent >= 5000:
            return "Gold"
        elif total_spent >= 1000:
            return "Silver"
        else:
            return "Bronze"

    def matches(self, name):
        return self.name == name

    def update_membership(self, name, email, phone, address, ID, total_spent):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.ID = ID
        self.total_spent = float(total_spent)
        self.membership_type = self.set_membership_type(self.total_spent)

    def copy(self):
        return LiquorMembership(self.name, self.email, self.phone, self.address, self.ID, self.total_spent)
