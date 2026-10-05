# Herencia
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"{self.nombre} - ${self.salario}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def dirigir_reunion(self):
        print(f"{self.nombre} esta dirigiendo una reunion")


gerente = Gerente("Cesario", 85000, "IT")
gerente.mostrar_info()
gerente.dirigir_reunion()


# Method overriding
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print("El empleado esta trabajando")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguage):
        super().__init__(nombre, salario)
        self.lenguage = lenguage

    def trabajar(self):
        print("El desarrollador esta programando")


empleado = Empleado("Lucas", 25000)
empleado.trabajar()
desarrollador = Desarrollador("Cesario", 45000, "Python")
desarrollador.trabajar()


# isinstance()
dev = Desarrollador("Cedrick", 65000, "Python")

print(isinstance(dev, Desarrollador))
print(isinstance(dev, Empleado))

# issubclass()
print(issubclass(Desarrollador, Empleado))
print(issubclass(Empleado, Desarrollador))

# Ejercicios


# Ejercicio 1.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Burk... burk...")


class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: Woof!")


bobi = Perro("Bobi")
bobi.hacer_sonido()


# Ejercicio 2
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"{self.marca} - {self.modelo}")


class Auto(Vehiculo):
    def calcular_velocidad(self, distancia, tiempo):
        try:
            velocidad = distancia / tiempo
            print(f"La velocidad del auto es: {velocidad}")
        except ZeroDivisionError:
            raise ZeroDivisionError("No se puede dividir entre cero")
        except ValueError:
            raise ValueError("Error al calcular la velocidad")


class Motocicleta(Vehiculo):
    def calcular_distancia(self, velocidad, tiempo):
        try:
            distancia = velocidad * tiempo
            print(f"La distancia restante es: {distancia}")
        except ValueError:
            raise ValueError("Error al calcular la distancia")


auto = Auto("Ford", "Focus")
auto.calcular_velocidad(12, 30)

moto = Motocicleta("Honda", "68")
moto.calcular_distancia(25, 30)


# Ejercicio 3 and ejercicio 4 (overriding)
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"{self.nombre} - {self.salario}")

    def trabajar(self):
        print(f"{self.nombre} empezo a trabajar con un salario de {self.salario}")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguage = lenguaje

    def programar(self):
        print(f"{self.nombre} esta desarrollando en: {self.lenguage}")

    def trabajar(self):
        print(f"{self.nombre} devenga un salario de {self.salario}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def dirigir_reunion(self):
        print(f"{self.nombre} tiene una reunion programada con {self.departamento}")

    def trabajar(self):
        print(f"{self.nombre} es gerente y gana {self.salario}")


dev = Desarrollador("Cesario", 72000, "Python")
gerente = Gerente("Cedrick", 60000, "IT")

dev.mostrar_info()
dev.programar()
gerente.mostrar_info()
gerente.dirigir_reunion()


# Ejercicio 5. isinstance() & issubclass()
print(issubclass(Desarrollador, Empleado))
print(isinstance(dev, Desarrollador))


# Ejercicio 6.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print("Trabajando...")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguage = lenguaje

    def trabajar(self):
        print(f"Trabjando como desarrollador en {self.lenguage}")

    def subir_cambios(self):
        print("Subiendo los cambios a Github")


class Disenador(Empleado):
    def __init__(self, nombre, salario, herramienta):
        super().__init__(nombre, salario)
        self.herramienta = herramienta

    def trabajar(self):
        print(f"Diseñando algo nuevo con {self.herramienta}")

    def mostrar_diseno(self):
        print("Mostrando el diseño al product manager")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def trabajar(self):
        print(f"Gerente de {self.departamento}")

    def pautar_reunion(self):
        print("Planeando una reunion")


dev = Desarrollador("Cesario", 72000, "Python")
disenador = Disenador("Cedrick", 45000, "Adobe")
gerente = Gerente("Josue", 80000, "HR")


dev.trabajar()
disenador.trabajar()
gerente.trabajar()


dev.subir_cambios()
disenador.mostrar_diseno()
gerente.pautar_reunion()
