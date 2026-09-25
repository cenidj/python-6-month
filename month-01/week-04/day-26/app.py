import logging

logging.basicConfig(
    filename="app-main.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Aplicacion iniciada")
logging.info("Usuario intentando iniciar sesion")
logging.warning("Contrasena incorrecta")
logging.info("Usuario autenticado")


def dividir(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.error("Can't divide by cero")
    except ValueError:
        logging.error("Can't divide charaters")


dividir(10, 2)
dividir(10, 0)


# Sistema de empleados
empleados = [
    {"nombre": "Ana", "salario": 50000},
    {"nombre": "Carlos", "salario": 65000},
    {"nombre": "John", "salario": 72000},
]


def buscar_empleado(nombre):
    logging.info(f"Se esta buscando el empleado {nombre}")
    encontrado = None
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            encontrado = empleado

    if encontrado is not None:
        logging.info("Empleado encontrado")
        print(encontrado)
        return encontrado
    else:
        logging.warning("Empleado no existe")


buscar_empleado("Cesario")
buscar_empleado("Ana")
