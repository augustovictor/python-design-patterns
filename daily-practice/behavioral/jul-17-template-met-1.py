import abc

# Template class
class Worker(metaclass=abc.ABCMeta):
    def work(self):
        self.go_to_work()
        self.do_work()
        self.give_report()
        self.return_from_work()

    def go_to_work(self):
        print('I am goint to work...')

    @abc.abstractmethod
    def do_work(self):
        pass

    @abc.abstractmethod
    def give_report(self):
        pass
    
    def return_from_work(self):
        print('Returnign from work...')

# Concrete classes
class Cooker(Worker):
    def do_work(self):
        print('I am cooking! =D')

    def give_report(self):
        print('Today I have baked a cake!')

class Made(Worker):
    def do_work(self):
        print('I am cleaning the house')

    def give_report(self):
        print('Today I cleaned everything!')

# Program
w1 = Cooker()
w2 = Made()

w1.work()
w2.work()