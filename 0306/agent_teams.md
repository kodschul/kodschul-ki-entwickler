[R] You are a senior .NET 9 developer with Clean Architecture experience.

-> Agent.md

[C] Online shop project: ASP.NET Core 9, EF Core 9, DDD, Clean Architecture.
Domain: Order (Aggregate Root), OrderLine (Entity), Product (Entity).

    -> Spec Driven -> spec.md

    -> System Prompt -> copilot-instructions.md, Claude.md, Agents.md

[E] Create IOrderRepository (interface) and EfOrderRepository (EF Core 9 implementation).
Methods: GetByIdAsync, GetByCustomerIdAsync (paginated), SaveAsync, SoftDeleteAsync.

    -> Prompt file -> prompt.md  / command.md

[F] C# code only. Interface first, then implementation.
XML documentation. CancellationToken everywhere. No explanations.

-> HOW TO -> store in a skill -> SKILL.md

---

Team Struktur

- Frontend Dev
- Backend
- Designer
- DevOps Engineer
  -> full-stack-agent.md

- Projektmanager
- Solutions Architect
  -> architect-agent.md

- QA Engineer
  -> qa-agent.md

- Cyber Security Specialist
  -> security-agent.md

Fähigkeiten: (Skills)

- Designs Guideline etc
  -> skills/frontend-designer.md

- Test writing
  -> skills/test-writer.md

- Code review
  -> skills/code-reviewer.md

- Code generation
  -> skills/code-writer.md

Aufgaben & Workflows:

- /frontend-review
  -> frontend-review.prompt.md -> code review skill nutzen + nur /frontend review
