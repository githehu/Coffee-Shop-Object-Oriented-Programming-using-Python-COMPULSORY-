# Coffee-Shop-Object-Oriented-Programming-using-Python-COMPULSORY-
# Coffee-Shop-Object-Oriented-Programming-using-Python-COMPULSORY-
# Coffee Shop OOP Python Project

This project models a coffee shop using Object-Oriented Programming in Python. It includes classes for customers, coffees, and orders, with relationships and business logic.

## Structure

- `coffee.py`: Defines the [`Coffee`](coffee.py) class.
- `customer.py`: Defines the [`Customer`](customer.py) class.
- `order.py`: Defines the [`Order`](order.py) class.
- `debug.py`: Example usage and debugging.
- `test/`: Contains unit tests for all classes.

## Features

- Track all coffees, customers, and orders.
- Enforce constraints on names and prices.
- Relationships: customers can order coffees, coffees track their orders and customers.
- Aggregates: number of orders, average price, most aficionado customer.

## Running Tests

Tests use `pytest` and are located in the `test/` directory:
```sh
pytest test/