class Order:
    _all = []  # Keep track of all orders

    def __init__(self, customer, coffee, price: float):
        self._customer = customer
        self._coffee = coffee
        self.price = price  # triggers setter
        Order._all.append(self)

    # ----------------------
    # Properties
    # ----------------------
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if not hasattr(self, "_price"):  # prevent modification after creation
            if isinstance(value, (int, float)) and 1.0 <= float(value) <= 10.0:
                self._price = float(value)
            else:
                raise Exception("Price must be a float between 1.0 and 10.0")
        else:
            raise Exception("Price cannot be changed after the order is created")

    # ----------------------
    # Utility
    # ----------------------
    @classmethod
    def all(cls):
        return cls._all
