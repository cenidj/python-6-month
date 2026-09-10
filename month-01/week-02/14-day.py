# Day 14 - Review + Github

# 1. Quick review - 20-30 mins

name = "Cesario"
age = 27
height = 1.80
is_learning = True

# What type has each variable
# 1 -> str
# 2 -> int
# 3 -> float
# 4 -> Boolean

# How to convert "27" to 27
converstion = int("27")  # -> 27

# What difference exists between int, float, str and bool
# int doesn't have floating numbers, float does; str is characters and bool to affirm or deny something

# conditionals
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Loops
for number in range(5):
    print(number)

# and
# while condition:
#

# collections
# list - tuple - set - dictionary

# comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

# and
users = {
    "Ana": 25,
    "John": 30
}

adults = {
    name: age
    for name, age in users.items()
    if age >= 18
}

# Strings
"""
.split()
.join()
.replace()
f"{variable}
"""
