# __init__ y methods


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")


empleado1 = Empleado("Cesario", 45000)
empleado1.mostrar_info()


# Methods can modify the object
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentar_salario(self, cantidad):
        self.salario += cantidad


empleado = Empleado("Josue", 45000)
print(empleado.salario)
empleado.aumentar_salario(15000)
print(empleado.salario)


# Metodos que retornan valores / not all needs print
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def salario_anual(self):
        return self.salario


empleado = Empleado("Cedrick", 25)
salario = empleado.salario_anual()
print(salario)


# Ejemplo mas completo
class Empleado:
    def __init__(self, nombre, edad, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad
        self.departamento = departamento

    def mostrar_info(self):
        return f"{self.nombre} - {self.edad} - {self.salario} - {self.departamento}"

    def aumentar_salario(self, cantidad):
        self.salario += cantidad

    def es_mayor_de_edad(self):
        return self.edad >= 18


empleado = Empleado("Ana", 25, 50000, "IT")

print(empleado.mostrar_info())
empleado.aumentar_salario(5000)
print(empleado.mostrar_info())
print(empleado.es_mayor_de_edad())


# Ejercicios
# Ejercicio 1.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


persona = Persona("Ana", 25)
persona.saludar()


# Ejercicio 2.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= cantidad

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.saldo}")


cuenta1 = CuentaBancaria("Cesario", 14765)

cuenta1.mostrar_saldo()
cuenta1.depositar(350)
cuenta1.mostrar_saldo()
cuenta1.retirar(12350)
cuenta1.mostrar_saldo()


# Ejercicio 3
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    # Ejercicio 4. Agregar a producto
    def aplicar_descuento(self, descuento):
        total = self.valor_total()
        valor_descuento = total * (descuento / 100)
        return total - valor_descuento


producto = Producto("Laptop", 2400, 2)
print(producto.valor_total())
print(producto.aplicar_descuento(20))


# Ejercicio 5
class Empleado:
    def __init__(self, nombre, edad, salario, departamento):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento

    def mostrar_info(self):
        return f"{self.nombre} - {self.edad} - {self.salario} - {self.departamento}"

    def aumentar_salario(self, cantidad):
        self.salario += cantidad

    def es_mayor_de_edad(self):
        return self.edad >= 18


empleado = Empleado("Cesario", 27, 65000, "IT")
print(empleado.mostrar_info())
empleado.aumentar_salario(2500)
print(empleado.es_mayor_de_edad())
print(empleado.mostrar_info())


# Ejercicio 7.
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


rectangulo = Rectangulo(5, 3)
print(f"Area: {rectangulo.area()}")
print(f"Perimetro: {rectangulo.perimetro()}")


# Ejercicio 8.
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        return f"{self.titulo} - {self.autor} - {self.paginas}"

    def es_largo(self):
        return self.paginas > 300


libro = Libro("Python Basics", "Cesario Nivar", 425)
print(libro.mostrar_info())
print(libro.es_largo())


# Ejercicio 9.
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
        return self.celsius * 1.8 + 32

    def a_kelvin(self):
        return self.celsius + 273.15


temperatura = Temperatura(16)
print(temperatura.a_fahrenheit())
print(temperatura.a_kelvin())


# Ejercicio 10.
class Empleado:
    def __init__(self, nombre, edad, salario, departamento):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento

    def mostrar_info(self):
        return f"{self.nombre} - {self.edad} - {self.salario} - {self.departamento}"

    def aumentar_salario(self, cantidad):
        self.salario += cantidad

    def salario_anual(self):
        return self.salario * 12

    def es_mayor_de_edad(self):
        return self.edad >= 18


def print_empleado_info(empleado):
    print(empleado.mostrar_info())
    empleado.aumentar_salario(5000)
    print(empleado.salario_anual())
    print(empleado.es_mayor_de_edad())
    print(empleado.mostrar_info())


empleado1 = Empleado("Ana", 25, 50000, "IT")
print_empleado_info(empleado1)

empleado2 = Empleado("Cesario", 27, 42000, "HR")
print_empleado_info(empleado2)

empleado3 = Empleado("Luz", 18, 35000, "Marketing")
print_empleado_info(empleado3)
