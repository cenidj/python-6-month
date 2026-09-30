import json

# Repaso python


# Ejercicio 1. Funciones
def calcular_promedio(numeros):
    try:
        return sum(numeros) / len(numeros)
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")


print(calcular_promedio([10, 20, 30, 40]))

# Ejercicio 2. List + dicitionaries
empleados = [
    {"nombre": "Ana", "salario": 50000, "departamento": "IT"},
    {"nombre": "Carlos", "salario": 65000, "departamento": "HR"},
    {"nombre": "John", "salario": 72000, "departamento": "IT"},
    {"nombre": "Maria", "salario": 48000, "departamento": "Marketing"},
]


def empleados_it(empleados):
    return list(filter(lambda empleado: empleado["departamento"] == "IT", empleados))


print(empleados_it(empleados))


# Ejercicio 3. Lambda/filter
def salarios_mayor(empleados):
    return list(filter(lambda empleado: empleado["salario"] >= 60000, empleados))


print(salarios_mayor(empleados))


# Ejercicio 4. Exceptions
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")


print(dividir(10, 5))
print(dividir(10, 0))

try:
    with open("empleados.json", "r") as file:
        content = json.load(file)
    print(content)

except FileNotFoundError:
    with open("empleados.json", "w") as file:
        data = [{"name": "Cesario"}]
        json.dump(data, file, indent=4)

        print(data)
