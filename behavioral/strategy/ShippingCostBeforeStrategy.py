from Shipper import Shipper

class ShippingCostBeforeStrategy(object):
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self.fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self.ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self.postal_cost(order)
        else:
            raise ValueError(f'Invalid shipper {order.shipper}')

    def fedex_cost(self, order):
        return 3.00
    
    def ups_cost(self, order):
        return 4.00

    def postal_cost(self, order):
        return 5.00