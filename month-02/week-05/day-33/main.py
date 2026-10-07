# Polimorfismo
class Empleado:
    def trabajar(self):
        print("El empleado esta trabajando")


class Gerente(Empleado):
    def trabajar(self):
        print("El gerente esta administrando el equipo")


class Desarrollador(Empleado):
    def trabajar(self):
        print("El desarrollador esta escribiendo codigo")


empleado = Empleado()
desarrollador = Desarrollador()
gerente = Gerente()

empleado.trabajar()
desarrollador.trabajar()
gerente.trabajar()

empleados = [Empleado(), Desarrollador(), Gerente()]

for empleado in empleados:
    empleado.trabajar()


def calcular_salario_anual(empleado):
    return empleado.salario * 12


# Ejercicio
class Empleado:
    def trabajar(self):
        print("Empleado trabajando")


class Desarrollador(Empleado):
    def trabajar(self):
        print("Desarrollador creando lineas de codigos")


class Disenador(Empleado):
    def trabajar(self):
        print("Innovando con nuevos disenos")


class Gerente(Empleado):
    def trabajar(self):
        print("Administrando el equipo de trabajo")


empleados = [
    Empleado(),
    Desarrollador(),
    Disenador(),
    Gerente(),
]

for empleado in empleados:
    empleado.trabajar()
