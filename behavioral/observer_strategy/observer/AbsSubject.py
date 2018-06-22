import abc
from .AbsObserver import AbsObserver

class AbsSubject(metaclass=abc.ABCMeta):
    def __init__(self):
        raise NotImplementedError('This class cannot be instantiated')
    observers = set()

    # @abc.abstractmethod
    def add_observer(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer should be a subclass of AbsObserver')
        observer.subject = self
        self.observers.add(observer)
    
    # @abc.abstractmethod
    def remove_observer(self, observer):
        observer.subject = None
        self.observers.remove(observer)

    # @abc.abstractmethod
    def notify(self, value):
        for observer in self.observers:
            observer.update(value)