from FeeStrategy import FeeStrategy

class CreditCardPaymentStrategy(FeeStrategy):
    @property
    def fee(self):
        return 0.05