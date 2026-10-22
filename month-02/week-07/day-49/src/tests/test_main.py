import pytest

from core.main import empleados_por_departamento


@pytest.fixture
def empleados():
    return [
        {"nombre": "Ana", "salario": 50000, "departamento": "IT"},
        {"nombre": "Carlos", "salario": 65000, "departamento": "HR"},
        {"nombre": "John", "salario": 72000, "departamento": "IT"},
        {"nombre": "Maria", "salario": 48000, "departamento": "Marketing"},
    ]


def test_empleados_por_IT(empleados):
    resultado = empleados_por_departamento(empleados, "IT")

    assert [empleado["nombre"] for empleado in resultado] == ["Ana", "John"]


def test_empleados_por_HR(empleados):
    resultado = empleados_por_departamento(empleados, "HR")

    assert [empleado["nombre"] for empleado in resultado] == ["Carlos"]


def test_empleados_por_departamento_vacio(empleados):
    resultado = empleados_por_departamento(empleados, "vacio")

    assert resultado == []
