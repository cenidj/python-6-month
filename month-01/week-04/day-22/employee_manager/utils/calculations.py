def salario_promedio(empleados):
    return sum(empleado["salario"] for empleado in empleados) / len(empleados)


def mayor_salario(empleados):
    return max(empleado["salario"] for empleado in empleados)
