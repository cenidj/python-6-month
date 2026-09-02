import random

# Day 6 - 20 exercises combining everything


# Exercise 1. Calculadora basica
def exercise1():
    print("\n== Calculadora basica ==\n")
    num1 = float(input("Input first number: "))
    num2 = float(input("Input second number: "))

    suma = round(num1 + num2, 2)
    rest = round(num1 - num2, 2)
    product = round(num1 * num2, 2)
    division = round(num1 / num2, 2)

    print(f"La suma es igual a {suma}")
    print(f"La resta es igual a {rest}")
    print(f"La multiplicacion es igual a {product}")
    print(f"La division es igual a {division}")


# Exercise 2. Numero par o impar
def exercise2():
    print("\n== Numero par o impar ==\n")
    num = int(input("Input the number: "))
    print("Es par" if num % 2 == 0 else "Es impar")


# Exercise 3. Mayor de tres numeros
def exercise3():
    print("\n== Mayor de tres numeros ==\n")
    numeros = ()
    for i in range(1, 4):
        num = int(input(f"Introduce numero {i}: "))
        numeros = numeros + (num,)  # Tuples are inmutable (way to add items)

    max_number: int = 0

    for i in numeros:
        if i > max_number:
            max_number = i

    print(f"Numero mayor: {max_number}")


# Exercise 4. Conversor de temperatura
def exercise4():
    print("\n== Conversor de temperatura ==\n")
    temp_celsius = float(input("Introduce la temperatura en Celsius: "))

    temp_farenheit = temp_celsius * 9 / 5 + 32
    print(f"{temp_celsius} celsius en farenheit es {temp_farenheit}")


# Exercise 5. Contador de vocales
def exercise5():
    print("\n== Contador de vocales ==\n")
    text = input("Introduce una palabra o frase: ")
    vocales = ["a", "e", "i", "o", "u"]
    count = 0

    for i in text:
        if i in vocales:
            count += 1
    print(count)


# Exercise 6. Tabla de multiplicar
def exercise6():
    print("\n== Tabla de multiplicar ==\n")
    num = int(input("Introduce un numero: "))
    for i in range(1, 11):
        product = num * i
        print(f"{i} x {num} = {product}")


# Exercise 7. Suma de numeros
def exercise7():
    print("\n== Suma de numeros ==\n")
    numeros = list()
    total_numeros = 5
    for i in range(1, total_numeros + 1):
        num = int(input(f"Introduce numero {i}: "))
        numeros.append(num)

    suma = 0

    for num in numeros:
        suma += num
    print(f"La suma de los numeros es igual a {suma}")


# Exercise 8. Promedio de notas
def exercise8():
    print("\n== Promedio de notas ==\n")
    notas = list()
    total_notas = int(input("Introduce cuantas notas en total: "))
    for i in range(1, total_notas + 1):
        nota = int(input(f"Nota {i}: "))
        notas.append(nota)

    suma_notas = sum(notas)
    promedio = suma_notas / total_notas

    print(f"Promedio: {promedio}")
    print("Aprobado" if promedio >= 70 else "Reprobado")


# Exercise 9. Buscar un elemento
def exercise9():
    print("\n== Buscar un elemento ==\n")
    nombres = ["Cesario", "Cedrick", "Josue",
               "Moises", "Lidia", "Kenia", "Cristina"]
    nombre = input("Introduce un nombre: ")

    if nombre in nombres:
        print(f"El nombre {nombre} si esta en la lista")
    else:
        print(f"El nombre {nombre} no esta en la lista")


# Exercise 10. Eliminar duplicados
def exercise10():
    print("\n== Eliminar duplicados ==\n")
    numeros_repetidos = [2, 3, 5, 2, 4, 6, 5, 3, 7, 1]
    numeros_unicos = set(numeros_repetidos)

    print(numeros_repetidos)
    print(numeros_unicos)


# Exercise 11. Contador de palabras
def exercise11():
    print("\n== Contador de palabras ==\n")
    frase = input("Introduce una frase: ")

    palabras = frase.split(None)
    print(f"La frase {frase} contiene {len(palabras)} palabras")


# Exercise 12. Diccionario de contactos
def exercise12():
    print("\n== Diccionario de contactos ==\n")
    contactos = {
        "Cesario": "865-247-3415",
        "Ronaldo": "865-240-7051",
        "Erika": "570-233-7513",
        "Jorge": "865-232-0993",
        "Amaurys": "865-804-8916",
        "Josue": "809-773-0273",
        "Kenia": "829-362-9877",
        "Tony": "809-850-6599",
        "Chulo": "829-532-9542",
        "Yordy": "667-464-1057",
        "Ana Erika": "865-202-1189",
        "Benjamin": "646-221-8078"
    }

    persona = input("Buscar a: ")
    numero = contactos.get(persona)
    print(numero)


# Exercise 13. Inventario
def exercise13():
    print("\n == Inventario ==\n")
    inventario = {
        "Arroz": "22",
        "Salami": "15",
        "Huevos": "9",
        "Jugo": "7",
        "Aceite": "5"
    }

    menu = ["1. Consultar producto", "2. Agregar unidades",
            "3. Mostrar inventario", "4. Salir"]

    for i in menu:
        print(i)

    selecion = input("\nSeleciona una opcion del menu: ")

    while selecion != "4":
        if selecion == "3":
            for key, value in inventario.items():
                print(f"{key} - ${value}")
        elif selecion == "2":
            nombre_producto = input("Introduce nombre producto: ")
            precio_producto = input("Introduce precio producto: ")
            inventario[nombre_producto] = precio_producto
        elif selecion == "1":
            termino_busqueda = input("Producto a buscar? ")
            resultado_busqueda = inventario.get(termino_busqueda)
            print(f"{termino_busqueda} - ${resultado_busqueda}")

        selecion = input("\nSeleciona una opcion del menu: ")


# Exercise 14. Funcion para saber si es primo
def exercise14(numero: int) -> str:
    if numero <= 1:
        return "No es primo"

    divisibles = list()

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisibles.append(i)

    return "Es primo" if len(divisibles) == 2 else "No es primo"


# Exercise 15. Numeros primos
def exercise15():
    print("\n== Numeros primos ==\n")
    for i in range(1, 101):
        print(f"{i} {exercise14(i)}")


# Exercise 16. Adivina el numero
def exercise16():
    print("\n== Adivina el numero ==\n")

    aleatorio = random.randrange(1, 100)
    num = int(input("Que numero crees que es? "))

    while num != aleatorio:
        if num > aleatorio:
            print("Debes bajar")
        else:
            print("Debes subir")
        num = int(input("Intentalo de nuevo: "))

    print(f"Correcto el numero aleatorio es el {num}")


# Exercise 17. Cajero automatico
def exercise17():
    print("\n== Cajero automatico ==\n")
    saldo = 1000.00

    menu = ["1. Consultar saldo", "2. Depositar", "3. Retirar", "4. Salir"]

    for opcion in menu:
        print(opcion)

    selecion = input("\nSeleciona una opcion del menu: ")

    while selecion != "4":
        if selecion == "1":
            print("Saldo actual es:", saldo)
        elif selecion == "2":
            depositar = float(input("Introduzca cantidad a depositar: "))
            saldo += depositar
            print(
                f"Deposito de {depositar} satisfactorio, saldo actual es {saldo}")
        elif selecion == "3":
            retirar = float(input("Introduzca cantidad a retirar: "))
            if retirar > saldo:
                print("Error! No puede retirar mas de la cantidad disponible")
            else:
                saldo -= retirar
                print("Retiro satisfactorio! Saldo actual: ", saldo)
        selecion = input("\nSelecciona una opcion del menu: ")


# Exercise 18. Sistema de calificaciones
def exercise18():
    print("\n== Sistema de calificaciones ==\n")
    alumnos = {
        "Ana": [8, 9, 10],
        "Luis": [6, 7, 8],
        "Pedro": [4, 5, 6]
    }

    for alumno, calificaciones in alumnos.items():
        promedio = sum(calificaciones) / len(calificaciones)
        estado = "Aprobado" if promedio > 5 else "Reprobado"
        print(f"{alumno} tiene un promedio de {promedio} y es {estado}")


# Exercise 19. Mini juego: Piedra, papel o tijera
def exercise19():
    print("\n== Mini juego: Piedra, papel o tijera ==\n")
    opciones = ["1. Piedra", "2. Papel", "3. Tijera"]
    cpu_victories = 0
    user_victories = 0

    for opcion in opciones:
        print(opcion)

    user_selecion = input("Seleccione una opcion: ")
    cpu_selecion = str(random.randrange(1, 3))

    while cpu_victories < 2 or user_victories < 2:
        if user_selecion == "1":
            if cpu_selecion == "2":
                cpu_victories += 1
                print("CPU win 🥳")

            if cpu_selecion == "3":
                user_victories += 1
                print("User win 🥳")

        if user_selecion == "2":
            if cpu_selecion == "1":
                user_victories += 1
                print("User win 🥳")

            if cpu_selecion == "3":
                cpu_victories += 1
                print("CPU win 🥳")

        if user_selecion == "3":
            if cpu_selecion == "1":
                cpu_victories += 1
                print("CPU win 🥳")

            if cpu_selecion == "2":
                user_victories += 1
                print("User win 🥳")

        if user_selecion == cpu_selecion:
            print("Tie")

        print("*** Siguiente juego ***")
        print(f"CPU Victories: {cpu_victories}")
        print(f"User Victories: {user_victories}")
        user_selecion = input("Seleccione una opcion: ")
        cpu_selecion = str(random.randrange(1, 3))

    if cpu_victories == 3:
        print("CPU win the championship 🏆")
    else:
        print("You win the championship 🏆")


# Exercise 20. Proyecto final - Sistema de gestion de estudiantes
def exercise20():
    print("\n===== GESTION DE ESTUDIANTES =====\n")
    menu = [
        "1. Agregar estudiante",
        "2. Mostrar etudiantes",
        "3. Buscar estudiante",
        "4. Agregar nota",
        "5. Mostrar promedio",
        "6. Mostrar aprobado/reprobado",
        "7. Eliminar estudiante",
        "8. Salir"
    ]

    def mostrar_menu():
        for opcion in menu:
            print(opcion)

    mostrar_menu()

    estudiantes = {
        "Luis": [5, 6, 8],
        "Carlos": [6, 9, 10]
    }

    user_selecion = input("\nSeleciona una opcion del menu: ")

    def agregar_estudiante():
        nombre_estudiante = input("Introduce el nombre agregar: ")
        nota_estudiante = int(input("Introduce la nota: "))
        estudiantes[nombre_estudiante].append(nota_estudiante)

    def mostrar_estudiantes():
        for estudiante, nota in estudiantes.items():
            print(f"{estudiante} - {nota}")

    def buscar_estudiante():
        nombre_estudiante = input("Introduzca el nombre estudiante: ")
        notas_estudiante = estudiantes.get(nombre_estudiante)
        if notas_estudiante != None:
            print(f"{nombre_estudiante} - {notas_estudiante}")
        else:
            print("Estudiante no encontrado!")

    def agregar_nota():
        nombre_estudiante = input("Introduzca el nombre del estudiante: ")
        nota_estudiante = int(input("Introduzca la nota: "))
        estudiantes[nombre_estudiante].append(nota_estudiante)

    def obtener_promedio(notas: list) -> float:
        promedio = sum(notas) / len(notas)
        return promedio

    def mostrar_promedio():
        for estudiante, notas in estudiantes.items():
            promedio = obtener_promedio(notas)
            print(f"{estudiante} - promedio notas: {promedio}")

    def mostrar_aprobado_reprobado():
        for estudiante, notas in estudiantes.items():
            promedio = obtener_promedio(notas)
            if promedio > 5:
                print(f"{estudiante}: Aprobado")
            else:
                print(f"{estudiante}: Reprobado")

    def eliminar_estudiante():
        nombre_estudiante = input("Introduzca el nombre del estudiante: ")
        estudiantes.pop(nombre_estudiante)

    while user_selecion != "8":
        if user_selecion == "1":
            agregar_estudiante()
        elif user_selecion == "2":
            mostrar_estudiantes()
        elif user_selecion == "3":
            buscar_estudiante()
        elif user_selecion == "4":
            agregar_nota()
        elif user_selecion == "5":
            mostrar_promedio()
        elif user_selecion == "6":
            mostrar_aprobado_reprobado()
        elif user_selecion == "7":
            eliminar_estudiante()
        else:
            print("Opcion no reconocida, intentlo de nuevo!")

        # mostrar_menu()
        user_selecion = input("\nSeleciona una opcion del menu: ")


exercise20()
