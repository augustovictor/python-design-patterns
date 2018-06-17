import abc

class AuthStrategy(metaclass = abc.ABCMeta):
    def auth(self, user):
        """Authenticate user"""