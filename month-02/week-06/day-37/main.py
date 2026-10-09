# Generators

# Ejercicio 1. Generator basico
def generar_numeros():
    yield from [10, 20, 30, 40, 50]


for numero in generar_numeros():
    print(numero)


# Ejercicio 2. Comprender yield
# Analiza el siguiente codigo:
def ejemplo():
    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3


generador = ejemplo()

print(next(generador))
print(next(generador))

# Que aparece en pantalla? aparece "A", 1, "B", 2
# Por que no aparece la letra "C"? Porque solo se esta llamando el generador 2 veces y la letra "C" seria la siguiente en imprimirse segun la lista de espera (ultimo yield llamado) del generador
# Que ocurriria si llamaras a next(generador) una tercera vez? imprimiria la letra "C" y el 3


# Ejercicio 3. Generator con range()
def generar_pares(limite):
    return (numero for numero in range(limite + 1) if numero != 0 and numero % 2 == 0)


for numero in generar_pares(10):
    print(numero)

# Ejercicio 4. Generar cuadrados
cuadrados = (numero * numero for numero in range(1, 6))

for numero in cuadrados:
    print(numero)

# Ejercicio 5. Filtrar empleados
empleados = [
    {"nombre": "Ana", "salario": 50000, "departamento": "IT"},
    {"nombre": "Carlos", "salario": 65000, "departamento": "HR"},
    {"nombre": "John", "salario": 72000, "departamento": "IT"},
    {"nombre": "Maria", "salario": 48000, "departamento": "Marketing"},
    {"nombre": "Alex", "salario": 80000, "departamento": "IT"},
]


def filtrar_empleados(empleados, salario_minimo):
    for empleado in empleados:
        if empleado["salario"] >= salario_minimo:
            yield empleado


for empleado in filtrar_empleados(empleados, 65000):
    print(empleado["nombre"])


# Ejercicio 6. Generador de nombres
empleados = [
    {"nombre": "Ana"},
    {"nombre": "Carlos"},
    {"nombre": "John"},
]


def generar_nombres(empleaods):
    for empleado in empleados:
        yield empleado["nombre"]


for nombre in generar_nombres(empleados):
    print(nombre)

# Ejercicio 7. Generator expression
numeros = (numero * numero for numero in range(1, 11))

for numero in numeros:
    if numero > 25:
        print(numero)


# Ejercicio 8. Procesamiento de transaciones
transacciones = [
    {"id": 1, "monto": 100},
    {"id": 2, "monto": 250},
    {"id": 3, "monto": 50},
    {"id": 4, "monto": 400},
    {"id": 5, "monto": 150},
]


def filtrar_transacciones(transacciones, monto_minimo):
    for transaccion in transacciones:
        if transaccion["monto"] >= monto_minimo:
            yield transaccion


for transaccion in filtrar_transacciones(transacciones, 150):
    print(transaccion["id"])


# Ejercicio 9. Generador de registros
def generar_registros(cantidad):
    for numero in range(1, cantidad + 1):
        yield {"id": numero, "activo": True}


for registro in generar_registros(3):
    print(registro)


# Ejercicio 10. Comparacion entre lista y generator
def generar_lista(limite):
    return [numero for numero in range(1, limite + 1)]


def generar_con_yield(limite):
    return (numero for numero in range(1, limite + 1))


print(type(generar_lista(5)))
print(type(generar_con_yield(5)))
