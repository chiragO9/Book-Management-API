from fastapi import Body, FastAPI
from pydantic import BaseModel
app  = FastAPI()

class Book:
  id : int
  title : str
  author : str
  description : str
  rating : str

  def __init__(self,id, tittle, author, description, rating):
    self.id = id
    self.title = tittle
    self.author = author
    self.description = description
    self.rating = rating

class BookRequest(BaseModel):
  id : int
  title : str
  author : str
  description : str
  rating : int 


BOOKS = [
  Book(1,"A light in the Attic", 'Shel Silverstein', 'A very good book....', 3),
  Book(2,"Soumission" ,'Flammarion', '"Dans une France assez proche de la nôtre....', 1),
  Book(3,"Sharp Objects" ,'Gillian Flynn', 'WICKED above her hipbone, GIRL across ....', 4),
  Book(4,"Sapiens" ,'Yuval Noah Harari', 'From a renowned historian comes a groundbreaking narrative ....', 5),
  Book(5,"Set me free" ,'Kitty Stephens', 'Aaron Ledbetter’s future had been planned....', 5)
]

@app.get("/books")
async def read_all_books():
  return BOOKS

@app.post("/create_book")
async def create_book(book_request = BookRequest):
  BOOKS.append(book_request)