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

        # ---------------------------------------------------------------
# BVA Tests for ISBN Length (must be exactly 13 digits)
# Boundaries: 11, 12, 13, 14, 15
# ---------------------------------------------------------------

@pytest.mark.parametrize('isbn', [
    "12345678901",      # 11 digits (too short)
    "123456789012",     # 12 digits (too short)
    "12345678901234",   # 14 digits (too long)
    "123456789012345",  # 15 digits (too long)
])
def test_validate_isbn_invalid_length(isbn):
    """BVA: ISBNs with lengths 11, 12, 14, 15 should raise ValueError."""
    with pytest.raises(ValueError):
        validate_isbn(isbn)


def test_validate_isbn_valid_length_13():
    """BVA: ISBN with exactly 13 digits should be valid."""
    assert validate_isbn("9780132350884") == True