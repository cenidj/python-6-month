from employees import agregar_empleado, buscar_empleado, eliminar_empleado, empleados
from utils.calculations import mayor_salario, salario_promedio

print(empleados)

agregar_empleado(
    {"nombre": "Cesario", "edad": 27, "salario": 65000, "departamento": "IT"}
)
print(empleados)

print(buscar_empleado("Cesario"))
print(eliminar_empleado("Lucas"))

print(mayor_salario(empleados))
print(salario_promedio(empleados))
