# Module 01 — Prompt Engineering for Software Development

---

## Lab 3.1 — Introduction to Modern Prompting

### The Core Idea

The quality of AI output depends directly on the quality of the input. Prompt engineering is the discipline of structuring inputs so that consistently high-quality results are produced.

**Prompt quality spectrum:**

```
"Write code"                             → 1 star: unusable
"Write a C# class for orders"            → 3 stars: too vague
"You are a senior .NET 9 developer...
 Create Order as Aggregate Root with
 private setters, validation, domain
 events. Code only. XML docs."           → 5 stars: directly usable
```

### The CREF Formula

| Letter | Element         | Purpose                               |
| ------ | --------------- | ------------------------------------- |
| **C**  | **C**ontext     | Project environment, technology stack |
| **R**  | **R**ole        | Who should the AI be?                 |
| **E**  | **E**xpectation | What exactly should be produced?      |
| **F**  | **F**ormat      | How should the output look?           |

**Example of a complete prompt:**

```
[R] You are a senior .NET 9 developer with Clean Architecture experience.

[C] Online shop project: ASP.NET Core 9, EF Core 9, DDD, Clean Architecture.
    Domain: Order (Aggregate Root), OrderLine (Entity), Product (Entity).

[E] Create IOrderRepository (interface) and EfOrderRepository (EF Core 9 implementation).
    Methods: GetByIdAsync, GetByCustomerIdAsync (paginated), SaveAsync, SoftDeleteAsync.

[F] C# code only. Interface first, then implementation.
    XML documentation. CancellationToken everywhere. No explanations.
```

---

## Lab 3.2 — Developing Effective Prompt Structures

### Few-Shot Prompting

Examples within the prompt dramatically improve the format and style of the output:

```
Create Domain Events following this pattern:

// Example (output should look exactly like this):
public record OrderConfirmed(Guid OrderId, DateTime OccurredAt) : IDomainEvent;
public record OrderShipped(Guid OrderId, string TrackingNumber, DateTime OccurredAt) : IDomainEvent;

Create events using exactly the same pattern for:
- CustomerRegistered (with FirstName, LastName, Email)
- ProductAddedToStock (with ProductId, AddedQuantity, NewTotalStock)
- OrderCancelled (with OrderId, Reason)
```

### Chain-of-Thought Prompting

For complex problems: explicitly request structured thinking **before** the answer comes:

```
Analyze this performance problem in exactly this order:

Step 1 - Possible causes: List all plausible causes
Step 2 - Weighting: Sort by probability (with reasoning)
Step 3 - Diagnosis: How to check the most likely cause?
Step 4 - Only then: Proposed solution

Problem: API response time increases linearly with growing database size.
Context: .NET 9 API, EF Core 9, SQL Server, 500k records in Orders table.
```

### System Prompts and Personas

For recurring tasks: set a persona at the beginning of a session:

```
From now on, you are an experienced C#/.NET code reviewer with a DDD focus.
You review every piece of code for:
1. DDD violations (public setters, missing validation, logic outside the entity)
2. EF Core anti-patterns (N+1, wrong lifecycle, no AsNoTracking for readonly)
3. .NET 9 improvement potential (newer APIs, C# 13 features)

Format: Problem → Why it's bad → Corrected version
```

---

## Lab 3.3 — Best Practices for Clear Prompts

### Golden Rules

**1. Use positive rather than negative phrasing**

```
❌ "Don't write overly complex code"
✅ "Write simple code: max. 20 lines per method, descriptive variable names"
```

**2. Always name frameworks and versions explicitly**

```
❌ "Use the current framework"
✅ "Use .NET 9, EF Core 9, xUnit 2.9, FluentAssertions 6.12, NSubstitute 5"
```

**3. Control output format precisely**

```
"Output: C# code blocks ONLY. No explanatory text. No markdown headings.
 XML documentation in English. Inline comments in English."
```

**4. Name restrictions explicitly**

```
"Restrictions:
 - No static methods except factory methods
 - No direct DbContext in Application Layer
 - All exceptions must use specific types (no base Exception)"
```

### Typical Prompt Mistakes

| Mistake             | Example                                 | Problem                             |
| ------------------- | --------------------------------------- | ----------------------------------- |
| Too vague           | "Improve my code"                       | AI doesn't know what "better" means |
| Contradictory       | "Short but complete and detailed"       | Impossible to optimize              |
| No context          | "Fix the bug" (without code)            | AI can't help                       |
| Everything at once  | 10 different requirements in one prompt | Quality suffers for each            |
| No format specified | "Write tests"                           | Which framework? What structure?    |

---

## Lab 3.4 — Prompting Templates for Daily Development

### Template: Generate a New Class

```
You are a senior C# developer. .NET 9, C# 13.
Create [CLASS] as [Entity / ValueObject / AggregateRoot / DomainService]:
Properties: [with types and nullability]
Methods: [with signatures and domain rules]
Validation: [specific rules + exception type]
Requirements: private setters, protected EF ctor, XML docs, Domain Events where appropriate.
Code only. No explanations.
```

### Template: Generate Unit Tests

```
Framework: xUnit + FluentAssertions + NSubstitute. .NET 9.
Create tests for: [CLASS.METHOD]

Test cases:
- Happy path: [what should pass successfully]
- Error case 1: [what should throw which exception]
- Error case 2: [additional error case]
- Edge case: [boundary condition]

Structure: Arrange / Act / Assert (with comments).
Naming: MethodName_Scenario_ExpectedOutcome.
Code only. Test class is named [CLASS]Tests.
```

### Template: Review Code

```
Review this C# code for:
1. DDD violations (public setters, missing validation, misplaced logic)
2. EF Core 9 anti-patterns
3. .NET 9 improvement potential (C# 13, new APIs)
4. Security issues

Format per problem: Identify location → explain problem → show corrected version
Ordering: most critical problems first.

[CODE HERE]
```

### Template: Debug an Exception

```
I am getting the following exception in .NET 9 / EF Core 9:
[EXCEPTION + STACKTRACE]

Context: [What was being executed?]
Code: [Relevant code snippet]

Analyze in this order:
1. Cause (name it precisely)
2. Why does this occur?
3. Fix (corrected code)
4. How to prevent this in the future?
```
