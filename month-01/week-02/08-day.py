
# Listas
frutas = ["manzana", "banana", "naranja", "uva"]
print(frutas)

datos = ["Carlos", 27, True, 3.14]

# indexing - python empieza a contar desde cero
print(frutas[0])  # manzana
print(frutas[1])  # banana

# Tambien se puede acceder desde el final usando indices negativos
print(frutas[-1])  # uva
print(frutas[-2])  # naranja

# slicing - permite obtener una parte de una lista
print(frutas[1:4])  # ["banana", "naranja", "uva"]

# basic structure is list[start:end] - last index is not include

print(frutas[:3])  # first three
print(frutas[2:])  # start at index 2
print(frutas[::2])  # every 2 elements

# list methods
frutas.append("mango")  # add to the end
frutas.insert(1, "pera")  # add to specify position
frutas.remove("banana")  # delete per value
frutas.pop()  # delete the last
frutas.sort()  # order
frutas.reverse()  # flip the list
print(len(frutas))  # count elements

# 🎯 challenge of the day
animales = ["perro", "gato", "leon", "tigre", "oso"]

# 1. print "leon" indexing
print(animales[2])

# 2. print last 3 elements using slicing
print(animales[-3:])

# 3. add "elefante" with append()
animales.append("elefante")

# 4. delete "gato" with a method
animales.remove("gato")

# 5. flip the list
animales.reverse()

# 6. print how many animals still on the list
print(len(animales))
