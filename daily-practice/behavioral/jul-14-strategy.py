import abc

# Context
class Fee:
    def __init__(self, strategy):
        self._strategy = strategy

    def fee(self):
        return self._strategy.fee()

    def __repr__(self):
        return f'The current fee is {self._strategy.fee()}'

# Strategy interface
class FeeStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fee(self):
        pass

# Concrete strategy
class LowFeeStrategy(FeeStrategy):
    def fee(self):
        return 0.1
    
# Concrete strategy
class MediumFeeStrategy(FeeStrategy):
    def fee(self):
        return 0.25

# Concrete strategy
class HighFeeStrategy(FeeStrategy):
    def fee(self):
        return 0.5

# Program
lowFeeStrategy = LowFeeStrategy()
mediumFeeStrategy = MediumFeeStrategy()
highFeeStrategy = HighFeeStrategy()

fee = Fee(lowFeeStrategy)
print(fee)

fee = Fee(mediumFeeStrategy)
print(fee)

fee = Fee(highFeeStrategy)
print(fee)