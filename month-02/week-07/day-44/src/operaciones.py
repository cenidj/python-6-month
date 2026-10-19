def multiplicar(a: int, b: int) -> int:
    return a * b


def es_par(numero: int) -> bool:
    return numero % 2 == 0


def validar_edad(edad: int) -> str:
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    return "Edad valida"


def calcular_descuento(precio: float, descuento: float) -> float:
    return precio - descuento
