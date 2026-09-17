# Lambda, sorted, map, filter

numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

ordenados = sorted(numeros, reverse=True)
print(ordenados)

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "John", "edad": 17},
]

usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario["edad"])

print(usuarios_ordenados)


# Exercises
# Level 1 - lambda
# 1. Create a lambda function which receive a number and
# return its square
number_square = lambda number: number**2
number = 5
result = number_square(number)
print(result)

# 2. lambda; determine if even
even = lambda number: number % 2 == 0
print(even(21))

# 3. lambda which receive a name and return "Hola, Cesario"
greeting = lambda name: f"Hola {name}"
print(greeting("Cesario"))

# 4. lambda which receive 2 numbers and return bigest
biggest = lambda number_1, number_2: max(number_2, number_1)
result = biggest(12, 26)
print(result)

# Level 2 - map()
# 5. You have
numeros = [1, 2, 3, 4, 5]
numeros_by_2 = list(map(lambda x: x * 2, numeros))
print(numeros_by_2)

# 6. with numeros_by_2 get their square with map
numeros_square = list(map(lambda num: num**2, numeros_by_2))
print(numeros_square)

# 7. You have
precios = [10, 20, 30, 40]

# with map add 7% taxes to every price
precios_con_impuestos = list(map(lambda precio: precio + (precio * 0.07), precios))
print(precios_con_impuestos)

# 8. You have
nombres = ["ana", "carlos", "cesario", "maria"]

# With map convert every name to uppercase
nombres_mayusculas = list(map(lambda nombre: nombre.upper(), nombres))
print(nombres_mayusculas)

# level 3 - filter
# 9.  you have
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# with filter get only the even numbers
even_numbers = list(filter(lambda number: number % 2 == 0, numeros))
print(even_numbers)

# 10. Use filter to obtain only the number greater than 5
greater_than_five = list(filter(lambda num: num > 5, numeros))
print(greater_than_five)

# 11. You have
edades = [12, 18, 25, 16, 30, 14, 21]

# get only the adults(18+)
adults = list(filter(lambda edad: edad >= 18, edades))
print(adults)

# 12. You have
usuarios = ["Ana", "John", "Carlos", "Maria", "Alex"]

# with filter get only the name with more than 4 characters
usuarios_four_characters = list(filter(lambda name: len(name) > 4, usuarios))
print(usuarios_four_characters)

# Level 4 - sorted()
# 13. Sort by lowest to greatest
numeros = [8, 3, 10, 1, 5, 2]

sorted_numeros_lowest = sorted(numeros)
print(sorted_numeros_lowest)

# 14. Sort from greatest to lowest
sorted_numeros_greatest = sorted(numeros, reverse=True)
print(sorted_numeros_greatest)

# 15. You have
nombres = ["Carlos", "Ana", "Sebastian", "John", "Maria"]
sorted_nombres = sorted(nombres, key=lambda nombre: len(nombre))
print(sorted_nombres)

# Leve 5 - Mixing everything
# 16. You have
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Do the following
# 1. filter to keep even numbers
filtered_numbers = filter(lambda numero: numero % 2 == 0, numeros)
# 2. map to multiply it by 10
multiply_numbers = map(lambda numero: numero * 10, filtered_numbers)
# 3. convert the result into list
result = list(multiply_numbers)
print(result)


# 17. You have
precios = [50, 10, 100, 25, 75]

# Use map to add 10% taxes and sorted to order it!
precios_taxeados = map(lambda precio: precio + (precio * 0.1), precios)
precios_ordenados = sorted(precios_taxeados)

print(precios_ordenados)

# 18. You have
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "John", "edad": 17},
    {"nombre": "Maria", "edad": 22},
]

# with filter get the adults
adults = list(filter(lambda usuario: usuario["edad"] >= 18, usuarios))
print(adults)

# Level 6 - backend-style
# 19. you have
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "John", "edad": 17},
    {"nombre": "Maria", "edad": 22},
]

# sort the user by age using sorted()
sorted_users_by_age = sorted(usuarios, key=lambda usuario: usuario["edad"])
print(sorted_users_by_age)

# 20 - last challenge
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Keyboard", "precio": 80},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Headphones", "precio": 150},
]

# use filter to get products over $100 or more
products_over_100 = list(filter(lambda product: product["precio"] >= 100, productos))
# use map to add 10% discount
final_price_products = list(
    map(
        lambda product: {
            "nombre": product["nombre"],
            "precio": product["precio"] - (product["precio"] * 0.1),
        },
        products_over_100,
    )
)
# use sorted to order products by final price
final_price_sorted = sorted(final_price_products, key=lambda product: product["precio"])

print(products_over_100)
print(final_price_products)
print(final_price_sorted)
