from FeeStrategy import FeeStrategy

class DebitCardPaymentStrategy(FeeStrategy):
    @property
    def fee(self):
        return 0.01