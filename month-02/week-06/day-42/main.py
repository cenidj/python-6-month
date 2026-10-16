# Repaso

# Ejercicio 1. Type hints
def calcular_promedio(notas: list[float]) -> float:
    if len(notas) == 0:
        raise ValueError("No hay notas")

    return sum(notas) / len(notas)


notas = [85.0, 90.0, 78.0]
print(calcular_promedio(notas))

# Ejercicio 2. Dataclasses y validacion
from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

        if self.cantidad < 0:
            raise ValueError("La cantidad no puede ser nagativa")

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad


producto = Producto("Laptop", 250, 1)
print(producto)


# Ejercicio 3. Properties y encapsulacion
class CuentaBancaria:
    def __init__(self, saldo):
        if saldo <= 0:
            raise ValueError("El saldo no puede ser cero o negativo")
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("No se permiten depositos de cero o cantidades negativas")

        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad < 0:
            raise ValueError("No se permiten retiros de cero o cantidades negativas")

        if cantidad > self.saldo:
            raise ValueError("No se puede retirar dinero no disponible")

        self.saldo -= cantidad


cuenta = CuentaBancaria(1000)

cuenta.depositar(250)
cuenta.retirar(100)

print(cuenta.saldo)


# Ejercicio 4. Herencia y polimorfismo
class Empleado:
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_bono(self) -> float:
        return self.salario_mensual * 0.05


class Desarollador(Empleado):
    def calcular_bono(self) -> float:
        return self.salario_mensual * 0.10


class Gerente(Empleado):
    def calcular_bono(self) -> float:
        return self.salario_mensual * 0.20


empleados = [
    Empleado("Cesario", 2500),
    Desarollador("Cedrick", 3500),
    Gerente("Josue", 4500),
]

for empleado in empleados:
    print(f"{empleado.nombre} tiene un bono de: {empleado.calcular_bono()}")


# Ejercicio 5. Iteradores y generadores
def generar_pares(limite):
    return (numero for numero in range(limite + 1) if numero % 2 == 0)


for numero in generar_pares(10):
    print(numero)


# Ejercicio 6. Decoradores
from functools import wraps


def registrar_llamada(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print("Ejecutando funcion")
        resultado = funcion(*args, **kwargs)
        return resultado

    return wrapper


@registrar_llamada
def sumar(a: int, b: int) -> int:
    return a + b


resultado = sumar(10, 20)
print(resultado)


# Ejercicio 7. Context manager y excepciones
from contextlib import contextmanager


@contextmanager
def gestionar_archivo(filename: str):
    with open(filename, "w") as file:
        try:
            yield file
        finally:
            print("Archivo cerrado")


with gestionar_archivo("registro.txt") as archivo:
    archivo.write("Dia 42, repaso de Python\n")


# Ejercicio 8. Mini proyecto
@dataclass
class Empleado:
    nombre: str
    edad: int
    salario_mensual: float
    departamento: str

    def __post_init__(self):
        if self.edad < 0:
            raise ValueError("La edad debe ser un numero positivo")

        if self.salario_mensual <= 0:
            raise ValueError("El salario no puede ser cero o negativo")

    def calcular_salario_anual(self) -> float:
        return self.salario_mensual * 12

    def mostrar_info(self) -> str:
        return self.__repr__()


def salarios_superiores(empleados: list[Empleado]):
    return (empleado for empleado in empleados if empleado.salario_mensual > 5000)


empleados = [
    Empleado("Cedrick", 2, 6500, "IT"),
    Empleado("Josue", 24, 5500, "HR"),
    Empleado("Cesario", 27, 3000, "IT"),
]


for empleado in salarios_superiores(empleados):
    print(empleado)


def registrar_ejecucion(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print("d")
        resultado = funcion(*args, **kwargs)
        return resultado

    return wrapper
