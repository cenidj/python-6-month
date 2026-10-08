# Iterators

# Iterable vs iterator

numeros = [10, 20, 30]

for numero in numeros:
    print(numero)

# list es iterable, pero no es directamente un iterator

# Podemos convertirla
numeros = [10, 20, 30]

iterator = iter(numeros)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# cuando llama a next obtiene el siguiente elemento

# 2. iter()
# convierte un iterable en un iterador

numeros = [10, 20, 30]

iterator = iter(numeros)

print(next(iterator))
print(next(iterator))

# la siguiente llamada continua donde se quedo
print(next(iterator))


# 3. next()
# obtiene el siguiente elemento del iterator
numeros = [10, 20, 30]

iterator = iter(numeros)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Pero, que ocurre cuando ya no quedan elementos?
# print(next(iterator))  # -> python lanza un StopIteration

# esto es importante por que for utiliza precisamente este mecanismo internamente

# 4. Que hace realmente un for?
numeros = [10, 20, 30]

for numero in numeros:
    print(numero)

# python conceptualmente hace algo parecido a:
iterator = iter(numeros)

while True:
    try:
        numero = next(iterator)
        print(numero)
    except StopIteration:
        break

# por eso iter() y next() son fundamentales para enteder como funciona un for

# 5. crear nuestro propio iterator
# un objeto se convierte en iterator cuando implementas:
# __iter__() y __next()__


# ejemplo...
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.numero = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero < self.limite:
            self.numero += 1
            return self.numero

        raise StopIteration


# ahora....
contador = Contador(5)

for numero in contador:
    print(numero)


# Ejercicios

# Ejercicio 1. Iterator basico
numeros = [10, 20, 30, 40, 50]

iterator = iter(numeros)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Ejercicio 2. StopIteration
colores = ["rojo", "azul", "verde"]

colores_iterator = iter(colores)
try:
    print(next(colores_iterator))
    print(next(colores_iterator))
    print(next(colores_iterator))
    print(next(colores_iterator))
except StopIteration:
    print("No hay mas elementos")


# Ejercicio 3. Crear tu iterator
class Contador:
    def __init__(self, limite, inicio=0):
        self.limite = limite
        self.inicio = inicio - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio < self.limite:
            self.inicio += 1
            return self.inicio

        raise StopIteration


contador = Contador(limite=10, inicio=5)

for numero in contador:
    print(numero)

# Ejercicio 4. Contador personalizado
# modificar Contador para que acepte inicio y limite

# Ejercicio 5. Empleados
empleados = [
    {"nombre": "Ana", "salario": 50000},
    {"nombre": "Carlos", "salario": 65000},
    {"nombre": "John", "salario": 72000},
    {"nombre": "Maria", "salario": 480000},
]

empleados_iterator = iter(empleados)

print(next(empleados_iterator))
print(next(empleados_iterator))
print(next(empleados_iterator))


# Mini reto
class CuentaRegresiva:
    def __init__(self, cuenta_desde):
        self.cuenta_desde = cuenta_desde + 1
        self.final = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cuenta_desde > 1:
            self.cuenta_desde -= 1
            return self.cuenta_desde
        raise StopIteration


cuenta = CuentaRegresiva(5)

for numero in cuenta:
    print(numero)
