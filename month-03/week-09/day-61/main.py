from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Validaciones Pydantic", description="Deep dive into pydantic")


class Empleado(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(gt=17, lt=100)
    departamento: str = Field(min_length=2)
    salario: float = Field(ge=0)
    telefono: str | None = None


class ProductoCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=40)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    categoria: str = Field(min_length=3)
    disponible: bool = True
    descripcion: str | None = None


# Data base simulator
empleados: list[Empleado] = []


@app.post("/empleados")
def crear_empleado(empleado: Empleado):
    empleados.append(empleado)
    return {"message": "Employee created sucessfully", "empleado": empleado}


@app.get("/empleados")
def obtener_empleados():
    return empleados


@app.post("/productos")
def crear_producto(producto: ProductoCreate):
    return {"message": "Producto agregado correctamente", "producto": producto}
