import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import validate_isbn


@pytest.mark.parametrize('isbn', [
    "9780132350884",  # Valid 13-digit ISBN
])
def test_validate_isbn_valid(isbn):
    """Test valid ISBN (exactly 13 numeric digits)."""
    assert validate_isbn(isbn) == True


@pytest.mark.parametrize('isbn', [
    "",                # Empty string
    "978013235",       # Too short
    "978-0132350884",  # Contains hyphen
    "9780132350884a",  # Contains letter
    "12345678901234",  # Too long (14 digits)
])
def test_validate_isbn_invalid(isbn):
    """Test invalid ISBNs."""
    with pytest.raises(ValueError):
        validate_isbn(isbn)