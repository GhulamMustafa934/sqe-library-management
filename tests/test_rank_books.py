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