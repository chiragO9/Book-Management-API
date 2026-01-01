# 📚 Book Management API
**Current Version:** v2.0 | **Status:** Active Development

A RESTful API for managing books built with FastAPI and Python. Browse, create, update, and delete books by title, author, and category with a fast and modern API.

---

## About

This is a learning project to master FastAPI and RESTful API design. The API provides full CRUD (Create, Read, Update, Delete) endpoints to manage a book collection across various genres.

---

## Features

**Current (v2.0):**
-  **Get all books** - Retrieve the complete book collection
-  **Search by title** - Find specific books (case-insensitive)
-  **Filter by category** - Get books by category using query parameters
-  **Filter by author & category** - Advanced filtering with multiple parameters
-  **Create books** - Add new books to the collection
-  **Update books** - Modify existing book information
-  **Delete books** - Remove books from the collection
-  **Fast API** - Built with FastAPI for high performance
-  **RESTful design** - Clean and intuitive endpoints
-  **Automatic docs** - Interactive API documentation

---

## 🛠 Technologies Used

- **Python 3.8+**
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/chiragO9/book-management-api.git
cd book-management-api
```

2. **Create virtual environment (recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install fastapi uvicorn
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

---

## How to Run

### Start the API server:
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### Access Interactive Documentation:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## API Endpoints

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints Reference

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | Welcome message | - |
| GET | `/books` | Get all books | - |
| GET | `/books/{book_title}` | Get book by title | `/books/sapiens` |
| GET | `/books/?category={category}` | Get books by category | `/books/?category=Mystery` |
| GET | `/books/{book_author}/?category={category}` | Get books by author and category | `/books/Stephen King/?category=Horror` |
| POST | `/books/create_book` | Create a new book | See example below |
| PUT | `/books/update_book` | Update an existing book | See example below |
| DELETE | `/books/delete_book/{book_title}` | Delete a book by title | `/books/delete_book/sapiens` |

---

## Example Requests & Responses

### GET `/books` - Get All Books
**Response:**
```json
[
  {
    "title": "One Hundred Years of Solitude",
    "author": "Gabriel García Márquez",
    "category": "Magical Realism"
  },
  {
    "title": "Murder on the Orient Express",
    "author": "Agatha Christie",
    "category": "Mystery"
  }
]
```

### GET `/books/sapiens` - Get Book by Title
**Response:**
```json
{
  "title": "Sapiens: A Brief History of Humankind",
  "author": "Yuval Noah Harari",
  "category": "Nonfiction"
}
```

### GET `/books/?category=Mystery` - Filter by Category
**Response:**
```json
[
  {
    "title": "Murder on the Orient Express",
    "author": "Agatha Christie",
    "category": "Mystery"
  }
]
```

### GET `/books/Stephen King/?category=Horror` - Filter by Author & Category
**Response:**
```json
[
  {
    "title": "The Shining",
    "author": "Stephen King",
    "category": "Horror"
  }
]
```

### POST `/books/create_book` - Create New Book
**Request Body:**
```json
{
  "title": "1984",
  "author": "George Orwell",
  "category": "Dystopian"
}
```

### PUT `/books/update_book` - Update Book
**Request Body:**
```json
{
  "title": "The Shining",
  "author": "Stephen King",
  "category": "Psychological Horror"
}
```

### DELETE `/books/delete_book/1984` - Delete Book
**Success:** Book removed from collection

---

## 📚 Current Book Collection

The API includes books from various genres:
- **Magical Realism** - Gabriel García Márquez
- **Mystery** - Agatha Christie
- **Nonfiction** - Yuval Noah Harari
- **Fantasy** - N.K. Jemisin
- **Classic** - Jane Austen
- **Horror** - Stephen King

---

## Testing the API

### Using cURL:
```bash
# Get all books
curl http://127.0.0.1:8000/books

# Get specific book
curl http://127.0.0.1:8000/books/sapiens

# Filter by category
curl "http://127.0.0.1:8000/books/?category=Mystery"

# Create a new book
curl -X POST "http://127.0.0.1:8000/books/create_book" \
  -H "Content-Type: application/json" \
  -d '{"title":"1984","author":"George Orwell","category":"Dystopian"}'

# Update a book
curl -X PUT "http://127.0.0.1:8000/books/update_book" \
  -H "Content-Type: application/json" \
  -d '{"title":"The Shining","author":"Stephen King","category":"Psychological Horror"}'

# Delete a book
curl -X DELETE "http://127.0.0.1:8000/books/delete_book/1984"
```

### Using Browser:
Simply open: `http://127.0.0.1:8000/docs` for interactive testing!

---

##  Important Notes

- **Case-insensitive searches:** All title, author, and category searches are case-insensitive
- **In-memory storage:** Books are stored in memory and will reset when the server restarts
- **No duplicate checking:** The API currently doesn't prevent duplicate book entries
- **Path vs Query parameters:** Note the difference between `/books/{title}` (path) and `/books/?category=x` (query)

---

## 🗺 Version History

### v2.0 - Current Release
-  **Full CRUD operations**
-  POST endpoint to create new books
-  PUT endpoint to update existing books
-  DELETE endpoint to remove books
-  Query parameter filtering by category
-  Advanced filtering by author and category
-  Enhanced documentation

### v1.0 - 16 December 2024
-  Initial release
-  GET all books endpoint
-  GET book by title endpoint (case-insensitive)
-  Welcome route
-  Basic book collection with 6 books
-  FastAPI automatic documentation

---

## Future Enhancements

Potential improvements for future versions:
- Database integration (SQLite/PostgreSQL)
- Data validation with Pydantic models
- Authentication and authorization
- Error handling improvements
---
