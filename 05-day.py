
# 1. For
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

for letra in "Python":
    print(letra)

# 2. Range
for numero in range(5):
    print(numero)

for numero in range(1, 6):
    print(numero)

for numero in range(0, 11, 2):
    print(numero)


# 3. While
numero = 1

while numero <= 5:
    print(numero)
    numero += 1

# 4. break


for numero in range(1, 11):
    if numero == 5:
        break
    print(numero)

print("---------")

# 5. continue
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

# Ejercicio del dia 5
for numero in range(1, 21):
    if numero % 2 == 0:
        continue
    if numero == 15:
        break

    print(numero)

# Reto extra
print("-----------")
print("Reto extra")
print("-----------")

for numero in range(1, 31):
    if numero % 2 == 0 or numero == 15:
        continue
    if numero == 25:
        break
    print(numero)
