import abc

class Command(metaclass=abc.ABCMeta):
    def __init__(self, light):
        self._light = light

    @abc.abstractmethod
    def execute(self):
        pass

class LightOnCmd(Command):
    def execute(self):
        self._light.switch_on()

class LightOffCmd(Command):
    def execute(self):
        self._light.switch_off()

# Receiver
class Light:
    def __init__(self):
        self._on = False

    def switch_on(self):
        print('Turn light on...')
        self._on = True

    def switch_off(self):
        print('Turn light off!')
        self._on = False
    
    def __repr__(self):
        state = 'turned on' if self._on else 'turned off'
        return f'The light is {state}'

# Invoker
class RemoteControl:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        if not isinstance(command, Command):
            raise TypeError('Provided command should be inherited from Command')
        self._commands.append(command)

    def execute_commands(self):
        for c in self._commands:
            c.execute()


light = Light()
lightOnCmd = LightOnCmd(light)
lightOffCmd = LightOffCmd(light)

control = RemoteControl()
control.add_command(lightOnCmd)
control.add_command(lightOffCmd)
control.add_command(lightOnCmd)


control.execute_commands()
print(light)