from CreditCardPaymentStrategy import CreditCardPaymentStrategy
from DebitCardPaymentStrategy import DebitCardPaymentStrategy
from SlipPayment import SlipStrategy
from Fee import Fee

# Creditcard
strategy = CreditCardPaymentStrategy()
total = Fee(strategy).calculate_total(100)
assert total == 105

# Debitcard
strategy = DebitCardPaymentStrategy()
total = Fee(strategy).calculate_total(100)
assert total == 101

# Slip
strategy = SlipStrategy()
total = Fee(strategy).calculate_total(100)
assert total == 100

print('All good')