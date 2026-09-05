# Dictionaries

# Key -> value
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Maryville"
}

print(persona["nombre"])
persona["edad"] = 26

persona["profesion"] = "Programador"

# .get()
print(persona.get("nombre"))

print(persona.get("telefono"))  # -> None

try:
    print(persona["telefono"])  # -> error (KeyError)
except:
    print("Use .get() method because it's safer, return None if key does not exist, the other way it throw an error!")

# Also you can put a predetermined value
print(persona.get("telefono", "No disponible"))

# .items()
# it allows you iterate over keys and values at the same time
for key, value in persona.items():
    print(key, ":", value)

# Mini exercise
print("\n === Mini Exercise ===\n")

videojuego = {
    "nombre": "Minecraft",
    "precio": 29.99,
    "genero": "Sandbox"
}

# 1. print the name using []
print(videojuego["nombre"])
# 2. print the price using .get()
print(videojuego.get("precio"))
# 3. add key "jugadores"
videojuego["jugadores"] = ["Carlos", "Luis", "Jose"]
# 4. iterate the dicitionary using .items()
for key, value in videojuego.items():
    print(f"{key} - {value}")
