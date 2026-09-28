import json

menu = [
    "1. Mostrar empleados",
    "2. Buscar empleado",
    "3. Agregar empleado",
    "4. Eliminar empleado",
    "5. Filtrar por departamento",
    "6. Filtrar por salario",
    "7. Ordenar empleados",
    "8. Mostrar salario promedio",
    "9. Mostrar salario más alto",
    "10. Guardar empleados",
    "11. Salir",
]


def create_employees_file(filename):
    with open(filename, "w") as file:
        json.dump([], file, indent=4)


def load_employees(filename):
    with open(filename, "r") as file:
        employees = json.load(file)

    return employees


def add_employee(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
