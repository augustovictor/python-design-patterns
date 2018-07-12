from ConcreteCommand import ConcreteCommand
from Invoker import Invoker
from Receiver import Receiver

receiver = Receiver()
realCommand = ConcreteCommand(receiver)

invoker = Invoker()
invoker.store_command(realCommand)

invoker.execute_commands()