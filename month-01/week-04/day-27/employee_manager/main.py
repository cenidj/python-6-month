import logging

from employees import (
    agregar_empleado,
    buscar_empleado,
    eliminar_empleado,
    filtrar_departamento,
    menu,
    mostrar_empleados,
    show_menu,
)

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
logger.info("App started.")

while True:
    print("\n\n\n=== Employees managment ===\n")

    show_menu(menu)

    select_option = input("\nSelect an option: ")

    if select_option == "1":
        mostrar_empleados()
    elif select_option == "2":
        buscar_empleado()
    elif select_option == "3":
        agregar_empleado()
    elif select_option == "4":
        eliminar_empleado()
    elif select_option == "5":
        filtrar_departamento()
    elif select_option == "11":
        break
    else:
        print("Opcion invalida")
