class Book:
    """A class representing a book in the library."""

    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a Book object.

        Args:
            title: Book title
            author: Book author
            isbn: ISBN number
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self) -> None:
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