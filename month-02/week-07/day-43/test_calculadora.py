from calculadora import (
    calcular_promedio,
    calcular_salario_anual,
    multiplicar,
    restar,
    sumar,
)


def test_sumar_dos_numeros_positivos():
    assert sumar(5, 3) == 8


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(5, 4) == 20


def test_calcular_promedio():
    notas = [80, 90, 100]
    assert calcular_promedio(notas) == 90


def test_calcular_salario_anual():
    assert calcular_salario_anual(4000) == 48000
    assert calcular_salario_anual(5500) == 66000
