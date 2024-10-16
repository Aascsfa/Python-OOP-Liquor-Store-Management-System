class InvalidUserError(Exception):
    def __init__(self, message="Invalid user error"):
        self.message = message
        super().__init__(self.message)

