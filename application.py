from fastapi import FastAPI
from books import BOOKS


app = FastAPI()

@app.get("/")
async def index():
    return "Bienvenido a la libreria!!"

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_bookTitle(book_title:str):
    for book in BOOKS:
        if book.get('nombre').casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def read_bookCategory(book_autor:str):
    booksautor = []
    for book in BOOKS:
        if book.get('autor').casefold() == book_autor.casefold():
            booksautor.append(book)
    return booksautor
               
@app.get("/books/")
async def read_bookCategory(book_category:str):
    bookscategory = []
    for book in BOOKS:
        if book.get('categoria').casefold() == book_category.casefold():
            bookscategory.append(book)
    return bookscategory