# TDD Log — rank_books_by_popularity

## Cycle 1: Empty Catalog
- **RED**: `test(rank): red - empty catalog returns empty list` — [hash]
- **GREEN**: `feat(rank): green - stub rank_books_by_popularity returning []` — [hash]

## Cycle 2: Single Book
- **RED**: `test(rank): red - single book returns list with that book` — [hash]
- **GREEN**: `feat(rank): green - return all books (unsorted)` — [hash]
- **REFACTOR**: `refactor(rank): move isbn reset to pytest fixture` — [hash]

## Cycle 3: Descending Sort by Borrow Count
- **RED**: `test(rank): red - descending sort by borrow count` — [hash]
- **GREEN**: `feat(rank): green - implement descending sort by times borrowed` — [hash]
- **REFACTOR**: `refactor(rank): extract make_book helper for tests` — [hash]

## Cycle 4: Tie-Breaking
- **RED**: `test(rank): red - tie-breaker alphabetical by title` — [hash]
- **GREEN**: `feat(rank): green - implement tie-breaker by title` — [hash]
- **REFACTOR**: `refactor(rank): verify full regression suite passes` — [hash]

## Cycle 5: Edge Case (Never Borrowed)
- **RED**: `test(rank): red - edge case never borrowed mixed with borrowed` — [hash]
- **GREEN**: `feat(rank): green - edge case already handled by sort logic` — [hash]
- **REFACTOR**: `refactor(rank): extract sort key into helper function` — [hash]

## Reflection

TDD forced me to slow down and think about the design before writing the implementation. By writing the failing test first, I was able to clearly define the expected behavior of `rank_books_by_popularity()` at each step. The Red-Green-Refactor cycle kept the codebase clean and ensured that every piece of code had a corresponding test. Refactoring felt much safer because the test suite acted as a safety net. In the end, the TDD approach resulted in a more robust, testable, and well-documented feature compared to writing the implementation first.