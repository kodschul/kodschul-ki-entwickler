---
applyTo: "**/*.ts"
---

# TypeScript Coding Guidelines

## General Principles

- Use strict mode: `"strict": true` in tsconfig.json
- Enable strict null checks and other strict compiler options
- Avoid `any` type - use explicit types instead
- Use meaningful variable and function names

## Naming Conventions

- Use camelCase for variables, functions, and methods
- Use PascalCase for classes, interfaces, and types
- Use UPPER_SNAKE_CASE for constants
- Prefix private members with underscore (e.g., `_privateProperty`)

## Type Annotations

- Always provide explicit return types for functions
- Define interfaces or types for object parameters
- Use union types (`|`) and intersection types (`&`) appropriately
- Avoid type assertions unless absolutely necessary

## Functions

- Keep functions small and focused on a single responsibility
- Use async/await instead of Promise chains when possible
- Properly handle errors with try/catch blocks
- Document complex functions with JSDoc comments

## Classes

- Use access modifiers (public, private, protected)
- Initialize all properties in the constructor
- Keep methods focused and well-organized
- Use inheritance sparingly; prefer composition

## Best Practices

- Remove unused variables and imports
- Use const by default, let only when necessary
- Prefer immutability for data structures
- Write tests for critical functions
- Use meaningful commit messages
