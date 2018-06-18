class Fee:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def calculate_total(self, amount):
        return (self.strategy.fee * amount) + amount