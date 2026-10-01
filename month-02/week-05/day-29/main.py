# Clases, objetos y atributos
class Empleado:
    pass


empleado1 = Empleado()
empleado2 = Empleado()


class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario


empleado1 = Empleado("Cesario", 27, 45000)
empleado2 = Empleado("Cedrick", 2, 25)


print(empleado1.nombre)
print(empleado2.nombre)


# Ejercicios
# Ejercicio 1. Clase persona con difentes atributos
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad


persona1 = Persona("Cesario", 27, "Tennessee")
persona2 = Persona("Ana", 25, "New York")

print(persona1.nombre, persona1.edad, persona1.ciudad)
print(persona2.nombre, persona2.edad, persona2.ciudad)


# Ejercicio 2. Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


producto1 = Producto("Laptop", 1200, 5)
producto2 = Producto("Mouse", 35, 20)
producto3 = Producto("Keyboard", 80, 10)

print(f"{producto1.nombre} - {producto1.precio} - {producto1.stock}")
print(f"{producto2.nombre} - {producto2.precio} - {producto3.stock}")
print(f"{producto3.nombre} - {producto3.precio} - {producto2.stock}")


# Ejercicio 3. Empleado
class Empleado:
    def __init__(self, nombre, edad, salario, departamento):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento


empleado1 = Empleado("Ana", 25, 50000, "IT")
empleado2 = Empleado("Carlos", 32, 65000, "HR")
empleado3 = Empleado("John", 28, 72000, "IT")
empleado4 = Empleado("Maria", 24, 48000, "Marketing")

print(f"{empleado1.nombre} - {empleado1.departamento} - ${empleado1.salario}")
print(f"{empleado2.nombre} - {empleado2.departamento} - ${empleado2.salario}")
print(f"{empleado3.nombre} - {empleado3.departamento} - ${empleado3.salario}")
print(f"{empleado4.nombre} - {empleado4.departamento} - ${empleado4.salario}")


# Ejercicio 4. Modificar atributos
class Empleado:
    def __init__(self, nombre, edad, salario, departamento):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento


empleado = Empleado("Cesario", 27, 50000, "IT")
print(empleado.salario)
print(empleado.departamento)

empleado.salario = 55000
print(empleado.salario)

empleado.departamento = "Accounting"
print(empleado.departamento)


# Ejercicio 5. Primer mini OOP
class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo


cuenta_cesario = CuentaBancaria("Cesario", 4023324923, 12000)
cuenta_josue = CuentaBancaria("Josue", 4023424254, 5000)

print(cuenta_cesario.titular, cuenta_cesario.numero_cuenta, cuenta_cesario.saldo)
print(cuenta_josue.titular, cuenta_josue.numero_cuenta, cuenta_josue.saldo)
