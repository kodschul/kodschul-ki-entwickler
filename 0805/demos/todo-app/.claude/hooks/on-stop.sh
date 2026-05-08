#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# .claude/hooks/on-stop.sh  –  Stop lifecycle hook
#
# Called when Claude finishes a turn (the "Stop" event).
# Use it for notifications, summaries, or cleanup.
#
# Environment variables available at Stop:
#   CLAUDE_STOP_REASON   → "end_turn" | "tool_use" | "max_tokens"
#   CLAUDE_NUM_TURNS     → number of turns in this session
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

REASON="${CLAUDE_STOP_REASON:-end_turn}"

# ── macOS desktop notification ────────────────────────────────────────────────
if command -v osascript &>/dev/null; then
  osascript -e "display notification \"Claude finished ($REASON)\" \
    with title \"Claude Code\" sound name \"Blow\"" 2>/dev/null || true
fi

# ── Terminal bell fallback ────────────────────────────────────────────────────
printf '\a'

exit 0
