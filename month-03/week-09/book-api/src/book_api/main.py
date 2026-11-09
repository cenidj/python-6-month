from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI(
    title="Books API", description="REST API to manage books", version="1.0.0"
)


class BookModel(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    published_year: int = Field(gt=0)
    price: float = Field(gt=0)
    available: bool = Field(default=True)


class BookModelResponse(BookModel):
    id: int


books = [
    {
        "id": 2,
        "title": "Atomic Habit",
        "author": "James Clear",
        "published_year": 2018,
        "price": 23.99,
        "available": True,
    }
]


@app.get(
    "/books",
    summary="Get all the books",
    description="Get a list of all the books in the library",
    response_model=list[BookModelResponse],
)
def get_books():
    return books


@app.get("/books/{book_id}", response_model=BookModelResponse)
def get_book(book_id: int = Path(description="Get book by id")):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found by id")


@app.post("/books")
def create_book(book: BookModel):
    book_id = int(books[-1]["id"]) + 1 if books else 1
    new_book = {"id": book_id, **book.model_dump()}
    books.append(new_book)

    return {"message": "book added sucesfully", **new_book}
