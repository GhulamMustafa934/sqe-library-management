import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library, borrow_percentile
from book import Book

@pytest.fixture(autouse=True)
def clean_isbns():
    Book.reset_isbns()
    yield

# ---------------------------------------------------------
# Gaps in src/book.py (Lines 20, 22, 24, 51, 62-64)
# ---------------------------------------------------------

def test_book_empty_isbn_raises():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("Title", "Author", "")

def test_book_duplicate_isbn_raises():
    Book("Title 1", "Author", "1111111111111")
    with pytest.raises(ValueError, match="already exists"):
        Book("Title 2", "Author", "1111111111111")

def test_book_invalid_total_copies_raises():
    with pytest.raises(ValueError, match="total_copies must be at least 1"):
        Book("Title", "Author", "1111111111111", total_copies=0)

def test_book_borrow_no_copies_raises():
    b = Book("Title", "Author", "1111111111111", total_copies=1)
    b.borrow_book() # Borrow the only copy
    with pytest.raises(ValueError, match="has no available copies"):
        b.borrow_book()

def test_book_return_without_borrow_raises():
    b = Book("Title", "Author", "1111111111111")
    with pytest.raises(ValueError, match="has no borrowed copies to return"):
        b.return_book()

# ---------------------------------------------------------
# Gaps in src/library.py (Lines 71, 95-100, 105, 173-178)
# ---------------------------------------------------------

def test_library_add_duplicate_book_raises():
    lib = Library()
    b = Book("Title", "Author", "1111111111111")
    lib.add_book(b)
    with pytest.raises(ValueError, match="already exists in library"):
        lib.add_book(b)

def test_library_borrow_not_found_raises():
    lib = Library()
    with pytest.raises(ValueError, match="not found in library"):
        lib.borrow_book("M1", "9999999999999")

def test_library_borrow_no_available_copies_raises():
    lib = Library()
    b = Book("Title", "Author", "1111111111111", total_copies=1)
    lib.add_book(b)
    lib.borrow_book("M1", "1111111111111")  # Borrow the only copy
    with pytest.raises(ValueError, match="has no available copies"):
        lib.borrow_book("M2", "1111111111111")

def test_library_return_not_on_loan_raises():
    lib = Library()
    with pytest.raises(ValueError, match="does not have book"):
        lib.return_book("M1", "1111111111111")

def test_borrow_percentile_member_not_found_returns_zero():
    lib = Library()
    b = Book("Title", "Author", "1111111111111")
    lib.add_book(b)
    lib.borrow_book("M1", "1111111111111")
    
    # Member "M99" doesn't exist, should return 0.0
    assert borrow_percentile("M99", lib) == 0.0