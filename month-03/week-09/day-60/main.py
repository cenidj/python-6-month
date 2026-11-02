from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Request Body")


class Empleado(BaseModel):
    nombre: str
    edad: int
    departamento: str
    salario: float


class EmpleadoCreate(BaseModel):
    nombre: str
    edad: int
    departamento: str
    salario: float


@app.post("/empleados")
def crear_empleado(empleado: Empleado):
    return {"mensaje": "Empleado creado correctamente", "empleado": empleado}


@app.post("/empleadosCreate")
def nuevo_empleado(empleado: EmpleadoCreate):
    return {"mensaje": "Empleado creado correctamente", "empleado": empleado}
