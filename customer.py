from order import Order

class Customer:
    _all = []  # Keep track of all customer instances

    def __init__(self, name: str):
        self.name = name  # will trigger the property setter
        Customer._all.append(self)

    # ----------------------
    # Properties
    # ----------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Customer name must be a string between 1 and 15 characters")

    # ----------------------
    # Relationships
    # ----------------------
    def orders(self):
        """Return all orders belonging to this customer"""
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        """Return a unique list of coffees this customer has purchased"""
        return list({order.coffee for order in self.orders()})

    # ----------------------
    # Behaviors
    # ----------------------
    def create_order(self, coffee, price: float):
        """Create a new order for this customer"""
        return Order(self, coffee, price)

    # ----------------------
    # Utility
    # ----------------------
    @classmethod
    def all(cls):
        return cls._all
