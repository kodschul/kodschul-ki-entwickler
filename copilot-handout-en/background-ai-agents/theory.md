# Module 02 — AI Agents and Multi-Step Prompting

## Lab 4.1 — AI Agents as a Working Model

### Agents vs. Simple Chat

```
Chat prompt:  Question → Answer (one step, no memory)

AI Agent:     Goal defined
                 ↓
              Plan created
                 ↓
              Tool A invoked (e.g. file system)
                 ↓
              Intermediate result evaluated
                 ↓
              Tool B invoked (e.g. terminal)
                 ↓
              Result delivered
```

**Examples from development practice:**

- GitHub Copilot Workspace: reads issue → plans changes → writes code → creates PR
- Cursor Cascade: reads error message → finds cause → changes files → runs tests
- Claude + MCP: access to filesystem, terminal, browser, database

### Opportunities and Risks

| Opportunities                      | Risks                                     |
| ---------------------------------- | ----------------------------------------- |
| Automation of multi-step workflows | Error from step 2 propagates to step 8    |
| Consistent, repeatable processes   | Hard to debug in long chains              |
| Fast for clearly defined tasks     | Context loss between steps goes unnoticed |
| 24/7 without fatigue               | Token costs are significant for long runs |

**Human-in-the-Loop:** After critical steps, a human must review the result before proceeding.

---

## Lab 4.2 — Multi-Step Prompting

### Breaking Tasks into Steps

**Anti-pattern:**

```
Analyze the requirements, create the domain model, implement all classes,
write EF Core configurations, migrations, tests and documentation.
→ Result: superficial, many errors, hard to correct
```

**Best practice – sequential chain:**

```
Prompt 1: Analyze requirements → identify entities and events
Prompt 2: [Result 1] → generate C# classes
Prompt 3: [Classes] → EF Core configuration
Prompt 4: [Classes] → unit tests
Prompt 5: [Everything] → generate README.md
```

### Checkpoints After Every Step

After every AI step, verify:

1. **Functionally correct?** Does the result match the requirement?
2. **Technically correct?** Does the code compile? Are patterns right?
3. **Complete?** Were all required elements created?
4. **Only then:** move to the next prompt

---

## Lab 4.3 — Systematically Structuring Workflows

### Repeatable Feature Workflow

```
STEP 1 — Requirements analysis
Input:  User story + acceptance criteria
Prompt: "Analyze using DDD: entities, methods, events, validation rules, edge cases"
Check:  All acceptance criteria covered?

STEP 2 — Domain classes
Input:  Analysis result from step 1
Prompt: "[Analysis] → Create DDD-compliant C# classes (.NET 9, private setters, XML docs)"
Check:  Compiles? Private setters? Validation present?

STEP 3 — Tests (TDD)
Input:  Classes from step 2
Prompt: "[Classes] → Create xUnit + FluentAssertions tests for all public methods"
Check:  All test cases present? Tests compile? Red (no implementation yet)?

STEP 4 — Implementation
Input:  Tests from step 3 + classes from step 2
Prompt: "Implement the methods so that all tests pass"
Check:  All tests green? No implementation going beyond the tests?

STEP 5 — Refactoring review
Input:  Implementation from step 4
Prompt: "Identify improvement potential: DDD, performance, readability"
Check:  Which suggestions to adopt?
```

---

## Lab 4.4 — Multi-Step AI Support in Practice

### Limits of Multi-Step Prompting

**When it fails:**

- Chain too long → context is lost or window becomes too large
- Step 2 contains errors → they inevitably propagate
- Task is too vague → each step generates something different than expected

**When it excels:**

- Clear, sequential tasks with verifiable intermediate results
- Each step is independently validatable
- Standardized workflow that repeats (e.g. for each new feature)

### Quality Reflection

After every multi-step run, ask:

1. Could I fully explain the generated code to a colleague?
2. Have errors from early steps propagated?
3. Was the effort less than manual implementation?
4. What would I do differently next time?
