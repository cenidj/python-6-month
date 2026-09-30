import logging

from utils import employees_filename, validate_new_employee

from employees import (
    add_employee,
    create_employees_file,
    load_employees,
    replace_employees_data,
)

logger = logging.getLogger(__name__)


def show_menu(menu):
    for option in menu:
        print(option)


def show_employee_data(employee):
    print(
        f"{employee['name']}\nEdad: {employee['age']}\nSalario: {employee['salary']}\nDepartamento: {employee['department']}\n------------------------------------------\n"
    )


def mostrar_empleados():
    try:
        print("\n")
        logger.info("Opening employees.json data ")
        employees = load_employees(employees_filename)

        if not employees:
            print("No employees!")
            logger.info("No employees registered.")
        else:
            for employee in employees:
                show_employee_data(employee)

    except FileNotFoundError:
        create_employees_file(employees_filename)

        print("No employees found!")
        logger.warning("No employees found, file didn't exist")
        logger.info("Employees data (employees.json) file just created!")
    except PermissionError:
        logger.warning("Not enough permission")
        print("Not permission")


def buscar_empleado():
    employee_input = input("Empleado a buscar: ").strip()
    try:
        employees = load_employees(employees_filename)

        for employee in employees:
            if employee["name"].lower() == employee_input.lower():
                show_employee_data(employee)
                logger.info(f"Empleado encontrado: {employee_input}")
                return

        print("Employee not found")
        logger.warning(f"Empleado no encontrado: {employee_input}")

    except FileNotFoundError:
        create_employees_file(employees_filename)
        print("Employee not found")

        logger.warning(f"Employee {employee_input} not found")


def agregar_empleado():
    new_employee = validate_new_employee()
    employees = load_employees(employees_filename)
    employees.append(new_employee)

    add_employee(employees_filename, employees)

    print("Empleado agregado correctamente")
    logger.info(f"Empleado agregado correctamente: {new_employee['name']}")


def eliminar_empleado():
    employee_name = input("Nombre: ").strip()
    employees: list = load_employees(employees_filename)

    empleado_eliminado = None

    for index, employee in enumerate(employees):
        if employee["name"].lower() == employee_name.lower():
            employees.pop(index)
            empleado_eliminado = employee

    if empleado_eliminado:
        replace_employees_data(employees_filename, employees)
        print("Empleado eliminado correctamente.")
        logger.info(f"Empleado: {employee_name} eliminado correctamente")
    else:
        print("Empleado no encontrado")
        logger.warning(f"Empleado no encontrado: {employee_name}")


def filtrar_departamento():
    department = input("Departamento: ").strip()

    employees = load_employees(employees_filename)

    employees_by_department = list(
        filter(
            lambda employee: employee["department"].lower() == department.lower(),
            employees,
        )
    )

    if employees_by_department:
        for employee in employees_by_department:
            show_employee_data(employee)

        logger.info(
            f"Se encontraron {len(employees_by_department)} empleados en el departamento {department}"
        )
    else:
        print(f"Empleados no encontrados para el departamento: {department}")
        logger.warning(f"Empleados no encontrados para el departamento: {department}")
