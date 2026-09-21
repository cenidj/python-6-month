empleados = [
    {"nombre": "Ana", "salario": 50000, "departamento": "IT"},
    {"nombre": "Carlos", "salario": 65000, "departamento": "HR"},
    {"nombre": "John", "salario": 72000, "departamento": "IT"},
]


def agregar_empleado(empleado):
    empleados.append(empleado)


def eliminar_empleado(nombre):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleados.remove(empleado)


def buscar_empleado(nombre):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado
    return None
