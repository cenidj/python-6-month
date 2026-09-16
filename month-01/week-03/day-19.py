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
