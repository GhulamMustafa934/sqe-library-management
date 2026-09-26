import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library
from book import Book


@pytest.fixture(autouse=True)
def reset_isbns():
    """Reset the Book ISBN registry before and after each test."""
    Book.reset_isbns()
    yield
    Book.reset_isbns()


# ---------------------------------------------------------------
# EP Tests
# ---------------------------------------------------------------

@pytest.mark.parametrize('initial_books, member_id, expected_count', [
    (3, 'M001', 4),
])
def test_borrow_valid_limit(initial_books, member_id, expected_count):
    """Test that a member can borrow when under the limit."""
    library = Library()

    isbns = [f"10000000000{i:02d}" for i in range(initial_books + 1)]
    for i, isbn in enumerate(isbns):
        library.add_book(Book(f"Book {i}", "Author", isbn))

    for i in range(initial_books):
        library.borrow_book(member_id, isbns[i])

    library.borrow_book(member_id, isbns[initial_books])

    assert library.get_borrowed_books_count(member_id) == expected_count


def test_borrow_exceeds_limit():
    """Test that borrowing when at 5 books raises ValueError."""
    library = Library()
    member_id = "M002"

    isbns = [f"20000000000{i:02d}" for i in range(6)]
    for i, isbn in enumerate(isbns):
        library.add_book(Book(f"Book {i}", "Author", isbn))

    for i in range(5):
        library.borrow_book(member_id, isbns[i])

    with pytest.raises(ValueError) as exc_info:
        library.borrow_book(member_id, isbns[5])

    assert "already has 5 books on loan" in str(exc_info.value)


# ---------------------------------------------------------------
# BVA Tests for Borrow Limit
# ---------------------------------------------------------------

def test_borrow_at_4_books_allows_5th():
    """BVA: Member at 4 books can borrow a 5th."""
    library = Library()
    member_id = "BVA001"

    isbns = [f"30000000000{i:02d}" for i in range(5)]
    for i, isbn in enumerate(isbns):
        library.add_book(Book(f"Book {i}", "Author", isbn))

    for i in range(4):
        library.borrow_book(member_id, isbns[i])

    assert library.get_borrowed_books_count(member_id) == 4

    library.borrow_book(member_id, isbns[4])
    assert library.get_borrowed_books_count(member_id) == 5


def test_borrow_at_5_books_rejects_6th():
    """BVA: Member at 5 books cannot borrow a 6th."""
    library = Library()
    member_id = "BVA002"

    isbns = [f"40000000000{i:02d}" for i in range(6)]
    for i, isbn in enumerate(isbns):
        library.add_book(Book(f"Book {i}", "Author", isbn))

    for i in range(5):
        library.borrow_book(member_id, isbns[i])

    with pytest.raises(ValueError) as exc_info:
        library.borrow_book(member_id, isbns[5])

    assert "already has 5 books on loan" in str(exc_info.value)
    assert library.get_borrowed_books_count(member_id) == 5