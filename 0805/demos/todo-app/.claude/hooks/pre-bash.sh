#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# .claude/hooks/pre-bash.sh  –  PreToolUse hook for Bash commands
#
# Claude Code calls this script BEFORE executing any Bash tool call.
# Environment variables available:
#   CLAUDE_TOOL_NAME          → name of the tool (e.g. "Bash")
#   CLAUDE_TOOL_INPUT         → full JSON input to the tool
#   CLAUDE_TOOL_INPUT_COMMAND → the bash command string (for Bash tool)
#
# Exit codes:
#   0  → allow the tool call to proceed
#   1  → block with a warning (Claude sees the output as context)
#   2  → block SILENTLY (Claude does not see it, just stops)
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

COMMAND="${CLAUDE_TOOL_INPUT_COMMAND:-}"

# ── Block destructive commands ────────────────────────────────────────────────
BLOCKED_PATTERNS=(
  "rm -rf /"
  "rm -rf ~"
  "git push --force"
  "git reset --hard"
  "DROP TABLE"
  "DROP DATABASE"
  "> /dev/sda"
)

for pattern in "${BLOCKED_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qiF "$pattern"; then
    echo "[HOOK] Blocked dangerous command: $COMMAND" >&2
    exit 2   # silent block
  fi
done

# ── Warn on git push ──────────────────────────────────────────────────────────
if echo "$COMMAND" | grep -qE "^git push"; then
  echo "[HOOK] Warning: Claude is about to run: $COMMAND" >&2
  echo "[HOOK] To allow git push, remove the guard in .claude/hooks/pre-bash.sh" >&2
  exit 1   # block with explanation shown to Claude
fi

# Allow everything else
exit 0
