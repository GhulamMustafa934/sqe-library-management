import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from library import Library
from book import Book


@pytest.fixture(autouse=True)
def reset_isbns():
    """Reset ISBN registry before and after each test."""
    Book.reset_isbns()
    yield
    Book.reset_isbns()


# =====================================================================
# TASK 4 — Parametrized Edge-Case Sweep for borrow_book()
# =====================================================================
#
# One consolidated test function covering 8 edge cases that would
# otherwise be 8 separate single-purpose tests.
#
# ids= documents each case clearly in pytest output.
# =====================================================================

@pytest.mark.parametrize(
    "setup_books, borrow_calls, expected_result, expected_count",
    [
        # 1. Borrow one book — happy path
        (
            [("Book A", "A1", "1000000000001", 1)],
            [("M1", "1000000000001")],
            None, 1,
        ),
        # 2. Borrow two books — same member
        (
            [
                ("Book A", "A1", "2000000000001", 1),
                ("Book B", "B1", "2000000000002", 1),
            ],
            [("M1", "2000000000001"), ("M1", "2000000000002")],
            None, 2,
        ),
        # 3. Borrow from a multi-copy book twice
        (
            [("Book A", "A1", "3000000000001", 3)],
            [("M1", "3000000000001"), ("M2", "3000000000001")],
            None, 1,  # only first member has 1
        ),
        # 4. Book not found in library
        (
            [],
            [("M1", "9999999999999")],
            "not found in library", 0,
        ),
        # 5. No available copies (single copy already borrowed)
        (
            [("Book A", "A1", "4000000000001", 1)],
            [("M1", "4000000000001"), ("M2", "4000000000001")],
            "has no available copies", 0,
        ),
        # 6. Member hits the 5-book limit (6th borrow fails)
        (
            [
                ("Book 1", "A", "5000000000001", 1),
                ("Book 2", "A", "5000000000002", 1),
                ("Book 3", "A", "5000000000003", 1),
                ("Book 4", "A", "5000000000004", 1),
                ("Book 5", "A", "5000000000005", 1),
                ("Book 6", "A", "5000000000006", 1),
            ],
            [
                ("M1", "5000000000001"),
                ("M1", "5000000000002"),
                ("M1", "5000000000003"),
                ("M1", "5000000000004"),
                ("M1", "5000000000005"),
                ("M1", "5000000000006"),   # 6th should fail
            ],
            "already has 5 books on loan", 5,
        ),
        # 7. Two members borrow the same single-copy book (2nd fails)
        (
            [("Book A", "A1", "6000000000001", 1)],
            [("M1", "6000000000001"), ("M2", "6000000000001")],
            "has no available copies", 0,
        ),
        # 8. Borrow 5 books — exactly at the limit (succeeds)
        (
            [
                ("Book 1", "A", "7000000000001", 1),
                ("Book 2", "A", "7000000000002", 1),
                ("Book 3", "A", "7000000000003", 1),
                ("Book 4", "A", "7000000000004", 1),
                ("Book 5", "A", "7000000000005", 1),
            ],
            [
                ("M1", "7000000000001"),
                ("M1", "7000000000002"),
                ("M1", "7000000000003"),
                ("M1", "7000000000004"),
                ("M1", "7000000000005"),
            ],
            None, 5,
        ),
    ],
    ids=[
        "borrow-single-book",
        "borrow-two-books-same-member",
        "borrow-multi-copy-book-twice",
        "book-not-found",
        "no-available-copies",
        "member-hits-5-book-limit",
        "two-members-same-single-copy",
        "borrow-exactly-5-books",
    ],
)
def test_borrow_book_edge_cases(setup_books, borrow_calls, expected_result, expected_count):
    """
    Consolidated parametrized test for Library.borrow_book() covering
    8 edge cases with clear ids.
    """
    # ---- Arrange ----
    library = Library()
    for title, author, isbn, copies in setup_books:
        library.add_book(Book(title, author, isbn, total_copies=copies))

    # ---- Act ----
    last_error = None
    for member_id, isbn in borrow_calls:
        try:
            library.borrow_book(member_id, isbn)
        except ValueError as e:
            last_error = str(e)

    # ---- Assert ----
    if expected_result is None:
        assert last_error is None, f"Expected success but got: {last_error}"
    else:
        assert last_error is not None, "Expected ValueError but no error was raised"
        assert expected_result in last_error

    # Check that the final borrow count for the last member matches
    if borrow_calls:
        last_member = borrow_calls[-1][0]
        # Count only if last_error is None (i.e., last call succeeded)
        if last_error is None:
            assert library.get_borrowed_books_count(last_member) == expected_count