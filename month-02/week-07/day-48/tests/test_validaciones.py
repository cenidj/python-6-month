import pytest

from src.validaciones import calcular_promedio, validar_edad


def test_edad_negativa():
    with pytest.raises(ValueError):
        validar_edad(-10)


def test_edad_valida():
    assert validar_edad(27) == "Edad valida"


def test_validar_edad_negativa_con_mensaje():
    with pytest.raises(ValueError, match="La edad no puede ser negativa"):
        validar_edad(-5)


def test_promedio_lista_vacia():
    with pytest.raises(ValueError):
        calcular_promedio([])
