import abc

class ShippingStrategy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost """