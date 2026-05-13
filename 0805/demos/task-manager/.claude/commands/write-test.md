# /write-test — Generate a Python test for a given file or function

Generate a `pytest`-based test for the specified target.

## Instructions for Claude

1. Read the file or function the user specifies (default: `db.py` if none given).
2. For each public method, write a `pytest` test that:
   - Covers the happy path
   - Covers at least one edge case or error condition
3. Use an in-memory SQLite database (`":memory:"`) so tests are isolated and leave no files on disk.
4. Write the output to `tests/test_<filename>.py`, creating the `tests/` directory if it doesn't exist.
5. Do not mock the database — use a real in-memory connection to catch SQL errors.

## Usage

```
/write-test db.py
/write-test app.py
```
