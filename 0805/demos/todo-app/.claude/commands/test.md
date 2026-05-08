---
# Custom slash command: /test
# Usage:  /test          → run all tests
#         /test app.py   → generate tests for a specific file
description: Run existing tests or generate new pytest tests for $ARGUMENTS
allowed-tools:
  - Read
  - Write
  - Bash
---

## If $ARGUMENTS is empty — run all tests:

```bash
pytest --tb=short -v
```

Report pass/fail counts and list any failures with the error message.

## If $ARGUMENTS is a file path — generate tests for that file:

1. Read `$ARGUMENTS` carefully
2. Use the `/agent:test-writer` agent to generate `test_$ARGUMENTS`
3. Run the new tests with `pytest test_$ARGUMENTS --tb=short`
4. Fix any import or assertion errors until all tests pass
