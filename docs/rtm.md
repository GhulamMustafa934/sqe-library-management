# Requirements Traceability Matrix (RTM) — Library Management System

| Requirement ID | Requirement Description | Test Case IDs |
|----------------|-------------------------|---------------|
| REQ-1 | The system shall allow adding a new book with title, author, and ISBN | TC-001, TC-012 |
| REQ-2 | The system shall reject a book with an empty ISBN | TC-003 |
| REQ-3 | The system shall reject a book whose ISBN already exists in the catalog | TC-002 |
| REQ-4 | The system shall allow borrowing a book if it is available | TC-004 |
| REQ-5 | The system shall reject borrowing a book that is already borrowed | TC-005, TC-010 |
| REQ-6 | The system shall allow returning a book that is currently borrowed | TC-006 |
| REQ-7 | The system shall reject returning a book that is not borrowed | TC-007, TC-011 |
| REQ-8 | The system shall display the current status of a book (borrowed/available) | TC-008, TC-009 |

## Traceability Summary

| Requirement | Linked Test Cases | Status |
|-------------|-------------------|--------|
| REQ-1 | TC-001, TC-012 | ✅ Covered |
| REQ-2 | TC-003 | ✅ Covered |
| REQ-3 | TC-002 | ✅ Covered |
| REQ-4 | TC-004 | ✅ Covered |
| REQ-5 | TC-005, TC-010 | ✅ Covered |
| REQ-6 | TC-006 | ✅ Covered |
| REQ-7 | TC-007, TC-011 | ✅ Covered |
| REQ-8 | TC-008, TC-009 | ✅ Covered |

## Coverage Analysis

| Total Requirements | 8 |
|---------------------|---|
| Requirements with Test Cases | 8 |
| Requirements without Test Cases | 0 |
| Coverage Percentage | **100%** |

✅ **All requirements are covered by at least one test case. No gaps found.**