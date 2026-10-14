# Dataclass
class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def __repr__(self):
        return (
            f"Empleado(nombre={self.nombre!r}, "
            f"salario={self.salario!r}, "
            f"departamento={self.departamento!r})"
        )


empleado = Empleado("Cesario", 72_000, "IT")
print(empleado)


from dataclasses import dataclass


@dataclass
class Empleado:
    nombre: str
    salario: float
    departamento: str


empleado = Empleado("Ana", 50_000, "IT")
print(empleado)
print(empleado.nombre)
print(empleado.salario)


# Parametros importantes de @dataclass


# frozen
@dataclass(frozen=True)
class Coordenada:
    x: int
    y: int


punto = Coordenada(10, 20)
print(punto.x)

# punto.x = 30  # Error: FrozenInstanceError

# Es util para representar datos qeu no deberian modificarse despues de crear el objeto


# order
@dataclass(order=True)
class Puntuacion:
    puntos: int


a = Puntuacion(100)
b = Puntuacion(200)

print(a < b)  # True
print(a > b)  # False

# las comparaciones utilizan el orden de los campos

# field()
# permite personalizar determinados campos
from dataclasses import dataclass, field


@dataclass
class Empleado:
    nombre: str
    tareas: list[str] = field(default_factory=list)


ana = Empleado("Ana")
carlos = Empleado("Carlos")

ana.tareas.append("Revisar API")

print(ana.tareas)
print(carlos.tareas)


# Dataclasses en un proyecto backend
@dataclass
class Empleado:
    id: int
    nombre: str
    salario: float
    departamento: str

    def calcular_salario_anual(self) -> float:
        return self.salario * 12


empleado = Empleado(id=1, nombre="Ana", salario=5000, departamento="IT")

print(empleado)
print(empleado.calcular_salario_anual())


# Ejercicios


# Ejercicio 1. Primera dataclass
@dataclass
class Empleado:
    nombre: str
    edad: int
    salario: float


josue = Empleado("Josue", 24, 65000)
moises = Empleado("Moises", 17, 45000)

print(josue)
print(moises)

print(josue.nombre)
josue.salario = 72000
print(josue)


# Ejercicio 2. Metodos personalizados
@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int

    def valor_total_stock(self) -> float:
        return self.precio * self.stock


producto = Producto("Pencil", 25, 10)
print(producto)
print(producto.valor_total_stock())


# Ejercicio 3. Inmutabilidad
@dataclass(frozen=True)
class Configuracion:
    host: str
    puerto: int


config = Configuracion("localhost", 8000)
print(config.host)
print(config.puerto)

# config.puerto = 3000
# El puerto no se puede cambiar porque la clase esta marcada como froze, es decir, no se puede modificar el atributo (en teoria) despues de crear el objeto


# Ejercicio 4. Listas independientes
@dataclass
class Empleado:
    nombre: str
    tareas: list[str] = field(default_factory=list)


cedrick = Empleado("Cedrick")
lidia = Empleado("Lidia")

cedrick.tareas.append("Talk to mom")
cedrick.tareas.append("Clean the house")

print(cedrick.tareas)
print(lidia.tareas)


# Ejercicio 5. Mini proyecto: gestion de empleados
@dataclass
class Empleado:
    id: int
    nombre: str
    salario: float
    departamento: str

    def calcular_salario_anual(self) -> float:
        return self.salario * 12

    def aplicar_aumento(self, porcentaje: float) -> None:
        aumentar = self.salario * porcentaje
        self.salario += aumentar

    def mostrar_info(self):
        print(self)
        print(f"Salario anual: $ {self.calcular_salario_anual():,.2f}")


crismely = Empleado(2, "Crismely", 3500, "IT")
crismely.aplicar_aumento(0.20)
crismely.mostrar_info()
