# API Manual Exploration - Library Management System

## 1. POST /books (Add a new book)
**Request:**
- Method: POST
- URL: `http://127.0.0.1:5000/books`
- Body (JSON):
```json
{
  "title": "Clean Code",
  "author": "R. Martin",
  "isbn": "9780132350884",
  "total_copies": 2
}