# Code Review Checklist

## 1. Correctness
- [ ] Does the code actually do what the requirement says (e.g., boundary conditions)?
- [ ] Are edge cases handled (e.g., empty library, member not found)?

## 2. Tests
- [ ] Are there unit tests for the new logic?
- [ ] Do the tests actually verify the behavior, or are they just asserting the implementation?

## 3. Readability
- [ ] Are variable and function names clear and descriptive?
- [ ] Is there a docstring explaining what the function does?

## 4. Design
- [ ] Does this fit the existing architecture (e.g., using the Library class properly)?
- [ ] Is there any unnecessary duplication that should be extracted?

## 5. Risk
- [ ] Are there any potential security or performance issues?
- [ ] Will this break any existing functionality (backwards compatibility)?


## Lessons Learned

**Most Valuable Checklist Item:** The "Correctness" checklist item (specifically checking boundary conditions) caught the most valuable issue. It helped me identify the off-by-one error in the `borrow_percentile` function, which would have caused incorrect percentile calculations for the top-ranked members. 

**New Item to Add:** In the future, I would add a checklist item under "Risk" that specifically asks: *"Does the code handle empty collections or zero-division scenarios?"* This would have forced me to catch the missing empty-library test earlier.