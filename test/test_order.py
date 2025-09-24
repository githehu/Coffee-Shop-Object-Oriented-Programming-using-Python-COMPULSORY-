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


def test_order_init_valid_price_and_all_tracking():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")

    o = Order(alice, espresso, 3.5)

    assert o.customer is alice
    assert o.coffee is espresso
    assert o.price == 3.5
    assert Order.all() == [o]


def test_order_invalid_price_raises():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")

    with pytest.raises(Exception):
        Order(alice, espresso, 0.99)  # below min
    with pytest.raises(Exception):
        Order(alice, espresso, 10.01)  # above max
    with pytest.raises(Exception):
        Order(alice, espresso, "not-a-number")  # invalid type


def test_order_price_is_immutable_after_creation():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")
    o = Order(alice, espresso, 2.0)

    with pytest.raises(Exception):
        o.price = 3.0


def test_order_does_not_validate_customer_or_coffee_type_but_keeps_reference():
    # The current implementation does not enforce type checks for customer/coffee
    alice = Customer("Alice")
    espresso = Coffee("Espresso")
    o = Order(alice, espresso, 5.0)

    assert o.customer is alice
    assert o.coffee is espresso


def test_multiple_orders_preserve_insertion_order():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")

    o1 = Order(alice, espresso, 1.0)
    o2 = Order(alice, espresso, 2.0)

    assert Order.all() == [o1, o2]
