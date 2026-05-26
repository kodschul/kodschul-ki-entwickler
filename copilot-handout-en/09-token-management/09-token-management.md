# 09 – Token Management

**Block:** 60 min | **Day 3**

---

## What is the Token Limit?

Every Copilot request has a **context window** – the amount of text (tokens) that can be processed per request.

```
Typical token budget per request: ~32,000–128,000 tokens
1 token ≈ 4 characters ≈ 0.75 words

A full app.py (200 lines) ≈ 1,500 tokens
@workspace on large codebase ≈ 10,000–50,000 tokens
1 hour of chat history ≈ 5,000–20,000 tokens
```

> When the budget is used up: **responses get worse** or **context is cut off**.

---

## Token Consumption by Context Type

| Context Type             | Token usage  | When to use                           |
| ------------------------ | ------------ | ------------------------------------- |
| `@workspace`             | Very high    | Searching the codebase                |
| `#file:large_file.py`    | High         | Only if the whole file is needed      |
| `#sym:func_name`         | Low          | When only one function is needed      |
| `#selection`             | Very low     | Currently selected text               |
| `#terminalLastCommand`   | Low          | Terminal output                       |
| Chat history (long)      | High         | Gets expensive fast                   |
| `copilot-instructions.md`| 200–500 tok. | Always active (keep short!)           |

---

## Strategy 1 – Targeted Context Instead of Everything

**Bad – too much context:**

```
❌ "@workspace Add error handling to the save function"
   → Copilot scans the entire codebase (unnecessary)

❌ "#file:app.py Explain the load_todos function"
   → Entire app.py loaded (unnecessary)
```

**Good – precise references:**

```
✅ "Add error handling to #sym:func_save_todos"
   → Only this function (few tokens)

✅ "#sym:func_load_todos Explain this function"
   → Only this symbol (few tokens)
```

**Comparison table:**

| Prompt                         | Tokens | Quality |
| ------------------------------ | ------ | ------- |
| `@workspace find todos`        | ~8,000 | Good    |
| `#file:app.py find todos`      | ~1,500 | Good    |
| `#sym:func_load_todos explain` | ~200   | Better  |

---

## Strategy 2 – Clear Chat Regularly

```
Chat history accumulates:
- Question 1 + Answer 1 = 500 tokens
- Question 2 + Answer 2 = 500 tokens
...
- After 20 exchanges: 10,000+ tokens ALWAYS in context
```

**Solution:** Start a **new chat** for each new topic.

```
⌘ Shift I → new Quick Chat   (fast, no history)
Chat → + (New Chat)           (clean slate)
```

---

## Strategy 3 – Keep copilot-instructions.md Lean

```markdown
❌ Too long (>100 lines):
# GitHub Copilot Instructions
## Detailed explanation of every Flask function...
## Complete architecture documentation...
## All edge cases...

✅ Good (<80 lines):
# GitHub Copilot Instructions
## Goal: Todo web app (Flask + Tailwind + todos.json)
## Start: FLASK_DEBUG=1 python app.py
## Test: python -m pytest
## Do: PRG pattern, type annotations
## Don't: no DB, no eval()
```

---

## Strategy 4 – Sharpen applyTo

```markdown
❌ Too broad – applies everywhere:
---
applyTo: "**"
---
# Flask Rules
Use PRG pattern...

✅ Only where needed:
---
applyTo: "**/app.py"
---
# Flask Rules
Use PRG pattern...
```

---

## Strategy 5 – Compact Prompts

```
❌ Long prompt:
"Please look at our project and explain all the functions
in app.py in great detail, especially focusing on how
the data loading, data saving, adding, and deleting work..."

✅ Short + precise:
"Explain #sym:func_load_todos – edge cases?"
```

---

## Strategy 6 – Inline Chat vs. Full Chat

| Scenario                       | Best choice       | Why                                      |
| ------------------------------ | ----------------- | ---------------------------------------- |
| Add docstring to one function  | Inline Chat `⌘ I` | Only current function in context         |
| Refactor one method            | Inline Chat `⌘ I` | Direct context, no chat history          |
| Analyze entire architecture    | Chat + #file      | Need multiple files                      |
| Debug error from terminal      | Chat + #terminalLastCommand | Context is the error          |
| Search for something in codebase | Chat + @workspace | Need search capability                |

---

## Strategy 7 – Specific Questions vs. Open-Ended

```
❌ Open-ended (expensive):
"What can you tell me about my project?"

✅ Specific (cheap):
"Does func_save_todos handle write errors?"
```

---

## Token-Saving Plan Summary

| Strategy                            | Saving potential  |
| ----------------------------------- | ----------------- |
| `#sym` instead of `#file`          | High (80%+)       |
| New chat per topic                  | High              |
| Short copilot-instructions.md       | Medium (always)   |
| Inline Chat for small changes       | High              |
| Specific question instead of open   | Medium            |
| Precise `applyTo`                   | Low               |

---

## gh copilot CLI – Token-Free Alternative

For terminal questions the CLI uses **separate quota** – not Copilot VS Code tokens:

```bash
# Free question (no Copilot Chat tokens!)
gh copilot suggest "Show all Python files that were changed in the last hour"

gh copilot explain "git log --since='1 hour ago' --name-only"
```
