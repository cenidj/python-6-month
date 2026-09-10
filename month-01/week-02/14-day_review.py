

# Exercise 1. List + comprehension
numbers = [-5, 10, 3, -2, 8, 0, -1, 15]
# Create a list with only positive numbers
positive_numbers = [number for number in numbers if number > 0]


# Exercise 2. Dictionary
# Given...
users = {
    "Ana": 25,
    "John": 17,
    "Carlos": 30,
    "Maria": 16
}
# Create a dictionary only with adults users
adult_users = {
    name: age
    for name, age in users.items()
    if age >= 18
}

# Exercise 3. Strings
# Given...
languages = "Python,Java,JavaScript,Go"
# Make this -> Python | Java | JavaScript | Go
languages_list = languages.split(",")
result = " | ".join(languages_list)

# Exercise 4. Loop
# Without using sum(), calculate the total using a loop
numbers = [10, 20, 30, 40, 50]
total_sum = 0
for number in numbers:
    total_sum += number


# Exercise 5. Mini problem
expenses = {
    "rent": 1300,
    "food": 400,
    "transportation": 200,
    "utilities": 150,
    "entertainment": 100
}

# Total spent
total_spent = 0
# Highest spent
highest_spent = 0
# Spent over $150
spents_over_150 = {}

for description, amount in expenses.items():
    total_spent += amount
    highest_spent = amount if amount > highest_spent else highest_spent
    if amount > 150:
        spents_over_150[description] = amount
