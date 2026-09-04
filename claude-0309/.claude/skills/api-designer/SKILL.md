---
name: api-designer
description: Instructs Claude how to design REST APIs — resource-oriented endpoints, HTTP verbs/status codes, Swagger/OpenAPI for documenting and testing endpoints, and static bearer token authentication. Activate when the user asks to design, add, or change an API, an endpoint, or API authentication.
---

# API Designer

If the project's CLAUDE.md forbids adding a REST API or a `/api` module, say so and confirm before proceeding.

RULES:
- Use REST API design (resource-based paths, correct HTTP verbs, standard status codes).
- Use Swagger/OpenAPI to document, test, and visualize the endpoints, including the Swagger UI
- Use a static bearer token for authentication and authorization.
- Store endpoints under `/api`, served by their own `api.py`.

Approach:
- Clarify the endpoints with the user.
- Check for duplicate or similar existing endpoints.
- Draft a concrete plan and propose it to the user for approval.
- Once approved, build the diff endpoints and keep the OpenAPI spec in sync.
