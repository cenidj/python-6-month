empleados = [
    {"nombre": "Ana", "salario": 50000, "departamento": "IT"},
    {"nombre": "Carlos", "salario": 65000, "departamento": "HR"},
    {"nombre": "John", "salario": 72000, "departamento": "IT"},
    {"nombre": "Maria", "salario": 48000, "departamento": "Marketing"},
]


def empleados_por_departamento(empleados, departamento):
    empleados_departamento = list(
        filter(lambda empleado: empleado["departamento"] == departamento, empleados)
    )

    return empleados_departamento
