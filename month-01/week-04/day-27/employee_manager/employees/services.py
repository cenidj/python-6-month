import logging

from utils import calcular_promedio, employees_filename, validate_new_employee

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


def filtrar_salario():
    try:
        salario_minimo = float(input("Salario minimo: "))

        employees = load_employees(employees_filename)

        employees_by_minimum_salary = list(
            filter(lambda employee: employee["salary"] >= salario_minimo, employees)
        )

        if employees_by_minimum_salary:
            for employee in employees_by_minimum_salary:
                show_employee_data(employee)

            logger.info(
                f"{len(employees_by_minimum_salary)} encontrados con un salario minimo de {salario_minimo}"
            )
        else:
            print(f"No hay empleados con un salario minimo de {salario_minimo}")
            logger.warning(
                f"No se encontraron empleados con un salario minimo de {salario_minimo}"
            )
    except ValueError as error:
        print(f"Error: {error}")


def ordenar_empleados():
    sort_options = ["1. Nombre", "2. Edad", "3. Salario", "4. Departamento"]

    sort_term = None
    reverse_sorting = False

    for option in sort_options:
        print(option)

    select_option = input("Selecciona una opcion para ordernar: ")
    if select_option == "1":
        sort_term = "name"
    elif select_option == "2":
        sort_term = "age"
    elif select_option == "3":
        sort_term = "salary"
    elif select_option == "4":
        sort_term = "department"
    else:
        sort_term = "name"
        print("Sorting by name! (default option)")

    if sort_term:
        reverse_options = ["1. Ascendente", "2. Descendente"]
        for option in reverse_options:
            print(option)

        select_option = input("Selecciona el tipo de ordenado: ")
        if select_option == "1":
            reverse_sorting = False
        elif select_option == "2":
            reverse_sorting = True
        else:
            print("Ordenando de forma ascendente (default option)")

    employees = load_employees(employees_filename)

    sorted_employees = sorted(
        employees, key=lambda employee: employee[sort_term], reverse=reverse_sorting
    )

    tipo_ordenado = "Descendente" if reverse_sorting else "Ascendente"

    logger.info(
        f"Se ordenaron {len(sorted_employees)} empleados por {sort_term} en orden {tipo_ordenado}"
    )

    for employee in sorted_employees:
        show_employee_data(employee)


def salario_promedio():
    employees = load_employees(employees_filename)
    salarios = []
    for employee in employees:
        salarios.append(employee["salary"])

    promedio_salarial = calcular_promedio(salarios)

    print(f"El promedio de salario es {promedio_salarial}")


def salario_mas_alto():
    try:
        employees = load_employees(employees_filename)
        employee_highest_salary = max(
            employees, key=lambda employee: employee["salary"]
        )

        show_employee_data(employee_highest_salary)
    except ValueError:
        print("No existen empleados para encontrar el salario mas alto")
        logger.error("No hay empleados guardados")


def guardar_empleados():
    try:
        employees = load_employees(employees_filename)
        replace_employees_data(employees_filename, employees)
        print("Empleados guardados correctamente")
        logger.info("Se guardaron los empleados")

    except PermissionError:
        print("Errores de permisos")
        logger.error("Error al guardar los empleados")
