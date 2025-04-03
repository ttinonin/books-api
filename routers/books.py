from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from models.Book import Book

books_db = []

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> Book:
    books_db.append(book)
    return book

@router.get("/")
async def read_books() -> list[Book]:
    return books_db

@router.get("/{id}")
async def read_single_book(id: int) -> Book:
    return books_db[id]

@router.put("/{id}")
async def update_book(id: int, book: Book) -> Book:
    book_encoded = jsonable_encoder(book)
    books_db[id] = book_encoded
    return book_encoded

@router.delete("/{id}")
async def delete_book(id: int) -> Book:
    book_delete = books_db[id]

    del books_db[id]
    
    return book_delete