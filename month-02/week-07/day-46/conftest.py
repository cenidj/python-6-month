import pytest


@pytest.fixture
def productos():
    return [
        {"nombre": "lápiz", "precio": 1.5},
        {"nombre": "cuaderno", "precio": 4.0},
        {"nombre": "borrador", "precio": 1.0},
    ]


@pytest.fixture(scope="module")
def configuracion():
    return {"moneda": "EUR"}
