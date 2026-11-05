from fastapi import FastAPI, Path

app = FastAPI(
    title="Sistema de Gestion de Empleados",
    description="API REST para administrar empleados.",
    version="1.0.0",
)


@app.get(
    "/empleados",
    summary="Obtener empleados",
    description="Devuelve una lista de todos los empleados registrados.",
)
def obtener_empleados():
    return [
        {"id": 1, "nombre": "Cesario"},
        {"id": 2, "nombre": "Cedrick"},
    ]


@app.get("/empleadoss/{empleado_id}")
def obtener_empleado(
    empleado_id: int = Path(description="Identificador unico del empleado", gt=0),
):
    return {"id": empleado_id}


@app.get(
    "/empleados/{empleado_id}",
    responses={
        200: {"description": "Empleado encontrado"},
        404: {"description": "Empleado no encontrado"},
    },
)
def obtener_empleado_by_id(empleado_id: int):
    return {"id": empleado_id}
