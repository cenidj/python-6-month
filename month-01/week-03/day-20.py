# Exercises combining everything

# Level 1 - Functions + return


# 1. Greeting - create a function which receive a name and return "Hola, Cesario"
# Don't use print inside the function. use return
def saludar(nombre="Cesario"):
    return f"Hola, {nombre}"


print(saludar("Cesario"))


# 2. Calculator - create a function which receive price and taxes fee
# and return final price
def calcular_total(precio, impuesto):
    precio_final = precio + (precio * impuesto)
    return precio_final


print(calcular_total(25, 0.1125))


# 3. Even number - create a function which return True if the number is even
# and false if is odd
def is_even(number):
    return number % 2 == 0


print(is_even(20))
print(is_even(21))


# 4. Mayor de tres
def mayor_de_tres(a, b, c):
    return max(a, b, c)


print(mayor_de_tres(10, 21, 14))


# Level 2 - Default + keyword argument
# 5. Create user
def crear_usuario(nombre, edad, rol="user"):
    return {"nombre": nombre, "edad": edad, "rol": rol}


usuario = crear_usuario("Cesario", 27)
print(usuario)
second_user = crear_usuario("Carlos", 30, rol="admin")
print(second_user)


# 6. Product
def crear_producto(nombre, precio, categoria="electronics"):
    return {"nombre": nombre, "precio": precio, "categoria": categoria}


product_1 = crear_producto(nombre="Laptop", precio=1200, categoria="electronics")
product_2 = crear_producto(nombre="Mouse", precio=45, categoria="electronics")

print(product_1)
print(product_2)


# 7. Discount
def aplicar_descuento(precio, descuento=0.10):
    precio_final = precio - (precio * descuento)
    return precio_final


total_pagar = aplicar_descuento(100, 0.25)
print(total_pagar)


# Level 3 - *args
# 8. add numbers
def sumar(*args):
    total = 0
    for el in args:
        total += el
    return total


result = sumar(1, 2, 3, 4, 5)
print(result)


# 9. Average
def promedio(*args):
    return sum(args) / len(args)


print(promedio(10, 20, 30))


# 10. Found max
def encontrar_maximo(*args):
    maximo = args[0]
    for element in args:
        if element > maximo:
            maximo = element

    return maximo


print(encontrar_maximo(150, 20, 21, 12, 34, 46, -3))


# Level 4 - **kwargs
# 11. User info
def mostrar_usuario(**kwargs):
    return kwargs
    # Other way to do it (I now the code below won't run)
    # usuario = {}
    # for key, value in kwargs.items():
    #     usuario[key] = value

    # return usuario


user = mostrar_usuario(nombre="Cesario", edad=27, rol="developer")
print(user)


# 12. Settings
def crear_configuracion(**kwargs):
    setting = {}
    for key, value in kwargs.items():
        setting[key] = value

    # return kwargs # Could return all the args but need to know each of them
    return setting


print(crear_configuracion(debug=True, port=8000, enviroment="development"))


# 13. *args + ** kwargs
def mostrar_datos(*args, **kwargs):
    for el in args:
        print(el)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


mostrar_datos("Python", "FastAPI", "PostgreSQL", nivel="junior", remoto=True)


# Level 5 - Lambda + map + filter
# 14. Double numbers
def doblar_numeros(numeros):
    return list(map(lambda numero: numero * 2, numeros))


print(doblar_numeros([1, 2, 3, 4]))


# 15.  Filter adults
def obtener_adultos(edades):
    return list(filter(lambda edad: edad >= 18, edades))


print(obtener_adultos([12, 18, 25, 16, 30, 14, 21]))


# 16. Proccess names
def procesar_nombres(nombres):
    return list(map(lambda nombre: nombre.upper(), nombres))


print(procesar_nombres(["ana", "carlos", "cesario"]))


# Level 6 - sorted() + funciones
# 17. order users
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "John", "edad": 17},
    {"nombre": "Maria", "edad": 22},
]


def ordernar_usuarios(usuarios):
    return sorted(usuarios, key=lambda x: x["edad"])


print(ordernar_usuarios(usuarios))

# 18 Order products
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Keyboard", "precio": 80},
    {"nombre": "M", "precio": 300},
]


def ordenar_productos(productos, descendente=False):
    if descendente:
        return sorted(productos, key=lambda producto: producto["precio"], reverse=True)
    else:
        return sorted(productos, key=lambda producto: producto["precio"])


print(ordenar_productos(productos))
print(ordenar_productos(productos, descendente=True))

# Level 7 - Backend-style
# 19. Procesar usuarios

usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Carlos", "edad": 30, "activo": False},
    {"nombre": "John", "edad": 17, "activo": True},
    {"nombre": "Maria", "edad": 22, "activo": True},
]


def obtener_usuarios_activos(usuarios):
    usuarios_activos = list(filter(lambda usuario: usuario["activo"], usuarios))

    return usuarios_activos


print(obtener_usuarios_activos(usuarios))

# 20. Last challenge - Employee manager
empleados = [
    {"nombre": "Ana", "salario": 50000, "departamento": "IT"},
    {"nombre": "Carlos", "salario": 65000, "departamento": "HR"},
    {"nombre": "John", "salario": 72000, "departamento": "IT"},
    {"nombre": "Maria", "salario": 48000, "departamento": "Marketing"},
    {"nombre": "Alex", "salario": 80000, "departamento": "IT"},
]


def gestionar_empleados(empleados, departamento=None, salario_minimo=0):
    resultado = empleados
    if departamento:
        resultado = list(
            filter(lambda empleado: empleado["departamento"] == departamento, resultado)
        )

    if salario_minimo > 0:
        resultado = list(
            filter(lambda empleado: empleado["salario"] >= salario_minimo, resultado)
        )

    resultado = sorted(resultado, key=lambda empleado: empleado["salario"])

    return resultado


print(gestionar_empleados(empleados, departamento="IT"))
print(gestionar_empleados(empleados, salario_minimo=60000))
