# Composition
class Motor:
    def encender(self):
        print("Motor encedido")


class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
        print("Auto arrancado")


auto = Auto()
auto.arrancar()

# Herencia is-a
# Composition has-a
