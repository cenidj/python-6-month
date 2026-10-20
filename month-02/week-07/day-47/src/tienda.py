def obtener_precio():
    # Simula la consulta de serviio externo
    return 100


def calcular_total(cantidad):
    precio = obtener_precio()
    return precio * cantidad


def obtener_descuento():
    return 10


def calcular_precio_final(precio):
    descuento = obtener_descuento()
    return precio - descuento
