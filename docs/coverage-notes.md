# Test Coverage Notes - Library Management System

## Task 1 - Baseline Coverage
- **Overall Line Coverage:** 84%
- **Overall Branch Coverage:** 50%


## Task 2 — Identify the Weakest Files

Based on the baseline HTML report, the weakest areas are:

1. **src/book.py (70% Coverage)**
   - **Missed Lines:** 20, 22, 24, 51, 62-64.
   - **Reason:** These are the error-handling branches (e.g., raising `ValueError` for empty ISBN, duplicate ISBN, invalid copies, and returning a book that wasn't borrowed).

2. **src/library.py (89% Coverage)**
   - **Missed Lines:** 71, 95-100, 105, 173->172, 178.
   - **Reason:** These are error paths for adding duplicate books, borrowing a book that doesn't exist, borrowing when no copies are left, returning a book not on loan, and the edge case for percentiles.



   ## Task 4 — Coverage vs. Quality Discussion

**The "Coverage Trap":**
The original version of `test_borrow_reduces_available_copies` simply asserted that the total available copies dropped to 5. While this executed the code and achieved 100% line coverage for the `borrow_book` method, it was a weak assertion. It only proved that *some* book was borrowed, but it didn't prove that the *correct* book was borrowed by the *correct* member.

A test that only checks for a broad state change (or just checks that "no exception was raised") is a coverage trap. It tricks you into thinking the code is fully tested, but a bug could easily swap the ISBN or the member ID, and the test would still pass. 

I strengthened the assertion by explicitly checking the book's status (`get_book_status`) and the specific member's borrow count (`get_borrowed_books_count`). This ensures the test verifies the actual business logic, not just that the function ran.