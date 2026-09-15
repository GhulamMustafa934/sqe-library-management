# Boundary Value Analysis — Library Management System

## 1. fine_tier(days_overdue)

| Boundary | value-1 | Expected at value-1 | value | Expected at value | value+1 | Expected at value+1 |
|----------|---------|---------------------|-------|-------------------|---------|---------------------|
| 0 (domain edge) | -1 | ValueError | 0 | None | 1 | Low |
| 0/1 (None → Low) | 0 | None | 1 | Low | 2 | Low |
| 7/8 (Low → Medium) | 7 | Low | 8 | Medium | 9 | Medium |
| 14/15 (Medium → High) | 14 | Medium | 15 | High | 16 | High |
| 30/31 (High → Severe) | 30 | High | 31 | Severe | 32 | Severe |

## 2. Borrow Limit (0–5 books)

| Boundary | value-1 | Expected at value-1 | value | Expected at value | value+1 | Expected at value+1 |
|----------|---------|---------------------|-------|-------------------|---------|---------------------|
| 5/6 (Valid → Invalid) | 4 | Allowed | 5 | Allowed | 6 | ValueError |

## 3. ISBN Length (13 digits)

| Boundary | value-1 | Expected at value-1 | value | Expected at value | value+1 | Expected at value+1 |
|----------|---------|---------------------|-------|-------------------|---------|---------------------|
| 13 (Valid length) | 12 | ValueError | 13 | Valid | 14 | ValueError |

## 4. BVA Limitation Note

BVA complements EP by testing the exact boundaries where defects are most likely. It catches off-by-one errors that EP alone might miss.

## 5. Defect Found Through BVA

### Defect #21 — Off-by-One Error in fine_tier at Boundary 15

| Item | Detail |
|------|--------|
| **Issue** | #21 |
| **Discovered by** | BVA test `test_fine_tier_boundaries[15-High]` |
| **Root cause** | Code used `15 < days_overdue <= 30` instead of `15 <= days_overdue <= 30` |
| **Impact** | Day 15 was incorrectly classified as 'Severe' instead of 'High' |
| **Fix** | Corrected the comparison operator on branch `fix/fine-tier-boundary` |
| **PR** | Merged and auto-closed Issue #21 via `Fixes #21` |
| **Severity** | High |
| **Priority** | P1 |

### Lesson Learned

This defect demonstrates why EP alone is insufficient — EP would test 14 (Medium) and 20 (High) but would miss the exact boundary at 15. BVA specifically targets boundaries, catching off-by-one errors that EP cannot detect.