from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=3)
    price: float = Field(ge=0)


class BookResponse(BaseModel):
    id: int
    title: str
    price: float
