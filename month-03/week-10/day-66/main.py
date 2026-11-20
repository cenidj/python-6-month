import time

from fastapi import FastAPI, Request

app = FastAPI(title="Middlewares")


# @app.middleware("http")
# async def medir_tiempo(request: Request, call_next):
#     inicio = time.time()

#     response = await call_next(request)

#     duracion = time.time() - inicio

#     print(f"Tiempo de respuesta {duracion:.4f} segundos")

#     return response


@app.middleware("http")
async def registrar_solicitudes(request: Request, call_next):
    print(f"Metodo: {request.method}")
    print(f"Ruta: {request.url.path}")

    response = await call_next(request)

    print(f"Status: {response.status_code}")

    return response


@app.get("/")
def root():
    return {"message": "Hello, from root"}
