# Test Cases — Library Management System

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |
|----|-------|-------------|---------------|-------|----------|----------|------|
| TC-001 | Add book with valid ISBN | REQ-1 | None | 1. Create book: Book("Python 101", "John Doe", "978-0132350884") | Book is created successfully with title, author, and ISBN | High | Positive |
| TC-002 | Add book with duplicate ISBN | REQ-3 | Catalog already contains a book with ISBN "978-0132350884" | 1. Create book: Book("Duplicate Book", "Jane Doe", "978-0132350884") | ValueError is raised: "Book with ISBN '978-0132350884' already exists" | High | Negative |
| TC-003 | Add book with empty ISBN | REQ-2 | None | 1. Create book: Book("Test Book", "Test Author", "") | ValueError is raised: "ISBN cannot be empty" | High | Negative |
| TC-004 | Borrow book when available | REQ-4 | Book exists and is not borrowed: Book("Clean Code", "Robert Martin", "978-0132350884") | 1. Call book.borrow_book() | Book status becomes borrowed (is_borrowed = True) | High | Positive |
| TC-005 | Borrow book when already borrowed | REQ-5 | Book exists and is already borrowed (is_borrowed = True) | 1. Call book.borrow_book() again | ValueError is raised: "Book is already borrowed" | High | Negative |
| TC-006 | Return book that is currently borrowed | REQ-6 | Book exists and is currently borrowed (is_borrowed = True) | 1. Call book.return_book() | Book status becomes available (is_borrowed = False) | High | Positive |
| TC-007 | Return book that is not borrowed | REQ-7 | Book exists and is not borrowed (is_borrowed = False) | 1. Call book.return_book() | ValueError is raised: "Book is not borrowed" | Medium | Negative |
| TC-008 | Check book status when available | REQ-8 | Book exists and is not borrowed | 1. Check book.is_borrowed | Returns False (book is available) | Medium | Positive |
| TC-009 | Check book status when borrowed | REQ-8 | Book exists and is borrowed | 1. Check book.is_borrowed | Returns True (book is borrowed) | Medium | Positive |
| TC-010 | Verify borrowed book cannot be borrowed again | REQ-5 | Book exists and is borrowed | 1. Call book.borrow_book() | ValueError is raised: "Book is already borrowed" | Medium | Negative |
| TC-011 | Verify available book cannot be returned | REQ-7 | Book exists and is not borrowed | 1. Call book.return_book() | ValueError is raised: "Book is not borrowed" | Medium | Negative |
| TC-012 | Verify book attributes after creation | REQ-1 | None | 1. Create book: Book("Test Book", "Author", "978-1234567890") 2. Check title, author, isbn, is_borrowed | Title = "Test Book", Author = "Author", ISBN = "978-1234567890", is_borrowed = False | Low | Positive |