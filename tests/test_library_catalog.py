import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library
from book import Book


# =====================================================================
# FIXTURES
# =====================================================================
#
# FIXTURE SCOPE EXPLANATION
# ---------------------------------------------------------------------
# scope="function" (default): the fixture is rebuilt for EVERY test.
#   Use this when the test mutates the object (e.g. borrows books),
#   because we want a clean copy for each test.
#
# scope="module": the fixture is built ONCE per test file and reused
#   across all tests in that file. Use this for EXPENSIVE setup that
#   is read-only (e.g. loading a big catalog from disk, spinning up a
#   database, or building a large in-memory structure).
#
# =====================================================================


@pytest.fixture(scope="module")
def book_catalog_data():
    """
    EXPENSIVE / read-only fixture shared across the whole module.

    scope="module" is appropriate here because building this catalog
    is expensive (or conceptually expensive) and no test mutates it.
    Rebuilding it for every test would waste time.
    """
    return [
        {"title": "Clean Code", "author": "R. Martin", "isbn": "9780132350884", "copies": 2},
        {"title": "The Pragmatic Programmer", "author": "D. Thomas", "isbn": "9780135957059", "copies": 1},
        {"title": "Refactoring", "author": "M. Fowler", "isbn": "9780134757599", "copies": 3},
    ]


@pytest.fixture(scope="function")
def populated_library(book_catalog_data):
    """
    FRESH library for each test.

    scope="function" (default) is appropriate because tests borrow
    books, which mutates state. Each test needs a clean library.
    """
    Book.reset_isbns()
    library = Library()
    for entry in book_catalog_data:
        library.add_book(
            Book(entry["title"], entry["author"], entry["isbn"],
                 total_copies=entry["copies"])
        )
    yield library
    Book.reset_isbns()


@pytest.fixture
def empty_library():
    """An empty library for edge-case tests."""
    Book.reset_isbns()
    yield Library()
    Book.reset_isbns()


@pytest.fixture
def single_book_library():
    """A library with exactly one book (single copy)."""
    Book.reset_isbns()
    library = Library()
    library.add_book(Book("Clean Code", "R. Martin", "9780132350884", total_copies=1))
    yield library
    Book.reset_isbns()


# =====================================================================
# TASK 2: total_available_copies() — 3 REQUIRED TESTS
# =====================================================================

def test_total_available_copies_empty_catalog(empty_library):
    """Task 2 — Empty catalog: 0 available copies."""
    # Act
    result = empty_library.total_available_copies()
    # Assert
    assert result == 0


def test_total_available_copies_single_book(single_book_library):
    """Task 2 — Single book: 1 available copy."""
    # Act
    result = single_book_library.total_available_copies()
    # Assert
    assert result == 1


def test_total_available_copies_multiple_books(populated_library):
    """Task 2 — Multiple books: 2 + 1 + 3 = 6 available copies."""
    # Act
    result = populated_library.total_available_copies()
    # Assert
    assert result == 6


def test_total_available_copies_after_borrow(populated_library):
    """Extra: borrowing reduces total available copies."""
    populated_library.borrow_book("M001", "9780132350884")
    assert populated_library.total_available_copies() == 5


# =====================================================================
# Other tests using the shared fixture
# =====================================================================

def test_borrow_reduces_available_copies(populated_library):
    isbn = "9780132350884"
    populated_library.borrow_book("M001", isbn)
    assert populated_library.total_available_copies() == 5


def test_get_book_status_available(populated_library):
    assert populated_library.get_book_status("9780132350884") == "Available"


def test_get_book_status_borrowed(populated_library):
    isbn = "9780135957059"
    populated_library.borrow_book("M001", isbn)
    assert populated_library.get_book_status(isbn) == "Borrowed"


def test_search_book_by_title(populated_library):
    results = populated_library.search_book("clean")
    assert len(results) == 1
    assert results[0].title == "Clean Code"


def test_search_book_by_author(populated_library):
    results = populated_library.search_book("fowler")
    assert len(results) == 1
    assert results[0].author == "M. Fowler"


def test_empty_library_search_returns_empty_list(empty_library):
    assert empty_library.search_book("anything") == []