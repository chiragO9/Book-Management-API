from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': "One Hundred Years of Solitude", 'author': 'Gabriel García Márquez', 'category': 'Magical Realism'},
    {'title': "Murder on the Orient Express", 'author': 'Agatha Christie', 'category': 'Mystery'},
    {'title': "Sapiens: A Brief History of Humankind", 'author': 'Yuval Noah Harari', 'category': 'Nonfiction'},
    {'title': "The Fifth Season", 'author': 'N.K. Jemisin', 'category': 'Fantasy'},
    {'title': "Pride and Prejudice", 'author': 'Jane Austen', 'category': 'Classic'},
    {'title': "The Shining", 'author': 'Stephen King', 'category': 'Horror'}
]

@app.get("/")
async def root():
    return {"message": "Welcome to Book Management API"}

@app.get("/books")
async def read_all_books():
  return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
  for book in BOOKS:
     if book.get('title').casefold() == book_title.casefold():  
        return book
