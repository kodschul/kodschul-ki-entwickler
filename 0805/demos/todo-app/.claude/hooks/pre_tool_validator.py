#!/usr/bin/env python3
"""
.claude/hooks/pre_tool_validator.py  –  Python PreToolUse hook

Claude Code can call ANY executable as a hook — shell scripts, Python, Node, etc.
Python hooks are great when you need:
  - JSON parsing of the full tool input  (CLAUDE_TOOL_INPUT env var is JSON)
  - Complex validation logic
  - Cross-platform compatibility (no bash needed)
  - Reuse of existing Python project utilities

Environment variables Claude Code injects into every hook process:
  CLAUDE_TOOL_NAME               → e.g. "Bash", "Write", "Read", "WebFetch"
  CLAUDE_TOOL_INPUT              → full JSON string of the tool's input arguments
  CLAUDE_TOOL_INPUT_COMMAND      → shortcut: the command string (Bash tool only)
  CLAUDE_TOOL_INPUT_FILE_PATH    → shortcut: the file path  (Write/Read tool only)
  CLAUDE_TOOL_RESULT             → JSON result (PostToolUse only)
  CLAUDE_NOTIFICATION_MESSAGE    → message text (Notification event only)
  CLAUDE_STOP_REASON             → "end_turn" etc. (Stop event only)

Exit codes:
  0  → allow, proceed normally
  1  → block and show this script's stdout/stderr to Claude as context
  2  → block silently (Claude does not see output, just stops)

Stdout rules:
  - Anything printed to STDOUT is fed back to Claude as context (on block)
  - Anything printed to STDERR appears in the terminal for the user
"""

import json
import os
import re
import sys

# ── Read environment ──────────────────────────────────────────────────────────
toolName = os.environ.get("CLAUDE_TOOL_NAME", "")
toolInputJson = os.environ.get("CLAUDE_TOOL_INPUT", "{}")
toolInputCommand = os.environ.get("CLAUDE_TOOL_INPUT_COMMAND", "")
toolInputFilePath = os.environ.get("CLAUDE_TOOL_INPUT_FILE_PATH", "")

try:
    toolInput = json.loads(toolInputJson)
except json.JSONDecodeError:
    toolInput = {}

# ── Validation rules ──────────────────────────────────────────────────────────


def func_checkBashCommand(command: str) -> tuple[bool, str]:
    """
    Validate a Bash command before Claude runs it.
    Returns (allowed: bool, reason: str).
    """
    # Block destructive patterns
    blockedPatterns = [
        (r"rm\s+-rf\s+/", "Recursive delete of root filesystem"),
        (r"rm\s+-rf\s+~", "Recursive delete of home directory"),
        (r">\s*/dev/sd", "Direct disk write"),
        (r"mkfs\.", "Filesystem formatting"),
        (r"dd\s+if=.*of=/dev/", "Low-level disk copy"),
        (r"git\s+push\s+--force", "Force push blocked (use --force-with-lease instead)"),
        (r"git\s+reset\s+--hard\s+HEAD~[2-9]",
         "Hard reset of more than 1 commit"),
        (r"DROP\s+DATABASE", "SQL DROP DATABASE"),
        (r"DROP\s+TABLE", "SQL DROP TABLE"),
    ]

    for pattern, reason in blockedPatterns:
        if re.search(pattern, command, re.IGNORECASE):
            return False, reason

    # Warn on pip install without version pins in production context
    if re.search(r"pip\s+install\s+(?!-r)(?!\S+=)", command):
        print(
            f"[PYTHON HOOK] Advisory: unpinned pip install detected: {command}\n"
            "Consider using pinned versions for reproducibility.",
            file=sys.stderr,
        )
        # advisory only – don't block
    return True, ""


def func_checkWritePath(filePath: str) -> tuple[bool, str]:
    """
    Validate a file path before Claude writes to it.
    Returns (allowed: bool, reason: str).
    """
    # Never overwrite .env files
    if re.search(r"\.env(\.|$)", filePath):
        return False, f"Writing to .env files is blocked: {filePath}"

    # Never write outside the project directory
    projectRoot = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../.."))
    absPath = os.path.abspath(filePath)
    if not absPath.startswith(projectRoot):
        return False, f"Write outside project root blocked: {filePath}"

    return True, ""


# ── Dispatch ──────────────────────────────────────────────────────────────────

if toolName == "Bash":
    command = toolInput.get("command", toolInputCommand)
    allowed, reason = func_checkBashCommand(command)
    if not allowed:
        # Print to stdout → Claude sees this as context explaining the block
        print(
            f"[PYTHON HOOK] Blocked Bash command.\nReason: {reason}\nCommand: {command}")
        print("Please use a safer alternative.")
        sys.exit(2)  # silent block

elif toolName == "Write":
    filePath = toolInput.get("file_path", toolInputFilePath)
    allowed, reason = func_checkWritePath(filePath)
    if not allowed:
        print(f"[PYTHON HOOK] Blocked Write tool.\nReason: {reason}")
        sys.exit(2)

# Log all tool calls (PostToolUse also ends up here if wired that way)
logFile = os.path.join(os.path.dirname(__file__), "../audit.log")
try:
    with open(logFile, "a") as f:
        f.write(
            f"[PreToolUse] tool={toolName} file={toolInputFilePath} cmd={toolInputCommand[:80]}\n")
except OSError:
    pass

sys.exit(0)  # allow
