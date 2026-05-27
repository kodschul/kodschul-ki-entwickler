# Module 01 — Exercises

---

## Exercise 01.1-A — Evaluate Prompt Quality

Rate the following prompts on a scale of 1–5 stars. Identify which CREF elements are missing in each and why the output would be problematic.

**Prompt 1:**

```
Help me with C#.
```

**Prompt 2:**

```
Write a class for orders.
```

**Prompt 3:**

```
You are a C# developer. Write an Order class with Id, CustomerId, Status and Lines.
```

**Prompt 4:**

```
You are a senior .NET 9 developer with DDD experience.
Create Order as an Aggregate Root:
- Id: Guid (private set)
- CustomerId: Guid (private set)
- Status: OrderStatus Enum (Open/Confirmed/Shipped/Completed, private set)
- Lines: IReadOnlyCollection<OrderLine> (readonly backing field)
- Method Confirm(): status transition Open→Confirmed, exception if no Lines
- Method AddLine(Product product, int quantity): only when Status Open, quantity validation
.NET 9, private setters everywhere, XML docs, code only.
```

**Evaluation template:**

| Prompt | Stars (1–5) | Missing CREF elements | Expected problem |
| ------ | ----------- | --------------------- | ---------------- |
| 1      |             |                       |                  |
| 2      |             |                       |                  |
| 3      |             |                       |                  |
| 4      |             |                       |                  |

---

## Exercise 01.1-B — Complete Missing CREF Elements

Complete the missing elements in these incomplete prompts:

**Prompt A (role missing):**

```
We are building a warehouse management system in .NET 9.
Create a ProductService with methods for inventory management.
Code only.
```

→ What role should the AI have? Write the complete prompt.

**Prompt B (context missing):**

```
You are an experienced software architect.
Create an interface IProductRepository.
```

→ What context is missing? Add it so that the output is directly usable.

**Prompt C (format and restrictions missing):**

```
You are a senior .NET developer in a DDD project with EF Core 9.
Analyze this database model and identify problems.
[Model description]
```

→ How should the output be structured? What are the restrictions?

---

## Exercise 01.2-A — Few-Shot Prompt for FluentValidation

Write a few-shot prompt that makes an AI generate FluentValidation classes in a consistent style.

**Pattern validator (show this to the AI):**

```csharp
public sealed class CreateCustomerValidator : AbstractValidator<CreateCustomerRequest>
{
    public CreateCustomerValidator()
    {
        RuleFor(x => x.FirstName)
            .NotEmpty().WithMessage("First name is required.")
            .MaximumLength(100).WithMessage("First name may not exceed 100 characters.");

        RuleFor(x => x.Email)
            .NotEmpty().WithMessage("Email is required.")
            .EmailAddress().WithMessage("Invalid email address.");
    }
}
```

**Target request class:**

```csharp
public sealed record CreateProductRequest(
    string Name,
    decimal Price,
    int InitialStock,
    string? Description);
```

**Validation rules:**

- Name: required, 1–200 characters
- Price: required, greater than 0, maximum 99,999.99
- InitialStock: required, 0 to 10,000
- Description: optional, maximum 500 characters

Write the complete few-shot prompt and execute it.

---

## Exercise 01.2-B — Chain-of-Thought for Architecture Decisions

**Scenario:** You need to decide: **CQRS with MediatR** or **simple service layer pattern** for a new .NET 9 application.

Write a chain-of-thought prompt that forces the AI to think in this order:

1. Categorize the project context
2. Compare pros and cons
3. Weight decision criteria (rated 1–5)
4. Only at the end: give a reasoned recommendation

Context for your prompt: 4 developers, medium-complexity business logic, no Event Sourcing, MVP desired in 3 months.

---

## Exercise 01.3-A — Fix Bad Prompts

Improve the following prompts so that they produce directly usable, high-quality .NET 9 / C# output:

**Bad prompt 1:**

```
Write a controller.
```

**Bad prompt 2:**

```
My code has a bug:
public decimal Calculate(int a, int b) { return a / b; }
```

**Bad prompt 3:**

```
Explain LINQ to me.
```

**Bad prompt 4:**

```
Write tests for my app. The app has products and orders.
```

For each prompt: name the problem, then write the improved version.

---

## Exercise 01.3-B — Build a Personal Prompt Library

Write a complete, reusable prompt with `[PLACEHOLDERS]` for **five** of the following tasks:

1. Generate a new DDD entity
2. Repository interface + EF Core 9 implementation
3. Unit tests for a single method
4. Code review of a class
5. Analyze and fix an exception + stack trace
6. Optimize a LINQ query for performance
7. Check async code for deadlock risks
8. Write a README.md for a module

**Format per prompt:**

```markdown
## [Task Name]

**When to use:** [Short description]

**Prompt:**
[Complete prompt with [PLACEHOLDERS]]

**Instructions:** [What goes in the placeholders?]
```

---

## Exercise 01.4-A — Iterative Refinement Process

Develop a complete `Product` class for the online shop project in **four iterations**.

**Iteration 1 — Basic structure:**
Start with a simple prompt. Document what was generated.

**Iteration 2 — Add domain logic:**
Based on the result: add methods for inventory management, price validation, domain rules.

**Iteration 3 — Make EF Core compatible:**
Based on the result: ensure EF Core 9 compatibility (protected ctor, Owned Types, etc.)

**Iteration 4 — Generate tests:**
Based on the finished class: xUnit + FluentAssertions tests for all methods.

**Document for each iteration:**

- Your complete prompt
- What the AI did well
- What you had to correct manually
- What you would phrase differently next time

---

## Exercise 01.4-B — Prompt Quality Proof

Empirically prove the quality difference between three prompt levels for the same use case.

**Level 1 — Minimal:**

```
Write an OrderService in C#.
```

**Level 2 — Medium:**

```
Write a C# OrderService with methods for orders.
Use .NET 9 and EF Core 9.
```

**Level 3 — Complete (write yourself using CREF):**
Write a complete CREF prompt for an `OrderApplicationService` with:

- `PlaceOrderAsync(PlaceOrderCommand cmd, CancellationToken ct)`: place a new order
- `ConfirmOrderAsync(Guid orderId, CancellationToken ct)`: confirm an order
- `GetOrderDetailsAsync(Guid orderId, CancellationToken ct)`: load details → `OrderDetailsDto?`

**Evaluation matrix:**

| Criterion                                   | Level 1 | Level 2 | Level 3 |
| ------------------------------------------- | ------- | ------- | ------- |
| Compiles without changes?                   |         |         |         |
| All 3 methods present?                      |         |         |         |
| CancellationToken in all async?             |         |         |         |
| Error handling (KeyNotFoundException etc.)? |         |         |         |
| XML documentation?                          |         |         |         |
| Estimated post-processing time (min)        |         |         |         |
