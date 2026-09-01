# Test Plan — Library Management System (LibraryHub)

## 1. Introduction
This document defines the test strategy, scope, approach, resources, and schedule for testing the Library Management System (LibraryHub). The system provides core functionality to manage books, including adding, borrowing, and returning books. The objective is to validate that all functional requirements are correctly implemented and that the system behaves as expected under normal and error conditions.

## 2. Test Items
The following modules and components will be tested:
- Book class (`book.py`) — initialization, attributes, and validation
- `add_book` functionality — adding new books with ISBN validation
- `borrow_book` functionality — borrowing available books
- `return_book` functionality — returning borrowed books
- Book status checking — verifying borrowed/available status

## 3. Features to be Tested
| Req ID | Feature |
|--------|---------|
| REQ-1 | Add a new book with valid title, author, and ISBN |
| REQ-2 | Reject a book with an empty ISBN |
| REQ-3 | Reject a book with a duplicate ISBN |
| REQ-4 | Borrow a book that is available |
| REQ-5 | Reject borrowing a book that is already borrowed |
| REQ-6 | Return a book that is currently borrowed |
| REQ-7 | Reject returning a book that is not borrowed |
| REQ-8 | Display current status of a book (borrowed/available) |

All features listed above will be verified through functional test cases.

## 4. Features Not to be Tested
The following features are explicitly excluded from this test plan:
- **User Interface (UI):** This system is a library management module with a programmatic interface (Python class). UI testing is out of scope for this document. Testing will be performed at the API/function level using Python shell or test scripts.
- **Performance Testing:** Performance, load, and stress testing are not covered in this plan due to the small scale of the system.
- **Security Testing:** Authentication, authorization, and data encryption are not applicable to this module.

## 5. Approach
Testing will be conducted manually by executing test cases against the `book.py` module using a Python shell. Each test case will be executed step-by-step, and actual results will be compared against expected results. Any failures will be logged as GitHub Issues. The testing will focus on functional, negative, and edge-case scenarios to ensure robustness.

## 6. Pass/Fail Criteria
The testing phase will be considered successful if:
- **100%** of planned test cases are executed (12 out of 12)
- **90%** or more of test cases pass
- **Zero Critical** or High severity defects remain open
- All Medium severity defects are either fixed or documented with a workaround

## 7. Test Deliverables
The following documents will be produced as part of this testing effort:
- `docs/test-plan.md` — This document
- `docs/test-cases.md` — Detailed test cases with steps and expected results
- `docs/rtm.md` — Requirements Traceability Matrix
- Execution results recorded in test cases with Pass/Fail/Blocked status
- GitHub Issues for any defects found during testing

## 8. Environmental Needs
The following environment and tools are required for test execution:
- **Python 3.8+** — To execute the `book.py` module
- **Python Shell / Terminal** — For manual test execution
- **VS Code / Text Editor** — For viewing and editing test documents
- **GitHub** — For storing test artifacts and tracking defects
- **Git** — For version control and collaboration

## 9. Schedule
| Activity | Duration |
|----------|----------|
| Pre-Lab Setup | 15 minutes |
| Task 1 — Author Test Plan | 60 minutes |
| Task 2 — Write 12 Test Cases | 75 minutes |
| Task 3 — Requirements Traceability Matrix | 30 minutes |
| Task 4 — Manual Execution Pass | 35 minutes |
| **Total** | **3 hours 35 minutes** |

## 10. Risks and Mitigation
| Risk | Mitigation |
|------|------------|
| Code changes during testing | Freeze code version; work on a stable branch |
| Test environment not available | Use local Python environment; no external dependencies |
| Defects found late | File issues immediately and prioritize fixes |
| Time constraints | Prioritize high-priority test cases; defer non-critical cases |