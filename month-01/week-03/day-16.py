def saludar(nombre="Usuario"):
    print(f"Hola {nombre}")


saludar("Cesario")
saludar()


def crear_usuario(nombre, rol="user"):
    print(f"{nombre} tiene el rol {rol}")


crear_usuario("Cesario")
crear_usuario("Ana", "admin")


def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")


presentar("Cesario", 27)
# nombre = "Cesario"
# edad = 27

# Also you can specify the parameter
presentar(nombre="Cesario", edad=27)


# Combining both
def crear_usuario(nombre, edad=18, rol="user"):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Rol: {rol}")


crear_usuario("Cesario")
crear_usuario("Cesario", 27)
crear_usuario("Cesario", 27, "admin")
crear_usuario(nombre="Cesario", rol="admin", edad=27)


# Required parameters go before default parameters
# ✅
def usuario(nombre, edad=18):
    pass


# ❌
# def usuario(edad=18, nombre):
#     pass


# Exercises day 16
# 1. Create default parameter
def saludar(nombre="Usuario"):
    print(f"Hola {nombre}")


# Should print Hola Cesario
saludar("Cesario")

# Should print Hola Usuario
saludar()


# 2. Two defaults
def informacion(nombre, edad=18, pais="USA"):
    print(f"{nombre} de {edad} años vive en {pais}")


informacion("Cesario", 27)
informacion("Ana")


# 3. Keyword arguments
def producto(nombre, precio, cantidad):
    print(f"{nombre} - {precio} - {cantidad}")


producto(precio=560, cantidad=1, nombre="PS5")


# 4. Mixing positional + keyword
def crear_usuario(nombre, edad=18, rol="user"):
    print(f"{nombre} tiene {edad} años y es un {rol}")


crear_usuario("Cesario")
crear_usuario("Cesario", 27)
crear_usuario("Cesario", rol="admin")
crear_usuario("Cesario", edad=27, rol="admin")


# 5. Mini backend challenge
# Imaging you building a function to register users
def registrar_usuario(nombre, email, rol="user", activo=True):
    print(f"Usuario: {nombre}")
    print(f"Email: {email}")
    print(f"Rol: {rol}")
    print(f"Activo: {activo}")


registrar_usuario("Cesario", "ing.cesarionivar@gmail.com", activo=False)
registrar_usuario("Junior", "cndj.dev@gmail.com")
registrar_usuario(nombre="Cedrick", email="cedrick@gmail.com", rol="admin", activo=True)
