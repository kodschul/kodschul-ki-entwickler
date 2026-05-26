# Exercise: Token Management

**Time:** 60 min | **Project:** `1205/todo-app/`

---

## Task 1 – Compare Context Types (20 min)

Ask the same question three ways and compare the quality of responses:

**Question:** "How does todo saving work?"

**Variant A – @workspace:**

```
@workspace How does todo saving work?
```

**Variant B – #file:**

```
How does todo saving work? #file:app.py
```

**Variant C – #sym:**

```
How does #sym:func_save_todos work?
```

**Fill in the comparison table:**

| Variant   | Response time | Quality | Tokens (estimated) |
| --------- | ------------- | ------- | ------------------ |
| @workspace |              |         | High               |
| #file     |              |         | Medium             |
| #sym      |              |         | Low                |

**Conclusion:** When does each variant make sense?

---

## Task 2 – Slim Down copilot-instructions.md (15 min)

Open your `.github/copilot-instructions.md`:

```
Analyze and shorten my copilot-instructions.md:
- Goal: max 60 lines (currently: ___ lines)
- Remove: repetitions, obvious rules, detailed explanations
- Keep: project goal, commands, the most important DOs and DON'Ts
- Rules that belong in .instructions.md files → move there
```

**Observe:** Is the quality of Copilot suggestions still as good?

---

## Task 3 – Chat History vs. New Chat (15 min)

**Experiment:**

1. Open a chat with lots of history (from today)
2. Ask: "Add error handling to func_load_todos"
3. Note the response

4. Start a new chat (`+` New Chat)
5. Ask: "Add error handling to #sym:func_load_todos"
6. Note the response

**Compare:**

- Is the response different?
- How much faster is the new chat?
- Is the answer more precise?

---

## Task 4 – CLI Instead of Chat for Terminal Questions (10 min)

Instead of asking Copilot Chat, use the CLI for terminal questions:

```bash
# Instead of: "How do I run only tests with 'todo' in the name?"
gh copilot suggest "Run only pytest tests with 'todo' in the name"

# Instead of: "How do I show git log nicely formatted?"
gh copilot suggest -t git "Show last 10 commits with author and date"

# Instead of: "How do I find all Python files changed today?"
gh copilot suggest "Find all Python files modified today"
```

**Benefit:** These questions don't use Copilot Chat tokens.
