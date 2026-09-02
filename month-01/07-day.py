# Calculadora de gastos personasl

class Gastos:
    def gastos_personales(self):
        print("\n===== CALCULADORA GASTOS PERSONALES =====\n")

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
            print(f"{categoria}: {gasto:.2f}")

        print("\n------------------------------------------")
        print(f"Total de gastos: ${total_gastos:.2f}")


gastos_cesario = Gastos()
gastos_cesario.gastos_personales()
