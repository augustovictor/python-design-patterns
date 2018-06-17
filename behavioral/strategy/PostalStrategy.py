from ShippingStrategy import ShippingStrategy

class PostalStrategy(ShippingStrategy):
    def calculate(self, order):
        return 5.00