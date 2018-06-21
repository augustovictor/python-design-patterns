import abc

class AbsObserver(metaclass=abc.ABCMeta):
    def __init__(self, name=None):
        self.name = name
        self.subject = None

    @abc.abstractmethod
    def update(self):
        pass