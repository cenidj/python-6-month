def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("El divisor no puede ser cero")

    return a / b
