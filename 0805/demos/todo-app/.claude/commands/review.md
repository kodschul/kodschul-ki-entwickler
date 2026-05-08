---
# ─────────────────────────────────────────────────────────────────────────────
# .claude/commands/<name>.md  –  Custom slash command
#
# Invoked in Claude Code chat with:  /review
# Commands can accept arguments:     /review app.py
#
# The special variable $ARGUMENTS is replaced with whatever the user typed
# after the command name.
#
# Frontmatter keys:
#   description  – shown in the command picker
#   allowed-tools – restrict which tools may be used during this command
# ─────────────────────────────────────────────────────────────────────────────
description: Run a full security + quality code review on $ARGUMENTS (or all Python files)
allowed-tools:
  - Read
  - Bash
---

Please perform a comprehensive code review on **$ARGUMENTS** (if no argument given, review all `.py` files in the project).

## Steps

1. Read all relevant Python files
2. Run `ruff check . --output-format=concise` if ruff is available
3. Run `bandit -r . -ll` if bandit is available (security scan)
4. Report findings grouped by severity: CRITICAL → HIGH → MEDIUM → LOW
5. For each finding, show the file, line number, and a concrete fix suggestion
6. End with a summary table: total issues per severity level
