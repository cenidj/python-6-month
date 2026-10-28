from fastapi import FastAPI

app = FastAPI(title="Mi primera API")


@app.get("/")
def inicio():
    return {"mensaje": "Mi primera API funciona"}


@app.get("/estado")
def consultar_estado():
    return {"estado": "OK", "dia": 57}


@app.get("/saludo")
def saludar():
    return {"saludo": "Hola, como estas?"}
