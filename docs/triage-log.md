# Triage Log — Library Management System

## Date: August 25, 2026

## Issues Ranked by Fix Priority

| Rank | Issue | Title | Severity | Priority | Rationale |
|------|-------|-------|----------|----------|-----------|
| 1 | #5 | System allows multiple books with same ISBN | High | P1 | Data integrity violation; ISBN must be unique |
| 2 | #1 | Borrowing an already borrowed book crashes | High | P1 | Core functionality broken; user cannot borrow |
| 3 | #2 | Creating a book with empty ISBN is allowed | Medium | P2 | Data quality issue; should be fixed |
| 4 | #3 | Returning a book that is not borrowed gives unhelpful error | Medium | P3 | Usability issue; low impact |
| 5 | #4 | Search for books is case-sensitive | Low | P3 | Usability issue; can be deferred |

---

## Trade-off Analysis

### Issue #5 vs Issue #1

Both issues have **High Severity** and **P1 Priority**, but Issue #5 is ranked first because:

- **Issue #5 (Duplicate ISBN)** affects **data integrity** — multiple books with the same ISBN cause catalog confusion and search errors.
- **Issue #1 (Borrow already borrowed)** affects **core functionality** — users can't borrow books, but the error is still somewhat handled.

**Trade-off:** Data integrity is more critical because it affects the entire system's reliability. Fixing duplicate ISBN ensures data quality, while borrowing can still be done correctly the first time.

---

### Issue #2 vs Issue #3

Both issues have **Medium Severity**, but different priorities:

- **Issue #2 (Empty ISBN)** — Priority P2 because empty ISBN can cause search and catalog problems later.
- **Issue #3 (Return not borrowed)** — Priority P3 because the error is correct, just not user-friendly.

**Trade-off:** Data quality (Empty ISBN) is more important than user experience (unhelpful error message). Empty ISBN can cause bigger problems later.

---

## Issues NOT Fixed in This Sprint

### Issue #3 — Returning a book that is not borrowed gives unhelpful error

**Label:** `status:wontfix`

**Reason:** The error message is technically correct, just not user-friendly. This does not affect core functionality. Users can still borrow and return books successfully. Will be fixed in a future sprint when we improve error handling.

---

### Issue #4 — Search for books is case-sensitive

**Label:** `status:wontfix`

**Reason:** This is a usability enhancement, not a critical bug. Users can work around it by using correct case. Search functionality is not the primary feature of the system. Will be fixed in a future sprint when we add proper search features.

---

## Summary

| Issue | Decision |
|-------|----------|
| #5 — Duplicate ISBN allowed | ✅ Fix this sprint (Highest priority) |
| #1 — Borrow already borrowed | ✅ Fix this sprint |
| #2 — Empty ISBN allowed | ✅ Fix this sprint |
| #3 — Return not borrowed | ❌ WONTFIX (Deferred) |
| #4 — Case-sensitive search | ❌ WONTFIX (Deferred) |