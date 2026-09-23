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

        return int(valor)

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
        numero = int(input("Introduce un numero: "))

    except ValueError:
        print("Error al convertir el numero")
    else:
        print("Numero valido")
    finally:
        print("Programa terminado")

    # 7. ZeroDivision
    def dividir(a, b):
        if b == 0:
            raise ValueError("Can't divide by cero")
        return a / b

    try:
        resultado = dividir(10, 0)
        print(resultado)
    except ValueError as error:
        print(error)

    # 8.
    def validar_edad(edad):
        if edad < 0:
            raise ValueError("Edad invalida")
        elif edad < 18:
            raise ValueError("Menor de eadd")
        else:
            return "Edad validad"

    try:
        validar_edad(27)
    except ValueError as e:
        print(f"Error: {e}")

    # 9.
    def retirar_saldo(saldo, cantidad):
        if cantidad <= 0:
            raise ValueError("No tiene balance")
        elif cantidad > saldo:
            raise ValueError("No tiene balance suficiente")

    try:
        retirar_saldo(1442, 971)
    except ValueError as e:
        print(f"Error: {e}")

    # 10.
    def calcular_promedio(numeros: list):
        if len(numeros) == 0:
            raise ValueError("Lista vacia")

        promedio = sum(numeros) / len(numeros)

        return promedio

    try:
        calcular_promedio([12, 14, 23, 15, 17])
    except ValueError as e:
        print(f"Error: {e}")

    # Level 3 - Backend thinking
    # 11.
    def buscar_empleado(empleados, nombre):
        empleado = next(filter(lambda empleado: empleado == nombre, empleados), None)

        if not empleado:
            raise ValueError("Empleado no encontrado")

        return empleado

    try:
        empleado = buscar_empleado(
            ["Cesario", "Angie", "Francis", "Jorge", "Daniel", "Dony"], "Cesario"
        )
        print(f"El empleado del mes es: {empleado}")
    except ValueError as e:
        print(f"Error {e}")

    # 12.
    def agregar_empleado(empleados, empleado):
        if not empleado["nombre"]:
            raise ValueError("Nombre es obligatorio")
        elif empleado["salario"] <= 0:
            raise ValueError("Salario debe ser mayor que cero")
        elif not empleado["departamento"]:
            raise ValueError("El departamento es requerido")

        empleados.append(empleado)
        print("Empleado agregado satisfactoriamente!")
        print(empleados)

    agregar_empleado(
        [
            {"nombre": "Cesario", "salario": 40000, "departamento": "IT"},
        ],
        {"nombre": "Carlos", "salario": 3900, "departamento": "IT"},
    )

    # 13.
    def calcular_salario_anual(salario_mensual):
        if salario_mensual < 0:
            raise ValueError("Salario debe ser mayor que 0")

        return salario_mensual * 12

    try:
        salario_anual = calcular_salario_anual(4000)
        print(salario_anual)
    except ValueError:
        print("Error el salario no debe ser menor que 0")

    # 14. Mini proyecto
    print("\n--- Empleados ---\n")
    menu = [
        "1. Agregar empleado",
        "2. Buscar empleado",
        "3. Mostrar empleados",
        "4. Salir",
    ]

    empleados = []

    while True:
        for option in menu:
            print(f"{option}")

        try:
            select_option = int(input("\nSelecciona una opcion del menu: "))

            if select_option > 4 or select_option <= 0:
                raise ValueError("Opcion no valida")

            if select_option == "4":  # 4. Salir
                break

            if select_option == "1":  # 1. Agregar empleado
                nombre = input("Nombre empleado: ").strip()
                if len(nombre) < 3:
                    raise ValueError("El nombre no es correcto")

                empleados.append(nombre)
                print(empleados)

            if select_option == "2":  # 2. Buscar empleado
                nombre = input("Nombre empleado").strip()
                index = empleados.index(nombre)
                return empleados[index]

            if select_option == "3":  # 3. Mostrar empleados
                for empleado in empleados:
                    print(empleado)

        except ValueError as error:
            print(f"Error: {error}")

        except IndexError:
            print("Empleado invalido")


exercises()
