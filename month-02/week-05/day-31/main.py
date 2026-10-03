# Encapsulation and @properties


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
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


empleado = Empleado("Cesario", 45000)
empleado.mostrar_info()
empleado.salario = 65000
empleado.mostrar_info()


class Empleado:
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self._salario_mensual = salario_mensual

    @property
    def salario_anual(self):
        return self._salario_mensual * 12


empleado = Empleado("Cedrick", 4500)
print(empleado.salario_anual)
