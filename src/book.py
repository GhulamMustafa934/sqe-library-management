class Book:
    """A class representing a book in the library."""

    _existing_isbns = set()  # Track all ISBNs

    def __init__(self, title: str, author: str, isbn: str, total_copies: int = 1):
        """
        Initialize a Book object.

        Args:
            title: Book title
            author: Book author
            isbn: ISBN number
            total_copies: Total number of copies owned (default 1)

        Raises:
            ValueError: If ISBN is empty/duplicate or total_copies < 1
        """
        if not isbn:
            raise ValueError("ISBN cannot be empty")
        if isbn in Book._existing_isbns:
            raise ValueError(f"Book with ISBN '{isbn}' already exists")
        if total_copies < 1:
            raise ValueError("total_copies must be at least 1")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.borrowed_copies = 0
        Book._existing_isbns.add(isbn)

    @property
    def available_copies(self) -> int:
        """Return the number of copies not currently borrowed."""
        return self.total_copies - self.borrowed_copies

    def is_available(self) -> bool:
        """Return True if at least one copy is available."""
        return self.available_copies > 0

    def borrow_book(self) -> None:
        """
        Borrow one copy of the book.

        Raises:
            ValueError: If no copies are available
        """
        if self.available_copies <= 0:
            raise ValueError(f"Book '{self.title}' has no available copies")
        self.borrowed_copies += 1

    def return_book(self) -> None:
        """
        Return one copy of the book.

        Raises:
            ValueError: If no copies are currently borrowed
        """
        if self.borrowed_copies <= 0:
            raise ValueError(f"Book '{self.title}' has no borrowed copies to return")
        self.borrowed_copies -= 1

    @classmethod
    def reset_isbns(cls) -> None:
        """Reset the ISBN registry (used for testing)."""
        cls._existing_isbns.clear()