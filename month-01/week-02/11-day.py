# List comprehesion

# Supongamos que queremos crear una lista
# con los numeros cuadrados del 1 al 5

# Traditional way
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# With list comprehesion
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)

# Structure -> [expresion for elemento in iterable]

# Adding conditions
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# example
users = [
    {"name": "Ana", "active": True},
    {"name": "Carlos", "active": False},
    {"name": "Luis", "active": True},
]

active_users = [user for user in users if user["active"]]

print(active_users)

# Structure now -> [expresion for elemento in iterable if condition]

# Dictionary comprehesions
# Works the same way but produce a dictionary
numbers = [1, 2, 3, 4, 5]

"""
We want:
{
    1: 1, 
    2: 4,
    3: 9,
    4: 12,
    5: 25
}
"""

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)

# Structure -> {clave: valor for elemento in iterable }

# Dictionary comprehesin with condition
numbers = range(1, 11)

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)

# For example:
# An API returns
users = [
    {"id": 1, "name": "Ana"},
    {"id": 2, "name": "Carlos"},
    {"id": 3, "name": "Luis"},
]

"""
We want
{
    1: "Ana",
    2: "Carlos",
    3: "Luis"
}
"""

users_by_id = {
    user["id"]: user["name"]
    for user in users
}

print(users_by_id)

# Exercises
# 1. given numbers make a list -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]
print(squares)


# 2. Get only the numbers greater than 5
greater_than = [number for number in numbers if number > 5]
print(greater_than)


# 3. given the following
users = [
    {"id": 1, "name": "Ana"},
    {"id": 2, "name": "Carlos"},
    {"id": 3, "name": "Luis"},
]

"""
{
    1: "Ana",
    2: "Carlos",
    3: "Luis"
}
"""

transformed_users = {
    user["id"]: user["name"]
    for user in users
}

print(transformed_users)


# Exercise 4.  Given...
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
]


# Crea un diccionario usando dictionary comprehension que tenga solamente productos cuyo precio sea mayor a 50:
productos_mayor_50 = {
    product["name"]: product["price"]
    for product in products
    if product["price"] > 50
}

print(productos_mayor_50)
