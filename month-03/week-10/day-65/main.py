from fastapi import Depends, FastAPI

app = FastAPI()


# def obtener_usuario_actual():
#     return {"id": 1, "nombre": "Cesario"}


# @app.get("/perfil", tags=["Users"])
# def obtener_perfil(usuario: dict = Depends(obtener_usuario_actual)):
#     return usuario


def verificar_rol(rol: str):
    return {"rol": rol}


@app.get("/admin")
def panel_admin(usuario: dict = Depends(lambda: verificar_rol("admin"))):
    return usuario
