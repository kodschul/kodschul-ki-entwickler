---
# Custom slash command: /commit
# Usage:  /commit               → commit all staged changes with an auto-generated message
#         /commit "feat: add X" → commit with the given message
description: Stage all changes and commit with a conventional commit message
allowed-tools:
  - Bash
---

1. Run `git diff --stat` to see what changed
2. Run `git add -A`
3. Generate a [Conventional Commits](https://www.conventionalcommits.org/) message:
   - `feat:` new feature
   - `fix:` bug fix
   - `refactor:` code change without feature/fix
   - `test:` adding tests
   - `docs:` documentation only
   - `chore:` maintenance
4. If `$ARGUMENTS` is provided, use it as the commit message directly
5. Run `git commit -m "<message>"`
6. Show the resulting `git log --oneline -3`
