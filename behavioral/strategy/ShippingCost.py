class ShippingCost(object):
    def __init__(self, strategy):
        self.strategy = strategy

    def shipping_cost(self, order):
        return self.strategy.calculate(order)