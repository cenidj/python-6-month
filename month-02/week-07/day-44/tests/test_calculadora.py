import pytest

from src.calculadora import dividir, restar, sumar


def test_sumar():
    assert sumar(5, 3) == 8


def test_restar():
    assert restar(10, 4) == 6


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
