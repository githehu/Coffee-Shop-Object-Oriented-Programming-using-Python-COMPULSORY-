import pytest

from coffee import Coffee
from customer import Customer
from order import Order


@pytest.fixture(autouse=True)
def clean_state():
    # Ensure class-level state is isolated between tests
    Coffee._all.clear()
    Customer._all.clear()
    Order._all.clear()
    yield
    Coffee._all.clear()
    Customer._all.clear()
    Order._all.clear()


def test_customer_init_valid_name_and_all_tracking():
    cust = Customer("Alice")
    assert cust.name == "Alice"
    assert Customer.all() == [cust]


def test_customer_invalid_name_raises():
    with pytest.raises(Exception):
        Customer("")  # too short (<1)
    with pytest.raises(Exception):
        Customer("x" * 16)  # too long (>15)
    with pytest.raises(Exception):
        Customer(123)  # not a string


def test_customer_name_is_mutable_within_constraints():
    cust = Customer("Bob")
    cust.name = "Charlie"
    assert cust.name == "Charlie"
    with pytest.raises(Exception):
        cust.name = ""  # invalid after change


def test_customer_orders_and_coffees_relationships_unique():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    o1 = Order(alice, espresso, 3.0)
    o2 = Order(alice, espresso, 4.0)
    o3 = Order(alice, latte, 5.0)

    assert alice.orders() == [o1, o2, o3]
    assert set(alice.coffees()) == {espresso, latte}


def test_create_order_convenience_method():
    alice = Customer("Alice")
    cappuccino = Coffee("Cappuccino")

    o = alice.create_order(cappuccino, 2.5)

    assert isinstance(o, Order)
    assert o.customer is alice
    assert o.coffee is cappuccino
    assert o.price == 2.5
