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
    usuario = {}
    for key, value in kwargs.items():
        usuario[key] = value

    return usuario


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
