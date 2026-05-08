#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# .claude/hooks/post-write.sh  –  PostToolUse hook for Write tool calls
#
# Runs AFTER Claude writes a file. Use it to auto-format, lint, or log.
#
# Environment variables:
#   CLAUDE_TOOL_NAME               → "Write"
#   CLAUDE_TOOL_INPUT_FILE_PATH    → absolute path of the written file
#   CLAUDE_TOOL_RESULT             → JSON result from the tool
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

FILE="${CLAUDE_TOOL_INPUT_FILE_PATH:-}"

if [[ -z "$FILE" ]]; then
  exit 0
fi

# ── Auto-format Python files with ruff ───────────────────────────────────────
if [[ "$FILE" == *.py ]]; then
  if command -v ruff &>/dev/null; then
    ruff format "$FILE" --quiet 2>/dev/null && \
      echo "[HOOK] Formatted: $FILE" >&2 || true
    ruff check "$FILE" --fix --quiet 2>/dev/null || true
  fi
fi

# ── Log all writes ────────────────────────────────────────────────────────────
LOG_FILE="$(dirname "$0")/../audit.log"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] WRITE: $FILE" >> "$LOG_FILE" 2>/dev/null || true

exit 0
