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