# Type hints

# Ejercicio 1. anotaciones basicas
def multiplicar(a: int, b: int) -> int:
    return a * b


# Ejercicio 2. listas
def obtener_nombres() -> list[str]:
    empleados: list[str] = ["Cesario", "Josue", "Cedrick"]
    return empleados


# Ejercicio 3. diccionarios
def obtener_salarios() -> dict[str, float]:
    return {"Ana": 50000.0, "Carlos": 65000.0, "John": 72000.0}


# Ejercicio 4. Valores opcionales
def buscar_empleado(nombre: str | None = None) -> str:
    if nombre is None:
        return "No se proporciono un nombre"
    return f"Buscando empleado: {nombre}"


# Ejercicio 5. programacion orientda a objetos
class Empleado:
    def __init__(self, nombre: str, salario: float) -> None:
        self.nombre = nombre
        self.salario = salario


def calcular_salario_anual(empleado: Empleado) -> float:
    return empleado.salario * 12


# Ejercicio 6. pregunta conceptual
def sumar(a: int, b: int) -> int:
    return a + b


print(sumar("10", "20"))

# print return "1020" una cadena, y las herramientas que podemos utilizar pueden ser pyright or mypy
