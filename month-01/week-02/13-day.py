
# 20 Exercises

# Level 1 - remembering

# Exercise 1.
# Given this list
numbers = [-5, 10, 3, -2, 8, 0, -1, 15]
positive_numbers = [number for number in numbers if number > 0]
print(f"Positive numbers are {len(positive_numbers)}")

# Exercise 2.
numbers = [10, 20, 5, 15, 30]
total = 0
for number in numbers:
    total += number
print(total)

# Other solution built-in function
total = sum(numbers)
print(total)

# Exercise 3. Find max number without max()
numbers = [12, 45, 7, 89, 23, 4]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

# Exercise 4. Filter users
users = ["Ana", "Carlos", "Maria", "Jose", "Luis"]

# built a list with the name only with more than 4 characters
users_more_characters = [name for name in users if len(name) >= 4]
print(users_more_characters)

# Level 2 - Strings + Lists

# Exercise 5. Analyse a phrase
text = "Python is great for backend development"
text_list = text.split(" ")

print(f"Words: {len(text_list)}")
print(f"First: {text_list[0]}")
print(f"Last: {text_list[-1]}")
print(" | ".join(text_list))

# Exercise 6. Convert CSV to list
languges = "Python,Java,Javascript,Go,Rust"
languages_list = languges.split(",")
print(languages_list)

# Exercise 7. Search a word
words = ["python", "java", "go", "rust", "javascript"]
search_word = input("Introduce una palabra a buscar: ")

exists = False
for word in words:
    if word == search_word:
        exists = True
    else:
        continue

print(f"Word '{search_word}' exists" if exists else f"Word '{search_word}' doesn't exists!")

# Alternative way - has to use try-except because if index not found throw ValueError
try:
    exists = words.index(search_word) >= 0
except:
    exists = False

print(f"Word '{search_word}' exists" if exists else f"Word '{search_word}' doesn't exists!")

# Exercise 8. Count characters
text = "backend developer"
text_modified = text.replace(" ", "")
print(f"There's {len(text_modified)} characters.")

# Level 3. Dicitionaries
user = {
    "name": "Carlos",
    "age": 27,
    "role": "backend developer",
    "active": True
}

# print every property using .items()
for key, value in user.items():
    print(f"{key}: {value}")

# Exercise 10. Obtain data with .get()
user = {
    "name": "Ana",
    "email": "ana@email.com"
}

print("Name:", user.get("name"))
print("Email:", user.get("email"))
print("Age:", user.get("age") or "Not provided")

# Exercise 11. Count words
text = "python java python go python java"
text_list = text.split(" ")

words = {}

for word in text_list:
    if words.get(word):
        words[word] += 1
    else:
        words[word] = 1

print(words)

# Exercise 12. Filter active users
users = [
    {"name": "Ana", "active": True},
    {"name": "Carlos", "active": False},
    {"name": "Maria", "active": True},
    {"name": "Jose", "active": False},
]

active_users = [user for user in users if user["active"]]
print(active_users)

# Level 4. Comprehesions

# Exercise 13.  Squares
numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]
print(squares)

# Exercise 14. Even numbers
numbers = range(1, 21)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Exercise 15. Dicitionary comprehesion
numbers = [1, 2, 3, 4, 5]
numbers_dict = {
    number: number ** 2
    for number in numbers
}

print(numbers_dict)

# Level 5. Thoughfull Backend
# Exercise 16. Users system
users = [
    {"name": "Ana", "age": 17, "active": True},
    {"name": "Carlos", "age": 25, "active": True},
    {"name": "Maria", "age": 31, "active": False},
    {"name": "Jose", "age": 22, "active": True},
]

mayors = [user["name"] for user in users if user["age"] >= 18]
active = [user["name"] for user in users if user["active"]]

print(mayors)
print(active)

# Exercise 17. Most expensive product without max() function
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 100},
    {"name": "Keyboard", "price": 40},
    {"name": "Monitor", "price": 350},
]

expensive: float = 0
expensive_product = {}

for product in products:
    if product["price"] > expensive:
        expensive = product["price"]
        expensive_product = product

print(expensive_product)

# Exercise 18. Login system
users = {
    "cesario": "python123",
    "admin": "admin456",
    "ana": "hello789"
}

username_input = input("Username? ")
password_input = input("Password? ")

if users.get(username_input) == password_input:
    print("Login successful")
else:
    print("Invalid credentials")

# Exercise 19. Proccess a request list
requests = [
    {"method": "GET", "status": 200},
    {"method": "POST", "status": 201},
    {"method": "GET", "status": 404},
    {"method": "GET", "status": 200},
    {"method": "DELETE", "status": 500},
]

total_get = 0
total_200 = 0
total_error = 0

counter = {
    "get": 0,
    "200": 0,
    "error": 0
}


for request in requests:
    if request["method"] == "GET":
        counter["get"] += 1

    if request["status"] == 200:
        counter["200"] += 1

    if request["status"] >= 400:
        counter["error"] += 1

print(counter)

# Exercise 20. Mini project - user manager
users = []

menu = [
    "1. Add user",
    "2. List user",
    "3. Find user",
    "4. Delete user",
    "5. Exit"
]

while True:
    for option in menu:
        print(option)

    selected_option = input("\nSelect an option: ")

    if selected_option == "5":
        break

    if selected_option == "1":
        name = input("User name? ")
        email = input("User email? ")
        age = int(input("User age? "))
        users.append({
            "name": name,
            "email": email,
            "age": age
        })

        print("User added succesfully!")

    if selected_option == "2":
        for user in users:
            print(f"{user['name']} - {user['email']} - {user['age']}")

    if selected_option == "3" or selected_option == "4":
        search_name = input("Name of user you looking for? ")
        user_found = {}

        for index, user in enumerate(users):
            if user["name"] == search_name:
                user_found = user

                if selected_option == "4":
                    users.pop(index)
                    print("User deleted successfully!")

        if selected_option == "3":
            if user_found:
                print("User found", user_found)
            else:
                print("User not found!")
