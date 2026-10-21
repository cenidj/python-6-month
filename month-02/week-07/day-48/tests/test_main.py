import pytest

from src.main import dividir


def test_dividir_entre_cero():
    with pytest.raises(ValueError, match="El divisor no puede ser cero"):
        dividir(10, 0)
