class Book:
    """A class representing a book in the library."""

    def __init__(self, title: str, author: str, book_id: str):
        """
        Initialize a Book object.

        Args:
            title: Book title
            author: Book author
            book_id: Book ID number
        """
        if not book_id:
            raise ValueError("Book ID cannot be empty")
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def borrow_book(self) -> None:
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True

    def return_book(self) -> None:
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")
        self.is_borrowed = False