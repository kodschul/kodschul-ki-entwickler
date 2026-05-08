---
# Custom slash command: /fix
# Usage:  /fix           → fix all linting + security warnings
#         /fix app.py    → fix only the given file
description: Auto-fix linting errors and apply safe security patches in $ARGUMENTS
allowed-tools:
  - Read
  - Write
  - Bash
---

Fix all auto-fixable issues in **$ARGUMENTS** (or the whole project if no argument given).

## Steps

1. Run `ruff check --fix $ARGUMENTS` to auto-fix safe linting issues
2. Run `ruff format $ARGUMENTS` to enforce consistent formatting
3. Read each file that was changed and verify the fixes look correct
4. For security issues flagged by `bandit` that cannot be auto-fixed:
   - Explain the issue inline as a `# SECURITY:` comment
   - Suggest the manual fix in a code block
5. Show a diff summary of all changes made
