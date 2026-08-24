class Book:
    """A class representing a book in the LIBRARY system."""

    def __init__(self, title: str, author: str, catalog_number: str):
        """
        Initialize a Book object.

        Args:
            title: Book title
            author: Book author
            catalog_number: Catalog number
        """
        if not catalog_number:
            raise ValueError("Catalog number cannot be empty")
        self.title = title
        self.author = author
        self.catalog_number = catalog_number
        self.is_borrowed = False

    def borrow_book(self) -> None:
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True

    def return_book(self) -> None:
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")
        self.is_borrowed = False