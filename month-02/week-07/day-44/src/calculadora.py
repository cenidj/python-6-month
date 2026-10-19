def sumar(a: int, b: int) -> int:
    return a + b


def restar(a: int, b: int) -> int:
    return a - b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b
