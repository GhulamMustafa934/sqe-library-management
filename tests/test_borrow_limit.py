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