from fastapi import FastAPI, HTTPException, Path

app = FastAPI(
    title="Sistema de Gestion de Productos",
    description="API REST para gestionar los productos de Nivar Enterprise",
    version="1.0.0",
)


productos = [
    {"id": 1, "name": "Mouse", "price": 25, "stock": 3},
    {"id": 5, "name": "Keyboard", "price": 50, "stock": 8},
    {"id": 30, "name": "Monitor", "price": 200, "stock": 2},
]


@app.get(
    "/productos",
    summary="Obtener productos",
    description="Devuelve todos los productos registrados",
)
def obtener_productos():
    return productos


@app.get(
    "/productos/{producto_id}",
    summary="Obtener producto",
    description="Busca un producto mediante su identificador",
    responses={
        200: {"description": "Producto encontrado"},
        404: {"description": "Producto no encontrado"},
    },
)
def obtener_producto(
    producto_id: int = Path(description="Identificador del producto a buscar", gt=0),
):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto

    raise HTTPException(status_code=404, detail="Producto no encontrado")
