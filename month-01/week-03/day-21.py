from termcolor import colored

colors = ["yellow", "magenta", "blue", "cyan"]
menu = [
    "1. Mostrar empleados",
    "2. Buscar empleado",
    "3. Filtrar por departamento",
    "4. Salario promedio",
    "5. Empleado con mayor salario",
    "6. Empleados con salario mayor a X",
    "7. Agregar empleado",
    "8. Eliminar empleado",
    "9. Salir",
]

empleados = [
    {"nombre": "Ana", "edad": 25, "salario": 50000, "departamento": "IT"},
    {"nombre": "Carlos", "edad": 32, "salario": 65000, "departamento": "HR"},
    {"nombre": "John", "edad": 28, "salario": 72000, "departamento": "IT"},
    {"nombre": "Maria", "edad": 24, "salario": 48000, "departamento": "Marketing"},
]


def mostrar_empleado(empleado):
    return f"Nombre: {empleado['nombre']} | Edad: {empleado['edad']} | Salario: {empleado['salario']} | Departamento: {empleado['departamento']}"


def mostrar_empleados():
    for empleado in empleados:
        print(mostrar_empleado(empleado))


def buscar_empleado(nombre_empleado):
    empleado = next(
        filter(lambda empleado: empleado["nombre"] == nombre_empleado, empleados), None
    )

    if empleado:
        print(colored("User found!", colors[2]))
        print(mostrar_empleado(empleado))
    else:
        print("🥲 User not found!")


def empleados_departamento(departamento_a_mostrar):
    empleados_por_departamento = list(
        filter(
            lambda empleado: empleado["departamento"] == departamento_a_mostrar,
            empleados,
        )
    )

    for empleado in empleados_por_departamento:
        print(mostrar_empleado(empleado))


def salario_promedio():
    salarios = []
    for empleado in empleados:
        salarios.append(empleado["salario"])

    avg_salary = sum(salarios) / len(salarios)
    print(f"Salario promedio: {avg_salary}")


def empleado_mayor_salario():
    empleado = max(empleados, key=lambda empleado: empleado["salario"])

    print(f"Empleado mayor salario: {mostrar_empleado(empleado)}")


def empleado_salario_por_encima_de():
    try:
        salario = float(input("Salario por encima de: "))
    except ValueError:
        print("Error con el salario introducido")
        return

    empleados_encima_salario = list(
        filter(lambda empleado: empleado["salario"] > salario, empleados)
    )

    if empleados_encima_salario:
        for empleado in empleados_encima_salario:
            print(mostrar_empleado(empleado))
    else:
        print(f"Ninguno gana por encima de {salario}")


def agregar_empleado():
    try:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        salario = float(input("Salario: "))
        departamento = input("Departamento: ")
    except ValueError:
        print("Error con los datos introducidos")
        return

    empleado_nuevo = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
        "departamento": departamento,
    }

    empleados.append(empleado_nuevo)
    print("Empleado agregado existosamente")
    print(mostrar_empleado(empleado_nuevo))


def eliminar_empleado_por_nombre(nombre_empleado):
    empleado_eliminado = None
    for idx, empleado in enumerate(empleados):
        if empleado["nombre"] == nombre_empleado:
            eliminado = empleados.pop(idx)
            empleado_eliminado = eliminado
            break

    if empleado_eliminado:
        print("\nEmpleado eliminado satisfactoriamente")
        print(mostrar_empleado(empleado_eliminado))
    else:
        print("\nEmpleado no encontrado")


while True:
    print(colored("\n--- SISTEMA DE EMPLEADOS ---\n", colors[0]))

    for option in menu:
        print(colored(option, colors[1]))

    user_selection = input(colored("\nSelect an option: ", colors[3]))

    if user_selection == "9":
        break

    if user_selection == "1":
        mostrar_empleados()

    if user_selection == "2":
        nombre_empleado = input("Empleado a buscar por nombre: ")
        buscar_empleado(nombre_empleado)

    if user_selection == "3":
        departamento_a_mostrar = input(
            "De que departamento quiere mostrar los empleados? "
        )
        empleados_departamento(departamento_a_mostrar)

    if user_selection == "4":
        salario_promedio()

    if user_selection == "5":
        empleado_mayor_salario()

    if user_selection == "6":
        empleado_salario_por_encima_de()

    if user_selection == "7":
        agregar_empleado()

    if user_selection == "8":
        nombre_empleado = input("Nombre empleado a eliminar: ")
        eliminar_empleado_por_nombre(nombre_empleado)
