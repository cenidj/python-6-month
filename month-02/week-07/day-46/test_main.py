import pytest


@pytest.fixture
def usuario():
    return {"nombre": "Ana", "activo": True}


def test_usuario_activo(usuario):
    assert usuario["activo"] is True


@pytest.fixture
def archivo_temporal(tmp_path):
    ruta = tmp_path / "datos.txt"
    ruta.write_text("hola", encoding="utf-8")

    yield ruta

    # cleanup
    if ruta.exists():
        ruta.unlink()


def test_archivo_contiene_texto(archivo_temporal):
    assert archivo_temporal.read_text(encoding="utf-8") == "hola"
