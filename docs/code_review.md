# Code Review — Library Management System

## 1. Review Objective

The purpose of this code review is to identify defects, missing functionality, validation problems, boundary conditions, and inconsistencies between the documented requirements and the current implementation.

The review covers the Library Management System source files, test plan, triage records, and automated tests.

---

## 2. Reviewed Components

The following components were reviewed:

* `src/book.py`
* `src/library.py`
* `src/calculator.py`
* `src/gradebook/gradebook.py`
* `docs/test-plan.md`
* `docs/test-cases.md`
* `docs/triage_log.md`
* Existing automated tests

---

# 3. Defects Identified

## DEF-001 — Borrowing an Already Borrowed Book

**Related Issue:** GitHub Issue #1

**Description:**
The system must prevent a book that is already borrowed from being borrowed again.

The `Book.borrow_book()` method contains a check for this condition:

```python
if self.is_borrowed:
    raise ValueError(f"Book '{self.title}' is already borrowed")
```

However, the Library-level borrowing implementation does not check the actual `Book` object's `is_borrowed` status. `Library.borrow_book()` only stores the ISBN in the member's list.

**Expected Behavior:**

Attempting to borrow an already borrowed book should raise a `ValueError`.

**Category:** Functional defect

**Severity:** High

**Priority:** P1

**Status:** Fix this sprint

---

## DEF-002 — Empty ISBN Validation

**Related Issue:** GitHub Issue #2

**Description:**
A book must not be created with an empty ISBN.

The current `Book.__init__()` implementation contains:

```python
if not isbn:
    raise ValueError("ISBN cannot be empty")
```

Therefore, the current implementation contains the required validation.

**Expected Behavior:**

```python
Book("Example", "Author", "")
```

should raise `ValueError`.

**Category:** Input validation

**Severity:** Medium

**Priority:** P2

**Status:** Verified / should remain covered by tests

---

## DEF-003 — Returning a Book That Is Not Borrowed

**Related Issue:** GitHub Issue #3

**Description:**
Returning a book that is not currently borrowed should produce a clear and useful error.

The current implementation correctly prevents the invalid operation:

```python
if not self.is_borrowed:
    raise ValueError(f"Book '{self.title}' is not borrowed")
```

However, this was identified during review as an error-message/usability issue.

**Category:** Error handling / usability

**Severity:** Medium

**Priority:** P3

**Status:** Deferred

---

## DEF-004 — Case-Sensitive Book Search

**Related Issue:** GitHub Issue #4

**Description:**
The documented system includes search functionality, but case-insensitive search behavior was identified as an issue.

Users should be able to search for a book without having to match the exact capitalization.

**Category:** Usability / Search

**Severity:** Low

**Priority:** P3

**Status:** Deferred

**Note:**
The current source code does not contain a search implementation, so this finding should also be treated as a missing-functionality issue until the search feature is implemented.

---

## DEF-005 — Duplicate ISBN Handling

**Related Issue:** GitHub Issue #5

**Description:**
ISBN values must be unique. Two different books should not be created with the same ISBN.

The current `Book` implementation uses:

```python
_existing_isbns = set()
```

and checks:

```python
if isbn in Book._existing_isbns:
    raise ValueError(f"Book with ISBN '{isbn}' already exists")
```

Therefore, duplicate ISBN protection is currently implemented at the `Book` level.

**Expected Behavior:**

Creating two books with the same ISBN should raise `ValueError`.

**Category:** Data integrity

**Severity:** High

**Priority:** P1

**Status:** Verified / should remain covered by tests

---

# 4. Missing Functionality Identified

## DEF-006 — `add_book()` Method Missing

**Description:**
The test plan explicitly identifies `add_book` as a required feature:

* REQ-1 — Add a new book with valid title, author, and ISBN

However, the current `Library` class does not contain an `add_book()` method.

The current `Library` implementation only provides:

```python
borrow_book()
get_borrowed_books_count()
```

There is no method for adding a `Book` to the library collection.

**Expected Behavior:**

The Library should provide functionality similar to:

```python
library.add_book(book)
```

and store the book so that it can later be borrowed, searched, and inspected.

**Category:** Missing functionality

**Severity:** High

**Priority:** P1

**Status:** Open

---

## DEF-007 — Book Search Functionality Missing

**Description:**
The test plan includes search-related functionality, and the previous review identified case-sensitive search as Issue #4.

However, the current `Library` class does not contain a search method.

There is no implementation such as:

```python
search_book()
```

or equivalent functionality.

**Expected Behavior:**

The Library should provide a method for finding books based on an appropriate search criterion, such as title, author, or ISBN.

**Category:** Missing functionality

**Severity:** Medium

**Priority:** P3

**Status:** Open / deferred

---

## DEF-008 — Book Status Functionality Missing

**Description:**
The test plan specifies:

> REQ-8 — Display current status of a book (borrowed/available)

The `Book` class internally maintains:

```python
self.is_borrowed = False
```

but there is no dedicated Library-level functionality for displaying or retrieving a book's current status.

**Expected Behavior:**

The system should provide a clear way to determine whether a book is:

* Available
* Borrowed

**Category:** Missing functionality

**Severity:** Medium

**Priority:** P2

**Status:** Open

---

## DEF-009 — Library Does Not Maintain a Book Collection

**Description:**
The `Library` class initializes only:

```python
self.member_books = {}
```

This stores ISBNs borrowed by members, but there is no collection of `Book` objects owned by the library.

Because of this, the Library cannot properly:

* Add books
* Search books
* Check a specific book's availability
* Connect an ISBN to its `Book` object
* Manage book state centrally

**Expected Behavior:**

The Library should maintain a collection of books, for example:

```python
self.books = {}
```

where ISBN can be used to identify a `Book`.

**Category:** Design / Missing functionality

**Severity:** High

**Priority:** P1

**Status:** Open

---

# 5. Fine Tier Boundary Findings

The `fine_tier()` function was also reviewed using Boundary Value Analysis.

The implementation currently defines:

| Days Overdue | Expected Tier |
| -----------: | ------------- |
|        `< 0` | ValueError    |
|          `0` | None          |
|        `1–7` | Low           |
|       `8–14` | Medium        |
|      `15–30` | High          |
|        `31+` | Severe        |

The important boundary values are:

```text
0
1
7
8
14
15
30
31
```

These values should be explicitly tested.

### Negative Input

Negative values should raise `ValueError`.

Example:

```python
def test_fine_tier_negative_days_raises():
    with pytest.raises(ValueError):
        fine_tier(-3)
```

### Boundary Tests

```python
@pytest.mark.parametrize('days,expected', [
    (0, 'None'),
    (1, 'Low'),
    (7, 'Low'),
    (8, 'Medium'),
    (14, 'Medium'),
    (15, 'High'),
    (30, 'High'),
    (31, 'Severe'),
])
def test_fine_tier_boundaries(days, expected):
    assert fine_tier(days) == expected
```

**Important:** These are test conditions, not automatically separate defects. A defect should only be reported if the implementation produces an incorrect result.

---

# 6. Documentation / Requirement Gaps

## DOC-001 — Test Plan and Implementation Are Not Fully Aligned

The test plan describes functionality including:

* Add book
* Borrow book
* Return book
* Search books
* Book status

However, the current implementation does not provide all of these features.

This creates a gap between the documented requirements and the implementation.

**Recommendation:**
Either implement the missing functionality or clearly document it as an open requirement/defect.

---

# 7. Summary of Findings

| ID      | Finding                              | Type                  | Severity | Status        |
| ------- | ------------------------------------ | --------------------- | -------- | ------------- |
| DEF-001 | Already borrowed book handling       | Functional            | High     | Fix           |
| DEF-002 | Empty ISBN validation                | Validation            | Medium   | Verified      |
| DEF-003 | Unhelpful return error               | Usability             | Medium   | Deferred      |
| DEF-004 | Case-sensitive search                | Usability             | Low      | Deferred      |
| DEF-005 | Duplicate ISBN handling              | Data Integrity        | High     | Verified      |
| DEF-006 | `add_book()` missing                 | Missing Functionality | High     | Open          |
| DEF-007 | Search functionality missing         | Missing Functionality | Medium   | Open/Deferred |
| DEF-008 | Book status functionality missing    | Missing Functionality | Medium   | Open          |
| DEF-009 | Library lacks book collection        | Design/Functionality  | High     | Open          |
| DOC-001 | Test plan vs implementation mismatch | Documentation         | Medium   | Open          |

---

# 8. Review Conclusion

The review identified both implemented validation behavior and gaps between the documented requirements and the current implementation.

Some previously reported issues are already addressed in the current source code, including empty ISBN validation, duplicate ISBN protection, and prevention of returning a book that is not borrowed.

However, important functionality described in the test plan is still missing from the current `Library` implementation, particularly `add_book()`, search functionality, book-status functionality, and centralized book storage.

Boundary Value Analysis should also be used to verify the `fine_tier()` function at every transition point.

All genuine implementation defects should be tracked through GitHub Issues, fixed on separate branches, tested, and submitted through Pull Requests. Missing functionality should be tracked separately as feature/enhancement work where appropriate.
