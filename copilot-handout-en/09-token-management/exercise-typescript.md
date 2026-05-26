# Exercise: Token Management – TypeScript Angular

**Time:** 60 min | **Project:** Angular Todo App

---

## Task 1 – Compare Context Types (20 min)

Ask the same question three ways and compare the quality of responses:

**Question:** "How does saving a todo work?"

**Variant A – @workspace:**

```
@workspace How does saving a todo work?
```

**Variant B – #file:**

```
How does saving a todo work? #file:src/app/services/todo.service.ts
```

**Variant C – #sym:**

```
How does #sym:funcSaveTodo work?
```

**Fill in the comparison table:**

| Variant    | Response time | Quality | Tokens (estimated) |
| ---------- | ------------- | ------- | ------------------ |
| @workspace |               |         | High               |
| #file      |               |         | Medium             |
| #sym       |               |         | Low                |

**Conclusion:** When does each variant make sense?

---

## Task 2 – Slim Down copilot-instructions.md (15 min)

Open your `.github/copilot-instructions.md`:

```
Analyze and shorten my copilot-instructions.md:
- Goal: max 60 lines (currently: ___ lines)
- Remove: repetitions, obvious rules, detailed explanations
- Keep: project goal, commands, the most important DOs and DON'Ts
- Rules that belong in angular.instructions.md → move there
```

**Check:** Does Copilot still know about Standalone Components and Signals?

---

## Task 3 – Chat History vs. New Chat (15 min)

**Experiment:**

1. Open a chat with lots of history
2. Ask: "Add error handling to funcLoadTodos"
3. Note the response

4. Start a new chat (`+` New Chat)
5. Ask: "Add error handling to #sym:funcLoadTodos"
6. Note the response

**Compare:**

- Is the response more precise in the new chat?
- Does the new chat use Signals correctly (as per instructions)?

---

## Task 4 – CLI Instead of Chat for Terminal Questions (10 min)

```bash
# Instead of: "How do I run tests in Angular without a browser?"
gh copilot suggest "Run Angular tests without browser in CI mode"

# Instead of: "How do I build Angular for production?"
gh copilot suggest "Build Angular app for production with source maps disabled"

# Instead of: "How do I analyze the bundle size?"
gh copilot suggest "Analyze Angular bundle size and show unused dependencies"
```

**Benefit:** These questions don't use Copilot Chat tokens.
