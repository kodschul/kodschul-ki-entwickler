# Module 02 — Solutions

---

## Solution 02.1-A — Agent vs. Chat (Expected Results)

| Criterion               | Single-step                                 | Multi-step                                 |
| ----------------------- | ------------------------------------------- | ------------------------------------------ |
| Completeness of classes | Superficial (missing methods, validation)   | Complete, following DDD                    |
| EF Core configuration   | Generic, without nuances                    | Specific, Owned Types, converters          |
| Quality of tests        | Often happy path only                       | All scenarios covered                      |
| Post-processing effort  | High (30–60 min)                            | Low (5–15 min)                             |
| Typical errors          | Everything mixed, public setters, no events | More precise, but step 2 depends on step 1 |

**Conclusion:** Multi-step pays off from medium complexity onwards. Simple CRUD operations can remain single-step.

---

## Solution 02.1-B — Opportunities and Risks Analysis

**Mandatory human checkpoints:**

- After step 2 (plan): Is the implementation plan correct? No misinterpretation of the issue?
- After step 3 (code): Code review! Logic errors, security issues, missing tests
- After step 4 (tests): Are the tests truly meaningful or just green placeholders?
- Step 5 (merge): Must always be manual — no auto-merging to production

**Concrete risks:**

- Step 1: Issue misinterpreted → wrong implementation
- Step 3: Security vulnerability generated (SQL injection, auth bypass)
- Step 5: Breaking change merged unnoticed

**Safe workflow:**

```
Read issue ← AGENT
Create plan ← AGENT
Show plan → HUMAN reviews and approves
Write code ← AGENT
Code review → HUMAN (mandatory)
Create PR ← AGENT
Run CI ← AUTOMATED
Merge → HUMAN (mandatory)
```

**Agent safety rules:**

```
You MUST NEVER:
- Push directly to main/master without a PR
- Read or write production databases
- Insert secrets, API keys or passwords into code
- Call external services without explicit approval
- Modify files outside the project directory

You MUST:
- Wait for human confirmation after every planning step
- Make all changes in a feature branch
- Stop and ask rather than guess when uncertain
```

---

## Solution 02.2-A — Prompt Chain for Stock Replenishment

| Step | Input                            | Prompt keyword                                                                                   | Expected output     | Checkpoint                      |
| ---- | -------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------- | ------------------------------- |
| 1    | User story + acceptance criteria | "Analyze using DDD: entities, method, validation rules, event structure"                         | Structured analysis | All ACs covered?                |
| 2    | Analysis                         | "Create/extend Product entity C# .NET 9: ReplenishStock(int, string) + StockReplenished event"   | C# classes          | Private setters? Event correct? |
| 3    | Classes                          | "Create xUnit tests for Product.ReplenishStock(): happy path, negative quantity, over max stock" | Test class          | All ACs as tests?               |
| 4    | Tests                            | "Implement ReplenishStock() so that all tests pass"                                              | Finished method     | Tests green?                    |
| 5    | Classes                          | "Create EF Core 9 configuration for Product including StockReplenished domain event storage"     | Configuration       | Owned Types? Index on FK?       |

---

## Solution 02.3-B — Safety Rules for Test Data Agent

```
You are a test data generation agent for the hotel reservation system.

SAFETY RULES (non-negotiable, always active):
- You may ONLY access databases with "_Test" or "_Dev" in the name
- You MUST NOT use production connection strings
- Execute all operations in a single transaction
- On any error: immediate ROLLBACK, output the error, STOP

MANDATORY VALIDATIONS (automatically after step 3):
- Check that all FK references can be resolved
- Check that generated date fields are realistic (no checkouts before check-ins)
- Check that all NOT NULL fields are populated
- Check that unique constraints are not violated

WORKFLOW:
Step 1: Read schema → show what was found → STOP
Step 2: Generate test data as JSON → show → STOP, wait for "OK"
Step 3: Create SQL script → show → STOP, wait for "OK"
Step 4: Only after explicit "EXECUTE" → start transaction → INSERTs → confirmation

Rollback instruction: The agent creates a ROLLBACK script before starting step 4.
```

---

## Solution 02.4-A — Mini-Sprint Plan (Order History)

| Step      | What                    | Tool    | Prompt keyword                                                 | Checkpoint           | Time AI    | Time manual |
| --------- | ----------------------- | ------- | -------------------------------------------------------------- | -------------------- | ---------- | ----------- |
| 1         | Requirement → ViewModel | Claude  | "OrderHistoryViewModel, OrderSummaryViewModel with pagination" | All UI fields?       | 5 min      | 20 min      |
| 2         | Query service interface | Claude  | "IOrderQueryService.GetCustomerOrdersAsync paginated"          | Signature correct?   | 3 min      | 10 min      |
| 3         | EF Core query           | Claude  | "EF Core 9 Include + pagination, avoid N+1"                    | No N+1? Performance? | 7 min      | 25 min      |
| 4         | Controller              | Copilot | Inline completion                                              | Review needed        | 5 min      | 15 min      |
| 5         | Views                   | Claude  | "Index + details view with Bootstrap, pagination controls"     | HTML correct?        | 10 min     | 45 min      |
| 6         | Unit tests              | Claude  | "Tests for query service + controller"                         | Coverage ok?         | 10 min     | 40 min      |
| **Total** |                         |         |                                                                |                      | **40 min** | **155 min** |

**Mandatory human checkpoints:**

- After step 3: Is the query performant? `.AsNoTracking()` set?
- After step 5: Responsive? Accessibility?
- After step 6: Are the tests actually testing the right things?
