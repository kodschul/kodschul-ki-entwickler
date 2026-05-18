# Research: Simple Todo App

**Phase**: 0 — Outline & Research
**Date**: 2026-05-12

## Decision Log

### Backend Framework

- **Decision**: Flask 3.x
- **Rationale**: Minimal overhead for a simple CRUD app; well-understood; excellent SQLAlchemy integration; no need for Django's full-stack complexity.
- **Alternatives considered**: Django (too heavy for a single-model app), FastAPI (adds async complexity without benefit for a UI-driven app).

### Database

- **Decision**: SQLite via SQLAlchemy ORM
- **Rationale**: Zero-configuration, file-based, sufficient for single-user scope. SQLAlchemy abstracts the DB layer cleanly if a switch to PostgreSQL is ever needed.
- **Alternatives considered**: PostgreSQL (overkill for single user), plain JSON file (no query capability, harder to extend).

### Frontend Approach

- **Decision**: Static HTML + vanilla JS + Tailwind CSS via CDN
- **Rationale**: No build step required; Tailwind CDN is fine for a simple app; vanilla fetch() handles CRUD calls without a framework dependency.
- **Alternatives considered**: React/Vue (adds npm build pipeline complexity unnecessary for a simple todo list), server-side Jinja2 templates (full-page reloads feel dated; JS fetch gives a snappier UX with minimal code).

### Tailwind CSS Delivery

- **Decision**: Tailwind CSS Play CDN (`<script src="https://cdn.tailwindcss.com">`)
- **Rationale**: No Node.js or build tooling required; instant setup; acceptable for a demo/simple app.
- **Alternatives considered**: PostCSS build pipeline (unnecessary complexity), inline styles (unmaintainable).

### Todo Persistence (client vs. server)

- **Decision**: Server-side (SQLite database)
- **Rationale**: Spec explicitly requires todos to survive page reload and positions this as a server-rendered/API-backed app. LocalStorage would only work in the same browser.
- **Alternatives considered**: LocalStorage (violates server-persistence requirement).

### Testing

- **Decision**: pytest + pytest-flask
- **Rationale**: Standard Python testing stack; pytest-flask provides a test client and app fixture; allows testing routes without a running server.
- **Alternatives considered**: unittest (more verbose), httpx (adds dependency without benefit over pytest-flask).

## Summary of Resolved Unknowns

| Unknown | Resolution |
|---------|------------|
| Backend framework | Flask 3.x |
| Database | SQLite + SQLAlchemy |
| Frontend | Static HTML + vanilla JS |
| CSS framework delivery | Tailwind CDN |
| Test framework | pytest + pytest-flask |
