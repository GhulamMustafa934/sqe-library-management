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
    b1 = Book("Book A", "Author", "1111111111111")
    b2 = Book("Book B", "Author", "2222222222222")
    b3 = Book("Book C", "Author", "3333333333333")
    
    # Simulate borrow counts (we will add times_borrowed to Book)
    b1.times_borrowed = 5
    b2.times_borrowed = 10
    b3.times_borrowed = 2
    
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    
    result = rank_books_by_popularity(library)
    
    # Expected order: b2 (10), b1 (5), b3 (2)
    assert result == [b2, b1, b3]