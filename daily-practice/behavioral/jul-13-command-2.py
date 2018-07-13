import abc

class Command(metaclass=abc.ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass

class LightOnCommand(Command):
    def execute(self):
        self._receiver.switchOn()

class LightOffCommand(Command):
    def execute(self):
        self._receiver.switchOff()

# Receiver
class Light:
    def __init__(self):
        self._on = False

    def switchOn(self):
        print('Light switched ON')
        self._on = True

    def switchOff(self):
        print('Light switched OFF')
        self._on = False

# Invoker
class RemoteControl:
    def __init__(self):
        self._commands = []
    
    def add_command(self, command):
        self._commands.append(command)
    
    def execute_commands(self):
        for c in self._commands:
            c.execute()


light = Light()
lighOnCmd = LightOnCommand(light)
lightOffCmd = LightOffCommand(light)

control = RemoteControl()
control.add_command(lighOnCmd)
control.add_command(lightOffCmd)

control.execute_commands()