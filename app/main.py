from fastapi import FastAPI
from datetime import datetime
import requests
import json

app = FastAPI()

BOOKS = [
    {'id': '01', 'nombre': 'Ríos de Fuego', 'autor': 'Lucía Fernández', 'categoria': 'Aventura', 'año_publicacion': 2005},
    {'id': '02', 'nombre': 'Ecos de la Luna', 'autor': 'Luis Martínez', 'categoria': 'Romance', 'año_publicacion': 1989},
    {'id': '03', 'nombre': 'Sueños Perdidos', 'autor': 'Ana Torres', 'categoria': 'Fantasía', 'año_publicacion': 2015},
    {'id': '04', 'nombre': 'Sombras de Acero', 'autor': 'Pedro Gómez', 'categoria': 'Ciencia Ficción', 'año_publicacion': 1999},
    {'id': '05', 'nombre': 'Tiempos Prohibidos', 'autor': 'María Díaz', 'categoria': 'Historia', 'año_publicacion': 1974},
    {'id': '06', 'nombre': 'Códigos del Pasado', 'autor': 'Sofía López', 'categoria': 'Misterio', 'año_publicacion': 2008},
    {'id': '07', 'nombre': 'Puertas Eternas', 'autor': 'Carlos Ramírez', 'categoria': 'Terror', 'año_publicacion': 1981},
    {'id': '08', 'nombre': 'Caminos de Cristal', 'autor': 'Elena Castro', 'categoria': 'Fantasía', 'año_publicacion': 2011},
    {'id': '09', 'nombre': 'Códigos de Fuego', 'autor': 'Juan Sánchez', 'categoria': 'Ficción', 'año_publicacion': 2020},
    {'id': '10', 'nombre': 'Sombras del Pasado', 'autor': 'Lucía Pérez', 'categoria': 'Misterio', 'año_publicacion': 1992},
    {'id': '11', 'nombre': 'Ríos de la Noche', 'autor': 'Daniel Castro', 'categoria': 'Romance', 'año_publicacion': 2016},
    {'id': '12', 'nombre': 'Secretos en Ruinas', 'autor': 'Laura Gómez', 'categoria': 'Terror', 'año_publicacion': 1987},
    {'id': '13', 'nombre': 'Tiempos de Cristal', 'autor': 'Sofía Ramírez', 'categoria': 'Historia', 'año_publicacion': 2002},
    {'id': '14', 'nombre': 'Caminos del Pasado', 'autor': 'Pedro Torres', 'categoria': 'Aventura', 'año_publicacion': 2009},
    {'id': '15', 'nombre': 'Ecos Eternos', 'autor': 'María Fernández', 'categoria': 'Fantasía', 'año_publicacion': 1995},
    {'id': '16', 'nombre': 'Códigos de Cristal', 'autor': 'Carlos Díaz', 'categoria': 'Ciencia Ficción', 'año_publicacion': 2023},
    {'id': '17', 'nombre': 'Puertas Perdidas', 'autor': 'Ana Martínez', 'categoria': 'Misterio', 'año_publicacion': 2013},
    {'id': '18', 'nombre': 'Sombras Prohibidas', 'autor': 'Luis Castro', 'categoria': 'Terror', 'año_publicacion': 1983},
    {'id': '19', 'nombre': 'Secretos de Acero', 'autor': 'Elena Sánchez', 'categoria': 'Ficción', 'año_publicacion': 2006},
    {'id': '20', 'nombre': 'Sueños de Cristal', 'autor': 'Juan López', 'categoria': 'Romance', 'año_publicacion': 1990},
    {'id': '21', 'nombre': 'Tiempos de Fuego', 'autor': 'Laura Ramírez', 'categoria': 'Historia', 'año_publicacion': 2001},
    {'id': '22', 'nombre': 'Ríos del Pasado', 'autor': 'Daniel Gómez', 'categoria': 'Aventura', 'año_publicacion': 1978},
    {'id': '23', 'nombre': 'Códigos Prohibidos', 'autor': 'Lucía Torres', 'categoria': 'Ciencia Ficción', 'año_publicacion': 1996},
    {'id': '24', 'nombre': 'Caminos Eternos', 'autor': 'Carlos Fernández', 'categoria': 'Fantasía', 'año_publicacion': 2010},
    {'id': '25', 'nombre': 'Ecos de Cristal', 'autor': 'Sofía Díaz', 'categoria': 'Misterio', 'año_publicacion': 2003},
    {'id': '26', 'nombre': 'Puertas de Fuego', 'autor': 'Pedro Pérez', 'categoria': 'Terror', 'año_publicacion': 2018},
    {'id': '27', 'nombre': 'Sueños Prohibidos', 'autor': 'Ana López', 'categoria': 'Romance', 'año_publicacion': 2004},
    {'id': '28', 'nombre': 'Sombras en Ruinas', 'autor': 'María Castro', 'categoria': 'Historia', 'año_publicacion': 1984},
    {'id': '29', 'nombre': 'Secretos de la Noche', 'autor': 'Luis Sánchez', 'categoria': 'Ficción', 'año_publicacion': 1998},
    {'id': '30', 'nombre': 'Ríos de Cristal', 'autor': 'Elena Ramírez', 'categoria': 'Fantasía', 'año_publicacion': 2019},
    {'id': '31', 'nombre': 'Tiempos de la Luna', 'autor': 'Juan Díaz', 'categoria': 'Ciencia Ficción', 'año_publicacion': 2007},
    {'id': '32', 'nombre': 'Códigos de Acero', 'autor': 'Lucía Gómez', 'categoria': 'Misterio', 'año_publicacion': 2012},
    {'id': '33', 'nombre': 'Ecos del Pasado', 'autor': 'Pedro Martínez', 'categoria': 'Historia', 'año_publicacion': 1980},
    {'id': '34', 'nombre': 'Caminos Perdidos', 'autor': 'Laura Castro', 'categoria': 'Aventura', 'año_publicacion': 2014},
    {'id': '35', 'nombre': 'Sueños de Acero', 'autor': 'Daniel López', 'categoria': 'Terror', 'año_publicacion': 1997},
    {'id': '36', 'nombre': 'Sombras de la Noche', 'autor': 'Ana Torres', 'categoria': 'Ficción', 'año_publicacion': 2000},
    {'id': '37', 'nombre': 'Ríos Eternos', 'autor': 'Carlos Ramírez', 'categoria': 'Romance', 'año_publicacion': 1993},
    {'id': '38', 'nombre': 'Secretos Prohibidos', 'autor': 'Sofía Sánchez', 'categoria': 'Misterio', 'año_publicacion': 2017},
    {'id': '39', 'nombre': 'Puertas del Pasado', 'autor': 'Pedro Fernández', 'categoria': 'Historia', 'año_publicacion': 1986},
    {'id': '40', 'nombre': 'Ecos de la Noche', 'autor': 'Luis Díaz', 'categoria': 'Ciencia Ficción', 'año_publicacion': 2022}
]

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

