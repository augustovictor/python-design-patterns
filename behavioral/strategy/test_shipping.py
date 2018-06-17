from Order import Order
from Shipper import Shipper
from ShippingCostBeforeStrategy import ShippingCostBeforeStrategy
from FedExStrategy import FedExStrategy
from UpsStrategy import UpsStrategy
from PostalStrategy import PostalStrategy
from ShippingCost import ShippingCost
from NewOrder import NewOrder

# Federal express shipping
order = Order(Shipper.fedex)
cost_calculator = ShippingCostBeforeStrategy()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.00

# Ups shipping
order = Order(Shipper.ups)
cost = ShippingCostBeforeStrategy().shipping_cost(order)
assert cost == 4.00

# Postal service shipping
order = Order(Shipper.postal)
cost = ShippingCostBeforeStrategy().shipping_cost(order)
assert cost == 5.00

"""With Strategies"""

# Federal express shipping
order = NewOrder()
strategy = FedExStrategy()
cost = ShippingCost(strategy).shipping_cost(order)
assert cost == 3.00

# Ups shipping
order = NewOrder()
strategy = UpsStrategy()
cost = ShippingCost(strategy).shipping_cost(order)
assert cost == 4.00

# Postal service shipping
order = NewOrder()
strategy = PostalStrategy()
cost = ShippingCost(strategy).shipping_cost(order)
assert cost == 5.00

print('Tests passed')