# Testing
def sumar(a: int, b: int) -> int:
    return a + b


print(sumar(5, 3))


def test_sumar():
    assert sumar(5, 3) == 8


test_sumar()


def calcular_aumento(salario: float, porcentaje: float) -> float:
    return salario + (salario * porcentaje / 100)


print(calcular_aumento(50000, 10))


def test_calcular_aumento():
    resultado = calcular_aumento(50000, 10)
    assert resultado == 55000
