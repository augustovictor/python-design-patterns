import abc

class FeeStrategy(metaclass = abc.ABCMeta):
    def calculate_total(self, amount):
        """This must be implemented"""