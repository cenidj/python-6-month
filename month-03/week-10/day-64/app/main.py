from fastapi import FastAPI, Request
from routers import authors, books, employees

app = FastAPI(title="Book API")


@app.middleware("http")
async def recolectar_solicitudes(request: Request, call_next):
    print(f"Metodo: {request.method}")
    print(f"Ruta: {request.url.path}")

    response = await call_next(request)

    print(f"Status: {response.status_code}")

    return response


app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
