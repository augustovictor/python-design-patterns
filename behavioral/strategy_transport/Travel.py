class Travel:
    def __init__(self, strategy):
        self.strategy = strategy

    @property
    def time_to_travel(self):
        return self.strategy.time_to_travel()