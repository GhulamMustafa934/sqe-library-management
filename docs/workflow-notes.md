# Workflow Notes

## Task 3 — Deliberate Merge Conflict

### What Caused the Conflict?

Two branches changed the same docstring line in `book.py`:

| Branch | Change |
|--------|--------|
| `feature/conflict-demo` | Changed docstring to "A class representing a book in the LIBRARY system." |
| `feature/conflict-demo-2` | Changed docstring to "A class representing a book in the LIBRARY MANAGEMENT system." |

### How We Resolved It

We kept the second version: "A class representing a book in the LIBRARY MANAGEMENT system."


## Task 4 — Commit Hygiene Audit

### Git Log (Last 10 Commits)
cb192ed (HEAD -> main, origin/main, origin/HEAD, feature/conflict-demo-2) Merge branch 'main' into feature/conflict-demo-20a18493 docs: add screenshot for merge conflict
d32448b Merge pull request #12 from GhulamMustafa934/feature/conflict-demo-2
31ae153 Merge branch 'main' into feature/conflict-demo-2
68eaae7 Merge pull request #11 from GhulamMustafa934/feature/conflict-demo
2508137 (origin/feature/conflict-demo-2) feat: change docstring to LIBRARY MANAGEMENT system
7299a49 (origin/feature/conflict-demo, feature/conflict-demo) feat: change docstring to LIBRARY system
dfc313d Merge pull request #10 from GhulamMustafa934/feature/rename-field-b
657d3ba (origin/feature/rename-field-b, feature/rename-field-b) feat: rename isbn to catalog_number
274059e Merge pull request #8 from GhulamMustafa934/feature/rename-field-a


### Weak Commit Messages and Improvements

#### Weak Commit 1:
**Original:** `Merge branch 'main' into feature/conflict-demo-2`

**Rewritten:** `chore: merge main into feature/conflict-demo-2 to resolve conflicts`

**Why it's better:** The original is vague and doesn't explain why the merge was needed. The rewritten version clarifies it was to resolve conflicts.

#### Weak Commit 2:
**Original:** `docs: add screenshot for merge conflict`

**Rewritten:** `docs: add screenshot of merge conflict resolution in workflow-notes.md`

**Why it's better:** The rewritten version specifies exactly what screenshot was added and where, making it more descriptive.