from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def obtener_libros():
    return {"books": []}


@router.get("/{book_id}")
def obtener_libro(book_id: int):
    return {"book_id": book_id}
