import pytest

from src.operaciones import calcular_descuento, es_par, multiplicar, validar_edad


def test_multiplicar():
    assert multiplicar(4, 5) == 20


def test_es_par():
    assert es_par(4) == True


def test_es_impar():
    assert es_par(7) == False


def test_validar_edad_valida():
    assert validar_edad(27) == "Edad valida"


def test_validar_edad_negativa():
    with pytest.raises(ValueError):
        validar_edad(-5)


def test_calcular_descuento():
    assert calcular_descuento(100, 20) == 80
    assert calcular_descuento(200, 50) == 150
    # assert calcular_descuento(50, 10) == 45
    assert calcular_descuento(50, 10) == 40
