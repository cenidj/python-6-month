# Review mini project

expenses = {
    "rent": 1300,
    "entertainment": 100,
    "food": 600,
    "transportation": 150,
    "utilities": 160
}

total_spent = 0
highest_amount = 0
highest_spent = ""
expenses_over_200 = {}

print("\n--- Monthly expenses ---\n")
for description, amount in expenses.items():
    print(f"{description}: ${amount}")
    total_spent += amount

    if amount > highest_amount:
        highest_spent = description
        highest_amount = amount

    if amount > 200:
        expenses_over_200[description] = amount

print(f"\nTotal: ${total_spent}")
print(
    f"Highest expense: {highest_spent}: ${highest_amount}")

print("\nExpenses over $200:")
for expense in expenses_over_200:
    print(expense)
