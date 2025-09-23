
from customer import Customer
from coffee import Coffee
from order import Order

# Create some objects
c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
c1.create_order(coffee1, 5.0)
c1.create_order(coffee2, 7.0)
c2.create_order(coffee1, 4.5)

# Check relationships
print(c1.orders())       # Orders by Alice
print(c1.coffees())      # Coffees Alice ordered
print(coffee1.orders())  # Orders for Latte
print(coffee1.customers()) # Customers who ordered Latte

# Aggregates
print(coffee1.num_orders())     # Number of orders for Latte
print(coffee1.average_price())  # Avg price for Latte

# Bonus
print(Coffee.most_aficionado(coffee1))  # Who spent the most on Latte
