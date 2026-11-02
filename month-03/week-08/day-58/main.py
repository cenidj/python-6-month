from fastapi import FastAPI, HTTPException

app = FastAPI(title="Path Paramethers")

empleados = [
    {"id": 1, "nombre": "Josue", "edad": 24},
    {"id": 2, "nombre": "Cedrick", "edad": 2},
]


@app.get("/")
def home():
    return {"message": "Hello, from main"}


@app.get("/empleados")
def get_empleados():
    return empleados


# Ejerciciops


@app.get("/empleados/{empleado_id}")
def get_empleado(empleado_id: int):
    empleado = next(
        filter(lambda empleado: empleado["id"] == empleado_id, empleados), None
    )

    # Empleado no encontrado
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    return empleado


@app.get("/libros/{libro_id}")
def get_libro(libro_id: int):
    return {"libro_id": libro_id, "mensaje": f"Se esta consultando el libro {libro_id}"}


@app.get("/productos/{producto_id}")
def get_producto(producto_id: int):
    return {
        "producto_id": producto_id,
        "mensaje": f"Consultando producto {producto_id}",
    }
