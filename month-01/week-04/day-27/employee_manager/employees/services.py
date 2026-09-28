import logging

from utils import employees_filename

from employees import add_employee, create_employees_file, load_employees

logger = logging.getLogger(__name__)


def show_menu(menu):
    for option in menu:
        print(option)


def show_employee_data(employee):
    print(
        f"{employee['name']}\nEdad: {employee['age']}\nSalario: {employee['salary']}\nDepartamento: {employee['department']}"
    )


def mostrar_empleados():
    try:
        logger.info("Opening employees.json data ")
        employees = load_employees(employees_filename)

        if len(employees) == 0:
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
    try:
        employee_name = input("Nombre: ").strip()
        employee_age = int(input("Edad: ").strip())
        employee_salary = float(input("Salario: ").strip())
        employee_department = input("Departamento: ").strip()

        employees = load_employees(employees_filename)

        new_employee = {
            "name": employee_name,
            "age": employee_age,
            "salary": employee_salary,
            "department": employee_department,
        }

        employees.append(new_employee)

        add_employee(employees_filename, employees)

        mostrar_empleados()

    except ValueError:
        logger.warning("Error to introduce one of the required fields")
