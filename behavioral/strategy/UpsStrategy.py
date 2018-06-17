from ShippingStrategy import ShippingStrategy

class UpsStrategy(ShippingStrategy):
    def calculate(self, order):
        return 4.00