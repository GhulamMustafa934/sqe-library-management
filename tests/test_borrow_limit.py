import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library


@pytest.mark.parametrize('initial_books, member_id, expected_count', [
    (3, 'M001', 4),  # Valid: member at 3 books, borrow one more -> 4
])
def test_borrow_valid_limit(initial_books, member_id, expected_count):
    """Test that a member can borrow when under the limit."""
    library = Library()
    
    # Add initial books for the member
    for i in range(initial_books):
        library.borrow_book(member_id, f"ISBN-{i}")
    
    # Borrow one more book
    library.borrow_book(member_id, "ISBN-NEW")
    
    # Check the count
    assert library.get_borrowed_books_count(member_id) == expected_count


def test_borrow_exceeds_limit():
    """Test that borrowing when at 5 books raises ValueError."""
    library = Library()
    member_id = "M002"
    
    # Borrow 5 books (reach the limit)
    for i in range(5):
        library.borrow_book(member_id, f"ISBN-{i}")
    
    # Try to borrow a 6th book
    with pytest.raises(ValueError) as exc_info:
        library.borrow_book(member_id, "ISBN-5")
    
    assert "already has 5 books on loan" in str(exc_info.value)

    # ---------------------------------------------------------------
# BVA Tests for Borrow Limit (0-5 books valid)
# Boundaries: 4 (valid), 5 (max), 6 (invalid)
# ---------------------------------------------------------------

def test_borrow_at_4_books_allows_5th():
    """BVA: Member at 4 books can borrow a 5th (max allowed)."""
    library = Library()
    member_id = "BVA001"
    
    # Member at 4 books
    for i in range(4):
        library.borrow_book(member_id, f"ISBN-{i}")
    
    assert library.get_borrowed_books_count(member_id) == 4
    
    # Borrow 5th book (boundary: max allowed)
    library.borrow_book(member_id, "ISBN-5th")
    assert library.get_borrowed_books_count(member_id) == 5


def test_borrow_at_5_books_rejects_6th():
    """BVA: Member at 5 books cannot borrow a 6th (over limit)."""
    library = Library()
    member_id = "BVA002"
    
    # Member at 5 books (max)
    for i in range(5):
        library.borrow_book(member_id, f"ISBN-{i}")
    
    assert library.get_borrowed_books_count(member_id) == 5
    
    # Attempt to borrow 6th book (boundary: invalid)
    with pytest.raises(ValueError) as exc_info:
        library.borrow_book(member_id, "ISBN-6th")
    
    assert "already has 5 books on loan" in str(exc_info.value)
    assert library.get_borrowed_books_count(member_id) == 5  # unchanged


def test_borrow_at_6_books_rejects_7th():
    """BVA: Member at 6 books (forced invalid state) cannot borrow more."""
    library = Library()
    member_id = "BVA003"
    
    # Force member to 6 books directly (simulating a corrupted state)
    library.member_books[member_id] = [f"ISBN-{i}" for i in range(6)]
    
    # Attempt to borrow 7th book
    with pytest.raises(ValueError) as exc_info:
        library.borrow_book(member_id, "ISBN-7th")
    
    assert "already has 5 books on loan" in str(exc_info.value)