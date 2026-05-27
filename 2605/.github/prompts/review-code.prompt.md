---
name: review-code
description: "Review code and report bugs, risks, regressions, and missing tests"
argument-hint: "What should be reviewed? (file, folder, diff, or feature)"
agent: agent
model: GPT-5.3-Codex (copilot)
---

# Review Code: ${input:review_target}

Perform a focused code review for ${input:review_target}.

Priorities:
1. Identify bugs and behavioral regressions.
2. Flag security, reliability, and performance risks.
3. Find missing or weak test coverage.
4. Note maintainability issues only if they can cause defects.

Output format:
1. Findings (ordered by severity)
   - For each finding include:
     - Severity: Critical, High, Medium, or Low
     - Location: file path and line
     - Why it matters
     - Concrete fix recommendation
2. Open questions and assumptions
3. Brief change summary
4. Suggested tests to add

Review rules:
- Cite exact locations when possible.
- Prefer actionable findings over stylistic feedback.
- If no issues are found, say so explicitly and list residual risks/testing gaps.