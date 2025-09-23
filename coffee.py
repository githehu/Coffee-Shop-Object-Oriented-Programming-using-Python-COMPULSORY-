from order import Order

class Coffee:
    _all = []  # Track all coffee instances

    def __init__(self, name: str):
        self.name = name  # triggers setter
        Coffee._all.append(self)

    # ----------------------
    # Properties
    # ----------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not hasattr(self, "_name"):  # Prevent changing after initialization
            if isinstance(value, str) and len(value) >= 3:
                self._name = value
            else:
                raise Exception("Coffee name must be a string with at least 3 characters")
        else:
            raise Exception("Coffee name cannot be changed once set")

    # ----------------------
    # Relationships
    # ----------------------
    def orders(self):
        """Return all orders for this coffee"""
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        """Return unique customers who ordered this coffee"""
        return list({order.customer for order in self.orders()})

    # ----------------------
    # Aggregates
    # ----------------------
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

    # ----------------------
    # Bonus
    # ----------------------
    @classmethod
    def most_aficionado(cls, coffee):
        """Find the customer who spent the most money on a given coffee"""
        spending = {}
        for order in coffee.orders():
            spending[order.customer] = spending.get(order.customer, 0) + order.price

        if not spending:
            return None
        return max(spending, key=spending.get)

    @classmethod
    def all(cls):
        return cls._all
