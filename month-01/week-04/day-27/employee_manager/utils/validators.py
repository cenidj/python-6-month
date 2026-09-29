import logging

logger = logging.getLogger(__name__)


def validate_new_employee():
    valid_name = False
    valid_age = False
    valid_salary = False
    valid_department = False

    while True:
        if not valid_name:
            employee_name = input("Nombre: ").strip()
            if not employee_name:
                print("El nombre no puede estar vacio")
                logger.warning("El nombre del empleado no puede estar vacio")
                continue

            if len(employee_name) < 3:
                print("El nombre del empleado es muy corto.")
                logger.warning("El nombre es demasiado corto.")
                continue

            valid_name = True

        if not valid_age:
            try:
                employee_age = int(input("Edad: ").strip())

                if employee_age <= 0:
                    logger.warning("La edad tiene que ser mayor que cero")
                    print("la edad tiene que ser mayor que cero")
                    continue

            except ValueError:
                print("La edad tiene que ser un numero")
                continue

            valid_age = True

        if not valid_salary:
            try:
                employee_salary = float(input("Salario: ").strip())
                if employee_salary <= 0:
                    logger.warning("Error al agregar salario menor que 1")
                    print("El salario debe ser mayor que cero.")
                    continue
            except ValueError:
                print("El salario debe de ser un numero.")
                continue

            valid_salary = True

        if not valid_department:
            employee_department = input("Departamento: ").strip()
            if not employee_department:
                print("El departamento del empleado no puede estar vacio")
                continue

            valid_department = True

        new_employee = {
            "name": employee_name,
            "age": employee_age,
            "salary": employee_salary,
            "department": employee_department,
        }

        return new_employee
