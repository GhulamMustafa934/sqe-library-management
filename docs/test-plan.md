# Test Plan — Library Management System

## 1. Introduction

This document defines the test strategy, scope, approach, and resources for testing the Library Management System (LibraryHub). The system provides functionality to manage books, including adding, borrowing, and returning books.

## 2. Test Items

The following modules will be tested:
- Book Management (add_book)
- Book Borrowing (borrow_book)
- Book Returning (return_book)
- Book Status Checking

## 3. Functional Requirements

| Req ID | Requirement |
|--------|-------------|
| REQ-1 | The system shall allow adding a new book with title, author, and ISBN. |
| REQ-2 | The system shall reject a book with an empty ISBN. |
| REQ-3 | The system shall reject a book whose ISBN already exists in the catalog. |
| REQ-4 | The system shall allow borrowing a book if it is available. |
| REQ-5 | The system shall reject borrowing a book that is already borrowed. |
| REQ-6 | The system shall allow returning a book that is currently borrowed. |
| REQ-7 | The system shall reject returning a book that is not borrowed. |
| REQ-8 | The system shall display the current status of a book (borrowed/available). |