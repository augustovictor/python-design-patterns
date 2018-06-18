from FeeStrategy import FeeStrategy

class SlipStrategy(FeeStrategy):

    @property
    def fee(self):
        return 0 