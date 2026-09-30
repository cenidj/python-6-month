import logging

logger = logging.getLogger(__name__)


def calcular_promedio(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print("No existe salario promedio o no existen empleados")
        logger.error("Se intento dividir entre 0")
        return 0
