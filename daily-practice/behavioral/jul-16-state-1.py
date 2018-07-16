import abc

# Context
class User:
    def __init__(self, state):
        self._state = state

    def request_content(self):
        self._state.request_content()

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        print('State changed')
        self._state = state

# State
class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request_content(self):
        pass

# ConcreteState
class LoggedInState(State):
    def request_content(self):
        print('You are logged in so here goes the private content')
        return 'You are logged in so here goes the private content'

class NotLoggedInState(State):
    def request_content(self):
        print('Not authorized')
        return 'Not authorized'

# Program
loggedState = LoggedInState()
notLoggedState = NotLoggedInState()

user = User(loggedState)
user.request_content()
