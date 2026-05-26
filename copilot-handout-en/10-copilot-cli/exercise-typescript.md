# Exercise: Copilot CLI – TypeScript Angular

**Time:** 90 min | **Project:** Angular Todo App

---

## Task 1 – suggest for Shell Commands (15 min)

```bash
# Install (if not done yet)
gh extension install github/gh-copilot

# Basic suggest:
gh copilot suggest "Run Angular tests without a browser"
gh copilot suggest "Show all TypeScript files modified in the last hour"
gh copilot suggest "Build Angular app for production"
```

---

## Task 2 – suggest -t git (20 min)

```bash
# Git-specific commands:
gh copilot suggest -t git "Stage only TypeScript files"

gh copilot suggest -t git "Show commits from today"

gh copilot suggest -t git "Create a branch 'feature/due-dates'"

gh copilot suggest -t git "Undo last commit but keep changes"
```

---

## Task 3 – explain Commands (15 min)

```bash
# Explain Angular commands:
gh copilot explain "ng test --watch=false --browsers=ChromeHeadless"

gh copilot explain "ng build --configuration production --source-map=false"

gh copilot explain "ng generate component components/due-date --standalone"

# Explain build output:
gh copilot explain "ng build 2>&1 | grep -E 'Error|Warning'"
```

---

## Task 4 – Set Up Aliases (10 min)

```bash
# gh aliases:
gh alias set cs 'copilot suggest'
gh alias set ce 'copilot explain'

# Shell aliases in ~/.zshrc:
echo "alias ghcs='gh copilot suggest'" >> ~/.zshrc
echo "alias ghce='gh copilot explain'" >> ~/.zshrc
source ~/.zshrc

# Test:
ghcs "Run Angular tests in CI mode"
ghce "ng serve --open --port 4200"
```

---

## Task 5 – Build a Review Script (20 min)

Create `review.sh`:

```bash
#!/bin/bash
# review.sh – Angular Code Review

set -e

echo "========================================="
echo "  Angular Todo App Code Review"
echo "========================================="

echo ""
echo "--- Running Tests ---"
ng test --watch=false --browsers=ChromeHeadless 2>&1 | tail -20

echo ""
echo "--- TypeScript Check ---"
npx tsc --noEmit 2>&1 | tail -10

echo ""
echo "--- Security Review ---"
cat src/app/services/todo.service.ts | gh copilot explain \
  "Check this Angular service for security issues and best practices."

echo ""
echo "--- Next Steps ---"
gh copilot suggest \
  "I have an Angular 17 app with todos. What should I check next for production readiness?"
```

```bash
chmod +x review.sh
./review.sh
```

---

## Task 6 – CLI vs. Chat Comparison (10 min)

Answer the same question with CLI and with Copilot Chat:

**Question:** "How do I run only one specific Angular test?"

**CLI:**

```bash
gh copilot suggest "Run only one specific test in Angular with Karma"
```

**Chat:**

```
How do I run only the tests for TodoService? #file:src/app/services/todo.service.spec.ts
```

**Fill in the comparison table:**

| Aspect           | CLI                    | Chat                   |
| ---------------- | ---------------------- | ---------------------- |
| Speed            |                        |                        |
| Context quality  | No file context        | With #file             |
| Tokens used      | 0 Copilot tokens       | ~500 tokens            |
| Best for         | Terminal questions      | Code analysis          |
