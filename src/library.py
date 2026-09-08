def fine_tier(days_overdue: int) -> str:
    """
    Map the number of days a book is overdue to a fine tier.

    Args:
        days_overdue: Number of days overdue (non-negative integer)

    Returns:
        Tier label: 'None', 'Low', 'Medium', 'High', or 'Severe'

    Raises:
        ValueError: If days_overdue is negative
    """
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")

    if days_overdue == 0:
        return 'None'
    elif 1 <= days_overdue <= 7:
        return 'Low'
    elif 8 <= days_overdue <= 14:
        return 'Medium'
    elif 15 <= days_overdue <= 30:
        return 'High'
    else:  # days_overdue >= 31
        return 'Severe'


class Library:
    """A class representing a library with book borrowing functionality."""

    def __init__(self):
        """Initialize the library with empty member records."""
        self.member_books = {}  # member_id -> list of borrowed book ISBNs

    def borrow_book(self, member_id: str, isbn: str) -> None:
        """
        Borrow a book for a member.

        Args:
            member_id: Unique identifier for the member
            isbn: ISBN of the book to borrow

        Raises:
            ValueError: If member already has 5 books on loan
        """
        # Initialize member's book list if not exists
        if member_id not in self.member_books:
            self.member_books[member_id] = []

        # Check if member already has 5 books
        if len(self.member_books[member_id]) >= 5:
            raise ValueError(f"Member {member_id} already has 5 books on loan")

        # Borrow the book
        self.member_books[member_id].append(isbn)

    def get_borrowed_books_count(self, member_id: str) -> int:
        """
        Get the number of books a member has on loan.

        Args:
            member_id: Unique identifier for the member

        Returns:
            Number of books on loan
        """
        return len(self.member_books.get(member_id, []))