from fastapi import FastAPI

app = FastAPI(title="Query Parameters")

empleados = [
    {"id": 1, "nombre": "Josue", "edad": 24, "departamento": "IT"},
    {"id": 2, "nombre": "Cedrick", "edad": 2, "departamento": "HR"},
    {"id": 3, "nombre": "Ana", "edad": 30, "departamento": "IT"},
    {"id": 4, "nombre": "Carlos", "edad": 27, "departamento": "Marketing"},
]


@app.get("/empleados")
def get_empleados(departamento: str | None = None, edad: int | None = None):
    resultado = empleados

    if departamento:
        resultado = [
            empleado
            for empleado in resultado
            if empleado["departamento"] == departamento
        ]

    if edad is not None:
        resultado = [empleado for empleado in resultado if empleado["edad"] == edad]

    return resultado
