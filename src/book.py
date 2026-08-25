class Book:
    """A class representing a book in the library."""

    _existing_isbns = set()  # Track all ISBNs

    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a Book object.

        Args:
            title: Book title
            author: Book author
            isbn: ISBN number

        Raises:
            ValueError: If ISBN is empty or already exists
        """
        if not isbn:
            raise ValueError("ISBN cannot be empty")
        if isbn in Book._existing_isbns:
            raise ValueError(f"Book with ISBN '{isbn}' already exists")
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        Book._existing_isbns.add(isbn)

    def borrow_book(self) -> None:
        """
        Mark the book as borrowed.

        Raises:
            ValueError: If the book is already borrowed
        """
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True

    def return_book(self) -> None:
        """
        Mark the book as returned.

        Raises:
            ValueError: If the book is not borrowed
        """
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")
        self.is_borrowed = False