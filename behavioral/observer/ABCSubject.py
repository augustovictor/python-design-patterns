import abc
from ABCObserver import ABCObserver

class ABCSubject(object):

    observers = set()

    def add_subscriber(self, observer):
        if not isinstance(observer, ABCObserver):
            raise TypeError('Observer is not a subclass of ABCObserver')
        self.observers.add(observer)

    def remove_subscriber(self, observer):
        self.observers.remove(observer)

    @abc.abstractmethod
    def notify(self, value=None):
        for observer in self.observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)