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


def test_coffee_init_valid_name_and_all_tracking():
    c = Coffee("Latte")
    assert c.name == "Latte"
    assert Coffee.all() == [c]


def test_coffee_invalid_name_raises():
    with pytest.raises(Exception):
        Coffee("La")  # too short (< 3)
    with pytest.raises(Exception):
        Coffee(123)  # not a string


def test_coffee_name_is_immutable():
    c = Coffee("Mocha")
    with pytest.raises(Exception):
        c.name = "Espresso"  # cannot be changed after initialization


def test_orders_and_customers_relationships_unique():
    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")

    o1 = Order(alice, espresso, 3.0)
    o2 = Order(alice, espresso, 4.0)
    o3 = Order(bob, espresso, 5.0)
    _ = Order(bob, cappuccino, 2.0)  # different coffee, should not appear in espresso orders

    assert espresso.orders() == [o1, o2, o3]
    assert set(espresso.customers()) == {alice, bob}  # order not guaranteed due to set usage in implementation


def test_num_orders_and_average_price():
    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")

    Order(alice, espresso, 3.0)
    Order(alice, espresso, 4.0)
    Order(bob, espresso, 5.0)

    assert espresso.num_orders() == 3
    assert espresso.average_price() == pytest.approx(4.0)


def test_average_price_zero_when_no_orders():
    americano = Coffee("Americano")
    assert americano.average_price() == 0


def test_most_aficionado_returns_highest_spender_and_none_when_no_orders():
    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")
    macchiato = Coffee("Macchiato")  # no orders

    Order(alice, espresso, 3.0)
    Order(alice, espresso, 4.0)  # Alice total: 7.0
    Order(bob, espresso, 5.0)    # Bob total: 5.0

    assert Coffee.most_aficionado(espresso) is alice
    assert Coffee.most_aficionado(macchiato) is None


def test_all_returns_all_instances():
    c1 = Coffee("Latte")
    c2 = Coffee("Mocha")
    assert Coffee.all() == [c1, c2]


def test_orders_and_customers_empty_when_no_orders():
    coffee = Coffee("Flat White")
    assert coffee.orders() == []
    assert coffee.customers() == []


def test_coffee_init_name_exactly_three_chars():
    c = Coffee("ABC")
    assert c.name == "ABC"


def test_average_price_with_boundary_prices():
    from customer import Customer
    from order import Order

    alice = Customer("Al")
    bob = Customer("Bo")
    cortado = Coffee("Cortado")

    Order(alice, cortado, 1.0)
    Order(bob, cortado, 10.0)

    assert cortado.average_price() == pytest.approx(5.5)


def test_most_aficionado_ignores_orders_for_other_coffees():
    from customer import Customer
    from order import Order

    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    Order(alice, espresso, 3.0)
    Order(alice, latte, 10.0)  # High spend on a different coffee should be ignored
    Order(bob, espresso, 4.0)

    assert Coffee.most_aficionado(espresso) is bob


def test_customers_unique_when_same_customer_multiple_orders():
    from customer import Customer
    from order import Order

    alice = Customer("Alice")
    espresso = Coffee("Espresso")

    Order(alice, espresso, 2.0)
    Order(alice, espresso, 3.0)

    # Only one unique customer should be listed
    assert espresso.customers() == [alice]
