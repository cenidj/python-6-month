# Calculadora de gastos personasl


def gastos_personales():
    print("\n===== GASTOS PERSONALES =====\n")

    alquiler = float(input("Cuanto gastas en alquiler? "))
    comida = float(input("Cuanto gastas en comida? "))
    transporte = float(input("Cuanto gastas en transporte? "))
    servicios = float(input("Cuanto gastas en servicios? "))
    entretenimiento = float(input("Cuanto gastas en entretenimiento? "))

    gastos = {
        "Alquiler": alquiler,
        "Comida": comida,
        "Transporte": transporte,
        "Servicios": servicios,
        "Entretenimiento": entretenimiento
    }

    total_gastos = sum(gastos.values())

    print("\n===== GASTOS PERSONALES =====\n")

    for categoria, gasto in gastos.items():
        print(f"{categoria}: {gasto}")

    print("\n------------------------------------------")
    print(f"Total de gastos: ${round(total_gastos, 2)}")


gastos_personales()
