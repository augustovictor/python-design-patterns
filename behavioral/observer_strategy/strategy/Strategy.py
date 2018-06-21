import abc

class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_total(self):
        pass