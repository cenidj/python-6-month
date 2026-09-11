# Functions
def saludar():
    print("Hello")


saludar()  # -> "Hello"


# Parameters
def saludar(nombre):
    print(f"Hola {nombre}")


saludar("Cesario")  # -> Hola Cesario
saludar("Ana")  # -> Hola Ana

# nombre is the parameter
# Cesario is the argument we pass in


# Multiple parameters
def sumar(a, b):
    print(a + b)


sumar(12, 3)  # -> 15


# Return
def sumar(a, b):
    return a + b


resultado = sumar(12, 3)
print(resultado)  # -> 15

# print() -> Want to show something
# return -> Want to give back something


# backend example
def calculate_total(price, tax):
    return price + (price * tax)


total = calculate_total(100, 0.07)
print(total)


# Exercise
# Create a function saludar which show Hola
def saludar():
    print("Hola")


saludar()


# Create a function saludar_persona(name) which show Hola Cesario
def saludar_persona(name):
    print(f"Hola {name}")


saludar_persona("Cesario")


# Create a function sumar(a, b) which return the sum
def sumar(a, b):
    return a + b


resultado = sumar(12, 43)
print(resultado)


# Create restar(a, b)
def restar(a, b):
    return a - b


resultado = restar(12, 3)
print(resultado)


def multiplicacion(a, b):
    return a * b


def es_par(num):
    return num % 2 == 0


def mayor(a, b):
    return a if a > b else b


def calcular_area_rectangulo(largo, ancho):
    return largo * ancho


def calcular_total(precio, cantidad):
    return precio * cantidad


def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)


resultado = calcular_promedio([10, 20, 30, 40])
print(resultado)

# Mini challenge


menu = ["1. Realizar operacion", "2. Salir"]

operaciones = ("sumar", "restar", "dividir", "multiplicar")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Can't divide by 0")
    return a / b


while True:
    print("\n--- Simple Calculator ---\n")
    for item in menu:
        print(item)
    user_option = input("\nSeleccione una opcion: ")

    if user_option == "2":
        break

    if user_option == "1":
        operacion = input("\nQue operacion quieres? ")
        if operacion in operaciones:
            numero1 = float(input("Primer numero: "))
            numero2 = float(input("Segundo numero: "))

            resultado = 0

            if operacion == "sumar":
                resultado = sumar(numero1, numero2)
            elif operacion == "restar":
                resultado = restar(numero1, numero2)
            elif operacion == "dividir":
                resultado = dividir(numero1, numero2)
            elif operacion == "multiplicar":
                resultado = multiplicar(numero1, numero2)

            print(f"\nResultado: {resultado}")
            continue

        else:
            print("\n⚠️ Operacion no reconocida")
