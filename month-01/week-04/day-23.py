# Exceptions
def theory():
    # 1. Exceptions
    """
    numero = int("Hola")  # -> Will raise an exception ValueError
    resultado = 10 / 0  # -> ZeroDivisionError
    """

    # 2. Try + Except
    """ Basic structure
    try:
        # codigo que podria producir un error
    except:
        # que hacer si ocurre el error
    """

    try:
        numero = int(input("Ingresa un numero: "))
    except:
        print("Debes ingresar un numero valido")

    # 3. Better practice: specify the exception
    # Avoid to do this
    try:
        numero = int(input("Numero: "))
    except:
        print("Error")

    # Is better
    try:
        numero = int(input("Numero: "))
    except ValueError:
        print("Debes ingresar un numero valido")

    # Why?
    # Cause you can manage different types of errors in different ways
    try:
        numero = int(input("Numero: "))
        resultado = 100 / numero
    except ValueError:
        print("Debes ingresar un numero")
    except ZeroDivisionError:
        print("No puedes dividir entre cero")

    # 4. as e
    # You can save the info of the exception
    try:
        numero = int("hola")
    except ValueError as e:
        print(e)

    # you can also do
    try:
        numero = int(input("Numero: "))
    except ValueError as error:
        print(f"Ocurrio un error {error}")

    # Few execptions:
    # you can have multiples exceptions
    try:
        numero = int(input("Numero: "))
        resultado = 100 / numero
        print(resultado)
    except ValueError:
        print("Debes ingresar un numero")
    except ZeroDivisionError:
        print("No puedes dividr entre cero")

    # else
    # only execute it if not exception occurred
    try:
        numero = int(input("Numero: "))
    except ValueError:
        print("Numero invalido")
    else:
        print(f"El numero es {numero}")

    """
    try:
        # codigo
    except:
        # error
    else:
        # si todo salio bien
    """

    # finally
    # finally always execute, even if an error occurrs

    try:
        numero = int(input("Numero: "))
    except ValueError:
        print("Numero invalido")
    finally:
        print("Programa terminado")

    # this is usefull to clean resources, close files, conections, etc.'abs

    try:
        archivo = open("datos.txt")
    finally:
        archivo.close()

    # 8. raise
    # raise allows you to make an execption

    edad = -5
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    # we're saying that condition is not allow

    # 9. raise inside a function
    def dividir(a, b):
        if b == 0:
            raise ValueError("El divisor no puede ser 0")
        return a / b

    print(dividir(10, 2))  # -> 5.0
    print(dividir(10, 0))  # ValueError: El divisor no puede ser cero

    # 10. raise + try/except
    def dividir(a, b):
        if b == 0:
            raise ValueError("El divisor no puede ser cero")
        return a / b

    try:
        resultado = dividir(10, 0)
        print(resultado)
    except ValueError as error:
        print(f"Error: {error}")

    # More real example for backend

    # imaging a function to create a user
    def crear_usuario(nombre, edad):
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        if edad < 18:
            raise ValueError("El usuario debe ser mayor de edad")
        return {"nombre": nombre, "edad": edad}

    # after...
    try:
        usuario = crear_usuario("Cesario", 27)
        print(usuario)
    except ValueError as error:
        print(f"Error: {error}")
    # this is a fundamental idea


# theory()


# Exercises
def exercises():
    # level 1. Basics
    try:
        numero = int(input("Numero: "))
        print(f"Numero introducido es {numero}")
    except ValueError as error:
        print(f"Error: {error}")

    # 2. Ask for 2 numbers and divide it - handle ValueError and ZeroDivisionError
    try:
        numero1 = float(input("Numero 1: "))
        numero2 = float(input("Numero 2: "))

        resultado = numero1 / numero2
        print(resultado)
    except ValueError:
        print("Error")
    except ZeroDivisionError:
        print("Can't divide by cero")

    # 3. Convert valor to int if can't handle the error with try/except
    def convertir_entero(valor):
        if not valor:
            raise ValueError("Can't convert value")

        return valor

    print("Convertir valor")
    convertir_entero("dsd")

    # 4. index error
    def obtener_elemento(lista: list, indice: int):
        if indice > len(lista) - 1 or indice < 0:
            raise IndexError("Index out of range")

        return lista[indice]

    print("---Index error exercise---")

    try:
        lista = [1, 2, 3, 4, 5]
        obtener_elemento(lista, 5)
    except IndexError:
        print("Index does not exists")

    # 5. Get users
    def obtener_usuario(usuarios, nombre):
        usuario = next(filter(lambda usuario: usuario == nombre, usuarios), None)
        if not usuario:
            raise ValueError("Users does not exists")

        return usuario

    try:
        usuario = obtener_usuario(["Cesario", "Ana", "Angie"], "Lucia")
        print(usuario)
    except ValueError:
        print("Error al obtener el usuario")

    # Level 2 - else and finally
    # 6. make a programa which ask for a number
    try:
        numero = input("Introduce un numero: ")
    except ValueError:
        print("Error al convertir el numero")
    else:
        print("Numero valido")
    finally:
        print("Programa terminado")


exercises()
