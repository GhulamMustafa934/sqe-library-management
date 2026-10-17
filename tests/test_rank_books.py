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
    
    assert result == [b2, b1, b3]

def test_rank_books_tie_breaker_alphabetical():
    """Two books with identical borrow counts should be sorted alphabetically by title."""
    library = Library()
    b_zebra = make_book("Zebra", "4444444444444", 5)
    b_apple = make_book("Apple", "5555555555555", 5)
    
    library.add_book(b_zebra)
    library.add_book(b_apple)
    
    result = rank_books_by_popularity(library)
    
    assert result == [b_apple, b_zebra]

def test_rank_books_never_borrowed_mixed_with_borrowed():
    """A book with 0 borrows should rank below a book with >0 borrows."""
    library = Library()
    never_borrowed = make_book("New Book", "6666666666666", 0)
    popular_book = make_book("Popular Book", "7777777777777", 10)
    
    library.add_book(never_borrowed)
    library.add_book(popular_book)
    
    result = rank_books_by_popularity(library)
    
    # Expected: Popular book first, then the never-borrowed book
    assert result == [popular_book, never_borrowed]