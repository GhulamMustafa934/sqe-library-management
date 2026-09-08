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