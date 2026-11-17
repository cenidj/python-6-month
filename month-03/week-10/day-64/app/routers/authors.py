from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def obtener_autores():
    return {"authors": []}
