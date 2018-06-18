import abc

class TravelStrategy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def time_to_travel(self):
        """Implement time_to_travel"""