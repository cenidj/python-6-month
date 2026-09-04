
# Tuples and sets
person = ("John", 30, "Developer")
print(person[0])
print(person[1])

coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])

try:
    coordinates[0] = 50  # Throw an error because tuples are inmutable
except:
    print("⚠️ Trying to update a tuple value, and tuples are inmutable")

# tuples can be used when we have conceptually related values
# examples
rgb = (255, 0, 128)
location = (35.7, -83.9)


def get_user():
    return ("John", 30)


name, age = get_user()  # tuple unpacking
print(name)
print(age)

# tuples vs list
# You can use it when need to modify the collection
users = ["John", "Mary", "Bob"]
users.append("Sarah")
users.remove("Bob")

user = ("John", 30, "Developer")  # You can use it when it shouldn't change

# List -> Collection that could change
# Tuple -> Collection that shouldn't change


# Sets

# A set is collection of unique elements
numbers = {1, 2, 3, 4, 5}

# if try to add a current number
numbers.add(5)
print(numbers)  # 5 won't appears twice

# Sets most important use is to delete duplicates
# for example:
numbers = [1, 2, 2, 2, 3, 3, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)

# Sets are excellent to check membership
# for example:
allowed_users = {"John", "Mary", "Bob"}

if "Mary" in allowed_users:
    print("Access granted")

# this operation is very common -> if username in allowed_users:

# Operations with sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # a.union(b) -> all elements

print(a & b)  # a.intersection(b) -> elements in common

print(a - b)  # Difference -> elements in a but not b

print(a ^ b)  # symmetric difference -> elements in one or the other but not in common


# important: sets doesn't have indices
numbers = {10, 20, 30}
try:
    print(numbers[0])
    numbers[1]
except:
    print("Can't index a set, probably you need a list or tuple")


# Mini exercise day 9 🧪:

# 1. What prints?
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(numbers)  # {1, 2, 3, 4}

# 2. What structure should I use?
"""
    A. Guardar las coordenadas (x, y) de un punto -> a tuple => coordenates = (x, y)
    B. Guardar productos de un carrito de compras -> a list => products = [a, b, c]
    C. Guardar IDs únicos de usuarios -> a set => ids = {1, 2, 3, 4, 5}
    D. Comprobar si un email ya está registrado -> a set => if email in registered_emails:
"""


# 3. Escribe una función que reciba una lista de números y devuelva solamente los números únicos.
def unique_numbers(numbers: list[int]) -> set[int]: return set(numbers)


print(unique_numbers([1, 2, 2, 3, 3, 4, 4, 5, 5]))
