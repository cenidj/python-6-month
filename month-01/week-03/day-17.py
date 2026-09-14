#  *args and **kwargs

# *args -> Multiples argumentos posicionales
# normally
def sumar(a, b):
    return a + b


print(sumar(10, 20))


# what happen if we don't know how many arguments we're gonna get
# there we use
def sumar(*args):
    print(args)


sumar(10, 20, 30)


# *args receive the arguments as a tuple
def sumar(*args):
    total = 0

    for numero in args:
        total += numero

    return total


print(sumar(10, 20, 30))
print(sumar(5, 10, 15, 20))

# * is the important. The name args is just a standar, technically we can call it different.


# **kwargs -> Multiple arguments with name
# imagine you want to create a user
def crear_usuario(nombre, edad, rol):
    print(nombre, edad, rol)


crear_usuario(nombre="Cesario", edad=27, rol="user")


# but in the future you want to get more info
# you can use **kwargs
def crear_usuario(**kwargs):
    print(kwargs)


crear_usuario(nombre="Cesario", edad=27, rol="admin")


# kwargs get the arguments as a dictionary
# you can access then
def crear_usuario(**kwargs):
    print(f"Nombre: {kwargs['nombre']}")
    print(f"Rol: {kwargs['rol']}")


crear_usuario(nombre="Cesario", rol="admin")

# *args -> tuple
# ** kwargs -> dictionary


def ejemplo(*args, **kwargs):
    print(args)
    print(kwargs)


ejemplo(10, 20, 30, nombre="Cesario", rol="admin")


# Excercises day 17
# Level 1. *args
# 1. create a function sumar_todos() which get any numbers and return their sum
def sumar_todos(*args):
    total = 0

    for num in args:
        total += num

    return total


resultado = sumar_todos(5, 10, 15)
print(resultado)


# Create a function mayor() which get any numbers an return the greater without using max
def mayor(*args):
    numero_mayor = args[0]

    for num in args:
        if num > numero_mayor:  # noqa: PLR1730
            numero_mayor = num

    return numero_mayor


resultado = mayor(10, 25, 7, 40)
print(resultado)


# level 2 - **kwargs
# 3. Create a function mostrar_usuariO() which receive information using **kwargs and show every key and value
def mostrar_usuario(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


mostrar_usuario(nombre="Cesario", edad=27, rol="backend developer")


# 4. Create a function crear_producto() using **kwargs
def crear_producto(**kwargs):
    print(f"Nombre: {kwargs['nombre']}")
    print(f"Precio: {kwargs['precio']}")
    print(f"Categoria: {kwargs['categoria']}")


crear_producto(nombre="MacBook", precio=1500, categoria="Tecnologia")


# Level 3. Combining
# 5. create
def registrar_compra(*productos, **datos):
    print("Productos:")
    for producto in productos:
        print(producto)

    print("Datos:")
    for k, v in datos.items():
        print(f"{k}: {v}")


registrar_compra(
    "Laptop", "Mouse", "Keyboard", cliente="Cesario", metodo_pago="Credit Card"
)
