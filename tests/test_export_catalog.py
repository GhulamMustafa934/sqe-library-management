import pytest
import sys
import os
from unittest.mock import call

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library, LibraryIOError
from book import Book


@pytest.fixture
def library_with_books():
    """Fresh library with two books for export tests."""
    Book.reset_isbns()
    library = Library()
    library.add_book(Book("Clean Code", "R. Martin", "9780132350884", total_copies=2))
    library.add_book(Book("Refactoring", "M. Fowler", "9780134757599", total_copies=3))
    yield library
    Book.reset_isbns()


# =====================================================================
# TASK 3 — Test 1: export_catalog() writes expected content (mocked open)
# =====================================================================

def test_export_catalog_writes_expected_content(mocker, library_with_books):
    """
    Mock built-in open() so no real file is written.
    Assert that write() was called with the expected CSV content.
    """
    # Arrange: mocker.mock_open() creates a mock that supports context manager
    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    # Act
    library_with_books.export_catalog("catalog.csv")

    # Assert: open() was called with the right path and mode
    mock_open.assert_called_once_with("catalog.csv", "w", encoding="utf-8")

    # Assert: write() was called with each expected line
    handle = mock_open()
    expected_calls = [
        call("Clean Code,R. Martin,9780132350884,2,0\n"),
        call("Refactoring,M. Fowler,9780134757599,3,0\n"),
    ]
    handle.write.assert_has_calls(expected_calls, any_order=True)


# =====================================================================
# TASK 3 — Test 2: export_catalog() raises LibraryIOError on OSError
# =====================================================================

def test_export_catalog_raises_library_io_error_on_oserror(mocker, library_with_books):
    """
    Mock open() to raise OSError.
    Assert that export_catalog() raises LibraryIOError (not raw OSError).
    """
    # Arrange
    mocker.patch("builtins.open", side_effect=OSError("Disk full"))

    # Act + Assert
    with pytest.raises(LibraryIOError) as exc_info:
        library_with_books.export_catalog("catalog.csv")

    # Assert: the custom error message includes the original cause
    assert "Failed to export catalog" in str(exc_info.value)
    assert "Disk full" in str(exc_info.value)


# =====================================================================
# TASK 3 — Extra: export_catalog() on empty library
# =====================================================================

def test_export_catalog_empty_library(mocker):
    """An empty library still creates the file (no write calls)."""
    Book.reset_isbns()
    library = Library()

    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    library.export_catalog("empty.csv")

    handle = mock_open()
    handle.write.assert_not_called()
    Book.reset_isbns()