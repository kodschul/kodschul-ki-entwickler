# Module 02 — Exercises

---

## Exercise 02.1-A — Agent vs. Chat: Experience the Difference

**Task:** Solve the same task once as a single-step chat prompt and once as a multi-step agent workflow. Then compare the quality.

**Task (single-step):**

```
Create complete domain classes, EF Core configuration and unit tests for an online shop.
```

**Task (multi-step):**

```
Step 1: Which domain classes does an online shop need (DDD perspective)?
Step 2: [Result from step 1] → Create the C# classes following DDD principles
Step 3: [Classes] → Create the EF Core 9 configuration
Step 4: [Classes] → Create xUnit + FluentAssertions tests
```

**Comparison matrix:**

| Criterion                        | Single-step | Multi-step |
| -------------------------------- | ----------- | ---------- |
| Completeness of classes          |             |            |
| Quality of EF Core configuration |             |            |
| Quality of tests                 |             |            |
| Post-processing effort           |             |            |
| Where were the errors?           |             |            |

---

## Exercise 02.1-B — Opportunities and Risks Analysis

**Scenario:** Your team is considering deploying a fully automated AI agent that:

1. Analyzes GitHub issues
2. Plans and describes code changes
3. Creates pull requests with implementation
4. Runs CI/CD tests
5. Auto-merges the PR when tests are green

**Tasks:**

1. At which steps is a human checkpoint mandatory? Justify your answer.
2. What concrete risks arise from full automation at each step?
3. Design a safe workflow with human-in-the-loop checkpoints.
4. Write the prompt safety rules for the agent (what must it never do?).

---

## Exercise 02.2-A — Translate a User Story into a Prompt Chain

**User story:**

```
As a warehouse employee, I want to increase the stock level of a product
when a delivery arrives, so that the current stock is always accurate.

Acceptance criteria:
- Stock is increased by the delivered quantity
- Quantity must be positive (> 0)
- Maximum stock: 50,000 units
- Domain Event StockReplenished is fired (with ProductId, AddedQuantity, NewStock)
- Supplier reference number is stored
```

**Task:** Break the implementation into a 5-step prompt chain.

Define for each step:
| | Input | Prompt (keyword) | Expected output | Checkpoint |
|---|---|---|---|---|
| Step 1 | | | | |
| Step 2 | | | | |
| Step 3 | | | | |
| Step 4 | | | | |
| Step 5 | | | | |

---

## Exercise 02.2-B — Actually Execute the Prompt Chain

**Task:** Execute the prompt chain from Exercise 4.2-A.

Start step 1 with this input:

```
User story: As a warehouse employee, I want to increase the stock level when a delivery arrives.

Acceptance criteria:
- Quantity must be positive
- Maximum stock 50,000
- Domain Event: StockReplenished(ProductId, AddedQuantity, NewStock, SupplierReference, OccurredAt)
- SupplierReference: string, max. 50 characters
```

**Document honestly:**

- What adjustments did you need to make between steps?
- Where did the AI make mistakes?
- How did you recognize and correct them?
- Did an error from an early step propagate into later steps?

---

## Exercise 02.3-A — Document a Repeatable Workflow

**Task:** Create a **workflow template** in Markdown that your team can use for every new feature in the online shop project.

The template must contain:

- Workflow name and description
- Prerequisites (what must be in place beforehand?)
- Step-by-step prompts with placeholders `[IN_BRACKETS]`
- Review criteria after each step (checklist)
- Abort conditions (when is it better to proceed manually?)
- Estimated time (AI run vs. manual)

---

## Exercise 02.3-B — Plan Human-in-the-Loop

**Scenario:** You are automating test data generation.

The agent should:

1. Read the database schema
2. Generate realistic test data (20 customers, 50 products, 100 orders)
3. Create SQL INSERT scripts
4. Execute the scripts against a local test database

**Tasks:**

1. After which steps MUST a human check? Justify.
2. Which automatic validations can the agent perform itself?
3. How is a rollback enabled if step 4 fails?
4. Write the complete safety rules for this agent as a prompt preamble.

---

## Exercise 02.4-A — Plan a Mini-Sprint with AI

**Feature:**

> Customers should be able to see their last 10 orders as a list. Clicking an order opens the detail view with all line items.

Create an AI-supported execution plan:

| Step      | What is done? | AI tool | Prompt keywords | Manual checkpoint? | Time AI | Time manual |
| --------- | ------------- | ------- | --------------- | ------------------ | ------- | ----------- |
| 1         |               |         |                 |                    |         |             |
| 2         |               |         |                 |                    |         |             |
| 3         |               |         |                 |                    |         |             |
| ...       |               |         |                 |                    |         |             |
| **Total** |               |         |                 |                    |         |             |

---

## Exercise 02.4-B — Reflection and Limits

**Task:** After completing Exercises 4.2-B and 4.4-A, write a structured reflection (min. ½ page).

Answer:

1. **Quality:** Where did AI support help the most? Where the least?
2. **Error propagation:** Were there errors that carried through multiple steps? How could they have been caught earlier?
3. **Traceability:** Can you fully explain every part of the generated code to a colleague? If not, what is missing?
4. **Efficiency:** Was multi-step actually faster than manual implementation? At what task size does this flip?
5. **Recommendation:** For which types of tasks do you recommend multi-step prompting on your team – and for which not?
