# Decorators
from functools import wraps


def mi_decorador(funcion):
    def wrapper():
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")

    return wrapper


def saludar():
    print("Hola, bienvenido!")


saludar = mi_decorador(saludar)

saludar()


# De forma mas sencilla podemos escribir la funcion anterior....
def mi_decorador(funcion):
    def wrapper():
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")

    return wrapper


@mi_decorador
def saludar():
    print("Hola, bienvenido!")


saludar()


@mi_decorador
def iniciar_sesion():
    print("Iniciando sesion")


@mi_decorador
def cerrar_sesion():
    print("Cerrando sesion")


iniciar_sesion()
cerrar_sesion()


# Decorators con argumentos en las funciones
def mi_decorador(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la funcion")
        resultado = funcion(*args, **kwargs)
        print("Despues de ejecutar la funcion")

        return resultado

    return wrapper


@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}")


saludar("Cesario")

print("\n")


@mi_decorador
def saludar():
    """Muestra un saludo."""
    print("Hola")


print(saludar.__name__)
print(saludar.__doc__)


# from functools import wraps


def registrar_ejecucion(funcion):

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"Ejecutando: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)

        print(f"Finalizada: {funcion.__name__}")

        return resultado

    return wrapper


@registrar_ejecucion
def obtener_usuarios():
    print("Obteniendo usuarios de la base de datos")


obtener_usuarios()


from functools import wraps
from time import perf_counter


def medir_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = perf_counter()

        resultado = funcion(*args, **kwargs)

        fin = perf_counter()

        print(f"Tiempo: {fin - inicio:.6f} segundos")
        return resultado

    return wrapper


@medir_tiempo
def calcular_suma():
    return sum(range(1_000_000))


resultado = calcular_suma()

print(resultado)

# from functools import wraps


def require_admin(funcion):

    @wraps(funcion)
    def wrapper(usuario, *args, **kwargs):
        if usuario.get("rol") != "admin":
            raise PermissionError("No tienes permisos para realizar esta operacion")

        return funcion(usuario, *args, **kwargs)

    return wrapper


@require_admin
def eliminar_usuario(usuario, usuario_id):
    print(f"Eliminando usuario {usuario_id}")


admin = {"nombre": "Ana", "rol": "admin"}
cliente = {"nombre": "Carlos", "rol": "user"}

eliminar_usuario(admin, 25)
# eliminar_usuario(cliente, 25)


# Ejercicios
# Ejercicio 1. Tu primer decorator
def mostrar_mensaje(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print("Iniciando funcion")
        resultado = funcion(*args, **kwargs)
        print("Funcion ejecutada")
        return resultado

    return wrapper


@mostrar_mensaje
def saludar():
    print("Hola, Python")


saludar()


# Ejercicio 2. Decorador con argumentos
def registrar(funcion):

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {funcion.__name__}")
        resultado = funcion(*args, **kwargs)

        return resultado

    return wrapper


@registrar
def presentar(nombre, edad):
    print(f"Me llamo {nombre} y tengo {edad} años")


presentar("Cesario", 27)


# Ejercicio 3. Conservar el resultado
@mi_decorador
def decorador(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print("Calculando...")
        resultado = funcion(*args, **kwargs)
        return resultado

    return wrapper


@decorador
def multiplicar(a, b):
    return a * b


resultado = multiplicar(5, 6)

print(resultado)


# Ejercicio 4. Medir el tiempo
def medir_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = perf_counter()
        print(f"Tiempo: {fin - inicio:.6f} segundos")
        return resultado

    return wrapper


@medir_tiempo
def contar():
    total = 0

    for numero in range(1_000_000):
        total += numero

    return total


contar()


# Ejercicio 5. Autorizacion en backend
def requiere_admin(funcion):
    @wraps(funcion)
    def wrapper(usuario, *args, **kwargs):
        if usuario.get("rol") != "admin":
            raise PermissionError("Accesso denegado")

        resultado = funcion(usuario, *args, **kwargs)
        return resultado

    return wrapper


@requiere_admin
def eliminar_producto(usuario, producto_id):
    print(f"Producto {producto_id} eliminado")


admin = {"nombre": "Ana", "rol": "admin"}
cliente = {"nombre": "Carlos", "rol": "user"}

eliminar_producto(admin, "1")

try:
    eliminar_producto(cliente, "2")
except PermissionError:
    print("El usuario no puede ser eliminado sin privilegios de administrador")
