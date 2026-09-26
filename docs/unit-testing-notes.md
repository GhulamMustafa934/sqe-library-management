# Unit Testing Notes — pytest Output and Fixture Scopes

## 1. Verbose vs Short Traceback Output

### `pytest -v tests/` — Verbose Output

The `-v` (verbose) flag lists every test individually with its full ID and PASSED/FAILED status.

```
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Ghulam Mustafa\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: D:\5TH sem\SQE\SQE lab\Lab 2\sqe-library-management
plugins: anyio-4.12.1, mock-3.15.1
collected 66 items

tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[borrow-single-book] PASSED [ 1%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[borrow-two-books-same-member] PASSED [ 3%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[borrow-multi-copy-book-twice] PASSED [ 4%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[book-not-found] PASSED [ 6%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[no-available-copies] PASSED [ 7%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[member-hits-5-book-limit] PASSED [ 9%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[two-members-same-single-copy] PASSED [ 10%]
tests/test_borrow_book_parametrized.py::test_borrow_book_edge_cases[borrow-exactly-5-books] PASSED [ 12%]
tests/test_borrow_limit.py::test_borrow_valid_limit[3-M001-4] PASSED [ 13%]
tests/test_borrow_limit.py::test_borrow_exceeds_limit PASSED [ 15%]
tests/test_borrow_limit.py::test_borrow_at_4_books_allows_5th PASSED [ 16%]
tests/test_borrow_limit.py::test_borrow_at_5_books_rejects_6th PASSED [ 18%]
tests/test_export_catalog.py::test_export_catalog_writes_expected_content PASSED [ 19%]
tests/test_export_catalog.py::test_export_catalog_raises_library_io_error_on_oserror PASSED [ 21%]
tests/test_export_catalog.py::test_export_catalog_empty_library PASSED [ 22%]
tests/test_fine_tier.py::test_fine_tier_boundaries[0-None] PASSED [ 24%]
tests/test_fine_tier.py::test_fine_tier_boundaries[1-Low] PASSED [ 25%]
tests/test_fine_tier.py::test_fine_tier_boundaries[7-Low] PASSED [ 27%]
tests/test_fine_tier.py::test_fine_tier_boundaries[8-Medium] PASSED [ 28%]
tests/test_fine_tier.py::test_fine_tier_boundaries[14-Medium] PASSED [ 30%]
tests/test_fine_tier.py::test_fine_tier_boundaries[15-High] PASSED [ 31%]
tests/test_fine_tier.py::test_fine_tier_boundaries[30-High] PASSED [ 33%]
tests/test_fine_tier.py::test_fine_tier_boundaries[31-Severe] PASSED [ 34%]
tests/test_fine_tier.py::test_fine_tier_valid_classes[0-None] PASSED [ 36%]
tests/test_fine_tier.py::test_fine_tier_valid_classes[4-Low] PASSED [ 37%]
tests/test_fine_tier.py::test_fine_tier_valid_classes[10-Medium] PASSED [ 39%]
tests/test_fine_tier.py::test_fine_tier_valid_classes[20-High] PASSED [ 40%]
tests/test_fine_tier.py::test_fine_tier_valid_classes[45-Severe] PASSED [ 42%]
tests/test_fine_tier.py::test_fine_tier_negative_days_raises[-3] PASSED [ 43%]
tests/test_fine_tier.py::test_fine_tier_negative_days_raises[-1] PASSED [ 45%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[0-None0] PASSED [ 46%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[1-Low0] PASSED [ 48%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[0-None1] PASSED [ 50%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[1-Low1] PASSED [ 51%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[2-Low] PASSED [ 53%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[7-Low] PASSED [ 54%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[8-Medium] PASSED [ 56%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[9-Medium] PASSED [ 57%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[14-Medium] PASSED [ 59%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[15-High] PASSED [ 60%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[16-High] PASSED [ 62%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[30-High] PASSED [ 63%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[31-Severe] PASSED [ 65%]
tests/test_fine_tier_bva.py::test_fine_tier_boundaries[32-Severe] PASSED [ 66%]
tests/test_fine_tier_bva.py::test_fine_tier_negative_raises PASSED [ 68%]
tests/test_library_catalog.py::test_total_available_copies_empty_catalog PASSED [ 69%]
tests/test_library_catalog.py::test_total_available_copies_single_book PASSED [ 71%]
tests/test_library_catalog.py::test_total_available_copies_multiple_books PASSED [ 72%]
tests/test_library_catalog.py::test_total_available_copies_after_borrow PASSED [ 74%]
tests/test_library_catalog.py::test_borrow_reduces_available_copies PASSED [ 75%]
tests/test_library_catalog.py::test_get_book_status_available PASSED [ 77%]
tests/test_library_catalog.py::test_get_book_status_borrowed PASSED [ 78%]
tests/test_library_catalog.py::test_search_book_by_title PASSED [ 80%]
tests/test_library_catalog.py::test_search_book_by_author PASSED [ 81%]
tests/test_library_catalog.py::test_empty_library_search_returns_empty_list PASSED [ 83%]
tests/test_validate_isbn.py::test_validate_isbn_valid[9780132350884] PASSED [ 84%]
tests/test_validate_isbn.py::test_validate_isbn_invalid[] PASSED [ 86%]
tests/test_validate_isbn.py::test_validate_isbn_invalid[978013235] PASSED [ 87%]
tests/test_validate_isbn.py::test_validate_isbn_invalid[978-0132350884] PASSED [ 89%]
tests/test_validate_isbn.py::test_validate_isbn_invalid[9780132350884a] PASSED [ 90%]
tests/test_validate_isbn.py::test_validate_isbn_invalid[12345678901234] PASSED [ 92%]
tests/test_validate_isbn.py::test_validate_isbn_invalid_length[12345678901] PASSED [ 93%]
tests/test_validate_isbn.py::test_validate_isbn_invalid_length[123456789012] PASSED [ 95%]
tests/test_validate_isbn.py::test_validate_isbn_invalid_length[12345678901234] PASSED [ 96%]
tests/test_validate_isbn.py::test_validate_isbn_invalid_length[123456789012345] PASSED [ 98%]
tests/test_validate_isbn.py::test_validate_isbn_valid_length_13 PASSED [100%]

================================================== 66 passed in 0.49s ===================================================
```

### `pytest --tb=short` — Short Traceback Output

The `--tb=short` flag reduces traceback output for failing tests to a short summary, showing only the essential lines instead of the full call stack.

```
============================= test session starts =============================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\5TH sem\SQE\SQE lab\Lab 2\sqe-library-management
plugins: anyio-4.12.1, mock-3.15.1
collected 66 items

tests/test_borrow_book_parametrized.py ........ [ 12%]
tests/test_borrow_limit.py .... [ 18%]
tests/test_export_catalog.py ... [ 22%]
tests/test_fine_tier.py .................. [ 45%]
tests/test_fine_tier_bva.py ............... [ 68%]
tests/test_library_catalog.py .......... [ 83%]
tests/test_validate_isbn.py ........... [100%]

============================== 66 passed in 0.65s ==============================
```

### When to Use Each

| Flag | When to Use |
|------|-------------|
| `-v` | During development — you want to see every test individually |
| `--tb=short` | In CI pipelines or when many tests fail — concise summary |
| `--tb=long` | Debugging a single failing test — full call stack |
| `--tb=no` | Only want pass/fail summary, no tracebacks |

**Combined:** `pytest -v --tb=short` gives visibility + compact failures.

---

## 2. Fixture Scopes

### `scope="function"` (default)

The fixture is rebuilt **for every test function**.

- **When to use:** When the test mutates the fixture's state (e.g. borrows books). Each test needs a fresh, isolated copy.
- **Example:** `populated_library` in `tests/test_library_catalog.py`

### `scope="module"`

The fixture is built **once per test file** and reused by all tests in that module.

- **When to use:** For expensive, read-only setup that no test mutates.
- **Example:** `book_catalog_data` in `tests/test_library_catalog.py`

### Other Scopes

| Scope | Built Once Per |
|-------|----------------|
| `function` | Test function (default) |
| `class` | Test class |
| `module` | Test file |
| `package` | Package |
| `session` | Entire pytest run |

### Rule of Thumb

- **Mutating state?** → `function`
- **Expensive & read-only?** → `module` or `session`

---

## 3. Test Configuration (`pytest.ini`)

The `pytest.ini` file configures pytest for the whole project.

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

| Setting | Purpose |
|---------|---------|
| `testpaths = tests` | Only search for tests in the `tests/` folder |
| `python_files = test_*.py` | Files matching `test_*.py` are test modules |
| `python_classes = Test*` | Classes starting with `Test` are tests |
| `python_functions = test_*` | Functions starting with `test_` are tests |

### Why This Matters for CI

Lab 14's CI pipeline will run `pytest` directly. With `pytest.ini` present:

- Only `tests/` is scanned
- Naming is consistent
- CI is fast and deterministic

---

## 4. Summary

| Topic | Takeaway |
|-------|----------|
| `-v` vs `--tb=short` | `-v` for visibility; `--tb=short` for CI |
| Fixture scope | `function` for mutation; `module` for expensive read-only |
| `pytest.ini` | Defines test discovery + naming for local & CI consistency |

---
