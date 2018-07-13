import abc

class Invoker:
    """
    Ask the command to carry out the request
    """

    def __init__(self):
        self._commands = []
    
    def store_command(self, command):
        self._commands.append(command)
    
    def execute_commands(self):
        for c in self._commands:
            c.execute()

class Command(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation
    """
    def __init__(self, receiver):
        self._receiver = receiver
    
    @abc.abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement the 'execute' by invoking the corresponding operation on Receiver
    """

    def execute(self):
        self._receiver.action()

class Receiver:
    """
    Know how to perform the operation
    """

    def action(self):
        print('Executed')


def main():
    receiver = Receiver()
    concCommand = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concCommand)
    invoker.execute_commands()

if __name__ == '__main__':
    main()