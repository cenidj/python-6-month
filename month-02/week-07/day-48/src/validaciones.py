def validar_edad(edad: int) -> str:
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return "Edad valida"


def calcular_promedio(notas: list[float]) -> float:
    if not notas:
        raise ValueError("La lista no puede estar vacía")

    return sum(notas) / len(notas)
