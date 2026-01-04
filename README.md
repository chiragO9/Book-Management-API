# 📚 FastAPI Learning Journey - Book Management API

A progressive learning project demonstrating FastAPI concepts from basic CRUD operations to advanced data validation with Pydantic models.

---

##  Projects in This Repository

### Project 1: Basic CRUD Operations (`main.py`)
**Status:**  Complete | **Version:** v2.0

Basic book management API with dictionary-based storage and simple CRUD operations.

**Key Concepts:**
- FastAPI basics
- Path and query parameters
- In-memory dictionary storage
- Body() for request data
- Basic routing

**Run:**
```bash
uvicorn main:app --reload
```
---

### Project 2: Data Validation with Pydantic (`books2.py`)
**Status:**  In Progress | **Version:** v1.0

Enhanced API using Pydantic models for data validation and type safety.

**Key Concepts:**
- Pydantic BaseModel for request validation
- Custom Python classes for data modeling
- Type hints and validation
- Structured data handling

**New Features:**
-  Pydantic `BookRequest` model for automatic validation
-  Custom `Book` class for internal data structure
-  Type-safe endpoints with automatic documentation
-  Built-in data validation (rating must be int, etc.)

**Run:**
```bash
uvicorn books2:app --reload
```

**API Endpoints:**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| POST | `/create_book` | Create book with Pydantic validation |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### One-Time Setup

1. **Clone the repository**
```bash
git clone https://github.com/chiragO9/book-management-api.git
cd book-management-api
```

2. **Create virtual environment**
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
pip install fastapi uvicorn pydantic
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

---

##  How to Run

**Important:** Only one project can run at a time since they both use port 8000.

### Running Project 1 (main.py):
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Run the server
uvicorn main:app --reload
```

### Running Project 2 (books2.py):
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Run the server
uvicorn books2:app --reload
```

**Access at:** `http://127.0.0.1:8000`

**Interactive Docs:**
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 📖 Project 1 Documentation

### About
Basic REST API for managing books with dictionary-based storage and full CRUD operations.

### Features
-  Get all books
-  Search by title (case-insensitive)
-  Filter by category
-  Filter by author & category
-  Create, Update, Delete books
-  In-memory storage

### API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | Welcome message | - |
| GET | `/books` | Get all books | - |
| GET | `/books/{book_title}` | Get book by title | `/books/sapiens` |
| GET | `/books/?category={category}` | Get books by category | `/books/?category=Mystery` |
| GET | `/books/{book_author}/?category={category}` | Filter by author and category | `/books/Stephen King/?category=Horror` |
| POST | `/books/create_book` | Create a new book | - |
| PUT | `/books/update_book` | Update an existing book | - |
| DELETE | `/books/delete_book/{book_title}` | Delete a book by title | `/books/delete_book/sapiens` |

### Example Responses

**GET /books**
```json
[
  {
    "title": "One Hundred Years of Solitude",
    "author": "Gabriel García Márquez",
    "category": "Magical Realism"
  }
]
```

**POST /books/create_book**
```json
{
  "title": "1984",
  "author": "George Orwell",
  "category": "Dystopian"
}
```

### Book Collection
- One Hundred Years of Solitude - Gabriel García Márquez
- Murder on the Orient Express - Agatha Christie
- Sapiens - Yuval Noah Harari
- The Fifth Season - N.K. Jemisin
- Pride and Prejudice - Jane Austen
- The Shining - Stephen King

---

## 📖 Project 2 Documentation

### About
Enhanced API demonstrating Pydantic data validation and structured data models.

### Key Differences from Project 1
-  Uses Pydantic `BaseModel` instead of `Body()`
-  Custom `Book` class for internal data structure
-  Automatic type validation (rating must be integer)
-  Better error messages for invalid data
-  More detailed book information (id, description, rating)

### Data Models

**Book Class (Internal):**
```python
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str
```

**BookRequest (API Request):**
```python
class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int  # Validated as integer
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books with detailed info |
| POST | `/create_book` | Create book (validated by Pydantic) |

### Example Request

**POST /create_book**
```json
{
  "id": 6,
  "title": "1984",
  "author": "George Orwell",
  "description": "A dystopian social science fiction novel",
  "rating": 5
}
```

### Book Collection
- A light in the Attic - Shel Silverstein (Rating: 3)
- Soumission - Flammarion (Rating: 1)
- Sharp Objects - Gillian Flynn (Rating: 4)
- Sapiens - Yuval Noah Harari (Rating: 5)
- Set me free - Kitty Stephens (Rating: 5)

---

##  Testing the APIs

### Using cURL (Project 1):
```bash
# Get all books
curl http://127.0.0.1:8000/books

# Create a book
curl -X POST "http://127.0.0.1:8000/books/create_book" \
  -H "Content-Type: application/json" \
  -d '{"title":"1984","author":"George Orwell","category":"Dystopian"}'
```

### Using cURL (Project 2):
```bash
# Get all books
curl http://127.0.0.1:8000/books

# Create a book (with validation)
curl -X POST "http://127.0.0.1:8000/create_book" \
  -H "Content-Type: application/json" \
  -d '{"id":6,"title":"1984","author":"George Orwell","description":"Dystopian novel","rating":5}'
```

### Using Browser:
Open `http://127.0.0.1:8000/docs` for interactive testing with Swagger UI!

---

## 📚 Learning Progress

###  Completed Concepts
- **Project 1:**
  - FastAPI application setup
  - GET/POST/PUT/DELETE operations
  - Path parameters
  - Query parameters
  - Body() for request data
  - Dictionary-based storage

- **Project 2:**
  - Pydantic BaseModel
  - Custom Python classes
  - Type validation
  - Data modeling

###  Currently Learning
- Pydantic data validation
- Type hints in Python
- Structured API responses

###  Coming Next
- Database integration
- Authentication
- Advanced validation
- Error handling

---

##  Important Notes

- **One server at a time:** Stop one project before running another (they use the same port)
- **Same environment:** Both projects use the same virtual environment - no reinstallation needed
- **Data persistence:** Both projects use in-memory storage - data resets on restart
- **Validation:** Project 2 automatically validates data types (e.g., rating must be integer)

---

## 🗺 Version History

### Project 2 - v1.0 (1 January 2026)
-  Added Pydantic models for validation
-  Implemented BookRequest BaseModel
-  Created custom Book class
-  In Progress

### Project 1 - v2.0 (1 January 2026)
-  Full CRUD operations complete
-  Query parameter filtering
-  Advanced filtering by author and category

### Project 1 - v1.0 (16 December 2025)
-  Initial release with basic endpoints

---
