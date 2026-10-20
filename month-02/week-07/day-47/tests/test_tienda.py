from unittest.mock import patch

from src.tienda import calcular_precio_final, calcular_total


def test_calcular_total():
    with patch("src.tienda.obtener_precio", return_value=50) as mock_precio:
        resultado = calcular_total(3)

    assert resultado == 150
    mock_precio.assert_called_once()


def test_calcular_precio_final():
    with patch("src.tienda.obtener_descuento", return_value=25):
        resultado = calcular_precio_final(100)

    assert resultado == 75
