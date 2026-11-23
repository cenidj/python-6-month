from fastapi import FastAPI

from app.routers import authors, books, employees

app = FastAPI(title="Book API")

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
