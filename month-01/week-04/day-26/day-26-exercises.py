import logging

logging.basicConfig(
    filename="main-app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 32},
    {"nombre": "John", "edad": 28},
]

for usuario in usuarios:
    if usuario["edad"] > 30:
        print(usuario["nombre"])


def calcular_promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio


numeros = [10, 20, 30, 40]

print(calcular_promedio(numeros))
