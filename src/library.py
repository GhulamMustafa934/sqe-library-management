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
        """Initialize the library with empty book and member records."""
        self.books = {}          # isbn -> Book object  (DEF-009)
        self.member_books = {}   # member_id -> list of ISBNs

    def add_book(self, book) -> None:
        """
        Add a book to the library collection. (DEF-006)

        Args:
            book: Book object to add

        Raises:
            ValueError: If a book with the same ISBN already exists
        """
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN '{book.isbn}' already exists in library")
        self.books[book.isbn] = book

        def borrow_book(self, member_id: str, isbn: str) -> None:
        """
        Borrow a book for a member.

        Raises:
        ValueError: If book not found, already borrowed, or limit reached
        """
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN '{isbn}' not found in library")

        book = self.books[isbn]

        if book.is_borrowed:
            raise ValueError(f"Book '{book.title}' is already borrowed")

        if member_id not in self.member_books:
            self.member_books[member_id] = []

        if len(self.member_books[member_id]) >= 5:
            raise ValueError(f"Member {member_id} already has 5 books on loan")

        book.borrow_book()
        self.member_books[member_id].append(isbn)

    def return_book(self, member_id: str, isbn: str) -> None:
        """
        Return a book from a member.

        Args:
            member_id: Unique identifier for the member
            isbn: ISBN of the book to return

        Raises:
            ValueError: If member does not have this book on loan
        """
        if member_id not in self.member_books or isbn not in self.member_books[member_id]:
            raise ValueError(f"Member {member_id} does not have book '{isbn}' on loan")

        book = self.books[isbn]
        book.return_book()
        self.member_books[member_id].remove(isbn)

        def get_book_status(self, isbn: str) -> str:
        """
        Get the status of a book.

        Returns:
            "Borrowed" or "Available"
        """
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN '{isbn}' not found in library")
        book = self.books[isbn]
        return "Borrowed" if book.is_borrowed else "Available"

    def search_book(self, query: str) -> list:
        """
        Search books by title, author, or ISBN (case-insensitive). (DEF-007)

        Args:
            query: Search string

        Returns:
            List of matching Book objects
        """
        query = query.lower()
        results = []
        for book in self.books.values():
            if (query in book.title.lower() or
                query in book.author.lower() or
                query == book.isbn):
                results.append(book)
        return results

    def get_borrowed_books_count(self, member_id: str) -> int:
        """
        Get the number of books a member has on loan.

        Args:
            member_id: Unique identifier for the member

        Returns:
            Number of books on loan
        """
        return len(self.member_books.get(member_id, []))


def validate_isbn(isbn: str) -> bool:
    """
    Validate an ISBN string.

    Args:
        isbn: ISBN string to validate

    Returns:
        True if valid, False otherwise

    Raises:
        ValueError: If ISBN is empty, contains non-numeric characters,
                    or is not exactly 13 digits
    """
    if not isbn:
        raise ValueError("ISBN cannot be empty")

    if not isbn.isdigit():
        raise ValueError("ISBN must contain only numeric digits")

    if len(isbn) != 13:
        raise ValueError(f"ISBN must be exactly 13 digits (got {len(isbn)})")

    return True