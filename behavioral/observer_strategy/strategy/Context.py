class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_total(self):
        return self.strategy.calculate_total()