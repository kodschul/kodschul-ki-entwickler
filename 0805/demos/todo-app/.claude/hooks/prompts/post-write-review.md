# Hook Prompt: Post-Write Review Instructions

<!--
  .claude/hooks/prompts/post-write-review.md
  ─────────────────────────────────────────────────────────────────────────────
  HOW THIS WORKS:
  A .md file cannot be a hook by itself — hooks must be executable commands.
  BUT you can use a hook shell command that READS this .md file and prints it
  to stdout. Claude receives stdout from hooks as injected context.

  This pattern lets you write your hook "prompt" in readable Markdown,
  then inject it at the right lifecycle moment without embedding a wall of
  text inside settings.json.

  Wire it up in settings.json like this:

    "PostToolUse": [
      {
        "matcher": "Write(**.py)",
        "hooks": [
          {
            "type": "command",
            "command": "cat .claude/hooks/prompts/post-write-review.md"
          }
        ]
      }
    ]

  Because the hook exits 0 (cat always succeeds), Claude is NOT blocked.
  The printed Markdown is injected as additional context for the next turn.
  ─────────────────────────────────────────────────────────────────────────────
-->

## Post-Write Instructions for Claude

You just wrote or modified a Python file. Before continuing, please:

1. **Re-read the file** you just wrote and verify it compiles correctly in your head
2. **Check naming conventions**:
   - Variables and functions → `camelCase`
   - Functions → must start with `func_`
   - Classes → `PascalCase`
3. **Security check** (quick scan):
   - No `eval()` or `exec()` calls
   - No hardcoded strings that look like passwords, tokens, or API keys
   - User inputs are validated before use
4. **If any issue is found**, fix it immediately in the same file without waiting to be asked.

Only proceed with the next task once these checks pass.
