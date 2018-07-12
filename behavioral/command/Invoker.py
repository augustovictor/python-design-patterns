import abc

class Invoker(metaclass=abc.ABCMeta):
    """
    Ask the command to store the request
    """
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for c in self._commands:
            c.execute()