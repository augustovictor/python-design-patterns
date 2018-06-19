import abc

class ABCObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        """Go fetch updates"""