"""Día 24
* Leer/escribir archivos
* JSON
* CSV
"""

# Leer archivos
with open("usuarios.txt", "r") as archivo:
    # contenido = archivo.read()
    # contenido = archivo.readline()
    contenido = archivo.readlines()


print(contenido)

# with open("usuarios.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())

# Escribir archivos
with open("usuarios.txt", "w") as archivo:
    archivo.write("Ana\n")
    archivo.write("Carlos\n")
    archivo.write("John\n")

# w -> Sobreescribe el contenido existente

# Agregar contenido
# para agregar sin borrar lo anterior utilizamos a
with open("usuarios.txt", "a") as archivo:
    archivo.write("Maria\n")
# a = append

# Modos importantes
"""
"r" -> Leer
"w" -> Escribir/sobreescribir
"a" -> Agregar
"r+" -> Leer + escribir
"""

# Manejo de excepciones
try:
    with open("usuarios", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
# also
except PermissionError:
    print("No tienes permisos para acceder al archivo")

# JSON. La parte mas importante para backend
# {"nombre": "Cesario", "edad": 27, "rol": "developer"}

import json

# Python -> JSON
usuario = {"nombre": "Cesario", "edad": 27, "rol": "developer"}

with open("usuario.json", "w") as archivo:
    json.dump(usuario, archivo, indent=4)

# json.dump() convierte el objeto python y lo escribe directamente en el archivo

# JSON -> Python
with open("usuario.json", "r") as archivo:
    usuario = json.load(archivo)
print(usuario)
print(usuario["nombre"])

# json.load() hace el proceso contrario

# La idea fundamental
"""
python        json
dict    ->   object
list    ->   array
str     ->   string
int     ->   number
float   ->   number
True    ->   true
False   ->   false
None    ->   null
"""

# dump vs dumps
"""
dump
python -> archivo
json.dump(datos, archivo)

dumps
python -> string
json_string = json.dumps(datos)

y al reves
load
archivo -> python
datos = json.load(archivo)

loads
string -> python
datos = json.loads(json_string)

# remember
dump/load -> archivos
dumps/loads -> strings

"""

# CSV - comma-separated values
"""csv
nombre,edad,departamento,salario
Ana,25,IT,50000
Carlos,32,HR,65000
John,28,IT,72000
Maria,24,Marketing,48000
"""

# Python tiene un modulo especifico
import csv

with open("empleados.csv", "r") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)

# los valores vienen como strings

# csv.DictReader
with open("empleados.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for empleado in lector:
        print(empleado)

        # print(empleado["nombre"])

# Escribir CSV

empleados = [
    ["Ana", 25, "IT", 50000],
    ["Carlos", 32, "HR", 65000],
    ["John", 28, "IT", 72000],
]

with open("empleados.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["nombre", "edad", "departamento", "salario"])
    escritor.writerows(empleados)


# Ejercicios

# Ejercicio 1. crear archivo
# crea notas.txt y escribe
with open("notas.txt", "w") as archivo:
    archivo.write("Python\n")
    archivo.write("FastApi\n")
    archivo.write("PostgreSQL\n")
    archivo.write("Docker\n")
    archivo.write("AWS\n")


# Ejercicio 2. Leer archivo
# lee notas.txt y muestra todo su contenido
try:
    with open("notas.txt", "r") as archivo:
        contenido = archivo.read()

    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado")
except PermissionError:
    print("No tiene privilegios")

# Ejercicio 3. Lineas
try:
    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("No encontrado")

# Ejercicio 4. Agregar
try:
    with open("notas.txt", "a") as archivo:
        archivo.write("Github\n")

    with open("notas.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado")


# Ejercicio 5. FileNotFoundError
try:
    with open("archivo_que_no_existe.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.\n")

# Ejercicio 6. JSON basico
usuario = {"nombre": "Cesario", "edad": 27, "lenguaje": "Python"}

with open("usuario2.json", "w") as archivo:
    json.dump(usuario, archivo)

# Ejercicio 7. Leer JSON
with open("usuario2.json", "r") as archivo:
    usuario = json.load(archivo)
    for key, value in usuario.items():
        print(f"{key}: {value}")

# Ejercicio 8. Lista de usuarios
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 32},
    {"nombre": "John", "edad": 28},
]

with open("usuarios.json", "w") as archivo:
    json.dump(usuarios, archivo)

# Ejercicio 9. Leer lista JSON
with open("usuarios.json", "r") as archivo:
    usuarios = json.load(archivo)
    for usuario in usuarios:
        print(usuario["nombre"])

# Ejercicio 10. Modificar JSON
with open("usuarios.json", "r") as archivo:
    usuarios = json.load(archivo)
with open("usuarios.json", "w") as archivo:
    usuarios.append({"nombre": "Maria", "edad": 24})
    json.dump(usuarios, archivo, indent=4)

# Ejercicio 11. CSV
empleados = [
    ["Ana", 25, "IT", 50000],
    ["Carlos", 32, "HR", 65000],
    ["John", 28, "IT", 72000],
    ["Maria", 24, "Marketing", 48000],
]

with open("empleados.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["nombre", "edad", "departamento", "salario"])
    escritor.writerows(empleados)

with open("empleados.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for linea in lector:
        print(linea)

# Ejercicio 12. CSV+DictReader
with open("empleados.csv", "r") as archivo:
    empleados = csv.DictReader(archivo)

    for empleado in empleados:
        print(f"{empleado['nombre']} trabaja en {empleado['departamento']}")

# Ejercicio 13. Filtrar CSV
# usando DictReader, muestra unicamente los empleados de: IT
with open("empleados.csv", "r") as archivo:
    empleados = csv.DictReader(archivo)

    for empleado in empleados:
        if empleado["departamento"] == "IT":
            print(f"{empleado['nombre']} es de IT")

# Ejercicio 14. Salario
# Usando el CSV, encuentra el empleado con el salario mas alto.
with open("empleados.csv", "r") as archivo:
    empleados = csv.DictReader(archivo)

    empleado_salario_alto = max(
        empleados, key=lambda empleado: int(empleado["salario"])
    )
    print(f"Empleado con salario mas alto: {empleado_salario_alto['nombre']}")


# Sistema de empleados
print("\n=== Sistema de empleados ===\n")
menu = [
    "1. Mostrar empleados",
    "2. Buscar empleado",
    "3. Agregar empleado",
    "4. Eliminar empleado",
    "5. Salir",
]

# empleados.json
while True:
    for option in menu:
        print(option)

    selection = input("\nSelect a menu option: ")

    if selection == "5":
        break

    if selection == "1":
        print("\nListado de empleados:\n")
        try:
            with open("empleados.json", "r") as file:
                empleados = json.load(file)
                for empleado in empleados:
                    print(f"{empleado['nombre']}.")
                print(" ")  # Salto de linea
        except FileNotFoundError:
            print("\nEl archivo no existe!\n")
        except PermissionError:
            print("\nNo tienes permisos para este archivo!\n")

    if selection == "3":
        try:
            nombre = input("Nombre: ").strip()

            if len(nombre) < 3:
                raise ValueError("El nombre es muy corto!")

            edad = int(input("Edad: "))

            with open("empleados.json", "r") as file:
                empleados = json.load(file)

            with open("empleados.json", "w") as file:
                empleados.append({"nombre": nombre, "edad": edad})
                json.dump(empleados, file)

        except ValueError as error:
            print(f"\nError: {error}\n")

        except FileNotFoundError:
            with open("empleados.json", "w") as file:
                json.dump([], file)

            print("El archivo no existia, creado recientemente. Intentalo de nuevo.")

    if selection == "2":
        print("\nBuscar empleado:\n")

        try:
            nombre = input("Nombre: ").strip().lower()

            with open("empleados.json", "r") as file:
                empleados = json.load(file)
                encontrado = False
                for empleado in empleados:
                    if empleado["nombre"].lower() == nombre:
                        encontrado = True
                        break

                if encontrado:
                    print(f"Empleado encontrado: {nombre}")
                else:
                    print("Empleado no encontrado.")

        except ValueError as error:
            print(f"Error: {error}")

        except FileNotFoundError:
            print("Crear archivo. El archivo no existe. ")

    if selection == "4":
        try:
            nombre = input("Nombre: ").strip().lower()

            with open("empleados.json", "r") as file:
                empleados = json.load(file)
                encontrado = None
                for index, empleado in enumerate(empleados):
                    if empleado["nombre"].lower() == nombre:
                        encontrado = index
                        break

                if encontrado:
                    empleados.pop(index)
                    with open("empleados.json", "w") as file:
                        json.dump(empleados, file)

                    print("Empleado eliminado satisfactoriamente!")
                else:
                    print("Empleado no encontrado!")

        except ValueError as error:
            print(f"Error: {error}")
