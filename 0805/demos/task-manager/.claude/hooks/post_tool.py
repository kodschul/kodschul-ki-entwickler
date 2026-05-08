"""
post_tool.py — Claude Code post-tool hook (skeleton)

This hook fires after every Claude tool call.
Participants will complete it to log tool usage and flag risky patterns.

Hook contract (Claude Code):
  - stdin:  JSON with keys: tool_name, tool_input, tool_response
  - stdout: anything written here is shown in the Claude Code UI
  - exit 0: hook passed, Claude continues
  - exit 1: hook failed, Claude is notified
"""

import json
import sys

# TODO: Import any extra stdlib modules you need (e.g. datetime, pathlib)


def func_parse_input():
    """Read and parse the JSON payload from stdin."""
    # TODO: Read sys.stdin, parse JSON, return dict
    pass


def func_check_risky_patterns(toolName, toolInput):
    """
    Return a list of warning strings if toolInput contains dangerous patterns.
    Examples to detect:
      - SQL strings without '?' placeholders
      - use of eval() or exec()
    """
    warnings = []
    # TODO: Implement pattern checks
    return warnings


def func_log_tool_call(toolName, warnings):
    """Append a one-line entry to security-log.md."""
    # TODO: Open security-log.md in append mode and write:
    #       [<timestamp>] <toolName> | warnings: <warnings>
    pass


def func_main():
    # TODO: Wire together parse → check → log
    # 1. Call func_parse_input()
    # 2. Extract tool_name and tool_input
    # 3. Call func_check_risky_patterns()
    # 4. Call func_log_tool_call()
    # 5. If warnings found, print them to stdout
    pass


if __name__ == "__main__":
    func_main()
