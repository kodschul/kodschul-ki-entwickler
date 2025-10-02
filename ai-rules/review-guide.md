Code Review Guide

Purpose

- Ensure correctness, readability, maintainability, security, and standards.
- Give respectful, actionable feedback.

Principles

- Be kind, specific, and actionable.
- Focus on code and outcomes, not people.
- Prefer simplicity and maintainability over cleverness.
- Prioritize high-impact issues.

Clean Code Means

- Readable names, simple control flow.
- Intent-revealing; minimal redundant comments.
- Small, focused functions and modules.
- Consistent with project conventions.
- Safe error handling and edge cases.
- Tested critical paths.
- Adequate docs for public APIs and changes.
- Performant enough; avoid obvious inefficiencies.
- Secure by default; no secrets in code.

Review Checklist

- Correctness: matches requirements; handles edge cases.
- Structure: no duplication; clear boundaries; early returns.
- Interfaces/Types: clear signatures; validation; avoid unsafe casts.
- Errors/Logging: purposeful handling; actionable logs.
- Tests: meaningful, deterministic, cover core behavior.
- Performance: reasonable complexity; measured when critical.
- Security/Privacy: sanitize inputs; least privilege; protect PII.
- Dependencies/Build: minimal, licensed, build/CI passes.
- Style: linters pass; no unrelated reformatting.
- Docs/DX: README and docstrings updated.

Severity

- Blocker: correctness, security, data loss, build breakage.
- High: major design or maintainability issues.
- Medium: style inconsistency, moderate test gaps.
- Low: nits and preferences.

Workflow

- Understand context: PR description, issues, commits.
- Evaluate design before code.
- Review implementation, then cross-cutting concerns.
- Provide concise, grouped, severity-tagged feedback.
- Collaborate, iterate, and approve when standards met.

If Not Clean

- Request refactors, tests, better handling, security fixes, and docs.
