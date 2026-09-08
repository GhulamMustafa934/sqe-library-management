<div align="center">

# 📚 SQE Library Management System

### A quality-first library management system built for the Software Quality Engineering course

[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Tested_with-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-D22128?style=for-the-badge&logo=apache&logoColor=white)](./LICENSE)
[![Status](https://img.shields.io/badge/Tests-14%2F14_Passing-2ECC71?style=for-the-badge&logo=checkmarx&logoColor=white)]()

</div>

---

## 📖 About

The **Library Management System** provides core functionality to manage books, members, and borrowing operations — built with **software quality engineering principles** at its core rather than as an afterthought.

This project was developed to demonstrate practical mastery of:

| Practice | Applied Through |
|---|---|
| 🔧 Version Control | Git & GitHub branching workflow |
| 🐞 Defect Tracking | Structured triage and prioritization |
| 📋 Test Planning | IEEE 829-compliant test plan |
| 🧩 Black-Box Testing | Equivalence Partitioning (EP) |
| 📝 Documentation | Full traceability from requirement to test |

---

## ✨ Features

- 📕 **Book Management** — Add, borrow, return, and search books
- 🔢 **ISBN Validation** — Enforces strict 13-digit numeric ISBN format
- 📊 **Borrow Limit** — Members can borrow between 0 and 5 books
- 💰 **Fine Calculation** — Tiered fine structure for overdue returns
- 👥 **Member Management** — Tracks borrowed books per member

---

## 🛠️ Built With

<div align="center">

| Tool | Purpose |
|:---:|:---|
| 🐍 **Python 3.14+** | Core logic & test implementation |
| ✅ **Pytest** | Unit testing & test automation |
| 🔀 **Git & GitHub** | Version control & collaboration |
| 📄 **Markdown** | Documentation & reporting |

</div>

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

### ✅ Prerequisites

- Python 3.14 or higher
- Pytest (for running tests)

### 📥 Installation

```bash
git clone https://github.com/GhulamMustafa934/sqe-library-management.git
cd sqe-library-management
pip install pytest
```

### ▶️ Running Tests

Run the full test suite:

```bash
pytest tests/ -v
```

Or run individual test files:

```bash
pytest tests/test_fine_tier.py -v
pytest tests/test_borrow_limit.py -v
pytest tests/test_validate_isbn.py -v
```

---

## 🧪 Test Coverage Summary

<div align="center">

| Test File | Test Cases | Status |
|---|:---:|:---:|
| `test_fine_tier.py` | 6 | ✅ Passing |
| `test_borrow_limit.py` | 2 | ✅ Passing |
| `test_validate_isbn.py` | 6 | ✅ Passing |
| **Total** | **14** | **✅ All Passing** |

</div>

> All tests are based on **Equivalence Partitioning (EP)** and validate both valid and invalid input classes.

---

## 📄 Documentation

All project documentation lives in the [`docs/`](./docs) folder:

| Document | Description |
|---|---|
| 📋 [`test-plan.md`](./docs/test-plan.md) | IEEE 829 Test Plan |
| 🧾 [`test-cases.md`](./docs/test-cases.md) | 12 detailed test cases with execution results |
| 🔗 [`rtm.md`](./docs/rtm.md) | Requirements Traceability Matrix (100% coverage) |
| 🧩 [`ep-analysis.md`](./docs/ep-analysis.md) | Equivalence Partitioning analysis |
| 🐞 [`triage-log.md`](./docs/triage-log.md) | Issue prioritization and triage decisions |
| 💭 [`workflow-notes.md`](./docs/workflow-notes.md) | Development workflow reflection |

---

## 👤 Contributors

<div align="center">

**Ghulam Mustafa**
<br>
BS Software Engineering · Sukkur IBA University

</div>

---

## 📜 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](./LICENSE) file for details.

<div align="center">

⭐ *If you found this project useful, consider giving it a star!* ⭐

</div>
