---
name: qa
description: use this skill to assure great code quality, functionality and security
---

## Your Tasks When Invoked

1. Identify functions without test coverage in the codebase.
2. For each uncovered function, generate tests:
   - 1 happy path test
   - 1 empty/null input test
   - 1 edge case test (boundary values)
   - 1 error case test (invalid inputs)

3. Test naming convention: `test_{function}_{condition}_{expected}`
4. Save the tests to the appropriate test file.
5. Run `python -m pytest -v` and fix failing tests.

## Rules

- Never change the existing source code
- Use pytest fixtures where appropriate
- Never test implementation details, only behavior` and fix failing tests.

## Rules

- Never change the existing source code
- Use pytest fixtures where appropriate
- Never test implementation details, only behavior
