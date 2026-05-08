# CLAUDE.md – Project Memory for Claude Code

<!--
  CLAUDE.md is read automatically by Claude Code at startup.
  It provides persistent project context, conventions, and instructions.

  File hierarchy (all are read & merged, more specific overrides less specific):
    ~/.claude/CLAUDE.md          → global user instructions (always loaded)
    <repo-root>/CLAUDE.md        → project-wide instructions
    <sub-folder>/CLAUDE.md       → folder-scoped instructions (loaded when cwd is inside)
    .claude/CLAUDE.md            → alternative project location (same as repo root)

  Use # @import path/to/file.md to import additional markdown files.
-->

## Project Overview

This is a Flask-based Todo application for demo/learning purposes.

- **Language**: Python 3.12+
- **Framework**: Flask
- **Storage**: JSON file (`todos.json`)
- **Templates**: Jinja2 in `templates/`

## Coding Conventions

- Use `camelCase` for variable and function names (project convention)
- All functions must start with `func_`
- Use `PascalCase` for class names
- Never hardcode secrets – use environment variables
- Validate all user input before processing

## Common Commands

```bash
# Run the dev server
python app.py

# Install dependencies
pip install -r requirements.txt
```

## Architecture Notes

- All routes live in `app.py`
- Static assets are served by Flask from `static/`
- `todos.json` is the persistence layer – treat it as ephemeral in tests

## Security Rules

- Never use `eval()` or `exec()`
- Always sanitize user-supplied strings before rendering
- Use parameterized patterns for any DB work

<!-- @import docs/architecture.md  ← example: import additional context files -->
