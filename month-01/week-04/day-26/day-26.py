# Día 26
# * Debugging
# * logging

# 1. Debugging
def calcular_total(precio, cantidad):
    print("precio", precio)
    print("cantidad", cantidad)
    total = precio * cantidad
    print("total", total)
    return total


resultado = calcular_total(100, 3)
print(resultado)

# print como debugging
# it works but in large project could be a disaster


def calcular_total(precio, cantidad):
    total = precio * cantidad  # breakpoint
    return total


resultado = calcular_total(100, 3)
print(resultado)

# Logging
"""
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Aplicacion iniciada")
logging.warning("El usuario tiene suficiente permisos")
logging.error("No se puede conectar a la base de datos")

# DEBUG
logging.debug("Valor de usuario_id: 25")

# INFO
logging.info("Usuario creado correctamente")

# WARNING
logging.warning("Intento de login fallido")

# ERROR
logging.error("No se pudo guardar el usuario")

# CRITICAL
logging.critical("Base de datos completamente inacesible")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Usuario creado")

try:
    numero = int(input("Numero: "))
    resultado = 100 / numero
except ValueError:
    logging.error("El usuario introdujo un valor invalido")
except ZeroDivisionError:
    logging.error("No se puede dividir entre cero.")


try:
    numero = int(input("Numero: "))
    resultado = 100 / numero
except Exception:
    logging.exception("Ocurrio un error")
"""

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Aplicacion iniciada")
logging.warning("Algo inesperado ocurrio")
logging.error("Ocurrio un error")
