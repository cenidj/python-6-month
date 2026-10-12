# Context managers
class MiContextManager:
    def __enter__(self):
        print("Entrando al contexto")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saliendo del contexto")


with MiContextManager() as contexto:
    print("Ejecutando el bloque")

with MiContextManager() as contexto:
    print(type(contexto))

# Crear un context manager con contextlib

from contextlib import contextmanager


@contextmanager
def mi_context_manager():
    print("Entrando al contexto")

    try:
        yield
    finally:
        print("Saliendo del contexto")


with mi_context_manager():
    print("Ejecuntando el bloque")

# Por que son importantes en backend?

# Ejemplo 1. archivos JSON
import json

with open("employees.json", "r", encoding="utf-8") as archivo:
    empleados = json.load(archivo)

print(empleados)

# Ejemplo 2. Conexiones a bases de datos
"""
from sqlalchemy import create_engine

engine = create_engine("sqlite://empleados.db")

with engine.connect() as conexion:
    resultado = conexion.exec_driver_sql("SELECT 1")
    print(resultado.scalar())
"""

# Ejemplol 3. bloqueo de recursos
import threading

bloqueo = threading.Lock()

with bloqueo:
    print("Acceso exclusivo al recurso")
print("\n")


# Ejercicios
# Ejercicio 1. Utilizar with con archivos
with open("mensaje.txt", "w", encoding="utf-8") as file:
    file.write("Estoy aprendiendo Context Managers")
    print("Archivo creado correctamente y escritura realizada!")

with open("mensaje.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print(contenido)


# Ejercicio 2. Comprender el ciclo de vida
class MiContextManager:
    def __enter__(self):
        print("A")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("C")


with MiContextManager():
    print("B")

# 1. Imprime A porque es la entra del contexto
# 2. Imprime segundo B, porque ya esta dentro del contexto como tal
# 3. imprime C para salir o finalizar el contexto
# 4. Se ejecuta porque es el que cierra el contexto, siempre se ejecutara sin importar si ocurre una excepcion


# Ejercicio 3. Detectar una excepcion
with MiContextManager():
    print("Ejecutando")
    # raise ValueError("Error de prueba")

# 1. Si, se ejecutara __exit__(); siempre se ejecutara a pesar de las excepciones
# 2. Si, se imprimira C
# 3. No, la excepcion de desaparecera automaticamente
# 4. __exit__() tendria que devolver el exc_value


# Ejercicio 4. crear un Context Manager personalizado
class GestorArchivo:
    def __enter__(self):
        print("Abriendo recurso")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cerrando recurso")


with GestorArchivo():
    print("Procesando informacion")

# Ejercicio 5. crear un context manager con @contextmanager
from contextlib import contextmanager


@contextmanager
def gestionar_recurso():
    try:
        print("Preparando recurso")
        yield
    finally:
        print("Liberando recurso")


with gestionar_recurso():
    print("Gestionando los recursos")

# Ejercicio 6
import json
from contextlib import contextmanager


@contextmanager
def gestionar_archivo_empleados():
    with open("employees.json", "r", encoding="utf-8") as archivo:
        try:
            yield archivo
        finally:
            print("Archivo cerrado")


with gestionar_archivo_empleados() as archivo:
    empleados = json.load(archivo)
    print(empleados)
