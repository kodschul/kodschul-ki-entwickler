# Module 01 — Solutions

---

## Solution 01.1-A — Evaluate Prompt Quality

| Prompt | Stars      | Missing elements                               | Expected problem                                       |
| ------ | ---------- | ---------------------------------------------- | ------------------------------------------------------ |
| 1      | ⭐         | Everything: role, context, expectation, format | Output: some code in some language                     |
| 2      | ⭐⭐       | Role, framework, properties, format            | Incomplete class, wrong pattern, unknown fields        |
| 3      | ⭐⭐⭐     | Methods, validation, format, framework         | Class present but without domain logic, public setters |
| 4      | ⭐⭐⭐⭐⭐ | Complete                                       | Directly usable, correct DDD implementation            |

---

## Solution 01.1-B — Complete Missing Elements

**Prompt A — role and format added:**

```
You are a senior .NET 9 developer with DDD and Clean Architecture experience.

Context: Warehouse management system, .NET 9, Clean Architecture.
Entity: Product (Id: Guid, Name: string, Price: decimal, Stock: int)

Create IProductStockService (interface) and ProductStockService (implementation):
- AddStockAsync(Guid productId, int quantity, CancellationToken ct)
- ReduceStockAsync(Guid productId, int quantity, CancellationToken ct)
- GetStockLevelAsync(Guid productId, CancellationToken ct) → int

Restrictions: IProductRepository via DI, KeyNotFoundException if not found,
InvalidOperationException if stock would go negative.
Code only. XML docs. CancellationToken everywhere.
```

**Prompt B — context added:**

```
You are an experienced software architect.

Context:
- Project: Online shop with Clean Architecture and DDD
- ORM: EF Core 9, SQL Server
- Entity: Product (Id: Guid, Name: string, Price: decimal, Stock: int, IsDeleted: bool)
- Pattern: Repository + Unit of Work

Create IProductRepository with:
- GetByIdAsync(Guid id, CancellationToken ct) → Product?
- SearchAsync(string? term, int page, int pageSize, CancellationToken ct) → PagedResult<Product>
- SaveAsync(Product product, CancellationToken ct)
- SoftDeleteAsync(Guid id, CancellationToken ct)

XML docs. CancellationToken everywhere. Interface only (no implementation).
```

**Prompt C — format and restrictions added:**

```
You are a senior .NET architect with DDD expertise and EF Core 9 knowledge.

Analyze this database model and identify problems:
[Model description]

Output format:
For each problem:
  Location: [TableName.Column or relationship]
  Problem: [What is wrong and why?]
  Impact: [What happens in the application as a result?]
  Solution: [Corrected EF Core configuration as C# code]

Ordering: most critical problems (data loss, inconsistency) first.
Conclusion: overall assessment in 2–3 sentences.
```

---

## Solution 01.2-A — Few-Shot Validator (Model Solution)

**Complete prompt:**

```
You are a senior C# developer with FluentValidation expertise. .NET 9.

Create a validator exactly following this pattern:

// Pattern (output must look exactly like this):
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

Create a validator for the following request using exactly the same style:

public sealed record CreateProductRequest(string Name, decimal Price, int InitialStock, string? Description);

Validation rules:
- Name: required, 1–200 characters
- Price: required, > 0, ≤ 99999.99
- InitialStock: 0–10000 (InclusiveBetween)
- Description: optional, maximum 500 characters (only check if not null)

Error messages in English. Code only. No explanatory text.
```

**Expected result:**

```csharp
public sealed class CreateProductValidator : AbstractValidator<CreateProductRequest>
{
    public CreateProductValidator()
    {
        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Name is required.")
            .Length(1, 200).WithMessage("Name must be between 1 and 200 characters.");

        RuleFor(x => x.Price)
            .GreaterThan(0).WithMessage("Price must be greater than 0.")
            .LessThanOrEqualTo(99999.99m).WithMessage("Price must not exceed 99,999.99.");

        RuleFor(x => x.InitialStock)
            .InclusiveBetween(0, 10000).WithMessage("Stock must be between 0 and 10,000.");

        RuleFor(x => x.Description)
            .MaximumLength(500).WithMessage("Description may not exceed 500 characters.")
            .When(x => x.Description is not null);
    }
}
```

---

## Solution 01.3-A — Bad Prompts Fixed

**Prompt 1 fixed:**

```
You are a senior ASP.NET Core 9 developer.

Create ProductsController (Web API, [ApiController]):
- GET /api/products → all products paginated (parameters: page=1, pageSize=20, search?)
- GET /api/products/{id} → single product (404 if not found)
- POST /api/products → create new product (400 on validation error)
- PUT /api/products/{id} → update
- DELETE /api/products/{id} → soft delete

Requirements: inject IProductService via DI, ProducesResponseType attributes,
ILogger<ProductsController>, CancellationToken, XML docs. Code only.
```

**Prompt 2 fixed:**

```
This C# code contains a critical bug:

public decimal Calculate(int a, int b) { return a / b; }

1. Explain precisely which error occurs and with which inputs
2. Show the correct solution with validation (ArgumentException if b == 0)
3. Also show the integer division bug and how to fix it
4. Write xUnit + FluentAssertions tests that prove both bugs and confirm the fix
```

**Prompt 3 fixed:**

```
You are a .NET trainer. Explain LINQ to a C# junior developer (1 year experience).

Structure:
1. What is LINQ and why is it useful? (3 sentences)
2. The 5 most important operators each with an example from an online shop context
3. Method syntax vs. query syntax – when to use which?
4. Common mistake: N+1 problem with EF Core (example + fix)

All code examples: Orders, Products, Customers (consistent domain model). .NET 9.
```

**Prompt 4 fixed:**

```
You are an experienced C# developer. Framework: xUnit + FluentAssertions + NSubstitute. .NET 9.

Test class: OrderServiceTests
Method under test: OrderApplicationService.ConfirmOrderAsync(Guid orderId, CancellationToken ct)

Behavior:
- Confirms an order (status: Open → Confirmed) and saves it
- Throws KeyNotFoundException if order with orderId not found
- Throws InvalidOperationException if status != Open

Test cases:
1. Happy path: open order → successfully confirmed + Repository.SaveAsync called
2. Not found: non-existent ID → KeyNotFoundException
3. Wrong status: already confirmed order → InvalidOperationException

Mocking: mock IOrderRepository with NSubstitute.
Naming: ConfirmOrderAsync_Scenario_ExpectedOutcome. Code only.
```

---

## Solution 01.4-B — Complete Level-3 Prompt (Model)

```
You are a senior .NET developer with Clean Architecture and DDD expertise.

[C] Context:
- Online shop, .NET 9, EF Core 9, Clean Architecture
- Pattern: Application Service (no MediatR)
- Interfaces: IOrderRepository, ICustomerRepository, IProductRepository
- CancellationToken in all async methods

[R] Role: Senior .NET architect who writes clean, maintainable code.

[E] Create OrderApplicationService with these three methods:

1. PlaceOrderAsync(PlaceOrderCommand cmd, CancellationToken ct) → Guid
   - Load customer (KeyNotFoundException if not found)
   - Load all products + check stock (InvalidOperationException if insufficient)
   - Create Order with OrderLines
   - Save + return OrderId

2. ConfirmOrderAsync(Guid orderId, CancellationToken ct)
   - Load order (KeyNotFoundException if not found)
   - Call order.Confirm() (throws InvalidOperationException for wrong status)
   - Save

3. GetOrderDetailsAsync(Guid orderId, CancellationToken ct) → OrderDetailsDto?
   - Load order, map to OrderDetailsDto, return null if not found

Records:
- PlaceOrderCommand(Guid CustomerId, IReadOnlyList<OrderLineRequest> Lines)
- OrderLineRequest(Guid ProductId, int Quantity)
- OrderDetailsDto(Guid Id, string CustomerName, string Status, decimal Total, IReadOnlyList<OrderLineDto> Lines)
- OrderLineDto(string ProductName, int Quantity, decimal UnitPrice, decimal LineTotal)

[F] Format:
- C# code only. No prose text.
- ILogger<OrderApplicationService> via DI, log critical operations
- XML docs for all public members
- Records at the end of the file
```

**Expected quality differences:**

| Criterion            | Level 1 | Level 2   | Level 3  |
| -------------------- | ------- | --------- | -------- |
| Compiles             | No      | Partially | Yes      |
| All methods          | No      | Partially | Yes      |
| CancellationToken    | No      | Partially | Yes      |
| Error handling       | No      | No        | Yes      |
| XML docs             | No      | No        | Yes      |
| Post-processing time | 60+ min | 20–30 min | 5–10 min |
