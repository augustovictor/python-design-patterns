import abc

class MyAbstractClass(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def do_something(self, value):
        pass
    
    @abc.abstractmethod
    def some_property(self):
        pass