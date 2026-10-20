# def test_hay_dos_productos(productos):
#     assert len(productos) == 2


def test_total_precio_productos(productos):
    precios = [producto["precio"] for producto in productos]
    total = sum(precios)

    assert total == 6.5


def test_hay_tres_productos(productos):
    assert len(productos) == 3
