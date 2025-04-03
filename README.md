# Books REST API

This is a RESTful API built with Python and FastAPI for a book management system. Users can register books they want to read or have already read.

## Instalation

First you need to create a python virtual environments to install the project dependencies:

```bash
python3 -m venv venv
```

```bash
source ./venv/bin/activate
```

Then install the required modules:

```bash
pip install -r requirements.txt
```

## Endpoints

### Books

- GET `/books` retrieve all books created.
- GET `/books/{id}` should return an single book by its Id.
- PUT `/books/{id}` should update the specific book by its Id.
- DELETE `/books/{id}` should delete a single book by its Id.
- POST `/books` create a book.