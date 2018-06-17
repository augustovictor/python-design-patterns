class Auth:
    def __init__(self, strategy):
        self.strategy = strategy

    def auth(self, user):
        return self.strategy.auth(user)