# Scope
nombre = "Cesario"  # Global


def saludar():
    mensaje = "Hola"

    print(nombre)
    print(mensaje)


saludar()

print(nombre)  # ✅
# print(mensaje) # ❌
# nombre exists in global scope while mensaje only in saludar()

# Local scope
# Every time you define a variable inside a function, normally belongs to that function


def calcular():
    total = 100
    print(total)


calcular()

# print(total) # ❌

# Global Scope
# A variable define outside a function is in the global scope
precio = 100


def mostrar_precio():
    print(precio)


mostrar_precio()

# the function can read precio, but be carefull when modifiing it!
contador = 0


def incrementar():
    # contador = (contador + 1)
    # produces an error because python consider contador as local variable
    pass


incrementar()

# to modify global exists `global`
contador = 0


def incrementar():
    global contador
    contador += 1


incrementar()
print(contador)  # 1


# Not recommend it to use global in backend. Normally we avoid this


# Function inside functions
def externa():
    def interna():
        print("Soy la funcion interna")

    interna()


externa()

# interna() only exists inside externa()


def saludar(name):
    def mensaje():
        return f"Hello {name}"

    return mensaje()


print(saludar("Cesario"))

# internal function can access variables in parent function


# Exercises
# 1. Local Scope
def mostrar_usuario():
    nombre_1 = "Cesario"
    edad_1 = 27

    print(nombre_1)
    print(edad_1)


mostrar_usuario()

# print(nombre_1) # ❌ nombre_1 is not in the global scope (not defined)


# Exercise 2 - Global scope
name = "Cesario"


def mostrar_usuario():
    print(f"Hello {name}")


mostrar_usuario()


# Exercise 3 - GLobal vs local
def cambiar_nombre():
    name = "Ana"
    print(name)


cambiar_nombre()
print(name)  # Will print "Cesario"


# Exercise 4.
def calcular_total():
    def sumar():
        return 100 + 50

    return sumar()


print(calcular_total())


# Exercise 5. Inside function using external variable
def crear_saludo(name):
    def mensaje():
        print(f"Hola {name}")

    mensaje()


crear_saludo("Cesario")


# Exercise 6. Mini challenge
def calcular_precio(precio, impuesto):
    def aplicar_impuesto():
        return precio + (precio * impuesto)

    return aplicar_impuesto()


print(calcular_precio(100, 0.07))
