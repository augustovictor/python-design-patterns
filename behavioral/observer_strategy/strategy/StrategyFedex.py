from Strategy import Strategy

class StrategyFedex(Strategy):
    def __init__(self, value):
        self.value = value

    def calculate_total(self):
        return self.value + self.value * 0.02