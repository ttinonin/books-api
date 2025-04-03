from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from models.Book import Book

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "It Works!"
    }

books_db = []

@app.post("/books/")
async def create_book(book: Book):
    books_db.append(book)
    return book

@app.get("/books/")
async def read_books():
    return books_db

@app.get("/books/{id}")
async def read_single_book(id: int):
    return books_db[id]

@app.put("/books/{id}")
async def update_book(id: int, book: Book):
    book_encoded = jsonable_encoder(book)
    books_db[id] = book_encoded
    return book_encoded

@app.delete("/books/{id}")
async def delete_book(id: int):
    book_delete = books_db[id]

    del books_db[id]
    
    return book_delete