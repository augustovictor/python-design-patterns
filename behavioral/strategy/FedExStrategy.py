from ShippingStrategy import ShippingStrategy

class FedExStrategy(ShippingStrategy):
    def calculate(self, order):
        return 3.00