import pytest
import sys
import os

# Add the project root to the path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.api.app import app, library
from src.book import Book

@pytest.fixture
def client():
    """Set up a test client and reset the global library state before each test."""
    app.config['TESTING'] = True
    library.books.clear()
    library.member_books.clear()
    Book.reset_isbns()
    with app.test_client() as client:
        yield client

# ==========================================
# TASK 3: Automate Positive-Path Tests
# ==========================================

def test_add_book_positive(client):
    """Test POST /books (201 Created)"""
    res = client.post('/books', json={
        "title": "Clean Code", "author": "R. Martin", "isbn": "9780132350884", "total_copies": 1
    })
    assert res.status_code == 201
    assert "isbn" in res.get_json()

def test_get_book_positive(client):
    """Test GET /books/<isbn> (200 OK)"""
    client.post('/books', json={"title": "T1", "author": "A1", "isbn": "1111111111111"})
    res = client.get('/books/1111111111111')
    assert res.status_code == 200
    assert res.get_json()["title"] == "T1"

def test_borrow_book_positive(client):
    """Test POST /members/<id>/borrow (200 OK)"""
    client.post('/books', json={"title": "T1", "author": "A1", "isbn": "1111111111111"})
    res = client.post('/members/M1/borrow', json={"isbn": "1111111111111"})
    assert res.status_code == 200
    assert res.get_json()["available_copies"] == 0

def test_return_book_positive(client):
    """Test POST /members/<id>/return (200 OK)"""
    client.post('/books', json={"title": "T1", "author": "A1", "isbn": "1111111111111"})
    client.post('/members/M1/borrow', json={"isbn": "1111111111111"})
    res = client.post('/members/M1/return', json={"isbn": "1111111111111"})
    assert res.status_code == 200
    assert "message" in res.get_json()

def test_get_fines_positive(client):
    """Test GET /members/<id>/fines (200 OK)"""
    res = client.get('/members/M1/fines?days_overdue=10')
    assert res.status_code == 200
    assert res.get_json()["fine_tier"] == "Medium"


# ==========================================
# TASK 4: Automate Negative and Boundary Tests
# ==========================================

def test_get_book_404(client):
    """Test GET for non-existent ISBN (404 Not Found)"""
    res = client.get('/books/9999999999999')
    assert res.status_code == 404
    assert res.get_json()["error"] == "Book not found"

def test_borrow_no_copies_400(client):
    """Test POST /borrow when zero copies available (400 Bad Request)"""
    client.post('/books', json={"title": "T1", "author": "A1", "isbn": "1111111111111", "total_copies": 1})
    client.post('/members/M1/borrow', json={"isbn": "1111111111111"}) # Borrow the only copy
    
    # Try to borrow it with another member
    res = client.post('/members/M2/borrow', json={"isbn": "1111111111111"})
    assert res.status_code == 400
    assert "has no available copies" in res.get_json()["error"]

def test_add_book_missing_title_400(client):
    """Test POST /books missing required field (400 Bad Request)"""
    res = client.post('/books', json={"author": "A1", "isbn": "1111111111111"})
    assert res.status_code == 400
    assert "Missing required fields" in res.get_json()["error"]

def test_borrow_limit_exceeded_400(client):
    """Test borrowing a 6th book when already at the 5-book limit (400 Bad Request)"""
    # Add 6 books
    for i in range(6):
        client.post('/books', json={"title": f"T{i}", "author": "A", "isbn": f"111111111111{i}"})
    
    # Borrow 5 books
    for i in range(5):
        client.post('/members/M1/borrow', json={"isbn": f"111111111111{i}"})
        
    # Try to borrow the 6th
    res = client.post('/members/M1/borrow', json={"isbn": "1111111111115"})
    assert res.status_code == 400
    assert "already has 5 books on loan" in res.get_json()["error"]


# ==========================================
# TASK 5: Schema and Contract Assertions
# ==========================================

def test_books_schema(client):
    """Test that GET /books returns a list of objects with exact keys."""
    client.post('/books', json={"title": "T1", "author": "A1", "isbn": "1111111111111"})
    res = client.get('/books')
    
    assert res.status_code == 200
    data = res.get_json()
    
    # 1. It should be a list
    assert isinstance(data, list)
    # 2. It should have exactly 1 item
    assert len(data) == 1
    
    # 3. Check exact schema (no leaked internal fields like 'borrowed_copies')
    expected_keys = {"title", "isbn", "author", "available_copies"}
    assert set(data[0].keys()) == expected_keys