import abc

class AbcSubscriber(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        """Implement this"""