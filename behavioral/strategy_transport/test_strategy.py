from Travel import Travel
from TravelBusStrategy import TravelBusStrategy
from TravelCarStrategy import TravelCarStrategy

# Bus travel
strategy = TravelBusStrategy()
time = Travel(strategy).time_to_travel
assert time == 50

# Car travel
strategy = TravelCarStrategy()
time = Travel(strategy).time_to_travel
assert time == 30

print('ALl good')