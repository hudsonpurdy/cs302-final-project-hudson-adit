class User:
    def __init__(self, username):
        self.username = username
        self.balance = 0
        self.private_key = self.compute_private_key()

    def compute_private_key(self):
        return "key"