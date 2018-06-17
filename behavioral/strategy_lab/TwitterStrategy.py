from AuthStrategy import AuthStrategy

class TwitterStrategy(AuthStrategy):
    def auth(self, user):
        return f'tokenTwitter{user.name}'