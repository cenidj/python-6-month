# Assertions

# Ejercicio 1.
edad = 25

assert edad >= 18, "Es menor de edad"


saldo = 500

assert saldo >= 0, "El saldo no puede ser negativo"


def calcular_promedio(notas: list[int]):
    assert len(notas) > 0, "La lista no puede estar vacia"

    return sum(notas) / len(notas)


resultado = calcular_promedio([80, 90, 100])
print(resultado)

resultado_vacio = calcular_promedio([])
print(resultado_vacio)


def aplicar_descuento(precio: float, descuento: float) -> float:
    if precio < 0:
        raise ValueError("El precio no puedde ser negativo")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar en un rango 0-100")

    return precio - (precio * descuento / 100)
