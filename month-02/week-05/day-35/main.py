# from dataclasses import dataclass


# I don't know how to handle private property with data classes and raise exception with init methods
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        if salario < 0:
            raise ValueError("El salario no puede ser negativo")

        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salario = nuevo_salario

    def mostrar_info(self):
        print(f"{self.nombre} - ${self.salario}")

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje

    def salario_anual(self):
        return self.salario * 12


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        print(f"{self.nombre} - Desarrollador - {self.lenguaje} - ${self.salario}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        print(f"{self.nombre} - Gerente - {self.departamento} - ${self.salario}")


empleados = [
    Desarrollador("Cesario", 72000, "Python"),
    Gerente("Jehinsi", 85000, "IT"),
    Desarrollador("Johan", 75000, "C#"),
]

for empleado in empleados:
    empleado.mostrar_info()


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            empleado.mostrar_info()


dev1 = Desarrollador("Cesario", 75000, "Python")
dev2 = Desarrollador("Cedrick", 45000, "JavaScript")
gerente = Gerente("Josue", 80000, "IT")


dev1.aumentar_salario(0.10)
print(dev1.salario)
print(dev1.salario_anual())

empresa1 = Empresa("Nivar Tech")
empresa1.agregar_empleado(dev1)
empresa1.agregar_empleado(dev2)
empresa1.agregar_empleado(gerente)

print(f"\nEmpresa: {empresa1.nombre}\n")

empresa1.mostrar_empleados()

# dev1.salario = -2500
