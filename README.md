# 📚 Book Management API

**Current Version:** v1.0 | **Status:** Active Development

A RESTful API for managing books built with FastAPI and Python. Browse books by title, author, and category with a fast and modern API.

---

## About

This is a learning project to master FastAPI and RESTful API design. The API provides endpoints to retrieve book information from a curated collection of literature across various genres.

---

## Features

**Current (v1.0):**
-  **Get all books** - Retrieve the complete book collection
-  **Search by title** - Find specific books (case-insensitive)
-  **Fast API** - Built with FastAPI for high performance
-  **RESTful design** - Clean and intuitive endpoints
-  **Automatic docs** - Interactive API documentation

---

##  Technologies Used

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

### Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | Welcome message | - |
| GET | `/books` | Get all books | - |
| GET | `/books/{title}` | Get book by title | `/books/sapiens` |

### Example Responses

**GET /books**
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

**GET /books/sapiens**
```json
{
  "title": "Sapiens: A Brief History of Humankind",
  "author": "Yuval Noah Harari",
  "category": "Nonfiction"
}
```

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

## 🧪 Testing the API

### Using URL:
```bash
# Get all books
curl http://127.0.0.1:8000/books

# Get specific book
curl http://127.0.0.1:8000/books/sapiens
```

### Using Browser:
Simply open: `http://127.0.0.1:8000/docs` for interactive testing!

---

##  Version History

### v1.0 - 16 December 2024
-  **Initial release**
-  GET all books endpoint
-  GET book by title endpoint (case-insensitive)
-  Welcome route
-  Basic book collection with 6 books
-  FastAPI automatic documentation

---
