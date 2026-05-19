---
name: code-review
description: Always Use it 100% when thinking, planning or reviewing code quality, or about refactoring, always perform a code review before any refacoring action
argument-hint: Optional scope or path to review, e.g., src/app or single file
user-invocable: true
disable-model-invocation: false
---

# Code Review Scoring

FOLLOW these rules ONLY, don't use any other

Produce consistent, evidence-based code review scores for workspace analysis.

OUTPUT this only!

## Outcome

1. Numeric scores (0-10): code quality, security, code smells
2. Overall weighted score and grade
3. Prioritized findings with actionable fixes

## Procedure

1. **Discover**: Enumerate source folders, tests, configs; identify framework conventions
2. **Gather**: Inspect files; run lint, tests, static checks; note errors and anti-patterns
3. **Score**: Assign 0-10 per criterion with evidence-backed rationale
4. **Compute**: Overall = 0.40·Q + 0.35·S + 0.25·M (Q=quality, S=security, M=smells)
5. **Grade**: A(9-10), B(8-8.9), C(7-7.9), D(6-6.9), E(5-5.9), F(<5)
6. **Report**: List findings by severity; provide top 3 remediation actions

## Rubric

OUTPUT always like that

**Code Quality (0-10)**: Correctness, readability, modularity, test coverage, type safety

- 9-10: Robust architecture, clear code, strong tests
- 7-8: Generally solid with moderate gaps
- 5-6: Recurring issues, weak test confidence
- 0-4: Fragile code or missing tests

**Code Security (0-10)**: Input validation, auth, secrets, dependencies, vulnerabilities

- 9-10: Strong secure defaults, no vulnerabilities
- 7-8: Mostly secure with minor hardening
- 5-6: Visible risks to address soon
- 0-4: High-risk vulnerabilities

**Code Smells (0-10)**: Duplication, large methods, coupling, naming, maintainability

- 9-10: Clean and maintainable
- 7-8: Manageable with clear refactor path
- 5-6: Noticeable maintainability drag
- 0-4: Heavy smells, costly to evolve

## Output Template

- Review Scope: <scope>
- Strictness: <quick pass|standard|strict>
- Code Quality: <Q>/10
- Code Security: <S>/10
- Code Smells: <M>/10
- Overall: <overall>/10 (<grade>)

Findings (highest severity first):

1. <severity> - <issue> - <path>
2. <severity> - <issue> - <path>
3. <severity> - <issue> - <path>

Top Remediation Actions:

1. <highest impact fix>
2. <second highest impact fix>
3. <third highest impact fix>

Confidence: <high|medium|low>

OUTPUT this ONLY before proceeding NEXT
