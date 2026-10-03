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


# Ejercicios
# Ejercicio 1. Cuenta bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    # Ejercicio 2. Permitir un setter en saldo
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")

        self._saldo = nuevo_saldo


# Ejercicio 3. Temperatura
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 1.8 + 32


temperatura = Temperatura(25)
print(temperatura.fahrenheit)


# Ejercicio 4.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self._precio = nuevo_precio


producto = Producto("Laptop", 2100)
print(producto.precio)
producto.precio = 2400


# Ejercicio 5.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @property
    def salario_anual(self):
        return self.salario * 12

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo")

        self._salario = nuevo_salario


empleado = Empleado("Cesario", 55000)
print(empleado.salario)
print(empleado.salario_anual)

empleado.salario = 68000
