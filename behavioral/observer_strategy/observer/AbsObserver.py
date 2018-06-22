import abc

class AbsObserver(metaclass=abc.ABCMeta):
    def __init__(self):
        raise NotImplementedError('This class should not be instantiated')
    @abc.abstractmethod
    def update(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def post_something(self, value):
        raise NotImplementedError