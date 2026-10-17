import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library, rank_books_by_popularity
from book import Book

@pytest.fixture(autouse=True)
def clean_isbns():
    """Ensure ISBNs are reset before every test."""
    Book.reset_isbns()
    yield

def make_book(title, isbn, times_borrowed=0):
    """Helper to create a book with a specific borrow count."""
    b = Book(title, "Author", isbn)
    b.times_borrowed = times_borrowed
    return b

def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()
    assert rank_books_by_popularity(library) == []

def test_rank_books_single_book():
    """A catalog with one book returns a list containing just that book."""
    library = Library()
    book = Book("Clean Code", "R. Martin", "9780132350884")
    library.add_book(book)
    
    result = rank_books_by_popularity(library)
    
    assert len(result) == 1
    assert result[0] == book

def test_rank_books_descending_by_borrow_count():
    """3 books with distinct borrow counts should rank highest-to-lowest."""
    library = Library()
    b1 = make_book("Book A", "1111111111111", 5)
    b2 = make_book("Book B", "2222222222222", 10)
    b3 = make_book("Book C", "3333333333333", 2)
    
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    
    result = rank_books_by_popularity(library)
    
    # Expected order: b2 (10), b1 (5), b3 (2)
    assert result == [b2, b1, b3]