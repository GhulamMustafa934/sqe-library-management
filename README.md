# SQE Library Management System

A comprehensive library management system developed for the **Software Quality Engineering (SQE)** course. This project demonstrates the application of software quality practices including version control, issue tracking, test planning, and black-box testing techniques.

---

## 📚 Project Overview

The Library Management System provides core functionality to manage books, members, and borrowing operations. It is designed with a focus on **software quality engineering principles**, including:

- Version control using Git and GitHub
- Defect tracking and triage
- Test planning and test case design
- Equivalence Partitioning (EP) for black-box testing
- Continuous integration and documentation

---

## ✨ Features

- **Book Management** – Add, borrow, return, and search books
- **ISBN Validation** – Enforces 13-digit numeric ISBN format
- **Borrow Limit** – Members can borrow between 0 and 5 books
- **Fine Calculation** – Overdue fines based on tiered structure
- **Member Management** – Track borrowed books per member

---

## 🛠️ Technologies

- **Python 3.14+** – Core logic and test implementation
- **Pytest** – Unit testing and test automation
- **Git & GitHub** – Version control and collaboration
- **Markdown** – Documentation and reporting

---


## 📁 Project Structure

```
sqe-library-management/
│
├── src/
│   └── library.py              # Core functions (fine_tier, validate_isbn, Library class)
│
├── tests/
│   ├── test_fine_tier.py       # EP tests for overdue fine tiers
│   ├── test_borrow_limit.py    # EP tests for borrow limit
│   └── test_validate_isbn.py   # EP tests for ISBN validation
│
├── docs/
│   ├── ep-analysis.md          # Equivalence Partitioning analysis
│   ├── test-plan.md            # IEEE 829 Test Plan
│   ├── test-cases.md           # 12 Test Cases with execution results
│   ├── rtm.md                  # Requirements Traceability Matrix
│   ├── triage-log.md           # Issue prioritization log
│   └── workflow-notes.md       # Workflow reflection
│
├── screenshots/                # Testing evidence and milestone screenshots
│
├── .github/
│   ├── ISSUE_TEMPLATE/         # Bug and feature request templates
│   └── workflows/              # CI/CD workflows (future)
│
├── README.md
├── LICENSE
└── .gitignore
```


---

## 🚀 Getting Started

### Prerequisites

- Python 3.14 or higher
- Pytest (for running tests)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/GhulamMustafa934/sqe-library-management.git
cd sqe-library-management
pip install pytest

Running Tests
Run the full test suite:

pytest tests/ -v

Run individual test files:
pytest tests/test_fine_tier.py -v
pytest tests/test_borrow_limit.py -v
pytest tests/test_validate_isbn.py -v


```
###🧪 Test Coverage Summary
- Test File	         Test Cases 	Status
- test_fine_tier.py	     6	      ✅ All Passing
- test_borrow_limit.py	 2	      ✅ All Passing
- test_validate_isbn.py	 6	      ✅ All Passing
- Total	                14	      ✅ All Passing

All tests are based on Equivalence Partitioning (EP) and validate both valid and invalid input classes.

---

### 📄 Documentation
- All project documentation is available in the docs/ folder:

- test-plan.md – IEEE 829 Test Plan

- test-cases.md – 12 detailed test cases with execution results

- rtm.md – Requirements Traceability Matrix (100% coverage)

- ep-analysis.md – Equivalence Partitioning analysis

- triage-log.md – Issue prioritization and triage decisions

- workflow-notes.md – Development workflow reflection


---

## 👤 Contributors

- **Ghulam Mustafa**
- BS Software Engineering
- Sukkur IBA University

---

📜 License
This project is licensed under the Apache License 2.0 – see the LICENSE file for details.
