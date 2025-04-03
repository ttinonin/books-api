from fastapi import FastAPI, status
from routers import books

app = FastAPI()

app.include_router(books.router)

@app.get("/")
async def root():
    return {
        "message": "It Works!"
    }