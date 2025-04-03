from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    title: str
    authors: List[str]
    year: int
    description: str
    is_read: bool