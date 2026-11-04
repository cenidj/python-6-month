from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Response Model")


class Empleado(BaseModel):
    nombre: str = Field(min_length=3)
    edad: int = Field(gt=17)
    departamento: str = Field(min_length=2)
    salario: float = Field(ge=0)


@app.get("/empleados", response_model=Empleado)
def obtener_empleado():
    return {
        "nombre": "Cesario",
        "edad": 27,
        "departamento": "IT",
        "salario": 65000,
        "status": "legal",
    }


# Ejercicios
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int


class ProductoResponse(BaseModel):
    nombre: str
    precio: float
    stock: int
    id: int


@app.post("/productos", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate):
    return {"id": 1, **producto.model_dump()}


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str


@app.get("/usuarios", response_model=UsuarioResponse)
def obtener_usuario():
    return {
        "id": 1,
        "nombre": "Cedrick",
        "email": "cedricknivar@gmail.com",
        "password": "password123",
    }
