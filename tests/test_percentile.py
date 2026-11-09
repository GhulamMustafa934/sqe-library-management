import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library, borrow_percentile
from book import Book

def test_borrow_percentile_multiple_members():
    library = Library()
    
    # Member 1 borrows 3 books
    for i in range(3):
        b = Book(f"Book {i}", "Author", f"11111111111{i}")
        library.add_book(b)
        library.borrow_book("M1", b.isbn)
        
    # Member 2 borrows 1 book
    b2 = Book("Book X", "Author", "2222222222222")
    library.add_book(b2)
    library.borrow_book("M2", b2.isbn)
    
    # M1 is ranked 1st (top), so their percentile should be 100
    # But due to the off-by-one bug, it will return 50.0
    assert borrow_percentile("M1", library) == 100.0