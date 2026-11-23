from fastapi import APIRouter

from app.schemas.book import BookCreate
from app.services.book_service import create_book

router = APIRouter()


@router.get("/")
def obtener_libros():
    return {"books": []}


@router.get("/{book_id}")
def obtener_libro(book_id: int):
    return {"book_id": book_id}


@router.post("/")
def create_book_route(book: BookCreate):
    return create_book(book)
