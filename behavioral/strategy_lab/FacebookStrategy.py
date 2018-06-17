from AuthStrategy import AuthStrategy

class FacebookStrategy(AuthStrategy):
    def auth(self, user):
        return f'tokenFb{user.name}'