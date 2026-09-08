# Equivalence Partitioning Analysis — Library Management System

## 1. fine_tier(days_overdue)

| Class | Range | Valid/Invalid | Representative |
|-------|-------|---------------|----------------|
| None | 0 | ✅ Valid | 0 |
| Low | 1 to 7 | ✅ Valid | 4 |
| Medium | 8 to 14 | ✅ Valid | 10 |
| High | 15 to 30 | ✅ Valid | 20 |
| Severe | 31+ | ✅ Valid | 45 |
| Invalid | Negative numbers | ❌ Invalid | -3 |

## 2. Borrow Limit (Books on Loan)

**Business Rule:** A member may have between 0 and 5 books on loan simultaneously.

| Class | Range | Valid/Invalid | Representative |
|-------|-------|---------------|----------------|
| Valid | 0 to 5 books | ✅ Valid | 3 |
| Invalid | 6+ books | ❌ Invalid | 8 |

## 3. ISBN Validation

**Business Rule:** ISBN must be exactly 13 numeric digits, no letters or symbols.

| Class | Description | Valid/Invalid | Representative |
|-------|-------------|---------------|----------------|
| Valid 13-digit ISBN | Exactly 13 numeric digits | ✅ Valid | "9780132350884" |
| Empty string | No input | ❌ Invalid | "" |
| Too short | Less than 13 digits | ❌ Invalid | "978013235" |
| Contains letters/symbols | Non-numeric characters | ❌ Invalid | "978-0132350884" |

## 4. EP Limitation Note

Equivalence Partitioning is effective for reducing test cases by selecting one representative value per class. However, it has a **boundary-blind-spot** — it can miss off-by-one errors at the exact boundaries between classes. For example, EP would test 5 (valid) and 6 (invalid) but might miss the boundary at 5/6 where the actual code could have an off-by-one error. This limitation is addressed in Lab 6 using Boundary Value Analysis (BVA).



## 5. Pytest Run Summary

collected 14 items

tests/test_borrow_limit.py::test_borrow_valid_limit[3-M001-4]      PASSED                [7%]

tests/test_borrow_limit.py::test_borrow_exceeds_limit              PASSED                [14%]

tests/test_fine_tier.py::test_fine_tier_valid_classes[0-None]      PASSED                [21%]

tests/test_fine_tier.py::test_fine_tier_valid_classes[4-Low]       PASSED                [28%]

tests/test_fine_tier.py::test_fine_tier_valid_classes[10-Medium]   PASSED                [35%]

tests/test_fine_tier.py::test_fine_tier_valid_classes[20-High]     PASSED                [42%]

tests/test_fine_tier.py::test_fine_tier_valid_classes[45-Severe]   PASSED                [50%]

tests/test_fine_tier.py::test_fine_tier_negative_days_raises       PASSED                [57%]

tests/test_validate_isbn.py::test_validate_isbn_valid[9780132350884] PASSED              [64%]

tests/test_validate_isbn.py::test_validate_isbn_invalid[]           PASSED               [71%]

tests/test_validate_isbn.py::test_validate_isbn_invalid[978013235]  PASSED               [78%]

tests/test_validate_isbn.py::test_validate_isbn_invalid[978-0132350884] PASSED           [85%]

tests/test_validate_isbn.py::test_validate_isbn_invalid[9780132350884a] PASSED           [92%]

tests/test_validate_isbn.py::test_validate_isbn_invalid[12345678901234] PASSED           [100%]

============================== 14 passed in 0.20s ===============================

✅ **All EP tests passed successfully!**